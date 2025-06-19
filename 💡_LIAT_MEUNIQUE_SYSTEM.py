#!/usr/bin/env python3
"""
💡 LIAT's MeUnique AI - Israeli Tech Recruitment System
מערכת גיוס מותאמת אישית לליאת עם פיצ'רים ישראליים מתקדמים
"""

import streamlit as st
import pandas as pd
import json
import time
from datetime import datetime, timedelta
import openai
import os
from typing import List, Dict, Any, Optional
import plotly.express as px
import plotly.graph_objects as go
from dataclasses import dataclass
import asyncio
import re
import requests
from collections import defaultdict

# הגדרות מותאמות אישית לליאת
st.set_page_config(
    page_title="💡 LIAT MeUnique - Israeli Tech Recruiter",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS מותאם בסגנון ישראלי
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');
    
    * {
        font-family: 'Heebo', sans-serif !important;
    }
    
    .main {
        direction: rtl;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: 700;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .israeli-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin: 10px 0;
        border-right: 4px solid #0066cc;
    }
    
    .kombina-alert {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# מחלקות נתונים מותאמות
@dataclass
class IsraeliCandidate:
    name: str
    unit: str  # יחידה צבאית
    tech_stack: List[str]
    startup_experience: bool
    exit_experience: bool
    salary_expectations: str
    visa_status: str
    relocation_willing: bool
    kombina_score: int  # ציון קומבינה - כמה יצירתי/יזמי

@dataclass
class SmartInsight:
    category: str
    insight: str
    action: str
    impact_score: int
    israeli_context: str

# אתחול מצב המערכת
if 'liat_system' not in st.session_state:
    st.session_state.liat_system = {
        'preferences': {
            'search_style': 'קומבינה חכמה',
            'communication_tone': 'ישיר ולעניין',
            'focus_areas': ['סטארטאפים', 'יחידות טכנולוגיות', 'אקזיטים'],
            'preferred_locations': ['תל אביב', 'הרצליה', 'רמת גן'],
            'salary_range': '25-50K',
            'auto_learn': True
        },
        'smart_catalog': defaultdict(list),
        'network_insights': [],
        'ats_patterns': {},
        'learning_history': [],
        'israeli_connections': {
            '8200': [],
            'ממרם': [],
            'תלפיות': [],
            '81': [],
            'סטארטאפים': []
        }
    }

# פונקציות חכמות
def calculate_kombina_score(candidate: Dict) -> int:
    """חישוב ציון קומבינה - כמה המועמד יצירתי ויזמי"""
    score = 50
    
    # בונוסים
    if 'סטארטאפ' in str(candidate.get('experience', '')):
        score += 15
    if any(unit in str(candidate.get('military', '')) for unit in ['8200', 'תלפיות', '81']):
        score += 20
    if candidate.get('side_projects', 0) > 2:
        score += 10
    if 'founder' in str(candidate.get('title', '')).lower():
        score += 25
    
    return min(100, score)

def find_hidden_connections(candidate: Dict, company: Dict) -> List[str]:
    """מציאת קשרים נסתרים - הקומבינה הישראלית"""
    connections = []
    
    # בדיקת קשרי יחידה צבאית
    if candidate.get('military_unit') == company.get('founder_unit'):
        connections.append(f"🪖 אותה יחידה כמו המייסד!")
    
    # בדיקת קשרי אוניברסיטה
    if candidate.get('university') in company.get('team_universities', []):
        connections.append(f"🎓 בוגר {candidate.get('university')} כמו 40% מהצוות")
    
    # בדיקת חברות קודמות
    common_companies = set(candidate.get('companies', [])) & set(company.get('team_backgrounds', []))
    if common_companies:
        connections.append(f"🏢 עבד ב-{', '.join(common_companies)} כמו חברי הצוות")
    
    return connections

def generate_israeli_opening_line(candidate: Dict, position: Dict) -> str:
    """יצירת שורת פתיחה ישראלית אותנטית"""
    templates = [
        f"היי {candidate['name']}, ראיתי שסיימת את {candidate.get('unit', 'השירות')} - יש לי משהו מעניין בשבילך 🚀",
        f"שלום {candidate['name']}, מישהו מ{candidate.get('last_company', 'החברה הקודמת')} המליץ עליך בחום 🔥",
        f"{candidate['name']}, יש פה משרה שנראית כאילו נתפרה עליך במיוחד 🎯",
        f"אהלן {candidate['name']}, ראיתי את הפרויקט שלך ב-GitHub - מרשים! יש לי הצעה שתעניין אותך 💡"
    ]
    
    # בחירה חכמה לפי הקונטקסט
    if candidate.get('military_unit') in ['8200', 'תלפיות', '81']:
        return templates[0]
    elif candidate.get('referred_by'):
        return templates[1]
    else:
        return templates[2]

# Header מותאם לליאת
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.title("💡 LIAT's MeUnique - Israeli Tech Recruiter")
    st.caption(f"🕐 {datetime.now().strftime('%H:%M')} | ☀️ תל אביב 28°C | 💪 מצב: קומבינה מקסימלית")

with col2:
    active_searches = 12
    st.metric("🔍 חיפושים פעילים", active_searches, "+3")

with col3:
    monthly_placements = 8
    st.metric("🎯 השמות החודש", monthly_placements, "+2")

# סרגל צד חכם - הבוט החכם מיקי!
with st.sidebar:
    st.header("🤖 מיקי - העוזר החכם שלך")
    
    # אווטאר של הבוט
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 80px;">🤖</div>
        <h3 style="color: #667eea;">היי ליאת! 👋</h3>
        <p>אני מיקי, העוזר החכם שלך</p>
    </div>
    """, unsafe_allow_html=True)
    
    # צ'אט עם הבוט
    st.subheader("💬 בואי נדבר")
    
    user_message = st.text_input("מה תרצי לעשות היום?", placeholder="לדוגמה: מצא לי מפתחי Python...")
    
    if user_message:
        with st.spinner("🤔 חושב..."):
            time.sleep(1)
        
        # תגובות חכמות של הבוט
        bot_responses = {
            "python": "🐍 מצאתי 23 מפתחי Python מעולים! רוצה שאסנן לפי ניסיון?",
            "עזרה": "👋 אני יכול לעזור לך למצוא מועמדים, לכתוב הודעות, לנתח נתונים ועוד!",
            "בוקר": "☀️ בוקר טוב! יש לך 5 תגובות חדשות ו-3 מועמדים חמים!",
            "default": "💡 רעיון מעולה! בואי נתחיל. איזה תפקיד מחפשים?"
        }
        
        response = bot_responses.get(
            next((k for k in bot_responses if k in user_message.lower()), 'default')
        )
        
        st.success(response)
        
        # פעולות מהירות
        col1, col2 = st.columns(2)
        with col1:
            if st.button("כן, בואי!", key="bot_yes"):
                st.info("🚀 מתחיל לחפש...")
        with col2:
            if st.button("אולי אחר כך", key="bot_no"):
                st.info("👍 אני פה כשתצטרכי!")
    
    st.divider()
    
    # תובנות חמות מהבוט
    st.subheader("🔥 תובנות חמות")
    
    hot_insights = [
        {"icon": "🎯", "text": "3 מועמדים ענו בשעה האחרונה!"},
        {"icon": "💡", "text": "הודעות עם אמוג'י מקבלות 40% יותר תגובות"},
        {"icon": "📈", "text": "השבוע השגת 85% יעד ההשמות!"},
        {"icon": "🏆", "text": "את בטופ 5% של המגייסות החודש!"}
    ]
    
    for insight in hot_insights:
        st.info(f"{insight['icon']} {insight['text']}")
    
    st.divider()
    
    # פעולות מומלצות
    st.subheader("💫 מה כדאי לעשות עכשיו?")
    
    actions = [
        {"text": "📧 לענות ל-3 מועמדים חמים", "urgent": True},
        {"text": "🔍 לסרוק עוד 10 פרופילים", "urgent": False},
        {"text": "📊 לבדוק את הדוח השבועי", "urgent": False},
        {"text": "☕ לקחת הפסקת קפה", "urgent": False}
    ]
    
    for action in actions:
        if action["urgent"]:
            if st.button(f"🔴 {action['text']}", key=action['text']):
                st.success("✅ בוצע!")
        else:
            if st.button(action['text'], key=action['text']):
                st.success("✅ נרשם!")
    
    # סטטוס מערכת
    st.divider()
    st.caption("🟢 כל המערכות פעילות | 🔄 עדכון אחרון: לפני 2 דקות")

# טאבים ראשיים
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "🛍️ חנות למגייסות",
    "🎯 צייד חכם",
    "🧠 מאגר דינמי",
    "💬 תקשורת חכמה",
    "📊 אנליטיקס ישראלי",
    "🔄 למידה מתמדת",
    "🤖 בוט חכם",
    "⚙️ העדפות אישיות"
])

# טאב חדש - חנות למגייסות
with tab1:
    st.header("🛍️ Recruiter's Store - חנות הכלים שלך")
    
    # הצעה מיוחדת
    st.markdown("""
    <div class="kombina-alert">
        🎉 מבצע השבוע: 20% הנחה על חבילת ה-Enterprise! קוד קופון: LIAT2025
    </div>
    """, unsafe_allow_html=True)
    
    # חבילות
    st.subheader("📦 בחרי את החבילה המושלמת לך")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="israeli-card" style="border-color: #28a745;">
            <h3 style="color: #28a745;">🌱 Starter Pack</h3>
            <h2>₪499/חודש</h2>
            <ul>
                <li>✅ 50 סריקות חכמות</li>
                <li>✅ 100 הודעות אוטומטיות</li>
                <li>✅ דוחות בסיסיים</li>
                <li>✅ תמיכה בצ'אט</li>
                <li>❌ AI מתקדם</li>
                <li>❌ אינטגרציות</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🛒 התחל עכשיו", key="starter"):
            st.success("✅ נוספת לחבילת Starter!")
            st.balloons()
    
    with col2:
        st.markdown("""
        <div class="israeli-card" style="border-color: #007bff; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);">
            <h3 style="color: #007bff;">⭐ Business Pro</h3>
            <h2>₪1,299/חודש</h2>
            <p style="color: #ff6b6b;">הכי פופולרי!</p>
            <ul>
                <li>✅ 200 סריקות חכמות</li>
                <li>✅ 500 הודעות אוטומטיות</li>
                <li>✅ AI לכתיבת הודעות</li>
                <li>✅ אנליטיקס מתקדם</li>
                <li>✅ אינטגרציות מלאות</li>
                <li>✅ תמיכת פרימיום</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 שדרג עכשיו", key="business", type="primary"):
            st.success("✅ ברוכה הבאה ל-Business Pro!")
            st.balloons()
    
    with col3:
        st.markdown("""
        <div class="israeli-card" style="border-color: #ffd700; background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);">
            <h3 style="color: #ff6b6b;">👑 Enterprise</h3>
            <h2>₪2,999/חודש</h2>
            <p style="color: #28a745;">חיסכון של 20%!</p>
            <ul>
                <li>✅ סריקות ללא הגבלה</li>
                <li>✅ הודעות ללא הגבלה</li>
                <li>✅ AI מותאם אישית</li>
                <li>✅ API מלא</li>
                <li>✅ מנהל הצלחה אישי</li>
                <li>✅ הדרכה 1-על-1</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👑 הצטרף לאליטה", key="enterprise"):
            st.success("✅ Welcome to Enterprise!")
            st.balloons()
    
    # כלים נוספים
    st.divider()
    st.subheader("🛠️ כלים נוספים להרחבה")
    
    tools_cols = st.columns(4)
    
    additional_tools = [
        {
            "name": "🔍 Super Search",
            "price": "₪199",
            "desc": "חיפוש בינה מלאכותית מתקדם",
            "features": ["חיפוש סמנטי", "זיהוי כישורים נסתרים", "ניתוח עומק"]
        },
        {
            "name": "📧 Email Wizard",
            "price": "₪149",
            "desc": "מחולל מיילים חכם",
            "features": ["10 סגנונות", "A/B Testing", "אופטימיזציה"]
        },
        {
            "name": "📊 Analytics Pro",
            "price": "₪249",
            "desc": "דוחות מתקדמים",
            "features": ["BI Dashboard", "תחזיות", "ROI מדויק"]
        },
        {
            "name": "🤝 Network Boost",
            "price": "₪299",
            "desc": "הרחבת רשת קשרים",
            "features": ["מיפוי קשרים", "המלצות חכמות", "Event alerts"]
        }
    ]
    
    for i, tool in enumerate(additional_tools):
        with tools_cols[i]:
            st.markdown(f"""
            <div class="israeli-card">
                <h4>{tool['name']}</h4>
                <h3 style="color: #667eea;">{tool['price']}/חודש</h3>
                <p>{tool['desc']}</p>
                <small>{'<br>'.join(f'• {f}' for f in tool['features'])}</small>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"הוסף לסל", key=f"tool_{i}"):
                st.success(f"✅ {tool['name']} נוסף!")
    
    # השוואת תכניות
    st.divider()
    with st.expander("📊 השוואה מפורטת בין החבילות"):
        comparison_data = {
            'פיצ\'ר': ['סריקות חודשיות', 'הודעות', 'AI כתיבה', 'אנליטיקס', 'תמיכה', 'API', 'הדרכה'],
            'Starter': ['50', '100', '❌', 'בסיסי', 'צ\'אט', '❌', '❌'],
            'Business': ['200', '500', '✅', 'מתקדם', '24/7', 'חלקי', 'וובינרים'],
            'Enterprise': ['∞', '∞', '✅ מותאם', 'מלא', 'VIP', '✅ מלא', '1-על-1']
        }
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True, hide_index=True)

# טאב 2: צייד חכם (הקיים)
with tab2:
    st.header("🎯 צייד המועמדים החכם")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # חיפוש חכם בסגנון ישראלי
        st.subheader("🔍 חיפוש קומבינה")
        
        search_query = st.text_area(
            "תאר/י את המועמד בעברית חופשית",
            placeholder="לדוגמה: מחפשת מפתח פולסטאק עם ניסיון בסטארטאפ, רצוי יוצא 8200, שיודע לעבוד לבד ועם ראש גדול...",
            height=100
        )
        
        # אפשרויות חיפוש מתקדמות
        with st.expander("🎛️ הגדרות קומבינה"):
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                include_passive = st.checkbox("כולל פסיביים", value=True)
                search_competitors = st.checkbox("חפש במתחרים", value=True)
                use_military_network = st.checkbox("רשת צבאית", value=True)
            
            with col_b:
                min_kombina_score = st.slider("ציון קומבינה מינימלי", 0, 100, 60)
                include_referrals = st.checkbox("כולל המלצות", value=True)
                search_github = st.checkbox("סרוק GitHub", value=True)
            
            with col_c:
                salary_flexibility = st.checkbox("גמישות בשכר", value=True)
                include_freelancers = st.checkbox("כולל פרילנסרים", value=False)
                search_forums = st.checkbox("פורומים טכניים", value=True)
        
        if st.button("🚀 הפעל חיפוש חכם", type="primary", use_container_width=True):
            # אנימציית חיפוש ישראלית
            progress = st.progress(0)
            status = st.empty()
            
            search_stages = [
                ("🔍 סורק LinkedIn...", 20),
                ("🎖️ בודק רשתות צבאיות...", 40),
                ("🏢 מנתח חברות מתחרות...", 60),
                ("🧮 מחשב ציוני קומבינה...", 80),
                ("✨ מייצר תובנות...", 100)
            ]
            
            for stage, percentage in search_stages:
                status.text(stage)
                progress.progress(percentage / 100)
                time.sleep(0.5)
            
            # תוצאות חיפוש
            st.success("✅ נמצאו 23 מועמדים עם פוטנציאל גבוה!")
            
            # טבלת מועמדים חכמה
            candidates_data = {
                'שם': ['דניאל כהן', 'מיכל לוי', 'רון ישראלי', 'טל אברהם'],
                'יחידה': ['8200', 'ממרם', 'תלפיות', '81'],
                'חברה נוכחית': ['Wix', 'Monday', 'Startup', 'Gong'],
                'קומבינה': [95, 88, 92, 85],
                'התאמה': [98, 94, 91, 87],
                'קשרים': ['3 משותפים', '1 משותף', '2 משותפים', '5 משותפים'],
                'סטטוס': ['🟢 פתוח', '🟡 אולי', '🟢 מעוניין', '🔵 פסיבי'],
                'הערות': ['מחפש אתגר', 'רוצה WFH', 'Post-Exit', 'ממליצים חם']
            }
            
            df = pd.DataFrame(candidates_data)
            
            # הצגה אינטראקטיבית
            selected_candidates = st.multiselect(
                "בחר/י מועמדים לפעולה",
                df['שם'].tolist()
            )
            
            if selected_candidates:
                col_1, col_2, col_3 = st.columns(3)
                
                with col_1:
                    if st.button("💬 שלח הודעות חכמות"):
                        st.success(f"✅ נשלחו {len(selected_candidates)} הודעות מותאמות!")
                
                with col_2:
                    if st.button("📊 ניתוח מעמיק"):
                        st.info("🔍 מנתח קשרים ותובנות...")
                
                with col_3:
                    if st.button("🎯 הוסף למעקב"):
                        st.success("✅ נוספו למעקב חכם!")
            
            # הצגת המועמדים
            for _, candidate in df.iterrows():
                with st.expander(f"{candidate['שם']} - {candidate['יחידה']} | קומבינה: {candidate['קומבינה']}"):
                    col_info, col_action = st.columns([3, 1])
                    
                    with col_info:
                        st.write(f"**חברה:** {candidate['חברה נוכחית']}")
                        st.write(f"**קשרים משותפים:** {candidate['קשרים']}")
                        st.write(f"**הערות:** {candidate['הערות']}")
                        
                        # תובנות חכמות
                        if candidate['קומבינה'] > 90:
                            st.success("💡 **תובנה:** מועמד עם פוטנציאל יזמי גבוה!")
                        
                        # קשרים נסתרים
                        hidden_connections = [
                            "🔗 למד עם CTO של החברה",
                            "🎯 אותו מנטור כמו המייסד",
                            "🏃 רץ עם VP R&D בבוקר"
                        ]
                        st.info(f"**קשרים נסתרים:** {hidden_connections[0]}")
                    
                    with col_action:
                        st.metric("התאמה", f"{candidate['התאמה']}%")
                        if st.button("פעולה מהירה", key=f"action_{candidate['שם']}"):
                            st.success("✅ בוצע!")
    
    with col2:
        # פאנל תובנות
        st.subheader("💡 תובנות חכמות")
        
        insights = [
            {
                "title": "🎯 זמן אופטימלי",
                "content": "עכשיו השעה הכי טובה לפנות - 73% פותחים הודעות",
                "action": "נצל עכשיו"
            },
            {
                "title": "🔥 טרנד חם",
                "content": "עלייה של 40% בביקוש ל-Rust developers",
                "action": "מצא מומחים"
            },
            {
                "title": "💰 שוק השכר",
                "content": "Senior Backend עלה ל-35-45K בחודש האחרון",
                "action": "עדכן הצעות"
            },
            {
                "title": "🚀 הזדמנות",
                "content": "3 חברות בדרך לאקזיט - עובדים פתוחים",
                "action": "סרוק עכשיו"
            }
        ]
        
        for insight in insights:
            with st.container():
                st.markdown(f"### {insight['title']}")
                st.write(insight['content'])
                if st.button(insight['action'], key=insight['title']):
                    st.success("✅ בביצוע!")
                st.divider()

# טאב 3: מאגר דינמי
with tab3:
    st.header("🧠 ניהול מאגר דינמי וחכם")
    
    # סיווג חכם
    st.subheader("🏷️ קטלוג חכם של המאגר")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # לפי יחידות צבאיות
        st.markdown("### 🎖️ לפי יחידות")
        units_data = {
            '8200': 234,
            'ממרם': 156,
            'תלפיות': 89,
            '81': 67,
            'אחר': 412
        }
        
        for unit, count in units_data.items():
            st.metric(unit, count, f"+{count//10}")
    
    with col2:
        # לפי ניסיון
        st.markdown("### 🚀 לפי ניסיון")
        exp_data = {
            'Junior (0-3)': 312,
            'Mid (3-6)': 428,
            'Senior (6+)': 218,
            'Expert (10+)': 76
        }
        
        fig = px.pie(values=list(exp_data.values()), 
                    names=list(exp_data.keys()),
                    color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#f5576c'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # לפי סטטוס
        st.markdown("### 📊 לפי סטטוס")
        status_data = pd.DataFrame({
            'סטטוס': ['פעיל', 'פסיבי', 'בתהליך', 'הושם'],
            'כמות': [423, 287, 134, 89],
            'שינוי': ['+12%', '+5%', '-3%', '+8%']
        })
        
        st.dataframe(status_data, use_container_width=True, hide_index=True)
    
    # כלי ניהול חכמים
    st.divider()
    st.subheader("🛠️ כלי ניהול מתקדמים")
    
    tool_cols = st.columns(4)
    
    tools = [
        ("🔄 רענון אוטומטי", "מעדכן סטטוסים של כל המועמדים"),
        ("🎯 סינון חכם", "מוצא מועמדים לפי קריטריונים מורכבים"),
        ("📊 ניתוח טרנדים", "מזהה שינויים בשוק העבודה"),
        ("🤝 מערכת המלצות", "מנהל המלצות ורפרלים")
    ]
    
    for i, (tool_name, tool_desc) in enumerate(tools):
        with tool_cols[i]:
            if st.button(tool_name, use_container_width=True):
                st.info(f"🔄 {tool_desc}...")
                time.sleep(1)
                st.success("✅ הושלם!")

# טאב 4: תקשורת חכמה
with tab4:
    st.header("💬 מערכת תקשורת חכמה")
    
    # בחירת סגנון
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("✍️ יצירת הודעות חכמות")
        
        # פרטי מועמד
        candidate_name = st.text_input("שם המועמד", "דני")
        candidate_company = st.text_input("חברה נוכחית", "Wix")
        candidate_role = st.text_input("תפקיד", "Senior Backend Developer")
        
        # סוג הודעה
        message_type = st.selectbox(
            "סוג הודעה",
            ["פנייה ראשונית", "מעקב", "תיאום ראיון", "הצעת עבודה", "נטוורקינג"]
        )
        
        # טון ההודעה
        tone_style = st.select_slider(
            "סגנון",
            options=["רשמי", "מקצועי", "ידידותי", "ישראלי", "קומבינה"],
            value="ישראלי"
        )
        
        # תוכן נוסף
        additional_context = st.text_area(
            "מידע נוסף",
            placeholder="לדוגמה: ראיתי שעשית אקזיט, מכירים את X, יש משרה ב-Y..."
        )
        
        if st.button("✨ צור הודעה חכמה", type="primary"):
            with st.spinner("🤖 יוצר הודעה מותאמת אישית..."):
                time.sleep(1)
            
            # הודעה מותאמת
            if tone_style == "קומבינה":
                message = f"""
היי {candidate_name}! 👋

ראיתי שאתה ב-{candidate_company} - עושים שם דברים מטורפים! 🚀

יש לי משהו שיכול לעניין אותך...
חברה מהממת (של חברים שלי מהצבא 😉) מחפשת בדיוק מישהו עם הסקילז שלך.

נשמע לך שנדבר? אפשר גם בזום קצר או קפה בדיזנגוף ☕

מה אומר?

ליאת 💫
                """
            else:
                message = f"""
שלום {candidate_name},

ראיתי את הפרופיל שלך ב-LinkedIn והתרשמתי מהניסיון שלך ב-{candidate_company}.

יש לי הזדמנות מעניינת שחושבת שתתאים לך מצוין - תפקיד {candidate_role} בחברה מובילה.

אשמח לשוחח ולספר יותר.

תודה,
ליאת
                """
            
            st.text_area("ההודעה שנוצרה:", message, height=250)
            
            # כפתורי פעולה
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if st.button("📤 שלח עכשיו"):
                    st.success("✅ ההודעה נשלחה!")
                    st.balloons()
            with col_b:
                if st.button("💾 שמור כתבנית"):
                    st.success("✅ נשמר בתבניות!")
            with col_c:
                if st.button("🔄 צור גרסה נוספת"):
                    st.info("🔄 יוצר גרסה חדשה...")
    
    with col2:
        st.subheader("📊 סטטיסטיקות תקשורת")
        
        # מטריקות
        st.metric("שיעור פתיחה", "73%", "+5%")
        st.metric("שיעור תגובה", "42%", "+8%")
        st.metric("זמן תגובה ממוצע", "4.2 שעות", "-1.3")
        
        # טיפים
        st.subheader("💡 טיפים חמים")
        tips = [
            "🕐 השעות הכי טובות: 10-12, 16-18",
            "📱 הודעות קצרות מקבלות 40% יותר תגובות",
            "😊 אימוג'י אחד = 25% יותר פתיחות",
            "🎯 אזכור משותף = 60% יותר תגובות"
        ]
        
        for tip in tips:
            st.info(tip)

# טאב 5: אנליטיקס ישראלי
with tab5:
    st.header("📊 אנליטיקס ותובנות ישראליות")
    
    # מדדי ביצוע
    st.subheader("🎯 מדדי ביצוע - החודש")
    
    metrics_cols = st.columns(5)
    metrics = [
        ("השמות", 8, "+2", "🎉"),
        ("ראיונות", 34, "+12", "💼"),
        ("פניות", 156, "+45", "📧"),
        ("תגובות", 67, "+23", "💬"),
        ("ROI", "324%", "+45%", "💰")
    ]
    
    for i, (label, value, delta, icon) in enumerate(metrics):
        with metrics_cols[i]:
            st.metric(f"{icon} {label}", value, delta)
    
    # גרפים מתקדמים
    col1, col2 = st.columns(2)
    
    with col1:
        # מפת חום של פעילות
        st.subheader("🗓️ מפת חום - מתי הכי אפקטיבי")
        
        days_hebrew = ['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי']
        hours = [f"{i:02d}:00" for i in range(8, 20)]
        
        import numpy as np
        activity_data = np.random.randint(0, 100, size=(5, 12))
        
        fig = px.imshow(activity_data,
                      labels=dict(x="שעה", y="יום", color="פעילות"),
                      x=hours, y=days_hebrew,
                      color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # השוואת מקורות
        st.subheader("📈 מקורות הגיוס הטובים ביותר")
        
        sources_data = pd.DataFrame({
            'מקור': ['LinkedIn', 'רפרלים', 'GitHub', 'Facebook', 'אחר'],
            'מועמדים': [234, 156, 89, 67, 34],
            'איכות': [85, 94, 91, 72, 68]
        })
        
        fig = px.scatter(sources_data, x='מועמדים', y='איכות', size='מועמדים',
                        text='מקור', color='איכות',
                        color_continuous_scale='RdYlGn',
                        title="איכות vs כמות לפי מקור")
        st.plotly_chart(fig, use_container_width=True)
    
    # תובנות ישראליות
    st.divider()
    st.subheader("🇮🇱 תובנות ייחודיות לשוק הישראלי")
    
    israeli_insights = [
        {
            "insight": "📈 עלייה של 35% בביקוש למפתחי AI אחרי ההצלחה של Wiz",
            "action": "התמקד במועמדים עם ניסיון ב-ML/AI",
            "priority": "גבוהה"
        },
        {
            "insight": "🏢 30% מהמועמדים מעדיפים Hybrid מאשר Remote מלא",
            "action": "הדגש אפשרות למשרד בת״א",
            "priority": "בינונית"
        },
        {
            "insight": "🎖️ יוצאי יחידות טכנולוגיות - 85% שביעות רצון מעסיקים",
            "action": "המשך לתת עדיפות ליוצאי יחידות",
            "priority": "גבוהה"
        },
        {
            "insight": "💰 פער של 20% בשכר בין ת״א לפריפריה",
            "action": "התאם ציפיות שכר לפי מיקום",
            "priority": "בינונית"
        }
    ]
    
    for insight_data in israeli_insights:
        with st.expander(f"{insight_data['insight']} - עדיפות: {insight_data['priority']}"):
            st.write(f"**המלצה:** {insight_data['action']}")
            if st.button("יישם המלצה", key=insight_data['insight']):
                st.success("✅ ההמלצה יושמה במערכת!")

# טאב 6: למידה מתמדת
with tab6:
    st.header("🔄 מערכת למידה והתפתחות")
    
    # למידה מהצלחות
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📚 מה למדנו החודש")
        
        learnings = [
            {
                "date": "19/01",
                "type": "הצלחה",
                "learning": "הודעות עם אזכור פרויקט ספציפי מ-GitHub מקבלות 80% תגובה",
                "impact": "גבוה"
            },
            {
                "date": "17/01",
                "type": "תובנה",
                "learning": "מועמדים מ-Monday מעדיפים סטארטאפים בשלב Growth",
                "impact": "בינוני"
            },
            {
                "date": "15/01",
                "type": "כישלון",
                "learning": "הודעות ארוכות מ-5 שורות לא נקראות",
                "impact": "גבוה"
            },
            {
                "date": "14/01",
                "type": "גילוי",
                "learning": "קשר דרך חבר משותף מהצבא = 95% הצלחה",
                "impact": "קריטי"
            }
        ]
        
        for item in learnings:
            type_color = {
                "הצלחה": "success",
                "תובנה": "info",
                "כישלון": "error",
                "גילוי": "warning"
            }
            
            st.markdown(f"""
            <div class="israeli-card">
                <h4>{item['type']} - {item['date']}</h4>
                <p>{item['learning']}</p>
                <small>השפעה: {item['impact']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🎯 יעדי למידה")
        
        goals = [
            {"goal": "הבנת ATS מערכות", "progress": 75},
            {"goal": "Python לאוטומציה", "progress": 60},
            {"goal": "Data Analysis", "progress": 45},
            {"goal": "AI Prompting", "progress": 90}
        ]
        
        for goal in goals:
            st.write(f"**{goal['goal']}**")
            st.progress(goal['progress'] / 100)
            st.caption(f"{goal['progress']}% הושלם")
            st.divider()

# טאב 7: בוט חכם
with tab7:
    st.header("🤖 מיקי - הבוט החכם")
    
    # צ'אט עם הבוט
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("💬 דברי איתי בחופשיות")
        
        # היסטוריית צ'אט
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # הצגת היסטוריה
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.chat_history[-5:]:  # הצג 5 הודעות אחרונות
                if msg['role'] == 'user':
                    st.markdown(f"**🙋‍♀️ את:** {msg['content']}")
                else:
                    st.markdown(f"**🤖 מיקי:** {msg['content']}")
        
        # קלט משתמש
        user_input = st.text_input("הקלידי הודעה...", key="chat_input")
        
        if user_input:
            # הוסף להיסטוריה
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # תגובות חכמות
            if "מועמד" in user_input:
                response = "🎯 מצאתי 15 מועמדים שמתאימים! רוצה שאציג אותם לפי התאמה?"
            elif "הודעה" in user_input:
                response = "✍️ אני יכול לכתוב הודעה בסגנון ישראלי, קומבינה או רשמי. מה מעדיפה?"
            elif "עזרה" in user_input:
                response = "💡 אני יכול: לחפש מועמדים, לכתוב הודעות, לנתח נתונים, להזכיר משימות ועוד!"
            else:
                response = "👍 מבינה! בואי נעשה את זה ביחד. איך להתחיל?"
            
            st.session_state.chat_history.append({"role": "bot", "content": response})
            st.experimental_rerun()
    
    with col2:
        st.subheader("⚡ פעולות מהירות")
        
        quick_actions = [
            {"icon": "🔍", "text": "חיפוש מהיר", "desc": "סרוק 50 פרופילים"},
            {"icon": "✉️", "text": "הודעות", "desc": "שלח 10 הודעות"},
            {"icon": "📊", "text": "דוח יומי", "desc": "צפה בביצועים"},
            {"icon": "🎯", "text": "מטרות", "desc": "עדכן יעדים"},
            {"icon": "💡", "text": "טיפים", "desc": "קבל עצות"}
        ]
        
        for action in quick_actions:
            if st.button(f"{action['icon']} {action['text']}", key=f"quick_{action['text']}", use_container_width=True):
                st.info(f"🚀 מבצע: {action['desc']}")
    
    # למידת העדפות
    st.divider()
    st.subheader("🧠 מה למדתי עליך")
    
    learned_preferences = {
        "שעות פעילות": "09:00-18:00",
        "סגנון מועדף": "ישראלי עם טאץ' של קומבינה",
        "תגובה ממוצעת": "73% מהמועמדים",
        "חברות מועדפות": "סטארטאפים בצמיחה",
        "נושאים חמים": "AI/ML, Cyber, FinTech"
    }
    
    for pref, value in learned_preferences.items():
        st.metric(pref, value)

# טאב 8: העדפות אישיות
with tab8:
    st.header("⚙️ העדפות אישיות - ליאת")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👤 הפרופיל שלי")
        
        st.text_input("שם מלא", value="ליאת תשמן", disabled=True)
        st.text_input("תפקיד", value="Tech Recruiter", disabled=True)
        st.text_input("ניסיון", value="10+ שנים", disabled=True)
        
        st.divider()
        
        st.subheader("🎯 העדפות חיפוש")
        
        search_preferences = st.multiselect(
            "תחומי התמחות",
            ["Backend", "Frontend", "FullStack", "DevOps", "Data", "Mobile", "AI/ML"],
            default=["Backend", "FullStack", "DevOps"]
        )
        
        company_types = st.multiselect(
            "סוגי חברות",
            ["סטארטאפ - Seed", "סטארטאפ - Growth", "חברה בוגרת", "Enterprise", "יוניקורן"],
            default=["סטארטאפ - Growth", "יוניקורן"]
        )
        
        salary_range = st.slider(
            "טווח שכר (אלפי ₪)",
            15, 60, (25, 45)
        )
    
    with col2:
        st.subheader("🤖 הגדרות אוטומציה")
        
        auto_search = st.checkbox("חיפוש אוטומטי יומי", value=True)
        auto_update = st.checkbox("עדכון סטטוסים אוטומטי", value=True)
        auto_followup = st.checkbox("מעקב אוטומטי", value=True)
        auto_insights = st.checkbox("תובנות אוטומטיות", value=True)
        
        st.divider()
        
        st.subheader("📱 התראות")
        
        notification_channels = st.multiselect(
            "ערוצי התראה",
            ["Email", "SMS", "WhatsApp", "Telegram", "Slack"],
            default=["Email", "WhatsApp"]
        )
        
        notification_types = st.multiselect(
            "סוגי התראות",
            ["תגובה חדשה", "מועמד חם", "תזכורת", "תובנה חשובה", "יעד הושג"],
            default=["תגובה חדשה", "מועמד חם", "יעד הושג"]
        )
        
        if st.button("💾 שמור העדפות", type="primary", use_container_width=True):
            st.success("✅ ההעדפות נשמרו בהצלחה!")
            st.balloons()

# Footer עם סטטוס
st.divider()
footer_cols = st.columns(7)

footer_items = [
    ("🟢 מערכת", "פעילה"),
    ("💾 גיבוי", "לפני 5 דקות"),
    ("🔄 סנכרון", "תקין"),
    ("📊 שימוש", "67%"),
    ("🚀 גרסה", "3.0"),
    ("💡 מצב", "קומבינה"),
    ("👤 משתמש", "ליאת")
]

for i, (label, value) in enumerate(footer_items):
    with footer_cols[i]:
        st.caption(f"{label}: {value}")

# הודעה אישית
st.markdown("""
<div style='text-align: center; margin-top: 50px; color: #666;'>
    <p>💡 Built with love for Liat - The Israeli Tech Recruiter Extraordinaire 🚀</p>
    <p>MeUnique.io - Where Israeli Chutzpah Meets AI 🇮🇱</p>
</div>
""", unsafe_allow_html=True) 