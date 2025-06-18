#!/bin/bash

echo "🚀 מפעיל את MeUnique..."
echo "=========================="

# נסה למצוא את streamlit
if command -v streamlit &> /dev/null; then
    streamlit run 💡_LIAT_MEUNIQUE_SYSTEM.py
elif command -v python3 &> /dev/null; then
    python3 -m streamlit run 💡_LIAT_MEUNIQUE_SYSTEM.py
else
    echo "❌ לא נמצא Python3!"
    echo "אנא התקיני Python3 מ: https://www.python.org/downloads/"
    exit 1
fi 