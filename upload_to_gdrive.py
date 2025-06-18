#!/usr/bin/env python3
"""
העלאה אוטומטית ל-Google Drive
"""

import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import datetime

# הגדרות
SERVICE_ACCOUNT_FILE = 'config/google_service_account.json'
FOLDER_NAME = f'MeUnique_Backup_{datetime.now().strftime("%Y%m%d")}'

def authenticate():
    """אימות עם Google Drive"""
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=['https://www.googleapis.com/auth/drive']
        )
        service = build('drive', 'v3', credentials=credentials)
        print("✅ התחברות ל-Google Drive הצליחה!")
        return service
    except Exception as e:
        print(f"❌ שגיאה בהתחברות: {e}")
        return None

def create_folder(service, folder_name):
    """יצירת תיקייה ב-Drive"""
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    try:
        folder = service.files().create(body=file_metadata, fields='id').execute()
        print(f"✅ נוצרה תיקייה: {folder_name}")
        return folder.get('id')
    except Exception as e:
        print(f"❌ שגיאה ביצירת תיקייה: {e}")
        return None

def upload_file(service, file_path, folder_id=None):
    """העלאת קובץ ל-Drive"""
    file_name = os.path.basename(file_path)
    file_metadata = {'name': file_name}
    
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    # קביעת סוג הקובץ
    if file_path.endswith('.zip'):
        mimetype = 'application/zip'
    elif file_path.endswith('.md'):
        mimetype = 'text/markdown'
    else:
        mimetype = 'application/octet-stream'
    
    media = MediaFileUpload(file_path, mimetype=mimetype, resumable=True)
    
    try:
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        print(f"✅ הועלה: {file_name}")
        return file.get('id')
    except Exception as e:
        print(f"❌ שגיאה בהעלאת {file_name}: {e}")
        return None

def main():
    print("🚀 מתחיל העלאה ל-Google Drive...")
    
    # התחברות
    service = authenticate()
    if not service:
        return
    
    # יצירת תיקייה
    folder_id = create_folder(service, FOLDER_NAME)
    
    # העלאת קבצים
    files_to_upload = [
        '~/Desktop/MeUnique_Upload_To_Drive/MeUnique_Complete_20250619_0004.zip',
        '~/Desktop/MeUnique_Upload_To_Drive/cursor_.md'
    ]
    
    for file_path in files_to_upload:
        expanded_path = os.path.expanduser(file_path)
        if os.path.exists(expanded_path):
            upload_file(service, expanded_path, folder_id)
        else:
            print(f"⚠️ קובץ לא נמצא: {file_path}")
    
    print("\n✅ ההעלאה הושלמה!")
    print(f"📁 התיקייה ב-Drive: {FOLDER_NAME}")

if __name__ == "__main__":
    main() 