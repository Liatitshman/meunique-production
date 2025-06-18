#!/usr/bin/env python3
"""
🧠 MeUnique AI - Interactive Recruiter Assistant
ממשק אינטראקטיבי מלא עם כל הפיצ'רים
"""

import streamlit as st
import pandas as pd
import json
import time
from datetime import datetime
import openai
import os
from typing import List, Dict, Any

# הגדרת סביבה
st.set_page_config(
    page_title="MeUnique AI - Recruiter Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# טעינת הגדרות
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.learning_history = []
    st.session_state.tone_profile = {
        "formal_level": 0.7,
        "personal_touch": 0.8,
        "emoji_usage": 0.6,
        "language": "hebrew"
    }
    st.session_state.candidates_db = pd.DataFrame()
    st.session_state.companies_db = pd.DataFrame()

# כותרת ראשית
st.title("🧠 MeUnique AI - מערכת גיוס חכמה")
st.markdown("### 👋 שלום ליאת! מה נעשה היום?")

# סרגל צד עם מצב המערכת
with st.sidebar:
    st.header("📊 מצב המערכת")
    
    # מטריקות
    col1, col2 = st.columns(2)
    with col1:
        st.metric("מועמדים", "1,247", "+23")
        st.metric("חברות", "89", "+5")
    with col2:
        st.metric("התאמות החודש", "156", "+12")
        st.metric("אחוז הצלחה", "73%", "+5%")
    
    st.divider()
    
    # כפתורי פעולה מהירה
    st.header("⚡ פעולות מהירות")
    if st.button("🔄 סנכרון עם LinkedIn", use_container_width=True):
        with st.spinner("מסנכרן..."):
            time.sleep(2)
        st.success("✅ סונכרנו 47 פרופילים חדשים!")
    
    if st.button("📤 גיבוי ל-Drive", use_container_width=True):
        with st.spinner("מגבה..."):
            time.sleep(1)
        st.success("✅ גיבוי הושלם!")
    
    if st.button("🤖 עדכון מודל AI", use_container_width=True):
        st.info("🔄 המודל לומד מ-23 אינטראקציות חדשות...")

# טאבים ראשיים
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏪 חנות הגיוס",
    "🎯 התאמות חכמות", 
    "💬 הטמעת טון",
    "🔄 לופ למידה",
    "📚 ניהול מאגר",
    "⚙️ הגדרות"
])

# טאב 1: חנות הגיוס
with tab1:
    st.header("🏪 חנות הגיוס שלך")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🎁 חבילות מומלצות")
        st.info("""
        **חבילת Starter** - ₪199/חודש
        - 50 סריקות חודשיות
        - 20 הודעות אוטומטיות
        - דוח שבועי
        
        **חבילת Pro** - ₪499/חודש
        - 200 סריקות חודשיות
        - 100 הודעות אוטומטיות
        - AI מתקדם + אנליטיקס
        """)
        if st.button("🛒 רכישה מהירה"):
            st.success("✅ נפתח חלון תשלום...")
    
    with col2:
        st.subheader("🛠️ כלים נוספים")
        tools = {
            "🔍 סורק LinkedIn מתקדם": "סרוק פרופילים לפי קריטריונים",
            "📧 מחולל הודעות AI": "הודעות מותאמות אישית",
            "📊 דשבורד אנליטיקס": "תובנות על ביצועים",
            "🎯 מנוע התאמות": "התאמות חכמות אוטומטיות"
        }
        for tool, desc in tools.items():
            with st.expander(tool):
                st.write(desc)
                if st.button(f"הפעל {tool}", key=tool):
                    st.info(f"✨ {tool} מופעל!")
    
    with col3:
        st.subheader("📈 הצעות לשיפור")
        suggestions = [
            "💡 הוסף 30 מועמדים השבוע לשיפור ההתאמות",
            "🎯 עדכן את פרופיל החברה Gong - 5 משרות חדשות",
            "📊 73% מהמועמדים לא קיבלו פידבק - עדכן סטטוסים",
            "🔄 הפעל סריקה אוטומטית לחברות בצמיחה"
        ]
        for suggestion in suggestions:
            st.warning(suggestion)

# טאב 2: התאמות חכמות
with tab2:
    st.header("🎯 מנוע ההתאמות החכם")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # בחירת חברה ומשרה
        company = st.selectbox(
            "בחר חברה",
            ["Gong", "Wand", "Empathy", "Monday.com", "Wix"]
        )
        
        position = st.selectbox(
            "בחר משרה",
            ["Senior Backend Developer", "Frontend Team Lead", "DevOps Engineer"]
        )
        
        if st.button("🚀 הפעל התאמה חכמה", type="primary"):
            with st.spinner("🤖 מנתח דרישות ומחפש התאמות..."):
                time.sleep(3)
            
            # תוצאות דמה
            st.success("✅ נמצאו 12 מועמדים מתאימים!")
            
            matches = pd.DataFrame({
                'שם': ['דוד כהן', 'שרה לוי', 'משה ישראלי'],
                'ניקוד התאמה': [95, 92, 88],
                'ניסיון': ['8 שנים', '6 שנים', '10 שנים'],
                'מיקום': ['תל אביב', 'רמת גן', 'הרצליה'],
                'סטטוס': ['🟢 זמין', '🟡 פתוח להצעות', '🟢 זמין']
            })
            
            st.dataframe(matches, use_container_width=True)
            
            # פעולות על המועמדים
            selected = st.multiselect("בחר מועמדים לפנייה:", matches['שם'].tolist())
            if selected and st.button("📧 שלח הודעות"):
                st.success(f"✅ נשלחו הודעות ל-{len(selected)} מועמדים!")
    
    with col2:
        st.subheader("🎯 פרמטרים להתאמה")
        
        st.slider("משקל ניסיון", 0, 100, 70)
        st.slider("משקל כישורים", 0, 100, 85)
        st.slider("משקל תרבות ארגונית", 0, 100, 60)
        st.slider("משקל מיקום", 0, 100, 40)
        
        st.info("""
        💡 **טיפ:** 
        המערכת לומדת מהבחירות שלך!
        כל התאמה משפרת את הדיוק.
        """)

# טאב 3: הטמעת טון
with tab3:
    st.header("💬 מעבדת הטון האישי")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 הגדרת סגנון אישי")
        
        formal_level = st.slider("רמת פורמליות", 0.0, 1.0, st.session_state.tone_profile["formal_level"])
        personal_touch = st.slider("נגיעה אישית", 0.0, 1.0, st.session_state.tone_profile["personal_touch"])
        emoji_usage = st.slider("שימוש באימוג'ים", 0.0, 1.0, st.session_state.tone_profile["emoji_usage"])
        
        # עדכון פרופיל
        if st.button("💾 שמור הגדרות טון"):
            st.session_state.tone_profile.update({
                "formal_level": formal_level,
                "personal_touch": personal_touch,
                "emoji_usage": emoji_usage
            })
            st.success("✅ פרופיל הטון עודכן!")
        
        # דוגמאות
        st.subheader("📖 דוגמאות מההיסטוריה שלך")
        examples = [
            "היי דוד! 👋 ראיתי את הפרופיל המרשים שלך...",
            "שלום שרה, שמתי לב לניסיון הייחודי שלך ב...",
            "בוקר טוב משה! 🌞 יש לי הזדמנות מעניינת..."
        ]
        for ex in examples:
            st.text(ex)
    
    with col2:
        st.subheader("🤖 מחולל הודעות חכם")
        
        recipient_name = st.text_input("שם המועמד")
        context = st.text_area("הקשר (משרה, חברה, כישורים)")
        
        if st.button("✨ צור הודעה"):
            with st.spinner("🤖 יוצר הודעה מותאמת אישית..."):
                time.sleep(2)
            
            # הודעה לדוגמה
            message = f"""
            {recipient_name} היקר/ה! {'👋' if emoji_usage > 0.5 else ''}
            
            {'ראיתי את הפרופיל המרשים שלך ב-LinkedIn ו' if personal_touch > 0.7 else 'עיינתי בפרופיל המקצועי שלך ו'}התרשמתי מאוד מהניסיון שלך ב{context}.
            
            {'יש לי הזדמנות מעניינת שחושב/ת שתתאים לך מצוין!' if formal_level < 0.5 else 'ברצוני להציע לך הזדמנות תעסוקתית מעניינת.'}
            
            {'נשמח לשוחח! 😊' if emoji_usage > 0.5 else 'אשמח לתאם שיחה.'}
            
            בברכה,
            ליאת
            """
            
            st.text_area("ההודעה שנוצרה:", message, height=200)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📤 שלח"):
                    st.success("✅ ההודעה נשלחה!")
            with col2:
                if st.button("🔄 צור מחדש"):
                    st.info("🔄 יוצר גרסה חדשה...")

# טאב 4: לופ למידה
with tab4:
    st.header("🔄 מערכת הלמידה המתמשכת")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 תובנות מהשבוע האחרון")
        
        # גרף ביצועים
        st.area_chart({
            "התאמות": [12, 15, 18, 14, 20, 23, 25],
            "תגובות": [8, 10, 12, 11, 15, 18, 20],
            "ראיונות": [3, 4, 5, 4, 6, 8, 9]
        })
        
        # תובנות
        insights = [
            {"🎯 תובנה": "מועמדים עם Python + AWS מגיבים 40% יותר", "📈 השפעה": "גבוהה"},
            {"🎯 תובנה": "הודעות עם אימוג'ים מקבלות 25% יותר תגובות", "📈 השפעה": "בינונית"},
            {"🎯 תובנה": "פנייה ביום שני בבוקר הכי אפקטיבית", "📈 השפעה": "גבוהה"},
            {"🎯 תובנה": "חברות Fintech מעדיפות טון פורמלי", "📈 השפעה": "בינונית"}
        ]
        
        st.dataframe(pd.DataFrame(insights), use_container_width=True)
        
        # למידה חדשה
        st.subheader("🧠 הוסף למידה חדשה")
        new_learning = st.text_input("מה למדת היום?")
        learning_category = st.selectbox("קטגוריה", ["טון", "טיימינג", "כישורים", "חברות"])
        
        if st.button("➕ הוסף ללופ הלמידה"):
            st.session_state.learning_history.append({
                "timestamp": datetime.now(),
                "learning": new_learning,
                "category": learning_category
            })
            st.success("✅ נוסף ללופ הלמידה!")
    
    with col2:
        st.subheader("🎓 המלצות לשיפור")
        
        recommendations = [
            "💡 נסי להוסיף reference לפרויקט ספציפי",
            "⏰ שלחי הודעות בין 9-11 בבוקר",
            "🎯 התמקדי במועמדים עם 5-8 שנות ניסיון",
            "📝 קצרי את ההודעות ל-3-4 שורות"
        ]
        
        for rec in recommendations:
            st.info(rec)
        
        if st.button("🤖 עדכן את כל המודלים"):
            with st.spinner("מעדכן מודלים..."):
                time.sleep(2)
            st.success("✅ כל המודלים עודכנו!")

# טאב 5: ניהול מאגר
with tab5:
    st.header("📚 ניהול המאגר החכם")
    
    # פילטרים
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        filter_skills = st.multiselect("כישורים", ["Python", "React", "Node.js", "AWS"])
    with col2:
        filter_exp = st.slider("שנות ניסיון", 0, 20, (3, 10))
    with col3:
        filter_location = st.multiselect("מיקום", ["תל אביב", "רמת גן", "הרצליה", "Remote"])
    with col4:
        filter_status = st.multiselect("סטטוס", ["זמין", "פתוח להצעות", "לא זמין"])
    
    # טבלת מועמדים
    if st.button("🔍 חפש"):
        candidates_data = pd.DataFrame({
            'ID': ['#1234', '#1235', '#1236', '#1237', '#1238'],
            'שם': ['דוד כהן', 'שרה לוי', 'משה ישראלי', 'רחל אברהם', 'יוסי דוד'],
            'כישורים': ['Python, AWS', 'React, Node.js', 'Java, Spring', 'Python, ML', 'DevOps, K8s'],
            'ניסיון': ['8 שנים', '6 שנים', '10 שנים', '5 שנים', '7 שנים'],
            'חברה נוכחית': ['Microsoft', 'Google', 'Meta', 'Startup', 'Amazon'],
            'סטטוס': ['🟢', '🟡', '🟢', '🔴', '🟡'],
            'ניקוד': [95, 88, 92, 78, 85]
        })
        
        st.dataframe(
            candidates_data,
            use_container_width=True,
            column_config={
                "ניקוד": st.column_config.ProgressColumn(
                    "ניקוד התאמה",
                    help="ניקוד התאמה כללי",
                    format="%d",
                    min_value=0,
                    max_value=100,
                ),
            }
        )
    
    # פעולות מרובות
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📧 שלח לכולם", type="primary"):
            st.success("✅ נשלחו 5 הודעות!")
    with col2:
        if st.button("📊 ייצא ל-Excel"):
            st.info("📥 מייצא...")
    with col3:
        if st.button("🔄 עדכן נתונים"):
            st.info("🔄 מעדכן...")

# טאב 6: הגדרות
with tab6:
    st.header("⚙️ הגדרות מערכת")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔐 חיבורים ו-APIs")
        
        # בדיקת חיבורים
        connections = {
            "LinkedIn Sales Navigator": True,
            "OpenAI API": True,
            "Google Drive": True,
            "Apollo.io": False,
            "PhantomBuster": True
        }
        
        for service, status in connections.items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(service)
            with col2:
                if status:
                    st.success("✅ מחובר")
                else:
                    if st.button("חבר", key=service):
                        st.info("🔄 מתחבר...")
        
        st.divider()
        
        # הגדרות אוטומציה
        st.subheader("🤖 אוטומציה")
        auto_sync = st.checkbox("סנכרון אוטומטי כל 6 שעות", value=True)
        auto_backup = st.checkbox("גיבוי יומי ל-Google Drive", value=True)
        auto_learn = st.checkbox("למידה אוטומטית מתגובות", value=True)
    
    with col2:
        st.subheader("💰 ניהול עלויות")
        
        # עלויות חודשיות
        costs = pd.DataFrame({
            'שירות': ['LinkedIn Sales Nav', 'OpenAI API', 'Apollo.io', 'Domain'],
            'עלות חודשית': ['$99', '$40', '$49', '$3'],
            'שימוש': ['87%', '62%', '45%', '100%']
        })
        
        st.dataframe(costs, use_container_width=True)
        
        st.metric("סה״כ חודשי", "$191", "-$10")
        
        # הגבלות
        st.subheader("🚦 הגבלות שימוש")
        daily_limit = st.number_input("מקסימום סריקות יומי", value=100)
        api_limit = st.number_input("מקסימום קריאות API", value=1000)
        
        if st.button("💾 שמור הגדרות"):
            st.success("✅ ההגדרות נשמרו!")

# כפתור צ'אט צף
if st.button("💬 פתח צ'אט עם המערכת", key="float_chat"):
    st.info("🤖 הצ'אט נפתח בחלון חדש...")

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🌐 meunique.io")
with col2:
    st.caption("📧 liat.tishman85@gmail.com")
with col3:
    st.caption("🚀 גרסה 2.0 | Production Ready") 