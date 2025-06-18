#!/bin/bash

echo "🔄 מסנכרן עם GitHub..."
echo "======================="

# בקש מהמשתמש את שם המשתמש שלו
read -p "👤 מה שם המשתמש שלך בGitHub? " GITHUB_USER

# בדוק אם יש remote
if ! git remote | grep -q origin; then
    echo "➕ מוסיף remote..."
    git remote add origin https://github.com/$GITHUB_USER/meunique.git
fi

# הצג את הremote
echo "📍 Remote URL:"
git remote -v

# שמור שינויים אם יש
git add .
git commit -m "Sync latest changes" || echo "אין שינויים חדשים"

# דחוף לGitHub
echo "📤 דוחף לGitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ סנכרון הושלם בהצלחה!"
    echo "🔗 https://github.com/$GITHUB_USER/meunique"
    echo ""
    echo "🎯 עכשיו כנסי ל-Streamlit Cloud:"
    echo "👉 https://streamlit.io/cloud"
    open "https://github.com/$GITHUB_USER/meunique"
else
    echo ""
    echo "❌ בעיה בדחיפה. נסי:"
    echo "1. וודאי שיש לך גישה לrepository"
    echo "2. אם הrepository פרטי, שני אותו לpublic"
    echo "3. נסי: git push --force origin main"
fi 