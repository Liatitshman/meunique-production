#!/usr/bin/env python3
"""
💡 LIAT's MeUnique AI - Enhanced System with Setup Wizards
"""

import streamlit as st
import pandas as pd
import json
import time
from datetime import datetime, timedelta
import os
from typing import List, Dict, Any, Optional
import plotly.express as px
import plotly.graph_objects as go
from dataclasses import dataclass
import re
from collections import defaultdict

# Page config
st.set_page_config(
    page_title="💡 MeUnique.io - Enhanced",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');
    
    * {
        font-family: 'Heebo', sans-serif !important;
    }
    
    .setup-wizard {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
    }
    
    .tone-card {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .tone-card:hover {
        border-color: #667eea;
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .tone-card.selected {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: #764ba2;
    }
    
    .admin-metric {
        background: #f8f9fa;
        border-left: 4px solid #667eea;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'setup_complete' not in st.session_state:
    st.session_state.setup_complete = False
    st.session_state.current_step = 1
    st.session_state.tone_preferences = []
    st.session_state.israeli_features = {
        'military_networks': True,
        'kombina_scoring': True,
        'hidden_connections': True,
        'local_slang': True
    }
    st.session_state.database_status = {
        'candidates': 1247,
        'companies': 342,
        'connections': 3891,
        'messages_sent': 5672
    }

# Setup Wizard Component
def setup_wizard_bot():
    """Interactive setup wizard that guides through initial configuration"""
    
    with st.expander("🤖 Setup Wizard - Click to Configure", expanded=not st.session_state.setup_complete):
        st.markdown("""
        <div class="setup-wizard">
            <h3>👋 Hi Liat! I'm your setup wizard</h3>
            <p>Let me help you configure MeUnique for your needs</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Step tracker
        progress = st.progress(st.session_state.current_step / 5)
        st.write(f"Step {st.session_state.current_step} of 5")
        
        # Step 1: Basic Info
        if st.session_state.current_step == 1:
            st.subheader("📝 Step 1: Basic Information")
            
            company_name = st.text_input("Your Company Name", value="MeUnique Recruiting")
            focus_roles = st.multiselect(
                "Primary roles you recruit for",
                ["Backend", "Frontend", "FullStack", "DevOps", "Data", "Product", "QA", "Mobile"],
                default=["Backend", "FullStack"]
            )
            
            if st.button("Next →", key="step1_next"):
                st.session_state.current_step = 2
                st.experimental_rerun()
        
        # Step 2: Tone Preferences
        elif st.session_state.current_step == 2:
            st.subheader("🎨 Step 2: Message Tone Preferences")
            st.write("Select your preferred communication styles (you can choose multiple)")
            
            tone_options = {
                "professional": {"name": "Professional", "emoji": "👔", "example": "Dear Daniel, I came across your impressive profile..."},
                "friendly": {"name": "Friendly", "emoji": "😊", "example": "Hi Daniel! Hope you're having a great day..."},
                "israeli_direct": {"name": "Israeli Direct", "emoji": "🇮🇱", "example": "היי דניאל, יש לי משהו מעניין בשבילך..."},
                "kombina": {"name": "Kombina Style", "emoji": "😎", "example": "דניאל! יש פה קומבינה של ממש..."},
                "tech_casual": {"name": "Tech Casual", "emoji": "💻", "example": "Hey Daniel, saw your GitHub - impressive stuff!"}
            }
            
            cols = st.columns(len(tone_options))
            for i, (key, tone) in enumerate(tone_options.items()):
                with cols[i]:
                    if st.checkbox(f"{tone['emoji']} {tone['name']}", key=f"tone_{key}"):
                        if key not in st.session_state.tone_preferences:
                            st.session_state.tone_preferences.append(key)
                    st.caption(tone['example'])
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Back", key="step2_back"):
                    st.session_state.current_step = 1
                    st.experimental_rerun()
            with col2:
                if st.button("Next →", key="step2_next"):
                    st.session_state.current_step = 3
                    st.experimental_rerun()
        
        # Step 3: Israeli Features
        elif st.session_state.current_step == 3:
            st.subheader("🇮🇱 Step 3: Israeli Market Features")
            st.write("Configure special features for the Israeli tech market")
            
            st.session_state.israeli_features['military_networks'] = st.checkbox(
                "🎖️ Use military unit networks (8200, Mamram, etc.)",
                value=True
            )
            
            st.session_state.israeli_features['kombina_scoring'] = st.checkbox(
                "🎯 Enable Kombina Score (creativity & entrepreneurship rating)",
                value=True
            )
            
            st.session_state.israeli_features['hidden_connections'] = st.checkbox(
                "🔗 Find hidden connections (same unit, university, etc.)",
                value=True
            )
            
            st.session_state.israeli_features['local_slang'] = st.checkbox(
                "💬 Use Israeli slang and expressions in messages",
                value=True
            )
            
            # Kombina examples
            if st.session_state.israeli_features['kombina_scoring']:
                st.info("🎯 Kombina Score examples:\n"
                       "• Ex-8200 founder: 95/100\n"
                       "• Startup experience: +15 points\n"
                       "• Side projects: +10 points")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Back", key="step3_back"):
                    st.session_state.current_step = 2
                    st.experimental_rerun()
            with col2:
                if st.button("Next →", key="step3_next"):
                    st.session_state.current_step = 4
                    st.experimental_rerun()
        
        # Step 4: Database Setup
        elif st.session_state.current_step == 4:
            st.subheader("🗄️ Step 4: Database Configuration")
            st.write("Let's set up your candidate database")
            
            # Import options
            import_method = st.radio(
                "How would you like to start?",
                ["Start fresh", "Import from LinkedIn", "Import from CSV", "Connect existing database"]
            )
            
            if import_method == "Import from LinkedIn":
                st.info("📤 We'll help you import your LinkedIn connections and saved candidates")
                if st.button("Start LinkedIn Import"):
                    with st.spinner("Connecting to LinkedIn..."):
                        time.sleep(2)
                    st.success("✅ Ready to import! We found 1,247 potential candidates")
            
            elif import_method == "Import from CSV":
                uploaded_file = st.file_uploader("Upload your candidate CSV", type=['csv'])
                if uploaded_file:
                    st.success(f"✅ File uploaded: {uploaded_file.name}")
            
            # Show current database status
            st.subheader("📊 Current Database Status")
            db_cols = st.columns(4)
            with db_cols[0]:
                st.metric("Candidates", st.session_state.database_status['candidates'], "+23")
            with db_cols[1]:
                st.metric("Companies", st.session_state.database_status['companies'], "+5")
            with db_cols[2]:
                st.metric("Connections", st.session_state.database_status['connections'], "+87")
            with db_cols[3]:
                st.metric("Messages", st.session_state.database_status['messages_sent'], "+156")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Back", key="step4_back"):
                    st.session_state.current_step = 3
                    st.experimental_rerun()
            with col2:
                if st.button("Next →", key="step4_next"):
                    st.session_state.current_step = 5
                    st.experimental_rerun()
        
        # Step 5: Final Review
        elif st.session_state.current_step == 5:
            st.subheader("✅ Step 5: Review & Launch")
            st.success("Great! Here's your configuration:")
            
            # Configuration summary
            st.write("**Message Tones:**", ", ".join(st.session_state.tone_preferences))
            
            st.write("**Israeli Features:**")
            for feature, enabled in st.session_state.israeli_features.items():
                if enabled:
                    st.write(f"✅ {feature.replace('_', ' ').title()}")
            
            st.write("**Database:**", f"{st.session_state.database_status['candidates']} candidates ready")
            
            if st.button("🚀 Complete Setup & Launch", type="primary", key="complete_setup"):
                st.session_state.setup_complete = True
                st.session_state.current_step = 1
                st.balloons()
                st.success("🎉 Setup complete! Welcome to MeUnique")
                time.sleep(2)
                st.experimental_rerun()

# Admin Panel
def admin_panel():
    """Admin dashboard with database overview and system status"""
    
    st.header("👤 Admin Panel")
    
    # System Health
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="admin-metric">
            <h4>🟢 System Status</h4>
            <h2>Operational</h2>
            <small>All systems running</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="admin-metric">
            <h4>📊 Database Size</h4>
            <h2>4.2 GB</h2>
            <small>87% capacity used</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="admin-metric">
            <h4>⚡ API Calls Today</h4>
            <h2>1,234</h2>
            <small>$12.34 cost</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="admin-metric">
            <h4>🔄 Last Sync</h4>
            <h2>5 min ago</h2>
            <small>Auto-sync active</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Database Overview
    st.subheader("🗄️ Database Overview")
    
    tab1, tab2, tab3 = st.tabs(["Candidates", "Companies", "Activity"])
    
    with tab1:
        # Candidate statistics
        st.write("**Candidate Distribution**")
        
        unit_data = {
            'Unit': ['8200', 'Mamram', 'Talpiot', '81', 'Other'],
            'Count': [234, 156, 89, 67, 701],
            'Active': [187, 134, 76, 45, 567],
            'Placed': [23, 12, 8, 5, 45]
        }
        df_units = pd.DataFrame(unit_data)
        
        fig = px.bar(df_units, x='Unit', y='Count', color='Active', 
                     title="Candidates by Military Unit")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Company statistics
        company_data = {
            'Type': ['Startup', 'Scale-up', 'Enterprise', 'Unicorn'],
            'Count': [156, 89, 67, 30],
            'Hiring': [134, 76, 45, 28]
        }
        df_companies = pd.DataFrame(company_data)
        
        fig = px.pie(df_companies, values='Count', names='Type', 
                     title="Companies by Type")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        # Activity log
        st.write("**Recent Activity**")
        
        activity_data = {
            'Time': ['2 min ago', '5 min ago', '12 min ago', '1 hour ago'],
            'Action': ['Message sent', 'Candidate added', 'Search performed', 'Report generated'],
            'User': ['Liat', 'Liat', 'System', 'Liat'],
            'Status': ['✅ Success', '✅ Success', '✅ Success', '✅ Success']
        }
        df_activity = pd.DataFrame(activity_data)
        st.dataframe(df_activity, use_container_width=True, hide_index=True)
    
    # Smart Suggestions
    st.subheader("💡 Smart Suggestions")
    
    suggestions = [
        {"icon": "🎯", "text": "23 candidates haven't been contacted in 30+ days", "action": "Review now"},
        {"icon": "📈", "text": "Response rate increased 15% with emoji usage", "action": "Update templates"},
        {"icon": "🔍", "text": "5 new Python developers match your criteria", "action": "View matches"},
        {"icon": "💰", "text": "Reduce costs by 20% with batch processing", "action": "Enable now"}
    ]
    
    cols = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 2]:
            with st.expander(f"{suggestion['icon']} {suggestion['text']}"):
                st.write("Recommended action based on your usage patterns")
                if st.button(suggestion['action'], key=f"suggest_{i}"):
                    st.success("✅ Action initiated")

# Main App
def main():
    # Header
    st.title("💡 MeUnique.io - Enhanced Recruitment Platform")
    
    # Show setup wizard if not complete
    if not st.session_state.setup_complete:
        setup_wizard_bot()
    else:
        # Main navigation
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🛍️ Agent Store",
            "🎯 Active Agents", 
            "💬 Smart Chat",
            "📊 Analytics",
            "⚙️ Settings",
            "👤 Admin"
        ])
        
        with tab1:
            st.header("🛍️ Choose Your AI Agent")
            
            # Agent cards with setup bots
            col1, col2, col3, col4 = st.columns(4)
            
            agents = [
                {
                    "name": "Smart Hunter",
                    "icon": "🎯",
                    "desc": "AI-powered candidate search",
                    "features": ["LinkedIn integration", "Military networks", "Kombina scoring"],
                    "status": "configured"
                },
                {
                    "name": "Message Wizard",
                    "icon": "💬",
                    "desc": "Personalized outreach at scale",
                    "features": ["5 tone styles", "A/B testing", "Auto-personalization"],
                    "status": "needs_setup"
                },
                {
                    "name": "Analytics Pro",
                    "icon": "📊",
                    "desc": "Data-driven insights",
                    "features": ["Real-time metrics", "Predictive analytics", "ROI tracking"],
                    "status": "configured"
                },
                {
                    "name": "Smart CRM",
                    "icon": "🧠",
                    "desc": "Intelligent relationship management",
                    "features": ["Auto-updates", "Relationship mapping", "Smart tagging"],
                    "status": "needs_setup"
                }
            ]
            
            for i, agent in enumerate(agents):
                with [col1, col2, col3, col4][i]:
                    st.markdown(f"""
                    <div class="israeli-card" style="text-align: center;">
                        <div style="font-size: 60px;">{agent['icon']}</div>
                        <h3>{agent['name']}</h3>
                        <p>{agent['desc']}</p>
                        <small>{'<br>'.join(f'• {f}' for f in agent['features'])}</small>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if agent['status'] == 'needs_setup':
                        if st.button(f"🔧 Setup {agent['name']}", key=f"setup_{agent['name']}"):
                            st.info(f"🤖 Setup wizard for {agent['name']} launching...")
                    else:
                        if st.button(f"✅ Launch {agent['name']}", key=f"launch_{agent['name']}"):
                            st.success(f"✅ {agent['name']} activated!")
        
        with tab3:
            # Smart Chat System
            st.header("💬 Smart Chat Assistant")
            
            # Initialize chat history
            if 'messages' not in st.session_state:
                st.session_state.messages = [
                    {"role": "assistant", "content": "👋 Hi Liat! I'm your AI recruitment assistant. I can help you find candidates, craft messages, and analyze your recruitment data. What would you like to do today?"}
                ]
            
            # Chat interface layout
            chat_col, suggestions_col = st.columns([2, 1])
            
            with chat_col:
                # Display chat messages
                chat_container = st.container()
                with chat_container:
                    for i, message in enumerate(st.session_state.messages):
                        if message["role"] == "user":
                            st.markdown(f"""
                            <div style="background: #e3f2fd; padding: 10px; border-radius: 10px; margin: 5px 0; text-align: right;">
                                <strong>You:</strong> {message["content"]}
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div style="background: #f5f5f5; padding: 10px; border-radius: 10px; margin: 5px 0;">
                                <strong>🤖 Assistant:</strong> {message["content"]}
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Add edit button for assistant messages
                            if st.button(f"✏️ Edit", key=f"edit_{i}"):
                                st.session_state[f"editing_{i}"] = True
                            
                            if st.session_state.get(f"editing_{i}", False):
                                edited_content = st.text_area(
                                    "Edit message:",
                                    value=message["content"],
                                    key=f"edit_area_{i}"
                                )
                                col1, col2 = st.columns(2)
                                with col1:
                                    if st.button("💾 Save", key=f"save_{i}"):
                                        st.session_state.messages[i]["content"] = edited_content
                                        st.session_state[f"editing_{i}"] = False
                                        st.experimental_rerun()
                                with col2:
                                    if st.button("❌ Cancel", key=f"cancel_{i}"):
                                        st.session_state[f"editing_{i}"] = False
                                        st.experimental_rerun()
                
                # Chat input
                user_input = st.text_input("Type your message...", key="chat_input")
                
                if user_input:
                    # Add user message
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    
                    # Generate AI response based on context
                    if "find" in user_input.lower() or "search" in user_input.lower():
                        response = "🔍 I'll help you find candidates. Here's what I found:\n\n"
                        response += "**Top Matches:**\n"
                        response += "1. **Daniel Cohen** - Senior Backend @ Wix\n"
                        response += "   • 8200 alumni, Python expert\n"
                        response += "   • Kombina Score: 87/100\n"
                        response += "   • Open to opportunities ✅\n\n"
                        response += "2. **Sarah Levy** - Full Stack @ Monday.com\n"
                        response += "   • Mamram graduate, React/Node.js\n"
                        response += "   • Kombina Score: 92/100\n"
                        response += "   • Passive candidate 🤔\n\n"
                        response += "Would you like me to draft personalized messages for them?"
                    
                    elif "message" in user_input.lower() or "write" in user_input.lower():
                        response = "✍️ I'll craft a personalized message. Choose a tone:\n\n"
                        response += "**Professional:** 'Dear Daniel, I noticed your impressive background...'\n"
                        response += "**Friendly:** 'Hi Daniel! 👋 Saw your awesome work at Wix...'\n"
                        response += "**Israeli Direct:** 'דניאל, יש לי משהו מעניין בשבילך...'\n"
                        response += "**Kombina Style:** 'דניאל! יש פה קומבינה מטורפת...'\n\n"
                        response += "Which tone would you prefer?"
                    
                    else:
                        response = "I understand you want to " + user_input.lower() + ". Let me help you with that!"
                    
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.experimental_rerun()
            
            with suggestions_col:
                st.subheader("💡 Quick Actions")
                
                # Quick action buttons
                quick_actions = [
                    {"icon": "🔍", "text": "Find Python developers"},
                    {"icon": "✍️", "text": "Write outreach message"},
                    {"icon": "📊", "text": "Show today's metrics"},
                    {"icon": "🎯", "text": "Review hot candidates"},
                    {"icon": "💰", "text": "Check response rates"},
                    {"icon": "🔗", "text": "Find mutual connections"}
                ]
                
                for action in quick_actions:
                    if st.button(f"{action['icon']} {action['text']}", key=f"quick_{action['text']}"):
                        st.session_state.messages.append({"role": "user", "content": action['text']})
                        st.experimental_rerun()
                
                # Context from current conversation
                st.subheader("📝 Conversation Context")
                st.info("This chat has access to:\n"
                       "• Your candidate database\n"
                       "• Message templates\n"
                       "• Analytics data\n"
                       "• Israeli tech networks")
                
                # Export chat
                if st.button("📥 Export Chat"):
                    chat_export = "\n\n".join([
                        f"{msg['role'].upper()}: {msg['content']}" 
                        for msg in st.session_state.messages
                    ])
                    st.download_button(
                        label="Download Chat History",
                        data=chat_export,
                        file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
        
        with tab2:
            # Active Agents Dashboard
            st.header("🎯 Active Agents")
            
            # Agent status cards
            active_agents = [
                {
                    "name": "Smart Hunter",
                    "status": "🟢 Running",
                    "current_task": "Scanning LinkedIn for Python developers",
                    "found_today": 23,
                    "messages_sent": 45,
                    "responses": 12
                },
                {
                    "name": "Message Wizard", 
                    "status": "🟡 Idle",
                    "current_task": "Waiting for new candidates",
                    "found_today": 0,
                    "messages_sent": 0,
                    "responses": 0
                }
            ]
            
            for agent in active_agents:
                with st.expander(f"{agent['name']} - {agent['status']}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Found Today", agent['found_today'])
                    with col2:
                        st.metric("Messages Sent", agent['messages_sent'])
                    with col3:
                        st.metric("Responses", agent['responses'])
                    
                    st.write(f"**Current Task:** {agent['current_task']}")
                    
                    # Agent controls
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        if st.button("⏸️ Pause", key=f"pause_{agent['name']}"):
                            st.success(f"✅ {agent['name']} paused")
                    with col2:
                        if st.button("🔄 Restart", key=f"restart_{agent['name']}"):
                            st.success(f"✅ {agent['name']} restarted")
                    with col3:
                        if st.button("⚙️ Configure", key=f"config_{agent['name']}"):
                            st.info("Opening configuration...")
        
        with tab5:
            admin_panel()

if __name__ == "__main__":
    main() 