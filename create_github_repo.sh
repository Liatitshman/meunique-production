#!/bin/bash

echo "🚀 מעלה את MeUnique ל-GitHub..."
echo "===================================="

# יוצר רפו ב-GitHub
gh repo create meunique --public --description "MeUnique AI - Israeli Tech Recruitment Platform" --source=. --remote=origin --push

# מוסיף שינויים נוספים אם יש
git add .
git commit -m "Add configuration files" || echo "No changes to commit"

# דוחף לGitHub
git push -u origin main

echo ""
echo "✅ הפרויקט הועלה בהצלחה!"
echo "🔗 כתובת: https://github.com/$(gh api user -q .login)/meunique"
echo ""
echo "🎯 השלב הבא: חבר ל-Streamlit Cloud"
echo "👉 https://streamlit.io/cloud" 