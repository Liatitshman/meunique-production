# 📋 רשימת בדיקה מהירה - Setup מלא

## ✅ מה שכבר עשית:
- [x] רכשת דומיין meunique.io ✨
- [x] הגדרת 301 redirect לאפליקציה
- [x] העלאת קוד ל-GitHub
- [x] פריסה ל-Streamlit Cloud
- [x] מצאת חלון Secrets בהגדרות

---

## 🔑 מה שנותר לעשות:

### 1. הגדרת Secrets (5 דקות)
- [ ] פתחי `docs/SECRETS_TEMPLATE.toml`
- [ ] מצאי מפתח OpenAI: https://platform.openai.com/api-keys
- [ ] מצאי פרטי Twilio: https://console.twilio.com/
- [ ] הדביקי בחלון Secrets ב-Streamlit

### 2. הגדרת Google Sheets (אופציונלי)
- [ ] צרי Google Sheet לעלויות
- [ ] צרי Service Account ב-Google Cloud
- [ ] השלימי ב-Secrets

### 3. הגדרת Scheduled Jobs (אופציונלי)
- [ ] לכי להגדרות Streamlit → Scheduled Jobs
- [ ] הוסיפי: `python3 scripts/openai_usage.py`
- [ ] תזמני ל-8:00 בבוקר יומית

---

## 🎯 הבדיקה הסופית:
1. **בדקי שהאפליקציה רצה** ללא שגיאות
2. **נסי לשלוח הודעה** לבוט
3. **ודאי שה-redirect** מ-meunique.io עובד

---

## 🆘 אם משהו לא עובד:
- **שגיאת API Key**: בדקי שהמפתח מתחיל ב-`sk-`
- **שגיאת Twilio**: בדקי שה-SID מתחיל ב-`AC`
- **שגיאת JSON**: בדקי שה-JSON תקין (מתחיל ב-`{` וגומר ב-`}`)

**🔗 קישור מהיר לאפליקציה:** https://meuniqueai.streamlit.app 