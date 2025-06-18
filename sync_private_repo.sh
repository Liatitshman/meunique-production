#!/bin/bash

echo "🔐 סנכרון עם Repository פרטי"
echo "============================"
echo ""

read -p "👤 שם המשתמש שלך בGitHub: " GITHUB_USER
read -p "📁 שם הRepository: " REPO_NAME

# בדיקה אם מחובר ל-GitHub
if ! gh auth status &>/dev/null; then
    echo ""
    echo "🔑 צריך להתחבר לGitHub..."
    gh auth login
fi

# הוסף remote
echo ""
echo "🔗 מתחבר ל: https://github.com/$GITHUB_USER/$REPO_NAME"
git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git

# שמור שינויים
git add .
git commit -m "Update all files for deployment" || true

# דחוף
echo ""
echo "📤 דוחף לRepository הפרטי..."
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ הצלחה!"
    echo ""
    echo "🎯 אפשרויות להעלאה:"
    echo ""
    echo "1️⃣ Vercel (תומך בפרטי + חינם!)"
    echo "   הרץ: vercel"
    echo ""
    echo "2️⃣ הפוך לPublic והשתמש בStreamlit Cloud"
    echo "   Settings > Danger Zone > Change visibility"
    echo ""
    echo "3️⃣ Heroku (תומך בפרטי)"
    echo "   heroku create $REPO_NAME"
    echo ""
    open "https://github.com/$GITHUB_USER/$REPO_NAME/settings"
else
    echo "❌ בעיה. נסי להתחבר מחדש:"
    echo "gh auth login"
fi 