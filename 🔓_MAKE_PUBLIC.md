# 🔓 איך להפוך Repository לPublic

## למה צריך Public?
Streamlit Cloud **חינמי** עובד רק עם repositories ציבוריים.

## 🎯 שלבים להפוך לPublic:

### 1️⃣ **כנסי לRepository שלך**
https://github.com/YOUR_USERNAME/meunique

### 2️⃣ **לחצי על Settings** (⚙️)
נמצא בתפריט העליון

### 3️⃣ **גללי למטה ל"Danger Zone"**
בתחתית העמוד

### 4️⃣ **לחצי על "Change visibility"**

### 5️⃣ **בחרי "Make public"**

### 6️⃣ **אשרי**
- הקלידי את שם הRepository
- לחצי על הכפתור האדום

---

## 🔐 אם את רוצה להשאיר פרטי:

### אופציה 1: Streamlit Cloud Pro (בתשלום)
- $250/חודש
- תומך בrepositories פרטיים

### אופציה 2: Vercel (חינם עם פרטי!)
```bash
vercel
```
(כבר מותקן אצלך)

### אופציה 3: Heroku
- חינם עד 550 שעות בחודש
- תומך בפרטי

---

## 💡 המלצה:
**הפכי לPublic** - זה הכי קל ומהיר!
הקוד שלך ממילא לא מכיל סודות (הם ב-secrets.toml) 

## 🔴 **אופציה 1: אשר את המפתחות בGitHub (מהיר!)**

GitHub נתן לך לינק לאישור:
https://github.com/Liatitshman/MeUnique-AI-Private/security/secret-scanning/unblock-secret/2yhaJF0r8o87MPa7Zy1GulYHuwF

1. **לחץ על הלינק**
2. **אשר שאת רוצה לדחוף את המפתחות** (זה בסדר כי זה repository פרטי)
3. **חזור לכאן והרץ שוב:**
   ```bash
   git push -u origin main --force
   ```

## 🟢 **אופציה 2: צור Repository חדש (נקי לגמרי)** 

# אחרי שיצרת את הRepository
git push -u origin main --force && open https://streamlit.io/cloud