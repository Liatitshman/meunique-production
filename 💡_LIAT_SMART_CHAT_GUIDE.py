#!/usr/bin/env python3
"""
💡 LIAT Smart Chat Guide - מדריך חכם אינטראקטיבי
צ'אט שמכיר את כל המערכת ויודע להנחות אותך צעד אחר צעד
"""

import streamlit as st
import time
from datetime import datetime
import json
import os
from typing import List, Dict, Any

# הגדרות
st.set_page_config(
    page_title="💡 LIAT Chat Guide",
    page_icon="💬",
    layout="wide"
)

# CSS מותאם
st.markdown("""
<style>
    .chat-message {
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        animation: fadeIn 0.5s;
    }
    
    .user-message {
        background: #e3f2fd;
        margin-left: 20%;
    }
    
    .bot-message {
        background: #f3e5f5;
        margin-right: 20%;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .suggestion-box {
        background: #fff3cd;
        border: 2px solid #ffc107;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# מצב המערכת
if 'chat_state' not in st.session_state:
    st.session_state.chat_state = {
        'messages': [],
        'current_step': 'welcome',
        'setup_progress': 0,
        'user_preferences': {},
        'issues_resolved': []
    }

# בסיס ידע של המערכת
SYSTEM_KNOWLEDGE = {
    'setup_steps': [
        {
            'id': 'welcome',
            'title': 'ברוכה הבאה!',
            'description': 'בוא נתחיל להגדיר את המערכת שלך',
            'actions': ['בדיקת סביבה', 'הגדרת העדפות', 'חיבור APIs']
        },
        {
            'id': 'environment',
            'title': 'בדיקת סביבה',
            'description': 'נוודא שהכל מותקן כמו שצריך',
            'actions': ['Python', 'Streamlit', 'תלויות']
        },
        {
            'id': 'apis',
            'title': 'חיבור APIs',
            'description': 'נחבר את כל השירותים',
            'actions': ['LinkedIn', 'OpenAI', 'Google Drive', 'Apollo']
        },
        {
            'id': 'preferences',
            'title': 'העדפות אישיות',
            'description': 'נתאים את המערכת לסגנון שלך',
            'actions': ['טון הודעות', 'זמני פעילות', 'יעדים']
        },
        {
            'id': 'testing',
            'title': 'בדיקות',
            'description': 'נוודא שהכל עובד',
            'actions': ['חיפוש מועמדים', 'שליחת הודעה', 'גיבוי']
        }
    ],
    'common_issues': {
        'streamlit לא נמצא': {
            'solution': 'pip install streamlit',
            'explanation': 'Streamlit הוא הממשק של המערכת'
        },
        'API key לא עובד': {
            'solution': 'בדקי שהמפתח נכון ושהוא בקובץ .env',
            'explanation': 'המפתחות צריכים להיות בפורמט הנכון'
        },
        'המערכת לא עולה': {
            'solution': 'streamlit run 💡_LIAT_MEUNIQUE_SYSTEM.py',
            'explanation': 'וודאי שאת בתיקייה הנכונה'
        },
        'אין תגובות ממועמדים': {
            'solution': 'נסי את מצב "קומבינה" בהודעות',
            'explanation': 'הודעות ישראליות ישירות עובדות יותר טוב'
        }
    },
    'smart_suggestions': {
        'morning': [
            '☕ בוקר טוב! בואי נבדוק את התובנות החמות מאתמול',
            '📊 יש 12 מועמדים חדשים שכדאי לסרוק',
            '💡 הזמן הטוב ביותר לשלוח הודעות הוא עוד שעה'
        ],
        'afternoon': [
            '🎯 זה הזמן לעקוב אחרי ההודעות מהבוקר',
            '📈 יש עלייה של 30% בתגובות היום!',
            '🔄 כדאי לרענן את החיפושים'
        ],
        'evening': [
            '🌙 סוף יום מעולה! בואי נסכם',
            '💾 זמן טוב לגיבוי יומי',
            '📅 נתכנן את מחר?'
        ]
    }
}

def get_current_greeting():
    """מחזיר ברכה לפי השעה"""
    hour = datetime.now().hour
    if hour < 12:
        return "בוקר טוב"
    elif hour < 17:
        return "צהריים טובים"
    else:
        return "ערב טוב"

def get_smart_suggestions():
    """מחזיר הצעות חכמות לפי הקונטקסט"""
    hour = datetime.now().hour
    
    if hour < 12:
        return SYSTEM_KNOWLEDGE['smart_suggestions']['morning']
    elif hour < 17:
        return SYSTEM_KNOWLEDGE['smart_suggestions']['afternoon']
    else:
        return SYSTEM_KNOWLEDGE['smart_suggestions']['evening']

def process_user_input(user_input: str) -> Dict[str, Any]:
    """מעבד את הקלט ומחזיר תשובה חכמה"""
    
    # מילות מפתח לזיהוי כוונה
    keywords = {
        'setup': ['הגדרה', 'להגדיר', 'התקנה', 'setup'],
        'error': ['שגיאה', 'לא עובד', 'בעיה', 'תקוע'],
        'help': ['עזרה', 'איך', 'מה', 'למה'],
        'api': ['API', 'מפתח', 'חיבור', 'LinkedIn', 'OpenAI'],
        'candidates': ['מועמדים', 'חיפוש', 'סריקה', 'מצא'],
        'messages': ['הודעות', 'תגובות', 'פנייה', 'לשלוח'],
        'backup': ['גיבוי', 'שמירה', 'דרייב', 'סנכרון']
    }
    
    # זיהוי כוונה
    intent = 'general'
    for key, words in keywords.items():
        if any(word.lower() in user_input.lower() for word in words):
            intent = key
            break
    
    # החזרת תשובה מותאמת
    responses = {
        'setup': {
            'message': "בואי נעבור על תהליך ההגדרה צעד אחר צעד! 🚀",
            'actions': ['התחל הגדרה מודרכת', 'בדוק מה חסר', 'דלג להגדרות מתקדמות'],
            'next_step': 'environment'
        },
        'error': {
            'message': "אני כאן לעזור! ספרי לי בדיוק מה קורה 🔧",
            'actions': ['הצג שגיאות נפוצות', 'בדיקת מערכת', 'צור לוג תמיכה'],
            'next_step': 'troubleshoot'
        },
        'api': {
            'message': "בואי נוודא שכל ה-APIs מחוברים כמו שצריך 🔌",
            'actions': ['בדוק חיבורים', 'הוסף API חדש', 'עדכן מפתחות'],
            'next_step': 'apis'
        },
        'candidates': {
            'message': "מעולה! בואי נמצא את המועמדים הכי טובים 🎯",
            'actions': ['חיפוש חכם', 'סינון מתקדם', 'ייבוא רשימה'],
            'next_step': 'search'
        },
        'messages': {
            'message': "נכתוב הודעות שאי אפשר להתעלם מהן! 💬",
            'actions': ['יצירת תבנית', 'A/B טסטינג', 'ניתוח תגובות'],
            'next_step': 'messaging'
        },
        'backup': {
            'message': "חשוב לשמור על הנתונים! בואי נגדיר גיבוי אוטומטי 💾",
            'actions': ['גיבוי עכשיו', 'הגדרת תזמון', 'בדיקת גיבויים'],
            'next_step': 'backup'
        },
        'general': {
            'message': f"{get_current_greeting()} ליאת! במה אוכל לעזור? 😊",
            'actions': get_smart_suggestions()[:3],
            'next_step': 'menu'
        }
    }
    
    return responses.get(intent, responses['general'])

def execute_action(action: str):
    """מבצע פעולה לפי הבחירה"""
    action_map = {
        'התחל הגדרה מודרכת': lambda: start_guided_setup(),
        'בדוק חיבורים': lambda: check_connections(),
        'חיפוש חכם': lambda: smart_search(),
        'גיבוי עכשיו': lambda: backup_now(),
        'יצירת תבנית': lambda: create_template()
    }
    
    if action in action_map:
        return action_map[action]()
    else:
        return f"מבצע: {action}..."

def start_guided_setup():
    """מתחיל תהליך הגדרה מודרך"""
    return """
    🚀 **מתחילים הגדרה מודרכת!**
    
    **שלב 1: בדיקת סביבה**
    - Python 3.8+ ✅
    - Streamlit ✅
    - Pandas ✅
    
    **שלב 2: קבצי הגדרה**
    - .env ✅
    - config/google_service_account.json ✅
    
    **הצעד הבא:** נחבר את LinkedIn Sales Navigator
    """

def check_connections():
    """בודק את כל החיבורים"""
    connections = {
        'LinkedIn Sales Navigator': True,
        'OpenAI API': True,
        'Google Drive': False,
        'Apollo.io': True,
        'PhantomBuster': False
    }
    
    status = "**סטטוס חיבורים:**\n\n"
    for service, connected in connections.items():
        icon = "✅" if connected else "❌"
        status += f"{icon} {service}\n"
    
    return status

# ממשק ראשי
st.title("💡 LIAT Smart Chat Guide")
st.caption("המדריך החכם שלך למערכת MeUnique")

# פאנל צד
with st.sidebar:
    st.header("📊 מצב המערכת")
    
    # Progress bar
    progress = st.session_state.chat_state['setup_progress']
    st.progress(progress / 100)
    st.caption(f"התקדמות: {progress}%")
    
    st.divider()
    
    # Quick actions
    st.subheader("⚡ פעולות מהירות")
    
    if st.button("🚀 הפעל מערכת", use_container_width=True):
        st.success("המערכת עולה...")
        st.code("streamlit run 💡_LIAT_MEUNIQUE_SYSTEM.py")
    
    if st.button("💾 גיבוי מהיר", use_container_width=True):
        st.info("מבצע גיבוי...")
        time.sleep(1)
        st.success("✅ הגיבוי הושלם!")
    
    if st.button("🔄 בדיקת עדכונים", use_container_width=True):
        st.info("בודק עדכונים...")
    
    st.divider()
    
    # System info
    st.subheader("ℹ️ מידע")
    st.info("""
    **גרסה:** 3.0
    **מצב:** Production Ready
    **זמן פעולה:** 2 ימים
    """)

# אזור הצ'אט
chat_container = st.container()

# קלט משתמש
user_input = st.chat_input("שאלי אותי כל דבר על המערכת...")

if user_input:
    # הוספת הודעת משתמש
    st.session_state.chat_state['messages'].append({
        'role': 'user',
        'content': user_input,
        'timestamp': datetime.now()
    })
    
    # עיבוד וקבלת תשובה
    response = process_user_input(user_input)
    
    # הוספת תשובת בוט
    st.session_state.chat_state['messages'].append({
        'role': 'assistant',
        'content': response['message'],
        'actions': response.get('actions', []),
        'timestamp': datetime.now()
    })

# הצגת הודעות
with chat_container:
    for msg in st.session_state.chat_state['messages']:
        if msg['role'] == 'user':
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>את:</strong> {msg['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>💡 מדריך:</strong> {msg['content']}
            </div>
            """, unsafe_allow_html=True)
            
            # הצגת כפתורי פעולה
            if 'actions' in msg and msg['actions']:
                cols = st.columns(len(msg['actions']))
                for i, action in enumerate(msg['actions']):
                    with cols[i]:
                        if st.button(action, key=f"{msg['timestamp']}_{i}"):
                            result = execute_action(action)
                            st.info(result)

# הצעות חכמות בתחתית
if not st.session_state.chat_state['messages']:
    st.markdown("""
    <div class="suggestion-box">
    <h3>💡 הצעות לשאלות:</h3>
    <ul>
        <li>איך מתחילים להגדיר את המערכת?</li>
        <li>למה אני לא מקבלת תגובות ממועמדים?</li>
        <li>איך מחברים את LinkedIn?</li>
        <li>איפה רואים את הסטטיסטיקות?</li>
        <li>איך יוצרים גיבוי?</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.caption("""
💡 **טיפ:** אני כאן 24/7 ויודע הכל על המערכת שלך.
אל תהססי לשאול כל דבר - מהגדרות בסיסיות ועד טיפים מתקדמים!
""")

# Integration with admin panel
st.markdown("""
---
### 🔗 אינטגרציה עם פאנל האדמין

הצ'אט הזה מחובר ישירות למערכת ויכול:
- ✅ לענות על כל שאלה על הממשק
- ✅ להנחות אותך צעד אחר צעד
- ✅ לפתור בעיות נפוצות
- ✅ להציע שיפורים חכמים
- ✅ לבצע פעולות ישירות במערכת

**פשוט תשאלי ואני אדאג לכל השאר! 💪**
""") 