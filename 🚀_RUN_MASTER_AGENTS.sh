#!/bin/bash

# 🎯 MeUnique Master Agents System - Quick Start Script
# Built by: ליאת תשמן (Liat Tishman)

echo "🎯 Starting MeUnique Master Agents System..."
echo "👑 Master Agent: ליאת תשמן"
echo "👥 6 Smart Sourcing Agents Ready"
echo ""

# Check if Python and Streamlit are installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8 or higher."
    exit 1
fi

if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit not found. Installing..."
    pip install streamlit
fi

# Check if requirements are installed
echo "📦 Checking dependencies..."
pip install -r requirements.txt

# Set environment variables if .env exists
if [ -f .env ]; then
    echo "🔐 Loading environment variables..."
    export $(cat .env | xargs)
fi

# Kill any existing Streamlit processes on port 8501
echo "🔄 Cleaning up existing processes..."
lsof -ti:8501 | xargs kill -9 2>/dev/null || true

# Start the Master Agents System
echo "🚀 Launching MeUnique Master Agents System..."
echo "🌐 Local URL: http://localhost:8501"
echo "🌍 Production URL: https://meuniqueai.streamlit.app"
echo "🔗 Domain: https://meunique.io"
echo ""
echo "✨ Features:"
echo "   👑 Master Agent Command Center"
echo "   🤖 6 Specialized Sourcing Agents"
echo "   🎭 4 Dynamic Personality Modes"
echo "   💬 8 Organized Chat Categories"
echo "   📊 Real-time Analytics Dashboard"
echo "   💰 Cost Optimization ($1,100/month savings)"
echo ""
echo "🎯 Ready to revolutionize recruitment!"
echo "💪 Built with Israeli Innovation & ADHD Superpowers"
echo ""

# Run the application
streamlit run app.py --server.port 8501 --server.headless false

echo "🔄 MeUnique Master Agents System stopped." 