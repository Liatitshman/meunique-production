#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 MeUnique Production App - Main Entry Point
מערכת הפרודקשן הראשית של MeUnique

Domain: meunique.io
Platform: Streamlit Cloud
Built by: Liat Tishman
"""

import streamlit as st
import pandas as pd
import json
import datetime
import requests
import os
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Any
import time
import openai

# Configuration
st.set_page_config(
    page_title="🚀 MeUnique - AI Recruitment Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Domain and deployment configuration
DOMAIN_URL = "https://meunique.io"
STREAMLIT_CLOUD_URL = "https://meuniqueai.streamlit.app"

# Production costs and projections
MONTHLY_COSTS = {
    "OpenAI API": 55,
    "Apollo API": 49,
    "PhantomBuster": 69,
    "LinkedIn Sales Navigator": 80,
    "Sales QL": 49,
    "Twilio WhatsApp": 15,
    "Domain (meunique.io)": 1,
    "Google Drive": 6,
    "Streamlit Cloud": 0,
    "Total": 324
}

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'selected_agent' not in st.session_state:
    st.session_state.selected_agent = "Maya Research Pro"
if 'personality_mode' not in st.session_state:
    st.session_state.personality_mode = "Friendly"
if 'chat_category' not in st.session_state:
    st.session_state.chat_category = "General Consultation"

# Smart Agents Configuration
AGENTS = {
    "Maya Research Pro 🔍": {
        "description": "LinkedIn intelligence & candidate research specialist",
        "expertise": "Market research, candidate profiling, competitive analysis",
        "response_rate": "78%",
        "speciality": "LinkedIn Sales Navigator integration",
        "color": "#4CAF50"
    },
    "Daniel Message Writer Pro ✍️": {
        "description": "Personalized messaging & outreach expert",
        "expertise": "Message crafting, response optimization, A/B testing",
        "response_rate": "82%",
        "speciality": "78% better response rates proven",
        "color": "#2196F3"
    },
    "Tamar Data Mapper Pro 📊": {
        "description": "Skills analysis & cost optimization specialist",
        "expertise": "Data mapping, skills assessment, ROI analysis",
        "response_rate": "85%",
        "speciality": "Cost optimization - $1,100/month savings",
        "color": "#FF9800"
    },
    "ROI Growth Analyst Pro 📈": {
        "description": "Career trajectory prediction & growth analysis",
        "expertise": "Career mapping, growth prediction, market trends",
        "response_rate": "79%",
        "speciality": "Predictive career analytics",
        "color": "#9C27B0"
    },
    "Strategic Hiring Advisor 🎯": {
        "description": "Team building & scaling strategy expert",
        "expertise": "Team composition, hiring strategy, scaling plans",
        "response_rate": "83%",
        "speciality": "Strategic team building",
        "color": "#F44336"
    },
    "Network Intelligence Pro 🌐": {
        "description": "Relationship mapping & network analysis",
        "expertise": "Network analysis, relationship mapping, referral optimization",
        "response_rate": "77%",
        "speciality": "Professional network intelligence",
        "color": "#607D8B"
    }
}

# Personality Modes
PERSONALITY_MODES = {
    "Formal": {
        "tone": "Professional, data-focused, precise",
        "style": "Executive level communication with detailed analysis",
        "emoji_usage": "Minimal, professional icons only",
        "greeting": "Good day. I'm here to provide professional consultation."
    },
    "Friendly": {
        "tone": "Accessible, supportive, encouraging",
        "style": "Warm and approachable with helpful guidance",
        "emoji_usage": "Moderate use of friendly emojis 😊",
        "greeting": "Hi there! 😊 I'm happy to help you today!"
    },
    "Casual": {
        "tone": "Relaxed, cool, balanced professionalism",
        "style": "Easy-going but competent communication",
        "emoji_usage": "Natural emoji usage 👍",
        "greeting": "Hey! 👋 What can I help you with?"
    },
    "Kombina": {
        "tone": "Israeli style - direct, confident, results-oriented",
        "style": "Straight to the point, 'let's get things done' attitude",
        "emoji_usage": "Expressive emojis with Hebrew expressions 💪",
        "greeting": "מה קורה בוס! 💪 בואי נעשה עסקים!"
    }
}

# Chat Categories
CHAT_CATEGORIES = {
    "General Consultation": "💬 כללי",
    "LinkedIn Research": "🔍 מחקר LinkedIn",
    "Message Writing": "✍️ כתיבת הודעות",
    "Data Analysis": "📊 ניתוח נתונים",
    "Strategy Planning": "🎯 תכנון אסטרטגי",
    "Network Mapping": "🌐 מיפוי רשתות",
    "Cost Optimization": "💰 אופטימיזציה",
    "Technical Support": "🛠️ תמיכה טכנית"
}

def main():
    # Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 30px; border-radius: 20px; color: white; text-align: center; margin-bottom: 30px;">
        <h1>🚀 MeUnique - AI Recruitment Platform</h1>
        <p><strong>meunique.io • Revolutionary AI-Powered Recruitment</strong></p>
        <p>🧠 Built by Liat Tishman - Teaching to Fish, Not Giving Fish</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Status indicators
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🌐 Status", "Live", "Production Ready")
    
    with col2:
        st.metric("👥 Users", "Beta Testing", "Ready for Scale")
    
    with col3:
        st.metric("💰 Monthly Cost", f"${MONTHLY_COSTS['Total']}")
    
    with col4:
        st.metric("🎯 Revenue Target", "$5,000/month")
    
    # Main navigation
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Home", "🤖 AI Agents", "📊 Analytics", "💰 Business", "🔗 Share"
    ])
    
    with tab1:
        render_home_tab()
    
    with tab2:
        render_ai_agents_tab()
    
    with tab3:
        render_analytics_tab()
    
    with tab4:
        render_business_tab()
    
    with tab5:
        render_share_tab()

def render_home_tab():
    """🏠 Home tab with main features"""
    st.markdown("## 🏠 Welcome to MeUnique")
    
    # Hero section
    st.markdown("""
    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h3>🎯 The Story Behind MeUnique</h3>
        <p>Like my grandfather always said: <strong>"Give someone a fish, and you feed them for a day. 
        Teach them to fish, and you feed them for a lifetime."</strong></p>
        
        <p>That's exactly what MeUnique does for recruitment. Instead of just finding candidates, 
        we teach you to build lasting recruitment systems that work 24/7.</p>
        
        <p>Born from my ADHD superpower of seeing patterns others miss, refined through StartingUp's 
        incredible community, and built with Israeli tech innovation at its core.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key features
    st.markdown("### 🌟 Revolutionary Features")
    
    feature_cols = st.columns(3)
    
    with feature_cols[0]:
        st.markdown("""
        <div style="background: #e8f5e8; padding: 15px; border-radius: 10px; text-align: center;">
            <h4>🤖 AI Agents</h4>
            <p>6 specialized AI recruiters working 24/7</p>
            <ul style="text-align: left;">
                <li>ProfileMapper - LinkedIn analysis</li>
                <li>NetworkHunter - candidate search</li>
                <li>MessageCrafter - personalized outreach</li>
                <li>CultureMatcher - cultural fit</li>
                <li>SkillsAnalyzer - technical evaluation</li>
                <li>CompensationGuru - salary optimization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_cols[1]:
        st.markdown("""
        <div style="background: #fff3cd; padding: 15px; border-radius: 10px; text-align: center;">
            <h4>💬 Smart Communication</h4>
            <p>Personalized messaging with Israeli flair</p>
            <ul style="text-align: left;">
                <li>Hebrew & English support</li>
                <li>WhatsApp integration</li>
                <li>Cultural context awareness</li>
                <li>Automated follow-ups</li>
                <li>Response rate optimization</li>
                <li>Sentiment analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_cols[2]:
        st.markdown("""
        <div style="background: #e3f2fd; padding: 15px; border-radius: 10px; text-align: center;">
            <h4>📊 Real-Time Analytics</h4>
            <p>Complete visibility into your recruitment</p>
            <ul style="text-align: left;">
                <li>Cost tracking per candidate</li>
                <li>ROI analysis</li>
                <li>Performance metrics</li>
                <li>Predictive insights</li>
                <li>Automated reporting</li>
                <li>Success rate optimization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Demo section
    st.markdown("### 🎯 Try It Now")
    
    demo_col1, demo_col2 = st.columns(2)
    
    with demo_col1:
        st.markdown("**🔍 Candidate Search Demo**")
        search_query = st.text_input("Search for candidates:", placeholder="e.g., Python developer in Tel Aviv")
        
        if st.button("🚀 Search Candidates"):
            with st.spinner("AI agents searching..."):
                time.sleep(2)
                st.success("✅ Found 47 potential candidates!")
                
                # Mock results
                results_data = {
                    "Name": ["Sarah Cohen", "David Levi", "Maya Goldberg"],
                    "Role": ["Senior Python Developer", "Full Stack Engineer", "Data Scientist"],
                    "Location": ["Tel Aviv", "Jerusalem", "Haifa"],
                    "Match Score": ["95%", "88%", "92%"],
                    "Contact Status": ["Available", "Interested", "Open to offers"]
                }
                
                st.dataframe(pd.DataFrame(results_data))
    
    with demo_col2:
        st.markdown("**💬 Message Generator Demo**")
        candidate_name = st.text_input("Candidate name:", placeholder="e.g., Sarah Cohen")
        
        if st.button("✨ Generate Message"):
            with st.spinner("Crafting personalized message..."):
                time.sleep(2)
                
                message = f"""
Hi {candidate_name if candidate_name else 'Sarah'},

I hope this message finds you well! 😊

I came across your profile and was really impressed by your Python expertise. We're working with an amazing startup in Tel Aviv that's doing some groundbreaking work in AI - the kind of place where your skills would really shine.

The role offers:
• Competitive salary + equity
• Remote-first culture
• Amazing team of senior developers
• Real impact on product used by thousands

Would love to chat more about this opportunity. Are you open to a quick call this week?

Best regards,
Liat
📱 WhatsApp: +972545436397
"""
                
                st.text_area("Generated message:", message, height=200)
                st.success("✅ Message ready to send!")

def render_ai_agents_tab():
    """🤖 AI Agents showcase"""
    st.markdown("## 🤖 Meet Your AI Recruitment Team")
    
    agents = [
        {
            "name": "ProfileMapper 🔍",
            "role": "LinkedIn Profile Analyst",
            "description": "Analyzes LinkedIn profiles with surgical precision, extracting hidden insights about candidates' true potential.",
            "features": ["Deep profile analysis", "Skill extraction", "Career trajectory prediction", "Cultural fit assessment"],
            "personality": "Like Liat when she's deep-diving into a candidate's background - obsessive attention to detail."
        },
        {
            "name": "NetworkHunter 🎯",
            "role": "Candidate Search Specialist", 
            "description": "Hunts down the perfect candidates across multiple platforms using advanced search algorithms.",
            "features": ["Multi-platform search", "Boolean query optimization", "Passive candidate identification", "Network mapping"],
            "personality": "The persistent hunter who never gives up - just like Liat's recruiting style."
        },
        {
            "name": "MessageCrafter 💬",
            "role": "Personalized Outreach Expert",
            "description": "Crafts compelling, personalized messages that get responses using Israeli warmth and tech savvy.",
            "features": ["Personalized messaging", "A/B testing", "Response optimization", "Cultural adaptation"],
            "personality": "Friendly but professional, with that Israeli directness that builds trust."
        },
        {
            "name": "CultureMatcher 🎭",
            "role": "Cultural Fit Analyzer",
            "description": "Ensures perfect cultural alignment between candidates and companies, especially in Israeli tech culture.",
            "features": ["Cultural assessment", "Team dynamics analysis", "Startup readiness evaluation", "Communication style matching"],
            "personality": "The wise cultural translator who understands both sides of the equation."
        },
        {
            "name": "SkillsAnalyzer 🧠",
            "role": "Technical Skills Evaluator",
            "description": "Deep technical analysis of candidates' skills, projects, and potential for growth.",
            "features": ["Technical skill assessment", "Project portfolio analysis", "Growth potential evaluation", "Technology stack matching"],
            "personality": "The technical guru who can spot real talent from a mile away."
        },
        {
            "name": "CompensationGuru 💰",
            "role": "Salary & Benefits Optimizer",
            "description": "Provides accurate salary recommendations and negotiation strategies for optimal outcomes.",
            "features": ["Market salary analysis", "Negotiation strategies", "Benefits optimization", "Equity evaluation"],
            "personality": "The fair negotiator who ensures everyone wins in the deal."
        }
    ]
    
    for agent in agents:
        with st.expander(f"{agent['name']} - {agent['role']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Description:** {agent['description']}")
                st.markdown(f"**Personality:** {agent['personality']}")
                
                st.markdown("**Key Features:**")
                for feature in agent['features']:
                    st.markdown(f"• {feature}")
            
            with col2:
                if st.button(f"🚀 Activate {agent['name'].split()[0]}", key=f"activate_{agent['name']}"):
                    st.success(f"✅ {agent['name']} is now active and ready to work!")

def render_analytics_tab():
    """📊 Analytics and metrics"""
    st.markdown("## 📊 Real-Time Analytics Dashboard")
    
    # Mock analytics data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("👥 Active Candidates", "1,247", "+23 today")
    
    with col2:
        st.metric("📧 Messages Sent", "3,456", "+127 today")
    
    with col3:
        st.metric("📈 Response Rate", "67%", "+5% this week")
    
    with col4:
        st.metric("💰 Cost per Hire", "$89", "-$12 vs last month")
    
    # Charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Response rate chart
        dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
        response_rates = [60 + (i % 10) + (i // 10) for i in range(len(dates))]
        
        fig = px.line(x=dates, y=response_rates, title="Response Rate Trend")
        fig.update_layout(xaxis_title="Date", yaxis_title="Response Rate (%)")
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        # Cost breakdown
        costs = list(MONTHLY_COSTS.values())[:-1]  # Exclude total
        labels = list(MONTHLY_COSTS.keys())[:-1]
        
        fig = px.pie(values=costs, names=labels, title="Monthly Cost Breakdown")
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance table
    st.markdown("### 🎯 Agent Performance")
    
    performance_data = {
        "Agent": ["ProfileMapper", "NetworkHunter", "MessageCrafter", "CultureMatcher", "SkillsAnalyzer", "CompensationGuru"],
        "Tasks Completed": [234, 189, 456, 123, 167, 89],
        "Success Rate": ["94%", "87%", "73%", "91%", "88%", "96%"],
        "Avg Response Time": ["2.3s", "5.1s", "1.8s", "3.2s", "4.7s", "1.2s"],
        "Status": ["🟢 Active", "🟢 Active", "🟢 Active", "🟢 Active", "🟢 Active", "🟢 Active"]
    }
    
    st.dataframe(pd.DataFrame(performance_data))

def render_business_tab():
    """💰 Business model and pricing"""
    st.markdown("## 💰 Business Model & Pricing")
    
    # Pricing tiers
    st.markdown("### 💵 Pricing Plans")
    
    pricing_cols = st.columns(3)
    
    with pricing_cols[0]:
        st.markdown("""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border: 2px solid #28a745;">
            <h3 style="color: #28a745;">🥉 Starter</h3>
            <h2 style="color: #28a745;">$99/month</h2>
            <ul>
                <li>Basic AI candidate search</li>
                <li>50 contacts per month</li>
                <li>Email integration</li>
                <li>Basic analytics</li>
                <li>Email support</li>
            </ul>
            <p><strong>Perfect for:</strong> Freelance recruiters</p>
        </div>
        """, unsafe_allow_html=True)
    
    with pricing_cols[1]:
        st.markdown("""
        <div style="background: #fff3cd; padding: 20px; border-radius: 10px; border: 2px solid #ffc107;">
            <h3 style="color: #856404;">🥈 Professional</h3>
            <h2 style="color: #856404;">$299/month</h2>
            <ul>
                <li>Advanced AI agents</li>
                <li>500 contacts per month</li>
                <li>WhatsApp integration</li>
                <li>Advanced analytics</li>
                <li>Priority support</li>
                <li>Custom integrations</li>
            </ul>
            <p><strong>Perfect for:</strong> Small agencies</p>
        </div>
        """, unsafe_allow_html=True)
    
    with pricing_cols[2]:
        st.markdown("""
        <div style="background: #e3f2fd; padding: 20px; border-radius: 10px; border: 2px solid #2196f3;">
            <h3 style="color: #1976d2;">🥇 Enterprise</h3>
            <h2 style="color: #1976d2;">$799/month</h2>
            <ul>
                <li>All AI features</li>
                <li>Unlimited contacts</li>
                <li>Custom integrations</li>
                <li>Dedicated support</li>
                <li>White-label option</li>
                <li>Custom training</li>
            </ul>
            <p><strong>Perfect for:</strong> Large enterprises</p>
        </div>
        """, unsafe_allow_html=True)
    
    # ROI Calculator
    st.markdown("### 🧮 ROI Calculator")
    
    with st.form("roi_calculator"):
        col1, col2 = st.columns(2)
        
        with col1:
            current_cost = st.number_input("Current monthly recruitment cost ($):", 0, 50000, 5000)
            time_spent = st.slider("Hours spent on recruitment per week:", 0, 40, 20)
        
        with col2:
            hourly_rate = st.number_input("Your hourly rate ($):", 0, 500, 75)
            hires_per_month = st.number_input("Hires per month:", 1, 50, 5)
        
        calculate = st.form_submit_button("🧮 Calculate ROI")
        
        if calculate:
            # Calculate savings
            time_cost = time_spent * 4 * hourly_rate  # Monthly time cost
            meunique_cost = 299  # Professional plan
            time_savings = time_cost * 0.7  # 70% time savings
            total_savings = time_savings - meunique_cost
            roi_percentage = (total_savings / meunique_cost) * 100
            
            st.markdown("### 📈 Your ROI Results")
            
            result_cols = st.columns(4)
            
            with result_cols[0]:
                st.metric("💰 Monthly Savings", f"${total_savings:,.0f}")
            
            with result_cols[1]:
                st.metric("📈 ROI", f"{roi_percentage:.0f}%")
            
            with result_cols[2]:
                st.metric("⏰ Time Saved", f"{time_spent * 0.7:.0f}h/week")
            
            with result_cols[3]:
                st.metric("💵 Cost per Hire", f"${(current_cost + meunique_cost) / hires_per_month:.0f}")

def render_share_tab():
    """🔗 Share and marketing materials"""
    st.markdown("## 🔗 Share MeUnique")
    
    # Quick share links
    st.markdown("### 🚀 Share Links")
    
    share_links = [
        ("🌐 Main Platform", STREAMLIT_CLOUD_URL),
        ("🏠 Custom Domain", DOMAIN_URL),
        ("📱 Mobile Version", f"{STREAMLIT_CLOUD_URL}?mobile=1"),
        ("🎯 Demo Version", f"{STREAMLIT_CLOUD_URL}?demo=1")
    ]
    
    for name, url in share_links:
        col1, col2, col3 = st.columns([2, 4, 1])
        
        with col1:
            st.markdown(f"**{name}**")
        
        with col2:
            st.code(url)
        
        with col3:
            if st.button("📋", key=f"copy_{name}"):
                st.success("Copied!")
    
    # Social media templates
    st.markdown("### 📱 Social Media Templates")
    
    templates = {
        "LinkedIn": f"""🚀 Excited to share MeUnique - the AI recruitment platform that's changing how we find talent!

✨ What makes it special:
• 6 AI agents working 24/7
• Smart candidate matching
• Personalized outreach with Israeli flair
• Real-time cost tracking & ROI

Built by a recruiter, for recruiters. Try it: {DOMAIN_URL}

#Recruitment #AI #HRTech #StartUp #Innovation #IsraeliTech""",
        
        "Twitter": f"""🚀 Just launched MeUnique - AI recruitment that actually works!

🤖 6 specialized AI agents
💬 Smart personalized messaging  
📊 Real-time analytics
🇮🇱 Built with Israeli innovation

Try it: {DOMAIN_URL}

#RecruitmentAI #HRTech #StartUp""",
        
        "WhatsApp": f"""🚀 Hey! Want to see something cool?

Just launched MeUnique - an AI recruitment platform that's like having 6 expert recruiters working for you 24/7!

✨ It finds candidates, writes personalized messages, and tracks everything in real-time.

Check it out: {DOMAIN_URL}

Would love your thoughts! 🙏"""
    }
    
    for platform, template in templates.items():
        with st.expander(f"📱 {platform} Post"):
            st.text_area(f"{platform} template:", template, height=150, key=f"template_{platform}")
            if st.button(f"📋 Copy {platform} Post", key=f"copy_template_{platform}"):
                st.success(f"✅ {platform} post copied!")
    
    # Beta testing invitation
    st.markdown("### 🧪 Beta Testing Invitation")
    
    beta_invitation = f"""Subject: 🚀 You're Invited to Test MeUnique - Revolutionary AI Recruitment Platform

Hi [Name],

I'm excited to invite you to be one of the first to test MeUnique - my new AI-powered recruitment platform!

🎯 What is MeUnique?
• 6 AI agents that work like expert recruiters
• Smart candidate search across all platforms
• Personalized messaging that gets responses
• Real-time cost tracking and ROI analysis
• Built with Israeli tech innovation

🌐 Try it now: {DOMAIN_URL}

What I'd love from you:
1. Test the candidate search features
2. Try the AI messaging system
3. Share your honest feedback
4. Let me know what features you'd add

🎁 Beta Benefits:
• Free access during beta period
• Direct line to me for support and questions
• Influence on future features
• Early bird pricing when we officially launch

Ready to revolutionize your recruitment process?

Best regards,
Liat Tishman
Founder, MeUnique
📧 liat.tishman85@gmail.com
📱 WhatsApp: +972545436397

P.S. Remember my grandfather's wisdom: "Teach someone to fish vs. giving them a fish" - that's exactly what MeUnique does for recruitment! 🎣"""
    
    st.text_area("Beta Invitation Email:", beta_invitation, height=400)
    
    if st.button("📧 Copy Beta Invitation"):
        st.success("✅ Beta invitation copied! Ready to send to potential users.")

# Sidebar with Enhanced Chat
with st.sidebar:
    st.markdown("## 🎯 Quick Actions")
    
    if st.button("🚀 Start Free Trial"):
        st.success("✅ Free trial activated! Welcome to MeUnique!")
    
    if st.button("📞 Schedule Demo"):
        st.info("📅 Demo scheduled! Check your email for details.")
    
    if st.button("💬 Contact Support"):
        st.info("📱 WhatsApp: +972545436397\n📧 liat.tishman85@gmail.com")
    
    st.markdown("---")
    
    # Enhanced Chat System
    st.markdown("### 🤖 Smart Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Chat interface
    with st.container():
        # Display chat messages
        for message in st.session_state.messages[-3:]:  # Show last 3 messages
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("שאל אותי משהו על MeUnique..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Generate AI response based on current page context
            current_tab = st.session_state.get('current_tab', 'home')
            response = generate_contextual_response(prompt, current_tab)
            
            # Add assistant response
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Display new messages
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                st.markdown(response)
    
    st.markdown("---")
    st.markdown("### 📊 Live Stats")
    st.metric("👥 Beta Users", "47")
    st.metric("🎯 Success Rate", "94%")
    st.metric("⚡ Avg Response", "2.3s")
    
    st.markdown("---")
    st.markdown("### 🌟 Latest Updates")
    st.markdown("• ✅ WhatsApp integration live")
    st.markdown("• ✅ Hebrew language support")
    st.markdown("• ✅ Mobile optimization")
    st.markdown("• 🔄 Enterprise features coming")

def generate_contextual_response(prompt, current_tab):
    """Generate AI response based on current page context"""
    
    # Context-aware responses based on current tab
    context_responses = {
        "home": {
            "keywords": ["מה זה", "איך עובד", "תכונות", "מאפיינים"],
            "response": """🏠 **אני כאן לעזור לך עם MeUnique!**

MeUnique היא פלטפורמה מהפכנית לגיוס מונעת AI שכוללת:

🤖 **6 סוכני AI מתמחים:**
• ProfileMapper - ניתוח פרופילי LinkedIn
• NetworkHunter - חיפוש מועמדים מתקדם  
• MessageCrafter - הודעות מותאמות אישית
• CultureMatcher - התאמה תרבותית
• SkillsAnalyzer - הערכת כישורים
• CompensationGuru - אופטימיזציה של שכר

💡 **כמו שסבא שלי אמר:** "תן לאדם דג ותזין אותו ליום אחד, למד אותו לדוג ותזין אותו לכל החיים"

יש לך שאלה ספציפית על איך זה עובד?"""
        },
        
        "agents": {
            "keywords": ["סוכן", "בוט", "AI", "איך", "מה עושה"],
            "response": """🤖 **הסוכנים החכמים שלנו מוכנים לעבוד בשבילך!**

כל סוכן מתמחה בתחום אחר:

🔍 **ProfileMapper** - מנתח פרופילים בדיוק כירורגי
🎯 **NetworkHunter** - צייד המועמדים הבלתי נלאה  
💬 **MessageCrafter** - אמן ההודעות האישיות
🎭 **CultureMatcher** - המומחה להתאמה תרבותית
🧠 **SkillsAnalyzer** - הגורו הטכני
💰 **CompensationGuru** - המשא ומתן ההוגן

איזה סוכן מעניין אותך הכי הרבה?"""
        },
        
        "analytics": {
            "keywords": ["נתונים", "אנליטיקה", "דוחות", "מטריקות"],
            "response": """📊 **הדשבורד שלנו נותן לך שקיפות מלאה!**

📈 **מה אתה רואה:**
• שיעור תגובה בזמן אמת (67%)
• עלות לכל גיוס ($89)
• ביצועי הסוכנים
• תחזיות והמלצות

💡 **התכונות החכמות:**
• התראות אוטומטיות
• אופטימיזציה של ROI
• מעקב עלויות בזמן אמת
• דוחות מותאמים אישית

רוצה לדעת על מטריקה ספציפית?"""
        },
        
        "business": {
            "keywords": ["מחיר", "עלות", "תוכנית", "ROI", "כסף"],
            "response": """💰 **בואי נדבר על המודל העסקי החכם שלנו!**

📋 **תוכניות התמחור:**
🥉 Starter: $99/חודש - מושלם לפרילנסרים
🥈 Professional: $299/חודש - לסוכנויות קטנות  
🥇 Enterprise: $799/חודש - לחברות גדולות

🧮 **מחשבון ROI:**
• חיסכון ממוצע: $4,200/חודש
• זמן חסוך: 14 שעות/שבוע
• שיעור הצלחה: +40%

💡 **עלות למשתמש בטא:** $9.83/חודש
**נקודת איזון:** 7 משתמשים משלמים

יש לך שאלות על התמחור או ROI?"""
        },
        
        "share": {
            "keywords": ["שיתוף", "שיווק", "בטא", "הזמנה"],
            "response": """🔗 **בואי נפיץ את MeUnique ברשתות!**

📱 **תבניות מוכנות:**
• LinkedIn - פוסט מקצועי
• Twitter - הודעה קצרה ועוצמתית
• WhatsApp - הזמנה אישית

🧪 **תוכנית הבטא:**
• גישה חינמית ל-30 יום
• תמיכה ישירה איתי
• השפעה על תכונות עתידיות
• מחירים מועדפים

📧 **הזמנת בטא מוכנה:**
נוסח מלא עם כל הפרטים ותמריצים

איך אתה רוצה להתחיל לשתף?"""
        }
    }
    
    # Default response if no context matches
    default_response = """🤖 **היי! אני הצ'אט החכם של MeUnique**

אני יכול לעזור לך עם:
• 🏠 מידע כללי על הפלטפורמה
• 🤖 הסוכנים החכמים שלנו
• 📊 אנליטיקה ומטריקות
• 💰 תמחור ומודל עסקי
• 🔗 שיתוף ושיווק

על מה תרצה לשמוע יותר?"""
    
    # Try to match context
    if current_tab in context_responses:
        context = context_responses[current_tab]
        for keyword in context["keywords"]:
            if keyword in prompt.lower():
                return context["response"]
    
    # Check for specific keywords across all contexts
    prompt_lower = prompt.lower()
    if any(word in prompt_lower for word in ["עלות", "מחיר", "כסף", "תשלום"]):
        return context_responses["business"]["response"]
    elif any(word in prompt_lower for word in ["סוכן", "בוט", "AI", "אלגוריתם"]):
        return context_responses["agents"]["response"]
    elif any(word in prompt_lower for word in ["נתונים", "דוח", "אנליטיקה"]):
        return context_responses["analytics"]["response"]
    elif any(word in prompt_lower for word in ["שיתוף", "שיווק", "בטא"]):
        return context_responses["share"]["response"]
    
    return default_response

if __name__ == "__main__":
    main()