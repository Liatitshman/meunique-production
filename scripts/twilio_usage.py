"""Fetch Twilio WhatsApp usage for today and append to CSV / Google Sheet.
Env vars: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, GSHEET_ID (optional).
"""
import csv
import datetime as dt
import os
from pathlib import Path

import requests
from requests.auth import HTTPBasicAuth

try:
    import gspread  # type: ignore
    from google.oauth2.service_account import Credentials  # type: ignore
except ImportError:
    gspread = None


def fetch_today_usage() -> float:
    sid = os.getenv("TWILIO_ACCOUNT_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    if not sid or not token:
        raise RuntimeError("Missing Twilio credentials")
    today = dt.date.today().isoformat()
    url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Usage/Records/Daily.json?StartDate={today}&EndDate={today}"
    r = requests.get(url, auth=HTTPBasicAuth(sid, token), timeout=15)
    r.raise_for_status()
    usage_records = r.json().get("usage_records", [])
    total_cost = 0.0
    for rec in usage_records:
        if rec.get("category", "").startswith("whatsapp"):
            total_cost += float(rec.get("price", 0))
    return round(total_cost, 4)


def append_csv(amount: float, csv_path: Path):
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    new_row = [dt.date.today().isoformat(), amount]
    write_header = not csv_path.exists()
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["date", "twilio_whatsapp_usd"])
        writer.writerow(new_row)


def append_gsheet(amount: float, sheet_id: str):
    if not gspread:
        return
    json_str = os.getenv("GCP_SERVICE_JSON")
    if not json_str:
        return
    creds = Credentials.from_service_account_info(eval(json_str), scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    gc = gspread.authorize(creds)
    sh = gc.open_by_key(sheet_id)
    ws = sh.worksheet("DailyCosts")
    ws.append_row([dt.date.today().isoformat(), amount], value_input_option="USER_ENTERED")


def main():
    try:
        amount = fetch_today_usage()
    except Exception as e:
        print("Twilio usage fetch failed", e)
        return
    csv_path = Path("data/usage/twilio_usage.csv")
    append_csv(amount, csv_path)
    sheet_id = os.getenv("GSHEET_ID")
    if sheet_id:
        append_gsheet(amount, sheet_id)
    print("Saved Twilio WhatsApp usage $", amount)


if __name__ == "__main__":
    main() 