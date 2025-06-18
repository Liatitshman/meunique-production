# 🎯 צעדים מהירים להעלאה - 10 דקות!

## 1️⃣ **יצירת Repository (אם עוד לא יצרת)**
בחלון שנפתח ב-GitHub:
- Repository name: `meunique-production` (או כל שם)
- Description: `MeUnique AI Platform`
- **חשוב:** סמן **Public** ✅
- לחץ: **Create repository**

## 2️⃣ **הרץ בטרמינל:**
```bash
./🚀_DEPLOY_TO_PRODUCTION.sh
```

כשישאל:
- שם משתמש: `Liatitshman`
- שם Repository: `meunique-production` (או מה שבחרת)

## 3️⃣ **בStreamlit Cloud (ייפתח אוטומטית):**
1. לחץ **"New app"**
2. בחר את הRepository שלך
3. Main file path: `💡_LIAT_MEUNIQUE_SYSTEM.py`
4. לחץ **"Deploy!"**

## 4️⃣ **הוסף Secrets (חשוב!):**
אחרי שהאפליקציה תתחיל לעלות:
1. לחץ על **⚙️ Settings**
2. לחץ על **"Secrets"**
3. פתח בטרמינל חדש: `cat .streamlit/secrets.toml`
4. העתק הכל והדבק
5. לחץ **"Save"**

## 5️⃣ **חבר את הדומיין:**
1. קבל את הURL (כמו: amazing-app-123.streamlit.app)
2. כנס לניהול הדומיין meunique.io
3. הוסף CNAME:
   - Type: CNAME
   - Name: @
   - Value: [הURL שקיבלת]

---

## ⏱️ **זמנים:**
- העלאה לGitHub: 1 דקה ✅
- Deploy בStreamlit: 3-5 דקות ⏳
- חיבור דומיין: 2 דקות ✅
- התפשטות DNS: עד 24 שעות ⏳

## 🎉 **זהו! בעוד 10 דקות את LIVE!**

כתובת זמנית: https://[your-app].streamlit.app
כתובת קבועה: https://meunique.io 