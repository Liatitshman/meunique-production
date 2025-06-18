#!/bin/bash

echo "🚀 העלאה לפרודקשיין - MeUnique"
echo "================================"
echo ""

# צבעים
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# בקש פרטים
echo -e "${YELLOW}📝 צריך כמה פרטים:${NC}"
read -p "👤 שם המשתמש שלך בGitHub: " GITHUB_USER
read -p "📁 שם הRepository החדש שיצרת: " REPO_NAME

# הסר remote קיים
git remote remove origin 2>/dev/null

# הוסף remote חדש
REPO_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"
echo -e "${BLUE}🔗 מתחבר ל: $REPO_URL${NC}"
git remote add origin $REPO_URL

# עבור ל-main branch
git checkout main 2>/dev/null || git checkout -b main

# שמור שינויים
echo -e "${YELLOW}💾 שומר את כל הקבצים...${NC}"
git add .
git commit -m "🎉 Initial commit - MeUnique Production Ready" || echo "No changes"

# דחוף לGitHub
echo -e "${YELLOW}📤 מעלה ל-GitHub...${NC}"
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ ✅ ✅ הועלה בהצלחה ל-GitHub! ✅ ✅ ✅${NC}"
    echo ""
    
    # פתח Streamlit Cloud
    echo -e "${BLUE}🌐 פותח את Streamlit Cloud...${NC}"
    open "https://streamlit.io/cloud"
    
    # פתח את הRepository
    echo -e "${BLUE}📂 פותח את הRepository...${NC}"
    open "$REPO_URL"
    
    echo ""
    echo -e "${GREEN}📋 השלבים הבאים:${NC}"
    echo ""
    echo "1️⃣  בStreamlit Cloud - לחץ 'New app'"
    echo "2️⃣  בחר:"
    echo "    • Repository: $GITHUB_USER/$REPO_NAME"
    echo "    • Branch: main"
    echo "    • Main file path: 💡_LIAT_MEUNIQUE_SYSTEM.py"
    echo "3️⃣  לחץ 'Deploy!'"
    echo ""
    echo -e "${RED}🔐 חשוב! אחרי שהאפליקציה תעלה:${NC}"
    echo "1. לחץ על ⚙️ Settings"
    echo "2. לחץ על Secrets"
    echo "3. העתק את כל התוכן מ: .streamlit/secrets.toml"
    echo "4. הדבק ולחץ Save"
    echo ""
    echo -e "${YELLOW}🌐 חיבור הדומיין meunique.io:${NC}"
    echo "1. קבל את הURL מStreamlit (משהו כמו: your-app.streamlit.app)"
    echo "2. כנס לניהול הדומיין שלך"
    echo "3. הוסף CNAME record:"
    echo "   • Name: @"
    echo "   • Value: your-app.streamlit.app"
    echo ""
    echo -e "${GREEN}💡 בעוד 10 דקות את תהיי LIVE ב: https://meunique.io 🎉${NC}"
    
    # צור קובץ עזר
    cat > DEPLOYMENT_INFO.txt << EOF
🚀 MeUnique Deployment Info
==========================

GitHub Repository: $REPO_URL
Streamlit App: https://share.streamlit.io/$GITHUB_USER/$REPO_NAME/main/💡_LIAT_MEUNIQUE_SYSTEM.py
Domain: meunique.io

Deployed at: $(date)

Next Steps:
1. Add secrets in Streamlit Cloud
2. Connect domain via CNAME
3. Test all features
4. Share with the world! 🎉
EOF

    echo ""
    echo -e "${GREEN}📄 נוצר קובץ DEPLOYMENT_INFO.txt עם כל הפרטים${NC}"
    
else
    echo ""
    echo -e "${RED}❌ משהו השתבש${NC}"
    echo "בדקי:"
    echo "1. שיצרת את הRepository ב-GitHub"
    echo "2. שהוא Public (לא Private)"
    echo "3. שהשם נכון: $GITHUB_USER/$REPO_NAME"
fi 