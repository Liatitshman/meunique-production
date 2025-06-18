#!/bin/bash

echo "🚀 מתחיל התקנה והרצה של MeUnique..."
echo "=================================="

# בדיקה אם Python3 מותקן
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 לא מותקן. מתקין..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install python3
    else
        echo "אנא התקן Python3 ידנית"
        exit 1
    fi
fi

echo "✅ Python3 מותקן"

# התקנת pip אם חסר
if ! python3 -m pip --version &> /dev/null; then
    echo "📦 מתקין pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    rm get-pip.py
fi

echo "📦 מתקין חבילות נדרשות..."
python3 -m pip install --upgrade pip
python3 -m pip install streamlit pandas plotly openai python-dotenv

# בדיקה אם קובץ .env קיים
if [ ! -f .env ]; then
    echo "⚠️  קובץ .env לא נמצא!"
    echo "צור קובץ .env עם המפתחות שלך"
    exit 1
fi

echo "✅ הכל מוכן!"
echo ""
echo "🎯 מריץ את המערכת..."
echo "=================================="
echo "🌐 כתובת: http://localhost:8501"
echo "📱 לעצירה: Ctrl+C"
echo "=================================="

# הרצת המערכת
python3 -m streamlit run 💡_LIAT_MEUNIQUE_SYSTEM.py 