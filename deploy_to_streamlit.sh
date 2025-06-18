#!/bin/bash

echo "🚀 העלאה אוטומטית של MeUnique"
echo "================================"

# בדיקה אם מחובר ל-GitHub
if ! gh auth status &>/dev/null; then
    echo "❌ לא מחובר ל-GitHub"
    echo "👉 רץ: gh auth login --web"
    exit 1
fi

echo "✅ מחובר ל-GitHub"

# יוצר רפו אם לא קיים
echo "📦 יוצר repository..."
gh repo create meunique --public --description "MeUnique AI - Israeli Tech Recruitment Platform" 2>/dev/null || echo "Repository כבר קיים"

# מוסיף remote אם לא קיים
git remote add origin https://github.com/$(gh api user -q .login)/meunique.git 2>/dev/null || echo "Remote כבר קיים"

# שומר שינויים
echo "💾 שומר שינויים..."
git add .
git commit -m "Update configuration and deployment files" || echo "אין שינויים חדשים"

# דוחף לGitHub
echo "📤 מעלה ל-GitHub..."
git push -u origin main --force

# מקבל את הURL
GITHUB_USER=$(gh api user -q .login)
REPO_URL="https://github.com/$GITHUB_USER/meunique"

echo ""
echo "✅ ✅ ✅ הועלה בהצלחה! ✅ ✅ ✅"
echo ""
echo "📍 הפרויקט שלך ב-GitHub:"
echo "🔗 $REPO_URL"
echo ""
echo "🎯 עכשיו תורך - 3 צעדים פשוטים:"
echo ""
echo "1️⃣  פתחי את: https://streamlit.io/cloud"
echo "2️⃣  לחצי 'New app' ובחרי:"
echo "    • Repository: $GITHUB_USER/meunique"
echo "    • Main file: 💡_LIAT_MEUNIQUE_SYSTEM.py"
echo "3️⃣  הוסיפי את הSecrets מהקובץ .streamlit/secrets.toml"
echo ""
echo "💡 תוך 5 דקות האתר שלך יהיה חי ב: https://meunique.io"
echo ""

# פותח בדפדפן
echo "🌐 פותח את GitHub..."
open "$REPO_URL"

echo "🌐 פותח את Streamlit Cloud..."
open "https://streamlit.io/cloud" 