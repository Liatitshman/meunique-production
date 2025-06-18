#!/bin/bash

echo "🧹 מנקה היסטוריה ומעלה מחדש"
echo "=============================="

# יצירת branch חדש לגמרי
git checkout --orphan fresh-start

# הוסף את כל הקבצים
git add .

# commit חדש
git commit -m "🎉 Fresh start - MeUnique Production Ready"

# מחק את הbranch הישן
git branch -D main 2>/dev/null

# שנה שם לmain
git branch -m main

# דחוף בכוח
git push origin main --force

echo "✅ הושלם! היסטוריה נקייה"
echo "🚀 עכשיו לך ל: https://streamlit.io/cloud" 