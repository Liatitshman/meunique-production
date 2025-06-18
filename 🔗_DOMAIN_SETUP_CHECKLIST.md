# 🔗 צ'קליסט הכנת דומיין - meunique.io

## 📊 סטטוס הדומיין
- ✅ **דומיין נרכש:** meunique.io
- ✅ **תשלום:** $34.98/שנה
- ⏳ **ממתין:** חיבור לשרת

---

## 🎯 שלבים להכנת הדומיין

### 1️⃣ **בדיקת בעלות על הדומיין**
```bash
# בדוק מידע WHOIS
whois meunique.io

# בדוק DNS
nslookup meunique.io
```

### 2️⃣ **הכנה להעלאה - 3 אפשרויות**

#### אופציה A: Vercel (מומלץ!)
```bash
# 1. התקן Vercel
npm install -g vercel

# 2. צור חשבון Vercel
# https://vercel.com/signup

# 3. העלה את הפרויקט
vercel

# 4. חבר דומיין בדשבורד
# Settings > Domains > Add meunique.io
```

#### אופציה B: Streamlit Cloud (חינם!)
1. העלה ל-GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/meunique
   git push -u origin main
   ```

2. כנס ל: https://streamlit.io/cloud
3. חבר את הרפו
4. הוסף דומיין מותאם אישית

#### אופציה C: Heroku
```bash
# 1. צור Procfile
echo "web: streamlit run 💡_LIAT_MEUNIQUE_SYSTEM.py --server.port $PORT" > Procfile

# 2. צור requirements.txt
pip freeze > requirements.txt

# 3. העלה
heroku create meunique
git push heroku main

# 4. חבר דומיין
heroku domains:add meunique.io
```

---

## 🔧 הגדרות DNS נדרשות

### לVercel:
```
Type: A
Name: @
Value: 76.76.21.21

Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

### לStreamlit Cloud:
```
Type: CNAME
Name: @
Value: YOUR-APP.streamlitapp.com

Type: CNAME  
Name: www
Value: YOUR-APP.streamlitapp.com
```

### לHeroku:
```
Type: CNAME
Name: @
Value: YOUR-APP.herokuapp.com

Type: CNAME
Name: www
Value: YOUR-APP.herokuapp.com
```

---

## ✅ צ'קליסט לפני Go-Live

### הכנת קבצים:
- [ ] קובץ `.env` עם כל המפתחות
- [ ] קובץ `requirements.txt` מעודכן
- [ ] קובץ `.gitignore` (לא לכלול .env!)
- [ ] README.md עם הוראות התקנה

### בדיקות אבטחה:
- [ ] אין מפתחות חשופים בקוד
- [ ] כל ה-inputs מסוננים
- [ ] HTTPS מופעל
- [ ] Rate limiting מוגדר

### בדיקות פונקציונליות:
- [ ] כל ה-APIs עובדים
- [ ] הממשק טוען נכון
- [ ] גיבוי אוטומטי פועל
- [ ] הצ'אט החכם זמין

---

## 🚀 הרצה מקומית לבדיקה

### בטרמינל 1:
```bash
cd /Users/liattishman/Desktop/🧠\ Agent_Navigator_Cursor_Sync\ 
python3 -m streamlit run 💡_LIAT_MEUNIQUE_SYSTEM.py
```
**כתובת:** http://localhost:8501

### בטרמינל 2:
```bash
python3 -m streamlit run 💡_LIAT_SMART_CHAT_GUIDE.py --server.port 8502
```
**כתובת:** http://localhost:8502

---

## 📱 בדיקה במובייל

1. **ברשת מקומית:**
   - מצא את ה-IP שלך: `ifconfig | grep inet`
   - גלוש מהנייד ל: `http://YOUR_IP:8501`

2. **עם ngrok:**
   ```bash
   ngrok http 8501
   ```
   - קבל URL ציבורי לבדיקה

---

## 🎉 סיכום

**הדומיין meunique.io מוכן לחיבור!**

נשארו רק 3 שלבים:
1. **בחר פלטפורמה** (Vercel/Streamlit/Heroku)
2. **העלה את הקוד** (10 דקות)
3. **חבר את הדומיין** (5 דקות)

**תוך 30 דקות את Live! 🚀** 