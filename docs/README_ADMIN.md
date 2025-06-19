# MeUnique – ‏מדריך אדמיני פשוט

ברוך/ה הבא/ה! כאן תמצאי בקצרה ובשפה "ללא כאבי-ראש" את כל מה שקורה בפרויקט – מה כבר עובד, מה עדיין בתהליך, ואיפה לוחצים.

## 1. מה רץ כרגע?

| מודול | מצב | איפה רואים | תלויות |
|-------|------|-------------|---------|
| דומיין `meunique.io` → ‎`meuniqueai.streamlit.app` | ✅ פעיל (301 Redirect) | בדפדפן | Namecheap Host Records |
| Smart-Tools Sidebar | ✅ רץ | סרגל-צד באפליקציה | OpenAI API Key |
| Bots (ProfileMapper …) | ✅ | "Select bot" בחלק העליון | ^ |
| Twilio WhatsApp Sandbox | 🟡 מוכן ‑ מחכה למפתחות | ‎Settings → Secrets | Account SID + Token |
| Dual-Bot + Alerts | ⏳ בתהליך ‑ אחרי Secrets | --- | Feature-Flag |

## 2. קבצי מפתח

```
meunique_english_app.py   # קובץ Streamlit הראשי
styles.css                # צבעים ופסטלים
scripts/                  # סקריפטים עזר (Sync, Cost…)
docs/                     # כל הקבצים המדריכים האלו
```

## 3. איפה לשמור מפתחות

Manage App → Secrets:
```
OPENAI_API_KEY = "sk-…"
[twilio]
account_sid="AC…"
auth_token="…"
from_whatsapp="whatsapp:+14155238886"
admin_phone  ="whatsapp:+972…"
```

## 4. זרימת עבודה קצרה
1. `git add . && git commit -m "msg" && git push` –
   Streamlit יבנה אוטומטית.
2. ב-Secrets מעדכנים מפתחות → Save.
3. מרעננים את האתר → רואים שינויים.

## 5. קשרי שירות וכלים
- **GitHub**: `Liatitshman/meunique-production` (branch `main`)
- **Streamlit Cloud**: https://share.streamlit.io (My apps → MeUnique)
- **Namecheap** (DNS): Domain List → `meunique.io` → Advanced DNS
- **Twilio Sandbox**: https://console.twilio.com → Messaging → Try it out → WhatsApp

## 6. TODO הקרוב
- ‎[ ] להדביק OPENAI_API_KEY
- ‎[ ] להדביק פרטי Twilio
- ‎[ ] לבדוק Build → Running
- ‎[ ] לאשר Pull-Request "Dual-Bot & Alerts"

> שמרי קובץ זה, הוא יתעדכן בכל Push אוטומטי. 