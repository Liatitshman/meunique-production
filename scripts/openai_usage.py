"""Fetch OpenAI usage stats and append to CSV & Google Sheet.
Requires env var OPENAI_API_KEY and optional GSHEET_ID.
Add to crontab / Streamlit Cloud scheduled job: 0 */6 * * * python scripts/openai_usage.py
"""
import csv
import datetime as dt
import os
from pathlib import Path

import requests

try:
    import gspread  # type: ignore
    from google.oauth2.service_account import Credentials  # type: ignore
except ImportError:
    gspread = None  # runtime will handle missing

BASE_URL = "https://api.openai.com/v1/dashboard/billing/usage"
HEADERS = {"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY', '')}"}


def fetch_today_usage() -> float:
    today = dt.date.today()
    start = today.strftime("%Y-%m-%d")
    end = start
    url = f"{BASE_URL}?start_date={start}&end_date={end}"
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    data = r.json()
    return round(data.get("total_usage", 0) / 100.0, 4)  # cents→$


def append_csv(amount: float, csv_path: Path):
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    new_row = [dt.date.today().isoformat(), amount]
    write_header = not csv_path.exists()
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["date", "openai_usd"])
        writer.writerow(new_row)


def append_gsheet(amount: float, sheet_id: str):
    if not gspread:
        print("gspread not installed; skipping Google Sheet")
        return
    json_str = os.getenv("GCP_SERVICE_JSON")
    if not json_str:
        print("Missing GCP_SERVICE_JSON secret – skipping Sheet")
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
        print("OpenAI usage fetch failed", e)
        return
    csv_path = Path("data/usage/openai_usage.csv")
    append_csv(amount, csv_path)
    sheet_id = os.getenv("GSHEET_ID")
    if sheet_id:
        append_gsheet(amount, sheet_id)
    print("Saved OpenAI usage $", amount)


if __name__ == "__main__":
    main() 