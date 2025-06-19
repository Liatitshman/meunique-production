#!/usr/bin/env python3
"""
💡 MeUnique.io - Enhanced Interactive Bot System
With comprehensive feature guidance, real-time assistance, and detailed admin interface
"""

import streamlit as st
import pandas as pd
import json
import time
from datetime import datetime, timedelta
import os
from typing import List, Dict, Any, Optional, Tuple
import plotly.express as px
import plotly.graph_objects as go
from dataclasses import dataclass
import random

# Page config
st.set_page_config(
    page_title="MeUnique.io - AI Recruitment with Smart Bots",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with bot animations and interactive elements
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Enhanced Bot Styling */
    .bot-bubble {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 15px 20px;
        border-radius: 20px 20px 5px 20px;
        margin: 10px 0;
        position: relative;
        animation: fadeIn 0.5s ease-in;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .bot-typing {
        display: inline-block;
        animation: typing 1.5s infinite;
    }
    
    @keyframes typing {
        0%, 60%, 100% { opacity: 0; }
        30% { opacity: 1; }
    }
    
    /* Feature Detail Card */
    .feature-detail-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        position: relative;
        overflow: hidden;
    }
    
    .feature-detail-card::before {
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: linear-gradient(135deg, #667eea20, #764ba220);
        border-radius: 0 0 0 100%;
    }
    
    /* Interactive Bot Assistant Enhanced */
    .bot-assistant-enhanced {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
    }
    
    .bot-main {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        animation: pulse 2s infinite;
        font-size: 30px;
    }
    
    .bot-menu {
        position: absolute;
        bottom: 70px;
        right: 0;
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        padding: 20px;
        width: 300px;
        display: none;
    }
    
    .bot-menu.active {
        display: block;
        animation: slideUp 0.3s ease-out;
    }
    
    @keyframes slideUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    /* Feature Structure View */
    .structure-view {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        border: 1px solid #e0e0e0;
    }
    
    .structure-item {
        padding: 5px 0;
        border-left: 3px solid #667eea;
        padding-left: 15px;
        margin: 5px 0;
    }
    
    /* Admin Feature Details */
    .admin-feature-detail {
        background: linear-gradient(to right, #f8f9fa, #ffffff);
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 5px;
        animation: statusPulse 2s infinite;
    }
    
    .status-active { background: #48bb78; }
    .status-pending { background: #f6ad55; }
    .status-inactive { background: #e53e3e; }
    
    @keyframes statusPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Interactive Guidance */
    .guidance-tooltip {
        background: #4a5568;
        color: white;
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 14px;
        position: absolute;
        z-index: 100;
        animation: fadeIn 0.3s;
    }
    
    .highlight-field {
        border: 2px solid #667eea !important;
        animation: highlightPulse 1s 3;
    }
    
    @keyframes highlightPulse {
        0%, 100% { border-color: #667eea; }
        50% { border-color: #764ba2; }
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Bot System Classes
@dataclass
class BotResponse:
    message: str
    suggestions: List[str]
    actions: List[Dict[str, str]]
    context: str
    feature_details: Optional[Dict] = None

@dataclass
class FeatureDetail:
    name: str
    description: str
    structure: Dict[str, Any]
    status: str
    guidelines: List[str]
    api_connections: List[str]
    data_flow: Dict[str, str]
    customization_options: List[str]

# Initialize enhanced session state
if 'bot_system' not in st.session_state:
    st.session_state.bot_system = {
        'active_bots': {
            'main': True,
            'hunter': False,
            'message': False,
            'analytics': False,
            'crm': False
        },
        'conversations': {},
        'guidance_mode': False,
        'current_feature_focus': None,
        'user_journey': [],
        'feature_requests': []
    }

# Comprehensive Feature Database
FEATURE_DATABASE = {
    "smart_hunter": FeatureDetail(
        name="🎯 Smart Hunter Agent",
        description="AI-powered candidate discovery with Israeli market understanding",
        structure={
            "components": ["Search Engine", "ML Matcher", "Network Analyzer", "Kombina Scorer"],
            "data_sources": ["LinkedIn", "GitHub", "Local Networks", "Military Databases"],
            "algorithms": ["NLP Analysis", "Pattern Matching", "Graph Networks", "Similarity Scoring"]
        },
        status="active",
        guidelines=[
            "Start with broad search, then refine",
            "Use military unit filters for tech roles",
            "Check Kombina score for startup fit",
            "Review mutual connections first"
        ],
        api_connections=["LinkedIn API", "GitHub API", "Internal DB", "IDF Alumni Network"],
        data_flow={
            "input": "Search criteria + preferences",
            "processing": "ML matching + scoring",
            "output": "Ranked candidate list with insights"
        },
        customization_options=[
            "Adjust weight for military service",
            "Set Kombina score threshold",
            "Configure industry preferences",
            "Define location priorities"
        ]
    ),
    "message_wizard": FeatureDetail(
        name="💬 Message Wizard",
        description="Personalized outreach with 5 tone styles and A/B testing",
        structure={
            "components": ["Tone Analyzer", "Template Engine", "Personalization AI", "A/B Tester"],
            "tone_styles": ["Professional", "Friendly", "Israeli Direct", "Kombina", "Tech Casual"],
            "personalization": ["Name", "Company", "Background", "Mutual Connections", "Recent Activity"]
        },
        status="active",
        guidelines=[
            "Always personalize the opening line",
            "Match tone to company culture",
            "Keep initial messages under 150 words",
            "Include clear call-to-action",
            "Test different approaches"
        ],
        api_connections=["OpenAI GPT-4", "Grammar API", "Translation Service", "Analytics DB"],
        data_flow={
            "input": "Candidate info + job details + tone",
            "processing": "AI generation + personalization",
            "output": "Customized message + variations"
        },
        customization_options=[
            "Create custom tone profiles",
            "Set message length limits",
            "Define personalization depth",
            "Configure follow-up sequences"
        ]
    ),
    "analytics_pro": FeatureDetail(
        name="📊 Analytics Pro",
        description="Real-time insights with predictive analytics and market trends",
        structure={
            "components": ["Dashboard Builder", "Metric Tracker", "Prediction Engine", "Report Generator"],
            "metrics": ["Response Rate", "Time to Hire", "Quality Score", "Market Trends"],
            "visualizations": ["Funnel Charts", "Heat Maps", "Trend Lines", "Comparison Tables"]
        },
        status="active",
        guidelines=[
            "Review daily performance metrics",
            "Set up weekly trend alerts",
            "Compare against industry benchmarks",
            "Export reports for stakeholders"
        ],
        api_connections=["Analytics API", "Market Data Feed", "Competitor Intel", "Internal Metrics"],
        data_flow={
            "input": "All platform activity data",
            "processing": "Aggregation + ML analysis",
            "output": "Interactive dashboards + insights"
        },
        customization_options=[
            "Create custom KPIs",
            "Design personalized dashboards",
            "Set alert thresholds",
            "Configure report schedules"
        ]
    )
}

# Enhanced Bot Functions
def get_bot_response(query: str, context: str = "general") -> BotResponse:
    """Generate intelligent bot responses with context awareness"""
    
    query_lower = query.lower()
    
    # Smart response generation based on query patterns
    if "how" in query_lower or "help" in query_lower:
        if "hunter" in query_lower or "find" in query_lower:
            return BotResponse(
                message="I'll guide you through the Smart Hunter! 🎯\n\nHere's how to use it effectively:",
                suggestions=[
                    "Start with role title and key skills",
                    "Add military unit preferences if relevant",
                    "Set salary range and location",
                    "Use advanced filters for better matches"
                ],
                actions=[
                    {"label": "Open Hunter", "action": "open_hunter"},
                    {"label": "See Example Search", "action": "demo_search"},
                    {"label": "View Video Guide", "action": "video_guide"}
                ],
                context="hunter_guidance",
                feature_details=FEATURE_DATABASE.get("smart_hunter")
            )
        elif "message" in query_lower or "write" in query_lower:
            return BotResponse(
                message="Let me show you the Message Wizard! 💬\n\nCreating perfect outreach is easy:",
                suggestions=[
                    "Choose from 5 pre-built tone styles",
                    "Or create your custom tone",
                    "Add candidate-specific details",
                    "Preview before sending"
                ],
                actions=[
                    {"label": "Open Message Wizard", "action": "open_messages"},
                    {"label": "Tone Examples", "action": "show_tones"},
                    {"label": "Best Practices", "action": "message_tips"}
                ],
                context="message_guidance",
                feature_details=FEATURE_DATABASE.get("message_wizard")
            )
    
    elif "what" in query_lower:
        if "fill" in query_lower or "enter" in query_lower:
            return BotResponse(
                message="I'll show you exactly what to fill in each field! 📝\n\nLet me highlight the important fields:",
                suggestions=[
                    "Required fields are marked with *",
                    "Hover over any field for examples",
                    "Use suggested values when available",
                    "Save drafts to continue later"
                ],
                actions=[
                    {"label": "Highlight Fields", "action": "highlight_required"},
                    {"label": "Show Examples", "action": "field_examples"},
                    {"label": "Auto-fill Demo", "action": "demo_autofill"}
                ],
                context="form_guidance"
            )
    
    elif "structure" in query_lower or "how built" in query_lower:
        return BotResponse(
            message="Here's the technical structure of this feature! 🔧\n\nI'll break down how it works:",
            suggestions=[
                "View component architecture",
                "See data flow diagram",
                "Check API connections",
                "Understand the algorithms"
            ],
            actions=[
                {"label": "Technical Diagram", "action": "show_architecture"},
                {"label": "API Docs", "action": "api_documentation"},
                {"label": "Dev Portal", "action": "open_cursor"}
            ],
            context="technical_details"
        )
    
    # Default helpful response
    return BotResponse(
        message="I'm here to help! 🤖 What would you like to know about?",
        suggestions=[
            "How to use any feature",
            "What to fill in forms",
            "Feature explanations",
            "Customization options"
        ],
        actions=[
            {"label": "Feature Tour", "action": "start_tour"},
            {"label": "Quick Start", "action": "quick_start"},
            {"label": "Contact Support", "action": "support"}
        ],
        context="general"
    )

def render_bot_interface():
    """Render the main bot interface"""
    
    # Floating bot assistant
    st.markdown("""
    <div class="bot-assistant-enhanced">
        <div class="bot-main" onclick="toggleBotMenu()">🤖</div>
        <div class="bot-menu" id="botMenu">
            <h4>MeUnique Assistant</h4>
            <p>How can I help you today?</p>
            <div class="bot-quick-actions">
                <button onclick="askBot('How do I use the Smart Hunter?')">🎯 Hunter Guide</button>
                <button onclick="askBot('Help me write a message')">💬 Message Help</button>
                <button onclick="askBot('Show me analytics')">📊 Analytics</button>
                <button onclick="askBot('What should I fill here?')">📝 Form Help</button>
            </div>
        </div>
    </div>
    
    <script>
    function toggleBotMenu() {
        document.getElementById('botMenu').classList.toggle('active');
    }
    
    function askBot(question) {
        // This would interact with Streamlit
        console.log('Bot question:', question);
    }
    </script>
    """, unsafe_allow_html=True)

def render_feature_detail_view(feature_key: str):
    """Render detailed view of a feature with all components"""
    
    feature = FEATURE_DATABASE.get(feature_key)
    if not feature:
        st.error("Feature not found")
        return
    
    st.markdown(f"""
    <div class="admin-feature-detail">
        <h2>{feature.name}</h2>
        <p style="font-size: 1.1rem; color: #666;">{feature.description}</p>
        
        <div style="display: flex; gap: 10px; margin: 20px 0;">
            <span class="status-indicator status-{feature.status}"></span>
            <strong>Status:</strong> {feature.status.title()}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for different aspects
    detail_tabs = st.tabs(["📋 Overview", "🔧 Structure", "📐 Guidelines", "🔌 Integrations", "🎨 Customize"])
    
    with detail_tabs[0]:  # Overview
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎯 Key Components")
            for component in feature.structure.get("components", []):
                st.markdown(f"• **{component}**")
        
        with col2:
            st.markdown("### 📊 Data Flow")
            st.markdown(f"""
            <div class="structure-view">
                <div class="structure-item"><strong>Input:</strong> {feature.data_flow['input']}</div>
                <div class="structure-item"><strong>Processing:</strong> {feature.data_flow['processing']}</div>
                <div class="structure-item"><strong>Output:</strong> {feature.data_flow['output']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    with detail_tabs[1]:  # Structure
        st.markdown("### 🏗️ Technical Architecture")
        
        # Create structure diagram
        structure_diagram = create_structure_diagram(feature.structure)
        st.markdown(structure_diagram, unsafe_allow_html=True)
        
        # Code view
        with st.expander("View Implementation Details"):
            st.code(f"""
# {feature.name} Implementation Structure

class {feature_key.title().replace('_', '')}Agent:
    def __init__(self):
        self.components = {feature.structure.get('components', [])}
        self.status = "{feature.status}"
    
    def process(self, input_data):
        # {feature.data_flow['processing']}
        return processed_result
            """, language="python")
    
    with detail_tabs[2]:  # Guidelines
        st.markdown("### 📐 Usage Guidelines")
        
        for i, guideline in enumerate(feature.guidelines, 1):
            st.markdown(f"""
            <div style="background: #f0f7ff; padding: 15px; border-radius: 10px; margin: 10px 0;">
                <strong>#{i}</strong> {guideline}
            </div>
            """, unsafe_allow_html=True)
        
        # Interactive examples
        if st.button("Show Interactive Example", key=f"example_{feature_key}"):
            st.info("🎯 Interactive demo loading...")
            time.sleep(1)
            st.success("✅ Try it out above!")
    
    with detail_tabs[3]:  # Integrations
        st.markdown("### 🔌 API Connections")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Connected Services:**")
            for api in feature.api_connections:
                status = "🟢" if "API" in api else "🟡"
                st.markdown(f"{status} {api}")
        
        with col2:
            st.markdown("**Data Exchange:**")
            st.markdown("""
            ```json
            {
                "request": "User criteria",
                "process": "AI matching",
                "response": "Ranked results"
            }
            ```
            """)
    
    with detail_tabs[4]:  # Customize
        st.markdown("### 🎨 Customization Options")
        
        for option in feature.customization_options:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"• {option}")
            with col2:
                if st.button("Configure", key=f"config_{option}"):
                    st.session_state.show_config = option

def create_structure_diagram(structure: Dict) -> str:
    """Create visual structure diagram"""
    
    components = structure.get("components", [])
    
    diagram = """
    <div style="background: #f8f9fa; padding: 20px; border-radius: 15px;">
        <h4>Component Architecture</h4>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px;">
    """
    
    for comp in components:
        diagram += f"""
        <div style="background: white; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <div style="font-size: 30px; margin-bottom: 10px;">🔧</div>
            <strong>{comp}</strong>
        </div>
        """
    
    diagram += """
        </div>
    </div>
    """
    
    return diagram

def render_bot_chat_panel():
    """Render the interactive chat panel"""
    
    st.markdown("""
    <div style="background: white; border-radius: 20px; padding: 25px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);">
        <h3>💬 Chat with MeUnique Assistant</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            {"role": "bot", "content": "👋 Hi! I'm your MeUnique assistant. I can help you understand any feature, guide you through forms, or explain how things work. What would you like to know?"}
        ]
    
    # Display chat
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"""
                <div style="text-align: right; margin: 10px 0;">
                    <span style="background: #e3f2fd; padding: 10px 15px; border-radius: 15px 15px 5px 15px; display: inline-block;">
                        {msg["content"]}
                    </span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="bot-bubble">
                    {msg["content"]}
                </div>
                """, unsafe_allow_html=True)
    
    # Quick action buttons
    st.markdown("### 🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🎯 Hunter Guide", use_container_width=True):
            response = get_bot_response("How do I use the Smart Hunter?")
            st.session_state.chat_history.append({"role": "user", "content": "Show me the Hunter guide"})
            st.session_state.chat_history.append({"role": "bot", "content": response.message})
            st.experimental_rerun()
    
    with col2:
        if st.button("💬 Message Help", use_container_width=True):
            response = get_bot_response("Help me write a message")
            st.session_state.chat_history.append({"role": "user", "content": "Help with messages"})
            st.session_state.chat_history.append({"role": "bot", "content": response.message})
            st.experimental_rerun()
    
    with col3:
        if st.button("📝 Form Guide", use_container_width=True):
            st.session_state.guidance_mode = True
            st.success("✅ Guidance mode activated! I'll highlight what to fill.")
    
    with col4:
        if st.button("🔧 Tech Details", use_container_width=True):
            response = get_bot_response("Show me the structure")
            st.session_state.chat_history.append({"role": "user", "content": "Technical details"})
            st.session_state.chat_history.append({"role": "bot", "content": response.message})
            st.experimental_rerun()
    
    # Chat input
    user_input = st.text_input("Ask me anything...", placeholder="e.g., How do I find Python developers?", key="bot_chat_input")
    
    if user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get bot response
        response = get_bot_response(user_input)
        st.session_state.chat_history.append({"role": "bot", "content": response.message})
        
        # Show suggestions if any
        if response.suggestions:
            suggestions_html = "<div style='margin-top: 10px;'><strong>💡 Suggestions:</strong><ul>"
            for suggestion in response.suggestions:
                suggestions_html += f"<li>{suggestion}</li>"
            suggestions_html += "</ul></div>"
            st.session_state.chat_history.append({"role": "bot", "content": suggestions_html})
        
        st.experimental_rerun()

def render_admin_dashboard():
    """Render comprehensive admin dashboard with all features"""
    
    st.header("👤 Admin Dashboard - Complete Feature Control")
    
    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Active Features", "12", "+2 new")
    with col2:
        st.metric("Bot Interactions", "847", "+125 today")
    with col3:
        st.metric("Feature Requests", "23", "+5 new")
    with col4:
        st.metric("System Health", "98%", "+2%")
    
    # Feature management
    st.markdown("---")
    st.subheader("🎯 Feature Management")
    
    # Feature grid
    feature_cols = st.columns(3)
    
    for i, (key, feature) in enumerate(FEATURE_DATABASE.items()):
        with feature_cols[i % 3]:
            st.markdown(f"""
            <div class="feature-detail-card">
                <h4>{feature.name}</h4>
                <p>{feature.description}</p>
                <div style="margin: 10px 0;">
                    <span class="status-indicator status-{feature.status}"></span>
                    Status: {feature.status.title()}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"View Details", key=f"view_{key}"):
                st.session_state.current_feature_focus = key
                st.experimental_rerun()
    
    # Detailed feature view
    if st.session_state.get('current_feature_focus'):
        st.markdown("---")
        render_feature_detail_view(st.session_state.current_feature_focus)
    
    # Feature requests
    st.markdown("---")
    st.subheader("📋 Pending Feature Requests")
    
    requests = [
        {"feature": "WhatsApp Integration", "votes": 45, "status": "In Development", "eta": "2 weeks"},
        {"feature": "Calendar Sync", "votes": 38, "status": "Planning", "eta": "1 month"},
        {"feature": "Voice Notes", "votes": 29, "status": "Under Review", "eta": "TBD"},
        {"feature": "Mobile App", "votes": 67, "status": "In Development", "eta": "3 weeks"}
    ]
    
    for req in requests:
        col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
        
        with col1:
            st.markdown(f"**{req['feature']}**")
        with col2:
            st.markdown(f"👍 {req['votes']}")
        with col3:
            st.markdown(f"📌 {req['status']}")
        with col4:
            st.markdown(f"⏱️ {req['eta']}")
        with col5:
            if st.button("Details", key=f"req_{req['feature']}"):
                st.info(f"Opening details for {req['feature']}...")

# Main Application
def main():
    # Header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="background: linear-gradient(90deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3rem;">
            MeUnique.io
        </h1>
        <p style="font-size: 1.2rem; color: #666;">AI Recruitment with Interactive Bot Assistance</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Render floating bot
    render_bot_interface()
    
    # Main navigation
    tabs = st.tabs([
        "🏠 Home",
        "🤖 Bot Assistant",
        "🛍️ AI Agents",
        "📊 Analytics",
        "👤 Admin Panel",
        "⚙️ Settings"
    ])
    
    with tabs[0]:  # Home
        st.header("Welcome to MeUnique.io")
        
        # Interactive guidance prompt
        if st.session_state.get('guidance_mode'):
            st.info("🤖 Guidance Mode Active! I'll help you fill out forms and understand features.")
        
        # Quick start section
        st.subheader("🚀 Quick Start")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="feature-detail-card">
                <h4>1️⃣ Choose Your Agent</h4>
                <p>Select from our AI agents based on your needs</p>
                <button>Start Here →</button>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-detail-card">
                <h4>2️⃣ Set Preferences</h4>
                <p>Customize tone, style, and targeting</p>
                <button>Configure →</button>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="feature-detail-card">
                <h4>3️⃣ Start Recruiting</h4>
                <p>Let AI do the heavy lifting</p>
                <button>Launch →</button>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:  # Bot Assistant
        render_bot_chat_panel()
    
    with tabs[2]:  # AI Agents
        st.header("🛍️ AI Agent Store")
        
        # Agent selection with detailed info
        agent_cols = st.columns(2)
        
        agents = [
            {
                "name": "Smart Hunter",
                "emoji": "🎯",
                "description": "Find perfect candidates with AI",
                "features": ["LinkedIn Scanner", "Kombina Score", "Network Analysis"],
                "bot_guide": "I'll show you exactly how to use each search filter!"
            },
            {
                "name": "Message Wizard",
                "emoji": "💬",
                "description": "Create personalized outreach",
                "features": ["5 Tone Styles", "A/B Testing", "Auto-personalize"],
                "bot_guide": "I'll help you write messages that get responses!"
            }
        ]
        
        for i, agent in enumerate(agents):
            with agent_cols[i]:
                st.markdown(f"""
                <div class="feature-detail-card">
                    <div style="text-align: center;">
                        <div style="font-size: 60px;">{agent['emoji']}</div>
                        <h3>{agent['name']}</h3>
                        <p>{agent['description']}</p>
                    </div>
                    <hr>
                    <div style="background: #f0f7ff; padding: 10px; border-radius: 10px; margin: 10px 0;">
                        <strong>🤖 Bot says:</strong> "{agent['bot_guide']}"
                    </div>
                    <h4>Features:</h4>
                    <ul>
                """, unsafe_allow_html=True)
                
                for feature in agent['features']:
                    st.markdown(f"<li>{feature}</li>", unsafe_allow_html=True)
                
                st.markdown("</ul></div>", unsafe_allow_html=True)
                
                if st.button(f"Activate {agent['name']}", key=f"activate_{agent['name']}"):
                    st.success(f"✅ {agent['name']} activated!")
                    st.info(f"🤖 Bot: Let me show you how to use {agent['name']}...")
    
    with tabs[3]:  # Analytics
        st.header("📊 Analytics Dashboard")
        
        # Sample metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 78,
                title = {'text': "Response Rate"},
                gauge = {'axis': {'range': [None, 100]},
                        'bar': {'color': "#667eea"}}
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = go.Figure(go.Indicator(
                mode = "gauge+number", 
                value = 4.2,
                title = {'text': "Avg. Days to Hire"},
                gauge = {'axis': {'range': [None, 10]},
                        'bar': {'color': "#48bb78"}}
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col3:
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 92,
                title = {'text': "Quality Score"},
                gauge = {'axis': {'range': [None, 100]},
                        'bar': {'color': "#f6ad55"}}
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    with tabs[4]:  # Admin Panel
        render_admin_dashboard()
    
    with tabs[5]:  # Settings
        st.header("⚙️ Personalization Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎨 Interface Preferences")
            
            theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
            language = st.selectbox("Language", ["English", "Hebrew", "Mixed 🤪"])
            
            st.subheader("🤖 Bot Preferences")
            
            bot_personality = st.select_slider(
                "Bot Personality",
                options=["Professional", "Friendly", "Casual", "Kombina"],
                value="Friendly"
            )
            
            auto_suggestions = st.checkbox("Enable auto-suggestions", value=True)
            guidance_tooltips = st.checkbox("Show guidance tooltips", value=True)
        
        with col2:
            st.subheader("📧 Communication Defaults")
            
            default_tone = st.multiselect(
                "Default Message Tones",
                ["Professional", "Friendly", "Israeli Direct", "Kombina", "Tech Casual"],
                default=["Friendly", "Professional"]
            )
            
            st.subheader("🔔 Notifications")
            
            email_updates = st.checkbox("Email updates", value=True)
            bot_reminders = st.checkbox("Bot reminders", value=True)
            feature_announcements = st.checkbox("New feature announcements", value=True)
        
        if st.button("💾 Save Settings", type="primary"):
            st.success("✅ Settings saved!")
            st.balloons()

    # Smart suggestions sidebar
    with st.sidebar:
        st.markdown("---")
        st.subheader("💡 Smart Suggestions")
        
        # Context-aware suggestions
        suggestions = [
            "🎯 Try the Kombina Hunter for startup roles",
            "💬 Test different message tones",
            "📊 Check your weekly performance",
            "🔧 Customize your dashboard"
        ]
        
        for suggestion in suggestions:
            if st.button(suggestion, key=f"suggest_{suggestion}"):
                st.info(f"Opening: {suggestion}")
        
        st.markdown("---")
        st.subheader("🔜 Coming Soon")
        
        upcoming = ["WhatsApp Integration", "Voice Commands", "Mobile App"]
        for feature in upcoming:
            st.info(f"• {feature}")

# Run the app
if __name__ == "__main__":
    main() 