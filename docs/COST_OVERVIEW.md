# COST & USAGE – ‏מעקב עלויות חכם

מטרה: לראות בזמן-אמת כמה עולה לנו כל שירות, לקבל התראות חריגה, ולבצע סימולציה להתרחבות.

---
## 1. שירותים בתשלום
| שירות | מה מחושב | היכן בודקים | עלות בסיסית |
|-------|----------|-------------|--------------|
| OpenAI | ‎$/tokens | https://platform.openai.com/usage | GPT-4o ‎$10/מיליון‬ tokens |
| Streamlit Cloud Pro | ‎$/חודש | Billing בלשונית Settings | ‎$25/user |
| Twilio WhatsApp | ‎$/message | Console › Usage | ‎$0.005 / הודעה יוצאת |
| Namecheap Domain | ‎$/שנה | Dashboard › Subscriptions | ‎$34.98/yr |

---
## 2. איך מושכים נתונים אוטומטית

1. **OpenAI** – קובץ `scripts/openai_usage.py` משתמש ב-`OPENAI_API_KEY` ומוריד CSV יומי.
2. **Twilio** – `scripts/twilio_usage.py` עם `TWILIO_ACCOUNT_SID` + `AUTH_TOKEN` קורא API UsageRecords.
3. **Google Sheet Dashboard** – הסקריפטים דוחפים נתונים באמצעות `gspread` לטאב "DailyCosts".

> כל הסקריפטים מוזנים ע"י ‎crontab‎ ב-Streamlit Cloud (Settings → Advanced → Scheduled jobs).

---
## 3. תרחיש סימולציה (דוגמא)
```
users            = 1000
avg_prompts/day  = 4
avg_tokens       = 800   # לטקסט + צ'אט
openai_cost      = users * avg_prompts * avg_tokens/1000 * 0.01  # $/1K tokens
whatsapp_msgs    = users * 1.5
whatsapp_cost    = whatsapp_msgs * 0.005
monthly_total    = openai_cost + whatsapp_cost + 25  # Streamlit Pro
print(monthly_total)
```

---
## 4. התראות חריגה
מוגדרות ב-`alert_router.py`:
- ‎> ‎$50 ביום → WhatsApp admin
- חריגת ‎HTTP 429‎ ב-OpenAI → In-App + Slack

---
## 5. צעדים הבאים
- ‎[ ] לחבר Google Sheet `MeUnique_Costs`
- ‎[ ] להגדיר cron ב-Streamlit Cloud (Every 6h)
- ‎[ ] להוסיף גרף קוֹסט ב-Admin Panel 