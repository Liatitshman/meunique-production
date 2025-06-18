#!/bin/bash

echo "🔄 מסנכרן ל-MeUnique-AI-Private"
echo "================================"
echo ""

# הגדרות
GITHUB_USER="Liatitshman"
REPO_NAME="MeUnique-AI-Private"
REPO_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"

# צבעים
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${YELLOW}🔗 מתחבר ל: $REPO_URL${NC}"

# הסר remote קיים
git remote remove origin 2>/dev/null

# הוסף remote חדש
git remote add origin $REPO_URL

# שמור את כל השינויים
echo -e "${YELLOW}💾 שומר שינויים...${NC}"
git add .

# commit עם תיאור מפורט
COMMIT_MSG="🚀 Update MeUnique System - Production Ready

Updates:
- ✅ Streamlit UI ready (💡_LIAT_MEUNIQUE_SYSTEM.py)
- ✅ Chat guide system (💡_LIAT_SMART_CHAT_GUIDE.py) 
- ✅ Auto backup system (auto_sync_to_drive.py)
- ✅ All API keys configured in .streamlit/secrets.toml
- ✅ Requirements.txt updated
- ✅ Deployment scripts ready
- ✅ Public repository configured

Technical Specs:
- Framework: Streamlit 1.29.0
- AI: OpenAI GPT-4
- APIs: LinkedIn, Apollo, PhantomBuster
- Backup: Google Drive API
- Domain: meunique.io (ready for connection)"

git commit -m "$COMMIT_MSG" || echo "אין שינויים חדשים"

# דחוף לGitHub
echo -e "${YELLOW}📤 דוחף לGitHub...${NC}"
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ ✅ ✅ סנכרון הושלם בהצלחה! ✅ ✅ ✅${NC}"
    echo ""
    echo -e "${GREEN}📍 הפרויקט שלך:${NC}"
    echo -e "${GREEN}👉 $REPO_URL${NC}"
    echo ""
    echo -e "${YELLOW}🎯 השלבים הבאים:${NC}"
    echo "1️⃣  כנסי ל: https://streamlit.io/cloud"
    echo "2️⃣  לחצי 'New app'"
    echo "3️⃣  בחרי:"
    echo "    • Repository: $GITHUB_USER/$REPO_NAME"
    echo "    • Branch: main"
    echo "    • Main file: 💡_LIAT_MEUNIQUE_SYSTEM.py"
    echo "4️⃣  לחצי Deploy"
    echo ""
    echo -e "${RED}🔐 חשוב! הוסיפי את הSecrets:${NC}"
    echo "   Settings > Secrets > הדביקי מ-.streamlit/secrets.toml"
    echo ""
    echo -e "${GREEN}💡 תוך 5 דקות את LIVE ב-meunique.io!${NC}"
    echo ""
    
    # פתח את הדפים הרלוונטיים
    open "$REPO_URL"
    open "https://streamlit.io/cloud"
else
    echo ""
    echo -e "${RED}❌ בעיה בדחיפה${NC}"
    echo "נסי להתחבר מחדש:"
    echo "gh auth login"
    echo ""
    echo "או בדקי שיש לך הרשאות ל-$REPO_URL"
fi 