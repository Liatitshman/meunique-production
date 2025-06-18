#!/usr/bin/env python3
"""
🧠 MeUnique AI - Advanced System with Full Features
מערכת מתקדמת עם כל הפיצ'רים והיכולות
"""

import streamlit as st
import pandas as pd
import json
import time
import asyncio
from datetime import datetime, timedelta
import openai
import os
from typing import List, Dict, Any, Optional
import plotly.express as px
import plotly.graph_objects as go
from dataclasses import dataclass
import smtplib
from email.mime.text import MIMEText
import telegram
import schedule
import threading

# הגדרות עיצוב מתקדמות
st.set_page_config(
    page_title="MeUnique AI - Advanced Recruiter System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://meunique.io/help',
        'Report a bug': "https://meunique.io/bug",
        'About': "# MeUnique AI\nThe most advanced recruitment system in Israel 🇮🇱"
    }
)

# CSS מותאם אישית
st.markdown("""
<style>
    .main {
        padding: 0rem 0rem;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #0052a3;
        transform: scale(1.05);
    }
    .notification-badge {
        background-color: #ff4444;
        color: white;
        border-radius: 50%;
        padding: 2px 6px;
        font-size: 12px;
        position: absolute;
        top: -5px;
        right: -5px;
    }
    .success-animation {
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# מחלקות נתונים
@dataclass
class Notification:
    id: str
    type: str
    title: str
    message: str
    timestamp: datetime
    priority: str
    action_required: bool

@dataclass
class SmartSuggestion:
    category: str
    suggestion: str
    expected_impact: str
    effort_level: str
    roi_estimate: float

# אתחול המערכת
if 'system_state' not in st.session_state:
    st.session_state.system_state = {
        'notifications': [],
        'active_campaigns': [],
        'learning_queue': [],
        'automation_rules': [],
        'cost_optimizations': [],
        'israeli_partnerships': [],
        'admin_settings': {
            'auto_pilot': True,
            'smart_notifications': True,
            'cost_alerts': True,
            'learning_mode': 'aggressive',
            'language': 'hebrew',
            'timezone': 'Asia/Jerusalem'
        },
        'bot_personality': {
            'name': 'מיקי',
            'style': 'friendly_professional',
            'emoji_level': 'high',
            'humor_level': 'medium',
            'israeli_slang': True
        }
    }

# פונקציות עזר
def send_telegram_notification(message: str, priority: str = "normal"):
    """שליחת התראה לטלגרם"""
    # כאן תהיה אינטגרציה אמיתית עם טלגרם
    st.toast(f"📱 התראה נשלחה: {message}", icon="📱")

def calculate_roi(investment: float, return_value: float) -> float:
    """חישוב ROI"""
    return ((return_value - investment) / investment) * 100

def get_israeli_holidays():
    """מחזיר חגים ומועדים ישראליים"""
    return {
        "ראש השנה": "הימנע משליחת הודעות",
        "יום כיפור": "אין פעילות",
        "סוכות": "פעילות מופחתת",
        "חנוכה": "זמן טוב למתנות לעובדים",
        "פורים": "הודעות עם הומור",
        "פסח": "הימנע מפגישות"
    }

def get_smart_suggestions() -> List[SmartSuggestion]:
    """מחזיר הצעות חכמות מבוססות AI"""
    return [
        SmartSuggestion(
            category="עלויות",
            suggestion="עבור ל-Apollo Basic + PhantomBuster Starter - חיסכון של $30/חודש",
            expected_impact="חיסכון 15% בעלויות",
            effort_level="נמוך",
            roi_estimate=180.0
        ),
        SmartSuggestion(
            category="ישראלי",
            suggestion="שותפות עם StartupNation - גישה ל-500 סטארטאפים ישראליים",
            expected_impact="גידול 40% במאגר",
            effort_level="בינוני",
            roi_estimate=320.0
        ),
        SmartSuggestion(
            category="אוטומציה",
            suggestion="הפעל סריקה אוטומטית בימי ראשון בבוקר - שיא הפעילות",
            expected_impact="עלייה של 25% בתגובות",
            effort_level="נמוך",
            roi_estimate=250.0
        )
    ]

# Header עם התראות
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.title("🧠 MeUnique AI - מערכת הגיוס המתקדמת")
    st.caption(f"⏰ {datetime.now().strftime('%d/%m/%Y %H:%M')} | 🌡️ 24°C תל אביב")

with col2:
    # מונה התראות
    notifications_count = len([n for n in st.session_state.system_state['notifications'] if not n.get('read', False)])
    if notifications_count > 0:
        st.markdown(f"""
        <div style="position: relative; display: inline-block;">
            <h3>🔔 התראות</h3>
            <span class="notification-badge">{notifications_count}</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("### 🔔 התראות")

with col3:
    st.metric("💰 תקציב החודש", "$191", "-$10", delta_color="normal")

# סרגל צד מתקדם
with st.sidebar:
    st.header("🎮 לוח בקרה מרכזי")
    
    # מצב המערכת
    system_health = 92
    st.progress(system_health / 100, text=f"🏥 בריאות המערכת: {system_health}%")
    
    # מטריקות ביצועים
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 יעילות", "87%", "+5%")
        st.metric("⚡ מהירות", "1.2s", "-0.3s")
    with col2:
        st.metric("🧠 למידה", "156", "+23")
        st.metric("💡 חיסכון", "$47", "+$12")
    
    st.divider()
    
    # בוט אינטראקטיבי
    st.header("🤖 מיקי - העוזר החכם")
    
    bot_message = st.text_input("💬 מה נעשה?", placeholder="שאל אותי כל דבר...")
    if bot_message:
        with st.spinner("🤔 מיקי חושב..."):
            time.sleep(1)
        st.success("💡 מיקי: בטוח! כבר מטפל בזה...")
        
    # הצעות חכמות
    st.subheader("✨ הצעות חמות")
    suggestions = get_smart_suggestions()
    for suggestion in suggestions[:3]:
        with st.expander(f"{suggestion.category}: ROI {suggestion.roi_estimate:.0f}%"):
            st.write(suggestion.suggestion)
            st.caption(f"📊 השפעה: {suggestion.expected_impact}")
            if st.button(f"בצע", key=suggestion.category):
                st.success("✅ בוצע!")
                send_telegram_notification(f"הצעה בוצעה: {suggestion.suggestion}", "high")

# טאבים ראשיים מורחבים
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "🏠 דשבורד",
    "🏪 חנות Pro",
    "🎯 מנוע חכם",
    "👮 אדמין",
    "📊 אנליטיקס",
    "🇮🇱 ישראלי",
    "🔔 התראות",
    "🤝 שותפויות"
])

# טאב 1: דשבורד מתקדם
with tab1:
    st.header("🏠 מרכז השליטה")
    
    # כרטיסי מידע מהירים
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.info("""
        **📈 היום**
        - 23 סריקות
        - 15 התאמות
        - 8 תגובות
        - 3 ראיונות
        """)
        
    with col2:
        st.success("""
        **✅ הושלם**
        - גיבוי אוטומטי
        - עדכון מאגר
        - למידת טון
        - אופטימיזציה
        """)
        
    with col3:
        st.warning("""
        **⏳ ממתין**
        - 5 אישורים
        - 12 תגובות
        - 3 עדכוני סטטוס
        - סריקה שבועית
        """)
        
    with col4:
        st.error("""
        **🚨 דחוף**
        - Apollo מתקרב למגבלה
        - 2 מועמדים VIP
        - עדכון LinkedIn
        - תשלום דומיין
        """)
    
    # גרפים אינטראקטיביים
    st.subheader("📊 ביצועים בזמן אמת")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # גרף ביצועים
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי'],
            y=[12, 19, 23, 17, 25],
            mode='lines+markers',
            name='התאמות',
            line=dict(color='#0066cc', width=3)
        ))
        fig.add_trace(go.Scatter(
            x=['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי'],
            y=[8, 12, 15, 11, 18],
            mode='lines+markers',
            name='תגובות',
            line=dict(color='#00cc66', width=3)
        ))
        fig.update_layout(
            title="ביצועים השבוע",
            height=300,
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # פילוח מקורות
        fig = px.pie(
            values=[35, 25, 20, 15, 5],
            names=['LinkedIn', 'רפרלים', 'אתר', 'Apollo', 'אחר'],
            title="מקורות מועמדים",
            color_discrete_sequence=['#0066cc', '#00cc66', '#ffcc00', '#ff6600', '#cc00cc']
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # לוח פעולות מהירות
    st.subheader("⚡ פעולות מהירות")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("🔄 סנכרון כולל", use_container_width=True):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
            st.success("✅ סונכרן!")
            send_telegram_notification("סנכרון הושלם - 47 פרופילים חדשים", "normal")
    
    with col2:
        if st.button("🤖 הפעל AI", use_container_width=True):
            st.info("🧠 AI מנתח...")
            time.sleep(1)
            st.success("✅ 23 התאמות חדשות!")
    
    with col3:
        if st.button("📧 פיצוץ הודעות", use_container_width=True):
            st.warning("📤 שולח 50 הודעות...")
            time.sleep(2)
            st.success("✅ נשלחו!")
    
    with col4:
        if st.button("📊 דוח מנהלים", use_container_width=True):
            st.info("📄 מייצר דוח...")
            time.sleep(1)
            st.success("✅ [הורד דוח]()")
    
    with col5:
        if st.button("🎯 מצב פוקוס", use_container_width=True):
            st.info("🎯 מצב פוקוס מופעל")

# טאב 2: חנות מתקדמת
with tab2:
    st.header("🏪 חנות הכלים המתקדמת")
    
    # מבצעים והנחות
    st.info("🎉 **מבצע השבוע:** 20% הנחה על חבילות שנתיות! | 🎁 **בונוס:** 1000 קרדיטים לסריקה")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🚀 חבילת Startup")
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 15px; color: white;'>
        <h3>₪149/חודש</h3>
        <p><s>₪199</s> - חסכון 25%!</p>
        <ul>
        <li>✅ 100 סריקות</li>
        <li>✅ 50 הודעות AI</li>
        <li>✅ דוחות בסיסיים</li>
        <li>✅ תמיכה בעברית</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🛒 רכוש עכשיו", key="startup"):
            st.balloons()
            st.success("✅ מעבר לתשלום מאובטח...")
    
    with col2:
        st.subheader("⭐ חבילת Business")
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 20px; border-radius: 15px; color: white;'>
        <h3>₪399/חודש</h3>
        <p>הכי פופולרי! 🔥</p>
        <ul>
        <li>✅ 500 סריקות</li>
        <li>✅ 200 הודעות AI</li>
        <li>✅ אנליטיקס מתקדם</li>
        <li>✅ אינטגרציות מלאות</li>
        <li>✅ מנהל חשבון אישי</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🛒 רכוש עכשיו", key="business"):
            st.balloons()
            st.success("✅ מעבר לתשלום מאובטח...")
    
    with col3:
        st.subheader("👑 חבילת Enterprise")
        st.markdown("""
        <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                    padding: 20px; border-radius: 15px; color: white;'>
        <h3>מותאם אישית</h3>
        <p>פתרון מלא לארגון</p>
        <ul>
        <li>✅ סריקות ללא הגבלה</li>
        <li>✅ AI מותאם אישית</li>
        <li>✅ API מלא</li>
        <li>✅ הדרכה והטמעה</li>
        <li>✅ SLA 99.9%</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📞 דברו איתנו", key="enterprise"):
            st.info("📞 נציג יחזור אליך תוך 24 שעות")
    
    # תוספות וכלים
    st.divider()
    st.subheader("🛠️ תוספות מומלצות")
    
    tools = [
        {
            "name": "🎨 מעצב הודעות Pro",
            "price": "₪49/חודש",
            "description": "עיצוב הודעות מקצועי עם תבניות",
            "savings": "חסכון של 3 שעות בשבוע"
        },
        {
            "name": "📱 אפליקציה לנייד",
            "price": "חינם!",
            "description": "נהל הכל מהטלפון",
            "savings": "עבודה מכל מקום"
        },
        {
            "name": "🔗 אינטגרציית CRM",
            "price": "₪99/חודש",
            "description": "חיבור ל-Salesforce/HubSpot",
            "savings": "סנכרון אוטומטי מלא"
        },
        {
            "name": "🎯 AI Targeting Pro",
            "price": "₪149/חודש",
            "description": "טירגוט מתקדם עם ML",
            "savings": "שיפור של 40% בהתאמות"
        }
    ]
    
    cols = st.columns(4)
    for i, tool in enumerate(tools):
        with cols[i]:
            with st.container():
                st.markdown(f"### {tool['name']}")
                st.caption(tool['description'])
                st.metric("מחיר", tool['price'])
                st.info(f"💡 {tool['savings']}")
                if st.button("הוסף", key=f"tool_{i}"):
                    st.success("✅ נוסף לסל!")

# טאב 3: מנוע חכם
with tab3:
    st.header("🎯 מנוע ההתאמות החכם 2.0")
    
    # הגדרות חיפוש מתקדמות
    with st.expander("⚙️ הגדרות מתקדמות", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_mode = st.selectbox(
                "מצב חיפוש",
                ["🚀 טורבו", "⚖️ מאוזן", "🎯 דיוק מקסימלי"]
            )
            include_passive = st.checkbox("כלול מועמדים פסיביים", value=True)
            use_ai_enhance = st.checkbox("שיפור AI להתאמות", value=True)
        
        with col2:
            location_radius = st.slider("רדיוס מיקום (ק״מ)", 0, 100, 25)
            experience_flexibility = st.slider("גמישות בניסיון (שנים)", 0, 5, 2)
            skill_match = st.slider("דיוק התאמת כישורים", 50, 100, 85)
        
        with col3:
            culture_fit = st.checkbox("התאמה תרבותית", value=True)
            salary_match = st.checkbox("התאמת שכר", value=True)
            growth_potential = st.checkbox("פוטנציאל צמיחה", value=True)
    
    # חיפוש חכם
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_area(
            "תאר את המועמד האידיאלי",
            placeholder="לדוגמה: מפתח פולסטאק עם 5 שנות ניסיון ב-React ו-Node.js, ניסיון בסטארטאפ, דובר אנגלית ברמה גבוהה...",
            height=100
        )
    
    with col2:
        st.metric("איכות החיפוש", "92%", "+5%")
        if st.button("🔍 חפש עכשיו", type="primary", use_container_width=True):
            # אנימציית חיפוש
            with st.spinner("🤖 סורק מאגרים..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                stages = [
                    "🔍 סורק LinkedIn...",
                    "📊 מנתח פרופילים...",
                    "🧠 מפעיל AI...",
                    "🎯 מחשב התאמות...",
                    "✨ מכין תוצאות..."
                ]
                
                for i, stage in enumerate(stages):
                    status_text.text(stage)
                    progress_bar.progress((i + 1) / len(stages))
                    time.sleep(0.5)
            
            # תוצאות
            st.success("✅ נמצאו 28 מועמדים מתאימים!")
            
            # טבלת תוצאות מתקדמת
            results_df = pd.DataFrame({
                'דירוג': ['🥇', '🥈', '🥉', '4', '5'],
                'שם': ['דוד כהן', 'שרה לוי', 'משה ישראלי', 'רחל אברהם', 'יוסי דוד'],
                'התאמה': [96, 94, 91, 88, 85],
                'ניסיון': ['6 שנים', '5 שנים', '7 שנים', '4 שנים', '8 שנים'],
                'כישורים': ['React, Node, AWS', 'Vue, Python, Docker', 'Angular, Java, K8s', 'React, GraphQL', 'Full Stack'],
                'סטטוס': ['🟢 זמין מיידי', '🟡 פתוח להצעות', '🟢 זמין', '🟡 מעוניין', '🔵 פסיבי'],
                'שכר': ['25-30K', '22-28K', '28-35K', '20-25K', '30-40K'],
                'מיקום': ['תל אביב', 'רמת גן', 'הרצליה', 'Remote', 'חיפה']
            })
            
            st.dataframe(
                results_df,
                use_container_width=True,
                column_config={
                    "התאמה": st.column_config.ProgressColumn(
                        "התאמה %",
                        help="אחוז ההתאמה למשרה",
                        format="%d%%",
                        min_value=0,
                        max_value=100,
                    ),
                    "דירוג": st.column_config.TextColumn(
                        "דירוג",
                        help="דירוג המועמד",
                        width="small",
                    ),
                }
            )
            
            # פעולות מרובות
            st.subheader("🎬 פעולות")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                selected = st.multiselect("בחר מועמדים", results_df['שם'].tolist())
            
            with col2:
                action = st.selectbox(
                    "פעולה",
                    ["📧 שלח הודעה", "📅 קבע ראיון", "💾 שמור לרשימה", "📤 שתף עם מנהל"]
                )
            
            with col3:
                template = st.selectbox(
                    "תבנית",
                    ["מותאמת אישית", "ראשונית", "מעקב", "דחופה"]
                )
            
            with col4:
                if st.button("▶️ בצע", type="primary"):
                    if selected:
                        with st.spinner(f"מבצע {action}..."):
                            time.sleep(1)
                        st.success(f"✅ {action} בוצעה ל-{len(selected)} מועמדים!")
                        send_telegram_notification(f"{action} בוצעה בהצלחה", "normal")

# טאב 4: פאנל אדמין
with tab4:
    st.header("👮 מרכז ניהול מתקדם")
    
    # בדיקת הרשאות
    password = st.text_input("🔐 סיסמת אדמין", type="password")
    
    if password == "admin123":  # במציאות תהיה אימות מאובטח
        st.success("✅ גישת אדמין אושרה")
        
        # תפריט אדמין
        admin_action = st.selectbox(
            "בחר פעולה",
            ["👥 ניהול משתמשים", "⚙️ הגדרות מערכת", "📊 דוחות מתקדמים", 
             "🔧 תחזוקה", "💰 ניהול תשלומים", "🚀 עדכוני מערכת"]
        )
        
        if admin_action == "👥 ניהול משתמשים":
            st.subheader("👥 ניהול משתמשים ותפקידים")
            
            # טבלת משתמשים
            users_df = pd.DataFrame({
                'ID': ['001', '002', '003', '004'],
                'שם': ['ליאת תשמן', 'דני כהן', 'מיכל לוי', 'Demo User'],
                'תפקיד': ['🔴 Admin', '🟡 Manager', '🟢 Recruiter', '⚪ Trial'],
                'סטטוס': ['פעיל', 'פעיל', 'חופשה', 'פעיל'],
                'התחברות אחרונה': ['לפני 5 דקות', 'אתמול', 'לפני שבוע', 'עכשיו'],
                'שימוש': ['100%', '75%', '60%', '20%']
            })
            
            st.dataframe(users_df, use_container_width=True)
            
            # הוספת משתמש
            with st.expander("➕ הוסף משתמש חדש"):
                new_name = st.text_input("שם מלא")
                new_email = st.text_input("אימייל")
                new_role = st.selectbox("תפקיד", ["Recruiter", "Manager", "Admin"])
                new_package = st.selectbox("חבילה", ["Starter", "Business", "Enterprise"])
                
                if st.button("✅ צור משתמש"):
                    st.success(f"✅ משתמש {new_name} נוצר בהצלחה!")
        
        elif admin_action == "⚙️ הגדרות מערכת":
            st.subheader("⚙️ הגדרות מערכת גלובליות")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🔧 הגדרות טכניות")
                
                api_rate_limit = st.number_input("מגבלת API לדקה", value=60)
                cache_ttl = st.number_input("זמן חיי מטמון (שניות)", value=3600)
                max_concurrent = st.number_input("חיבורים מקבילים", value=10)
                debug_mode = st.checkbox("מצב Debug", value=False)
                
                if st.button("💾 שמור הגדרות טכניות"):
                    st.success("✅ הגדרות טכניות נשמרו!")
            
            with col2:
                st.markdown("### 🎨 הגדרות UI/UX")
                
                theme = st.selectbox("ערכת נושא", ["🌞 בהיר", "🌙 כהה", "🎨 מותאם אישית"])
                language = st.selectbox("שפת ברירת מחדל", ["🇮🇱 עברית", "🇺🇸 English", "🇷🇺 Русский"])
                animations = st.checkbox("אנימציות", value=True)
                tooltips = st.checkbox("טיפים", value=True)
                
                if st.button("💾 שמור הגדרות UI"):
                    st.success("✅ הגדרות UI נשמרו!")
        
        elif admin_action == "💰 ניהול תשלומים":
            st.subheader("💰 מרכז תשלומים וחיובים")
            
            # סיכום פיננסי
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("הכנסות החודש", "$4,580", "+12%")
            with col2:
                st.metric("הוצאות", "$191", "-5%")
            with col3:
                st.metric("רווח נקי", "$4,389", "+15%")
            with col4:
                st.metric("לקוחות פעילים", "23", "+3")
            
            # גרף הכנסות
            revenue_data = pd.DataFrame({
                'תאריך': pd.date_range('2024-01-01', periods=30, freq='D'),
                'הכנסות': [150 + i*10 + (i%7)*20 for i in range(30)]
            })
            
            fig = px.area(revenue_data, x='תאריך', y='הכנסות', 
                         title='הכנסות 30 ימים אחרונים',
                         color_discrete_sequence=['#0066cc'])
            st.plotly_chart(fig, use_container_width=True)
    
    else:
        st.error("❌ סיסמה שגויה. אנא נסה שוב.")

# טאב 5: אנליטיקס מתקדם
with tab5:
    st.header("📊 מרכז אנליטיקס מתקדם")
    
    # בחירת תקופה
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        date_range = st.selectbox(
            "תקופה",
            ["היום", "השבוע", "החודש", "3 חודשים", "שנה", "מותאם אישית"]
        )
    
    with col2:
        comparison = st.checkbox("השווה לתקופה קודמת", value=True)
    
    with col3:
        export_format = st.selectbox(
            "ייצוא",
            ["PDF", "Excel", "PowerBI", "Google Sheets", "API"]
        )
    
    # KPIs ראשיים
    st.subheader("🎯 KPIs ראשיים")
    
    kpi_cols = st.columns(6)
    kpis = [
        ("🎯 יעד חודשי", "156/200", "78%"),
        ("💰 ROI", "324%", "+45%"),
        ("⏱️ זמן למילוי", "18 ימים", "-3"),
        ("📈 שיעור המרה", "23%", "+5%"),
        ("😊 שביעות רצון", "4.8/5", "+0.2"),
        ("🚀 יעילות", "87%", "+12%")
    ]
    
    for i, (label, value, change) in enumerate(kpis):
        with kpi_cols[i]:
            st.metric(label, value, change)
    
    # דשבורדים אינטראקטיביים
    tab_a, tab_b, tab_c, tab_d = st.tabs(["📊 ביצועים", "👥 מועמדים", "🏢 חברות", "💡 תובנות"])
    
    with tab_a:
        col1, col2 = st.columns(2)
        
        with col1:
            # גרף משפך
            funnel_data = pd.DataFrame({
                'שלב': ['צפיות', 'קליקים', 'תגובות', 'ראיונות', 'הצעות', 'גיוסים'],
                'כמות': [1000, 650, 380, 120, 45, 23],
                'אחוז': [100, 65, 38, 12, 4.5, 2.3]
            })
            
            fig = px.funnel(funnel_data, x='כמות', y='שלב', 
                          title='משפך הגיוס',
                          color_discrete_sequence=['#0066cc'])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # מפת חום
            import numpy as np
            
            days = ['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי', 'שישי', 'שבת']
            hours = [f"{i:02d}:00" for i in range(24)]
            
            activity_data = np.random.randint(0, 100, size=(7, 24))
            
            fig = px.imshow(activity_data,
                          labels=dict(x="שעה", y="יום", color="פעילות"),
                          x=hours, y=days,
                          title="מפת חום - פעילות שבועית",
                          color_continuous_scale="Blues")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab_b:
        # ניתוח מועמדים
        st.subheader("🔍 ניתוח מעמיק של מועמדים")
        
        # פילוח לפי מיקום
        location_data = pd.DataFrame({
            'מיקום': ['תל אביב', 'רמת גן', 'הרצליה', 'חיפה', 'ירושלים', 'Remote'],
            'מועמדים': [450, 320, 280, 180, 150, 220]
        })
        
        fig = px.bar(location_data, x='מיקום', y='מועמדים',
                    title='פילוח מועמדים לפי מיקום',
                    color='מועמדים',
                    color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)

# טאב 6: פיצ'רים ישראליים
with tab6:
    st.header("🇮🇱 פיצ'רים ישראליים ייחודיים")
    
    # לוח שנה עברי וחגים
    st.subheader("📅 לוח שנה עברי וחגים")
    
    holidays = get_israeli_holidays()
    
    holiday_df = pd.DataFrame(
        list(holidays.items()),
        columns=['חג', 'המלצה']
    )
    
    st.dataframe(holiday_df, use_container_width=True)
    
    # שותפויות ישראליות
    st.subheader("🤝 שותפויות מקומיות")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **🚀 Start-Up Nation Central**
        - גישה ל-6,000+ סטארטאפים
        - מידע על גיוסי הון
        - קשרים ישירים למייסדים
        
        [חבר עכשיו →]()
        """)
    
    with col2:
        st.info("""
        **🎓 אוניברסיטאות**
        - ת"א, העברית, הטכניון
        - גישה לבוגרים טריים
        - תוכניות השמה ייחודיות
        
        [פרטים נוספים →]()
        """)
    
    with col3:
        st.info("""
        **💼 לשכות מסחר**
        - לשכת המסחר ת"א
        - התאחדות התעשיינים
        - רישות עסקי מובנה
        
        [הצטרף →]()
        """)
    
    # כלים בעברית
    st.subheader("🛠️ כלים מותאמים לשוק הישראלי")
    
    tools_il = [
        {
            "name": "🔍 סורק דרושים ישראלי",
            "description": "סורק AllJobs, JobMaster, Drushim",
            "status": "פעיל"
        },
        {
            "name": "📱 ווטסאפ Bot",
            "description": "תקשורת ישירה עם מועמדים",
            "status": "בפיתוח"
        },
        {
            "name": "🪖 מאגר חיילים משוחררים",
            "description": "גישה למשוחררי יחידות טכנולוגיות",
            "status": "פעיל"
        },
        {
            "name": "📊 מדד שכר ישראלי",
            "description": "נתוני שכר מעודכנים לפי תפקיד ואזור",
            "status": "פעיל"
        }
    ]
    
    for tool in tools_il:
        with st.expander(f"{tool['name']} - {tool['status']}"):
            st.write(tool['description'])
            if tool['status'] == "פעיל":
                if st.button(f"הפעל {tool['name']}", key=tool['name']):
                    st.success("✅ הכלי מופעל!")
            else:
                st.info("🔜 בקרוב...")

# טאב 7: מרכז התראות
with tab7:
    st.header("🔔 מרכז התראות והודעות")
    
    # הגדרות התראות
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📬 התראות אחרונות")
        
        notifications = [
            {
                "time": "לפני 5 דקות",
                "type": "success",
                "icon": "✅",
                "title": "התאמה חדשה!",
                "message": "דוד כהן התאים ב-95% למשרת Senior Developer ב-Gong",
                "action": "צפה בפרופיל"
            },
            {
                "time": "לפני 20 דקות",
                "type": "warning",
                "icon": "⚠️",
                "title": "מגבלת API",
                "message": "נותרו 150 קריאות מתוך 1000 היומיות",
                "action": "נהל מגבלות"
            },
            {
                "time": "לפני שעה",
                "type": "info",
                "icon": "📧",
                "title": "תגובה חדשה",
                "message": "שרה לוי הגיבה להודעתך",
                "action": "קרא תגובה"
            },
            {
                "time": "לפני 2 שעות",
                "type": "success",
                "icon": "🎯",
                "title": "יעד הושג!",
                "message": "הגעת ל-100 התאמות החודש",
                "action": "צפה בסטטיסטיקות"
            }
        ]
        
        for notif in notifications:
            alert_type = "success" if notif["type"] == "success" else "warning" if notif["type"] == "warning" else "info"
            
            with st.container():
                col_icon, col_content, col_action = st.columns([1, 6, 2])
                
                with col_icon:
                    st.markdown(f"# {notif['icon']}")
                
                with col_content:
                    st.markdown(f"**{notif['title']}**")
                    st.caption(f"{notif['message']} • {notif['time']}")
                
                with col_action:
                    if st.button(notif['action'], key=f"notif_{notif['time']}"):
                        st.info("✨ פותח...")
                
                st.divider()
    
    with col2:
        st.subheader("⚙️ הגדרות התראות")
        
        st.markdown("### 📱 ערוצי התראה")
        email_notif = st.checkbox("📧 אימייל", value=True)
        telegram_notif = st.checkbox("💬 טלגרם", value=True)
        whatsapp_notif = st.checkbox("📱 ווטסאפ", value=False)
        browser_notif = st.checkbox("🌐 דפדפן", value=True)
        
        st.markdown("### 🔔 סוגי התראות")
        new_match = st.checkbox("התאמות חדשות", value=True)
        responses = st.checkbox("תגובות מועמדים", value=True)
        system_alerts = st.checkbox("התראות מערכת", value=True)
        cost_alerts = st.checkbox("התראות עלות", value=True)
        
        st.markdown("### ⏰ תזמון")
        quiet_hours = st.checkbox("שעות שקטות", value=True)
        if quiet_hours:
            start_time = st.time_input("מ-", value=pd.to_datetime("22:00").time())
            end_time = st.time_input("עד", value=pd.to_datetime("07:00").time())
        
        if st.button("💾 שמור הגדרות התראות"):
            st.success("✅ ההגדרות נשמרו!")

# טאב 8: שותפויות ואינטגרציות
with tab8:
    st.header("🤝 מרכז שותפויות ואינטגרציות")
    
    # אינטגרציות פעילות
    st.subheader("🔗 אינטגרציות פעילות")
    
    integrations = {
        "LinkedIn Sales Navigator": {"status": "🟢", "usage": 87, "limit": 1000},
        "OpenAI GPT-4": {"status": "🟢", "usage": 62, "limit": 10000},
        "Google Drive": {"status": "🟢", "usage": 45, "limit": "Unlimited"},
        "Apollo.io": {"status": "🟡", "usage": 92, "limit": 1000},
        "PhantomBuster": {"status": "🟢", "usage": 73, "limit": 5000},
        "Slack": {"status": "🔴", "usage": 0, "limit": 0},
        "Zoom": {"status": "🟡", "usage": 100, "limit": 100}
    }
    
    cols = st.columns(3)
    for i, (service, data) in enumerate(integrations.items()):
        with cols[i % 3]:
            with st.container():
                st.metric(
                    service,
                    f"{data['usage']}%",
                    f"מתוך {data['limit']}" if data['limit'] != "Unlimited" else "ללא הגבלה"
                )
                st.caption(f"סטטוס: {data['status']}")
                
                if data['status'] == "🔴":
                    if st.button(f"חבר {service}", key=f"connect_{service}"):
                        st.info("🔄 מתחבר...")
                elif data['usage'] > 80:
                    st.warning("⚠️ קרוב למגבלה")
    
    # הצעות לשותפויות חדשות
    st.divider()
    st.subheader("✨ שותפויות מומלצות")
    
    recommendations = [
        {
            "partner": "🏢 Microsoft Teams",
            "benefit": "אינטגרציה מלאה לתקשורת פנים ארגונית",
            "cost": "חינם",
            "roi": "שיפור של 30% בתקשורת"
        },
        {
            "partner": "📊 Tableau",
            "benefit": "דשבורדים מתקדמים ו-BI",
            "cost": "$70/חודש",
            "roi": "חיסכון של 10 שעות בחודש"
        },
        {
            "partner": "🤖 Clay.com",
            "benefit": "העשרת נתונים אוטומטית",
            "cost": "$149/חודש",
            "roi": "שיפור של 40% באיכות הנתונים"
        }
    ]
    
    for rec in recommendations:
        with st.expander(f"{rec['partner']} - ROI: {rec['roi']}"):
            st.write(f"**יתרון:** {rec['benefit']}")
            st.write(f"**עלות:** {rec['cost']}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔍 למד עוד", key=f"learn_{rec['partner']}"):
                    st.info("🌐 פותח דף מידע...")
            with col2:
                if st.button("🚀 התחל ניסיון", key=f"trial_{rec['partner']}"):
                    st.success("✅ ניסיון ל-14 יום הופעל!")

# Footer מתקדם
st.divider()

# סטטוס בר תחתון
status_cols = st.columns(8)

status_items = [
    ("🟢 מערכת", "תקין"),
    ("⚡ מהירות", "1.2s"),
    ("💾 גיבוי", "לפני 5 דק׳"),
    ("🔄 סנכרון", "פעיל"),
    ("🛡️ אבטחה", "מאובטח"),
    ("📊 שימוש", "67%"),
    ("👥 משתמשים", "4/5"),
    ("🌐 גרסה", "2.5.1")
]

for i, (icon_label, value) in enumerate(status_items):
    with status_cols[i]:
        st.caption(f"{icon_label}: {value}")

# צ'אט בוט צף
if 'chat_open' not in st.session_state:
    st.session_state.chat_open = False

# כפתור צ'אט
if st.button("💬 צ'אט עם מיקי", key="main_chat_button"):
    st.session_state.chat_open = not st.session_state.chat_open

if st.session_state.chat_open:
    with st.container():
        st.markdown("### 🤖 מיקי - העוזר החכם שלך")
        
        chat_input = st.text_input(
            "שאל אותי כל דבר...",
            placeholder="לדוגמה: איך לשפר את אחוז התגובות?",
            key="chat_input"
        )
        
        if chat_input:
            with st.spinner("🤔 מיקי חושב..."):
                time.sleep(1)
            
            responses = {
                "תגובות": "💡 נסי לשלוח הודעות בימי שני-רביעי בין 9-11 בבוקר. הוסיפי אמוג׳י אחד בכותרת ותראי שיפור של 25%!",
                "עלות": "💰 יש לך אפשרות לחסוך $30 בחודש אם תעברי ל-Apollo Basic. התשואה שלך לא תיפגע!",
                "התאמה": "🎯 הפעילי את מצב הטורבו בחיפוש והגדירי רדיוס של 50 ק״מ. זה ירחיב את המאגר ב-40%!",
                "default": "🤗 מעולה! אני כאן כדי לעזור. תני לי לבדוק את זה ואחזור אלייך עם תשובה מדויקת..."
            }
            
            response = responses.get(
                next((key for key in responses if key in chat_input.lower()), 'default')
            )
            
            st.success(f"מיקי: {response}")
            
            # הצעות המשך
            st.caption("💡 אולי גם מעניין אותך:")
            suggestion_cols = st.columns(3)
            suggestions = ["📊 דוח ביצועים", "🎯 טיפים להתאמות", "💰 אופטימיזציה"]
            
            for i, suggestion in enumerate(suggestions):
                with suggestion_cols[i]:
                    if st.button(suggestion, key=f"suggestion_{i}"):
                        st.info(f"פותח {suggestion}...")

# סקריפט לרענון אוטומטי
st.markdown("""
<script>
    // רענון אוטומטי כל 5 דקות
    setTimeout(function(){
        window.location.reload();
    }, 300000);
</script>
""", unsafe_allow_html=True) 