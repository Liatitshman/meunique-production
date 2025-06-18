#!/bin/bash

echo "🚀 סנכרון מהיר לGitHub"
echo "====================="
echo ""

# הסר remote קיים
git remote remove origin 2>/dev/null

echo "📝 צריך את הפרטים הבאים:"
echo ""
read -p "👤 שם המשתמש שלך בGitHub: " GITHUB_USER
read -p "📁 שם הRepository (ברירת מחדל: meunique): " REPO_NAME
REPO_NAME=${REPO_NAME:-meunique}

# הוסף remote
echo ""
echo "🔗 מתחבר ל: https://github.com/$GITHUB_USER/$REPO_NAME"
git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git

# שמור שינויים
git add .
git commit -m "Update all files" || true

# דחוף
echo ""
echo "📤 דוחף לGitHub..."
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ ✅ ✅ הצלחה! ✅ ✅ ✅"
    echo ""
    echo "🔗 הפרויקט שלך:"
    echo "👉 https://github.com/$GITHUB_USER/$REPO_NAME"
    echo ""
    echo "🎯 עכשיו:"
    echo "1. כנסי ל: https://streamlit.io/cloud"
    echo "2. חברי את: $GITHUB_USER/$REPO_NAME"
    echo "3. בחרי: 💡_LIAT_MEUNIQUE_SYSTEM.py"
    echo ""
    open "https://github.com/$GITHUB_USER/$REPO_NAME"
else
    echo ""
    echo "❌ משהו לא עבד. בדקי:"
    echo "1. שהRepository קיים בGitHub"
    echo "2. שיש לך הרשאות"
    echo "3. שהשם נכון: $GITHUB_USER/$REPO_NAME"
fi 