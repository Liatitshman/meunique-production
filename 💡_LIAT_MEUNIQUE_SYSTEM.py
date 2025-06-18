#!/usr/bin/env python3
"""
💡 LIAT's MeUnique AI - Israeli Tech Recruitment System
מערכת גיוס מותאמת אישית לליאת עם פיצ'רים ישראליים מתקדמים
"""

import streamlit as st
import pandas as pd
import json
import time
from datetime import datetime
import os

# הגדרות
st.set_page_config(
    page_title="💡 LIAT MeUnique - Israeli Tech Recruiter",
    page_icon="💡",
    layout="wide"
)

# כותרת ראשית
st.title("💡 LIAT's MeUnique - Israeli Tech Recruiter")
st.caption(f"🕐 {datetime.now().strftime('%H:%M')} | ☀️ תל אביב 28°C | 💪 מצב: קומבינה מקסימלית")

# טאבים ראשיים
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 צייד חכם",
    "🧠 מאגר דינמי", 
    "💬 תקשורת חכמה",
    "📊 אנליטיקס",
    "⚙️ העדפות"
])

with tab1:
    st.header("🎯 צייד המועמדים החכם")
    
    # חיפוש חכם
    search_query = st.text_area(
        "תאר/י את המועמד האידיאלי",
        placeholder="מפתח פולסטאק עם ניסיון בסטארטאפ, יוצא 8200..."
    )
    
    if st.button("🚀 חפש מועמדים", type="primary"):
        with st.spinner("🔍 מחפש..."):
            time.sleep(2)
        st.success("✅ נמצאו 23 מועמדים!")
        
        # תוצאות דמה
        candidates = pd.DataFrame({
            'שם': ['דני כהן', 'מיכל לוי', 'רון ישראלי'],
            'יחידה': ['8200', 'ממרם', 'תלפיות'],
            'חברה': ['Wix', 'Monday', 'Startup'],
            'התאמה': [95, 92, 88]
        })
        
        st.dataframe(candidates)

with tab2:
    st.header("🧠 ניהול מאגר דינמי")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("סה״כ מועמדים", "1,247", "+23")
    with col2:
        st.metric("פעילים", "423", "+12")
    with col3:
        st.metric("השמות החודש", "8", "+2")
    
    # כלי ניהול
    if st.button("🔄 רענון אוטומטי"):
        st.info("מעדכן סטטוסים...")

with tab3:
    st.header("💬 יצירת הודעות חכמות")
    
    candidate_name = st.text_input("שם המועמד")
    tone = st.select_slider("סגנון", ["רשמי", "מקצועי", "ידידותי", "ישראלי"])
    
    if st.button("✨ צור הודעה"):
        message = f"היי {candidate_name}! ראיתי את הפרופיל שלך ויש לי משהו מעניין..."
        st.text_area("ההודעה:", message)

with tab4:
    st.header("📊 אנליטיקס ותובנות")
    
    # מטריקות
    metrics = st.columns(4)
    with metrics[0]:
        st.metric("שיעור תגובה", "42%", "+5%")
    with metrics[1]:
        st.metric("זמן למילוי", "18 ימים", "-3")
    with metrics[2]:
        st.metric("ROI", "324%", "+45%")
    with metrics[3]:
        st.metric("יעילות", "87%", "+12%")

with tab5:
    st.header("⚙️ העדפות אישיות")
    
    st.text_input("שם", value="ליאת תשמן", disabled=True)
    auto_search = st.checkbox("חיפוש אוטומטי", value=True)
    
    if st.button("💾 שמור"):
        st.success("✅ נשמר!")

# Footer
st.divider()
st.caption("💡 MeUnique.io - Built for Liat with ❤️") 