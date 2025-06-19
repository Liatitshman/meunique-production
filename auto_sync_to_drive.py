#!/usr/bin/env python3
"""
💡 LIAT Auto Sync to Google Drive
סקריפט לסנכרון אוטומטי של הפרויקט לגוגל דרייב עם שמות מותאמים לליאת
"""

import os
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
import time
import schedule
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
import streamlit as st
from twilio.rest import Client
import json

# הגדרות
PROJECT_PATH = Path(__file__).parent
BACKUP_FOLDER = PROJECT_PATH / "backups"
SERVICE_ACCOUNT_FILE = PROJECT_PATH / "config" / "google_service_account.json"
OPENAI_API_KEY = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
GOOGLE_TRANSLATE_KEY = "..."

# יצירת תיקיית גיבויים אם לא קיימת
BACKUP_FOLDER.mkdir(exist_ok=True)

def create_backup():
    """יוצר גיבוי ZIP עם שם שכולל את השם ליאת ואמוג'י"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"💡_LIAT_MeUnique_Backup_{timestamp}"
    backup_path = BACKUP_FOLDER / f"{backup_name}.zip"
    
    print(f"📦 יוצר גיבוי: {backup_name}")
    
    # רשימת קבצים לגיבוי (כולל החדשים)
    important_files = [
        ".env",
        "🎯_LIAT_MEUNIQUE_AI_MASTER_SPEC_2025.docx",
        "💡_LIAT_MEUNIQUE_SYSTEM.py",
        "meunique_interactive_app.py",
        "meunique_advanced_system.py",
        "liat_meunique_system.py",
        "auto_sync_to_drive.py",
        "upload_to_gdrive.py"
    ]
    
    # יצירת קובץ ZIP
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        # גיבוי קבצים חשובים
        for file in important_files:
            file_path = PROJECT_PATH / file
            if file_path.exists():
                backup_zip.write(file_path, file)
                print(f"  ✅ נוסף: {file}")
        
        # גיבוי תיקיות
        for folder in ["backend", "config", "GPT Project Hub", "docs"]:
            folder_path = PROJECT_PATH / folder
            if folder_path.exists():
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(PROJECT_PATH)
                        backup_zip.write(file_path, arcname)
                print(f"  ✅ נוספה תיקייה: {folder}")
    
    print(f"✅ הגיבוי נוצר: {backup_path}")
    return backup_path

def upload_to_drive(file_path):
    """מעלה קובץ לגוגל דרייב"""
    try:
        # בדיקה אם קובץ השירות קיים
        if not SERVICE_ACCOUNT_FILE.exists():
            print("❌ קובץ service account לא נמצא")
            return False
        
        # יצירת חיבור לגוגל דרייב
        credentials = service_account.Credentials.from_service_account_file(
            str(SERVICE_ACCOUNT_FILE),
            scopes=['https://www.googleapis.com/auth/drive.file']
        )
        
        service = build('drive', 'v3', credentials=credentials)
        
        # העלאת הקובץ
        file_metadata = {
            'name': f"💡_LIAT_{file_path.name}",
            'mimeType': 'application/zip'
        }
        
        media = MediaFileUpload(str(file_path), mimetype='application/zip')
        
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        print(f"✅ הקובץ הועלה לדרייב: {file.get('id')}")
        return True
        
    except HttpError as error:
        print(f"❌ שגיאה בהעלאה לדרייב: {error}")
        return False
    except Exception as e:
        print(f"❌ שגיאה כללית: {e}")
        return False

def sync_to_drive():
    """פונקציה ראשית לסנכרון"""
    print(f"\n🔄 מתחיל סנכרון - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # יצירת גיבוי
    backup_path = create_backup()
    
    # העלאה לדרייב
    if upload_to_drive(backup_path):
        print("✅ הסנכרון הושלם בהצלחה!")
        
        # מחיקת גיבויים ישנים (שמירת 5 אחרונים)
        backups = sorted(BACKUP_FOLDER.glob("*.zip"), key=lambda p: p.stat().st_mtime, reverse=True)
        for old_backup in backups[5:]:
            old_backup.unlink()
            print(f"🗑️ נמחק גיבוי ישן: {old_backup.name}")
    else:
        print("⚠️ הסנכרון הושלם עם שגיאות")

def update_main_document():
    """מעדכן את המסמך הראשי עם כל השינויים"""
    doc_path = PROJECT_PATH / "🎯_LIAT_MEUNIQUE_AI_MASTER_SPEC_2025.docx"
    
    if doc_path.exists():
        # כאן ניתן להוסיף לוגיקה לעדכון המסמך
        # לדוגמה: הוספת תאריך עדכון אחרון
        print(f"📄 המסמך הראשי קיים: {doc_path.name}")
        
        # יצירת עותק עם תאריך
        timestamp = datetime.now().strftime("%Y%m%d")
        updated_name = f"💡_LIAT_MEUNIQUE_MASTER_{timestamp}.docx"
        updated_path = PROJECT_PATH / updated_name
        
        # אם עדיין לא נוצר עותק היום
        if not updated_path.exists():
            shutil.copy2(doc_path, updated_path)
            print(f"✅ נוצר עותק מעודכן: {updated_name}")

def run_scheduled_sync():
    """הרצת סנכרון מתוזמן"""
    print("⏰ מתחיל סנכרון מתוזמן...")
    
    # עדכון המסמך הראשי
    update_main_document()
    
    # סנכרון לדרייב
    sync_to_drive()
    
    print("✅ הסנכרון המתוזמן הושלם")

# תזמון סנכרון כל 6 שעות
schedule.every(6).hours.do(run_scheduled_sync)

# סנכרון גם אחרי כל שינוי משמעותי
def watch_for_changes():
    """מעקב אחר שינויים בקבצים חשובים"""
    watched_files = [
        "💡_LIAT_MEUNIQUE_SYSTEM.py",
        "meunique_interactive_app.py",
        "meunique_advanced_system.py",
        ".env"
    ]
    
    # כאן ניתן להוסיף לוגיקה למעקב אחר שינויים
    # ולהפעיל סנכרון אוטומטי
    pass

def send_whatsapp(body, to=None):
    cfg = st.secrets["twilio"]
    to = to or st.secrets["admin"]["phone_whatsapp"]
    client = Client(cfg["account_sid"], cfg["auth_token"])
    client.messages.create(
        body=body,
        from_=cfg["from_whatsapp"],
        to=to
    )

def alert_router(event):
    channels = st.session_state.get("alert_channels",
                    st.secrets["alerts"]["default_channels"])
    text = f"⚠️ {event['type']} – {json.dumps(event['data'])}"
    if "inapp" in channels:
        st.session_state.alert_stack.append(text)
    if "slack" in channels:
        send_slack(text)              # כבר קיים
    if "whatsapp" in channels:
        send_whatsapp(text)

if __name__ == "__main__":
    print("""
    💡 LIAT Auto Sync System
    ========================
    סנכרון אוטומטי לגוגל דרייב
    
    אפשרויות:
    1. סנכרון מיידי
    2. הפעלת סנכרון אוטומטי (כל 6 שעות)
    3. יציאה
    """)
    
    choice = input("בחר/י אפשרות (1-3): ")
    
    if choice == "1":
        # סנכרון מיידי
        update_main_document()
        sync_to_drive()
        
    elif choice == "2":
        # הפעלת סנכרון אוטומטי
        print("🔄 מפעיל סנכרון אוטומטי...")
        print("   (Ctrl+C להפסקה)")
        
        # סנכרון ראשוני
        run_scheduled_sync()
        
        # לולאת תזמון
        while True:
            schedule.run_pending()
            time.sleep(60)  # בדיקה כל דקה
            
    else:
        print("👋 להתראות!")

if daily_cost > alert_limit:
    st.sidebar.error("⚠️ Usage exceeds limit – $%.2f" % daily_cost)
    send_slack_alert(daily_cost)

[admin]
password = "SuperSecret123"
slack_webhook = "https://hooks.slack.com/..."
[feature_flags]
enable_ai_detector = true

channels = st.multiselect(
    "🔔 Where do you want notifications?",
    ["inapp", "whatsapp", "slack"],
    default=["inapp"]
)
st.session_state.alert_channels = channels 

[twilio]
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_twilio_token"
from_whatsapp = "whatsapp:+14155238886"

[admin]
password = "SuperSecret123"
phone_whatsapp = "whatsapp:+9725XXXXXXXX" 