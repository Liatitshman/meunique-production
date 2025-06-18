#!/usr/bin/env python3
"""
💡 LIAT Quick Backup Script
גיבוי מהיר של הפרויקט
"""

import os
import zipfile
from datetime import datetime
from pathlib import Path

def create_backup():
    """יוצר גיבוי מהיר"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"💡_LIAT_MeUnique_Backup_{timestamp}.zip"
    
    print(f"💡 יוצר גיבוי: {backup_name}")
    
    # קבצים חשובים לגיבוי
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
    
    # יצירת ZIP
    with zipfile.ZipFile(backup_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        # גיבוי קבצים
        for file in important_files:
            if os.path.exists(file):
                zf.write(file)
                print(f"  ✅ {file}")
        
        # גיבוי תיקיות חשובות
        for folder in ["backend", "config", "GPT Project Hub", "docs"]:
            if os.path.exists(folder):
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zf.write(file_path)
                print(f"  ✅ תיקייה: {folder}")
    
    print(f"\n✅ הגיבוי נוצר בהצלחה: {backup_name}")
    print(f"📍 מיקום: {os.getcwd()}")
    
    return backup_name

if __name__ == "__main__":
    print("""
    💡 LIAT Quick Backup
    ===================
    """)
    
    backup_file = create_backup()
    
    print(f"\n💡 טיפ: העתק את הקובץ {backup_file} לדרייב ידנית")
    print("   או השתמש ב-upload_to_gdrive.py להעלאה אוטומטית") 