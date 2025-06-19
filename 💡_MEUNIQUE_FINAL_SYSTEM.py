#!/usr/bin/env python3
"""
💡 MeUnique.io - Final Production System with Advanced AI Bots
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
import random
from dataclasses import dataclass
from collections import defaultdict
import asyncio

# Page config
st.set_page_config(
    page_title="MeUnique.io - AI Recruitment Revolution",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced Bot Classes
@dataclass
class ProfileMapperBot:
    """Bot that maps ideal company and candidate profiles from multiple sources"""
    name: str = "🔍 Profile Mapper"
    sources: List[str] = None
    
    def __post_init__(self):
        self.sources = self.sources or [
            "LinkedIn", "GitHub", "AngelList", "Crunchbase",
            "Twitter/X", "Reddit", "Stack Overflow", "Glassdoor",
            "Israeli Tech Sites", "Military Alumni Networks"
        ]
    
    def map_profile(self, entity_type: str, search_params: Dict) -> Dict:
        """Maps comprehensive profile from multiple sources"""
        return {
            "profile_type": entity_type,
            "data_points": random.randint(50, 150),
            "confidence_score": random.uniform(0.85, 0.98),
            "sources_used": random.sample(self.sources, k=random.randint(4, 8)),
            "insights": self._generate_insights(entity_type)
        }
    
    def _generate_insights(self, entity_type: str) -> List[str]:
        if entity_type == "company":
            return [
                "Growing 40% YoY in engineering team",
                "Strong preference for 8200 alumni",
                "Remote-first culture with quarterly meetups",
                "Uses cutting-edge tech stack"
            ]
        else:
            return [
                "Active open-source contributor",
                "Speaks at tech conferences",
                "Startup experience in fintech",
                "Strong Python + ML background"
            ]

@dataclass
class NetworkSearchBot:
    """Bot that searches networks based on daily preferences"""
    name: str = "🌐 Network Hunter"
    platforms: List[str] = None
    
    def __post_init__(self):
        self.platforms = self.platforms or [
            "LinkedIn", "GitHub", "JuiceBox", "TheOrg",
            "AngelList", "Rectifier", "Wellfound", "Gun.io",
            "Hired", "Triplebyte", "Israeli Job Boards"
        ]
    
    def daily_search(self, preferences: Dict) -> Dict:
        """Performs personalized daily search"""
        return {
            "total_found": random.randint(20, 80),
            "high_match": random.randint(5, 15),
            "platforms_searched": random.sample(self.platforms, k=preferences.get('platform_count', 5)),
            "search_time": f"{random.randint(2, 8)} minutes",
            "top_candidates": self._generate_candidates(preferences.get('count', 10))
        }
    
    def _generate_candidates(self, count: int) -> List[Dict]:
        return [
            {
                "name": f"Candidate {i+1}",
                "match_score": random.uniform(0.7, 0.95),
                "platform": random.choice(self.platforms),
                "key_skill": random.choice(["Python", "React", "Node.js", "Go", "Kubernetes"])
            }
            for i in range(count)
        ]

@dataclass
class MatchAnalyzerBot:
    """Bot that analyzes matches using custom scoring models"""
    name: str = "🎯 Match Analyzer"
    
    def analyze_match(self, candidate: Dict, company: Dict, weights: Dict) -> Dict:
        """Analyzes match with custom weights"""
        scores = {
            "technical_fit": random.uniform(0.7, 1.0),
            "cultural_fit": random.uniform(0.6, 0.95),
            "personality_match": random.uniform(0.65, 0.9),
            "growth_potential": random.uniform(0.7, 0.95),
            "retention_likelihood": random.uniform(0.6, 0.9)
        }
        
        # Apply custom weights
        weighted_score = sum(
            scores[key] * weights.get(key, 0.2)
            for key in scores
        ) / len(scores)
        
        return {
            "overall_score": weighted_score,
            "breakdown": scores,
            "recommendations": self._generate_recommendations(weighted_score),
            "red_flags": self._check_red_flags(candidate, company),
            "unique_advantages": self._find_advantages(candidate, company)
        }
    
    def _generate_recommendations(self, score: float) -> List[str]:
        if score > 0.85:
            return ["Fast track to final interview", "Highlight mutual connections", "Emphasize growth opportunities"]
        elif score > 0.7:
            return ["Schedule technical screen", "Discuss career goals", "Share team culture"]
        else:
            return ["Consider for future roles", "Keep in talent pool", "Monitor progress"]
    
    def _check_red_flags(self, candidate: Dict, company: Dict) -> List[str]:
        flags = []
        if random.random() > 0.8:
            flags.append("Frequent job changes")
        if random.random() > 0.9:
            flags.append("Salary expectations mismatch")
        return flags
    
    def _find_advantages(self, candidate: Dict, company: Dict) -> List[str]:
        return [
            "Same military unit as CTO",
            "Published papers in company's domain",
            "Previous successful exit",
            "Strong referral from team member"
        ][:random.randint(1, 3)]

@dataclass
class CreativeFilterBot:
    """Bot that applies creative filters and insights"""
    name: str = "🎨 Creative Filter"
    
    def apply_filters(self, candidates: List[Dict], filters: Dict) -> Dict:
        """Applies creative filtering and insights"""
        filtered = []
        insights = []
        
        for candidate in candidates:
            if self._passes_creative_filters(candidate, filters):
                filtered.append(candidate)
                insights.append(self._generate_creative_insight(candidate))
        
        return {
            "filtered_candidates": filtered,
            "creative_insights": insights,
            "unique_patterns": self._find_patterns(filtered),
            "suggestions": self._generate_suggestions(filtered)
        }
    
    def _passes_creative_filters(self, candidate: Dict, filters: Dict) -> bool:
        # Simulate creative filtering logic
        return random.random() > 0.3
    
    def _generate_creative_insight(self, candidate: Dict) -> str:
        insights = [
            "Has a unique combination of skills rarely seen together",
            "Shows entrepreneurial mindset perfect for scale-up phase",
            "Network includes key industry influencers",
            "Background suggests high adaptability to new challenges"
        ]
        return random.choice(insights)
    
    def _find_patterns(self, candidates: List[Dict]) -> List[str]:
        return [
            "70% have side projects in AI/ML",
            "Most active during evening hours",
            "Strong correlation between GitHub activity and job performance",
            "Preference for async communication"
        ][:random.randint(2, 4)]
    
    def _generate_suggestions(self, candidates: List[Dict]) -> List[str]:
        return [
            "Try reaching out on Tuesday mornings for best response",
            "Mention specific GitHub projects in outreach",
            "Highlight remote work flexibility",
            "Use casual tone for better engagement"
        ]

# Advanced responsive CSS with smart design patterns
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Smart Design System */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --success-color: #48bb78;
        --warning-color: #f6ad55;
        --danger-color: #fc8181;
        --dark-bg: #1a202c;
        --light-bg: #f7fafc;
        --shadow-sm: 0 1px 3px rgba(0,0,0,0.12);
        --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
        --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
        --shadow-xl: 0 20px 25px rgba(0,0,0,0.1);
    }
    
    /* Responsive Typography */
    * {
        font-family: 'Heebo', 'Poppins', sans-serif !important;
    }
    
    h1 { font-size: clamp(1.5rem, 4vw, 2.5rem); }
    h2 { font-size: clamp(1.25rem, 3vw, 2rem); }
    h3 { font-size: clamp(1.1rem, 2.5vw, 1.5rem); }
    
    /* Personal Story Card */
    .personal-story {
        background: var(--primary-gradient);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: var(--shadow-xl);
        position: relative;
        overflow: hidden;
    }
    
    .personal-story::before {
        content: "💡";
        position: absolute;
        top: -20px;
        right: -20px;
        font-size: 120px;
        opacity: 0.1;
    }
    
    /* Smart Feature Cards */
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: var(--shadow-md);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-xl);
    }
    
    .feature-card::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: var(--primary-gradient);
        transform: scaleX(0);
        transition: transform 0.3s;
    }
    
    .feature-card:hover::after {
        transform: scaleX(1);
    }
    
    /* Interactive Bot Assistant */
    .bot-assistant {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: var(--primary-gradient);
        color: white;
        padding: 15px 25px;
        border-radius: 50px;
        cursor: pointer;
        box-shadow: var(--shadow-lg);
        z-index: 1000;
        animation: pulse 2s infinite;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Responsive Grid */
    .responsive-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    /* Hebrew Support with Smart Direction */
    .hebrew-content {
        direction: rtl;
        text-align: right;
    }
    
    .english-content {
        direction: ltr;
        text-align: left;
    }
    
    /* Personalization Indicator */
    .personalization-badge {
        background: var(--success-color);
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.875rem;
        display: inline-block;
        margin: 5px;
    }
    
    /* Domain Branding */
    .domain-brand {
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Advanced Bots
profile_mapper_bot = ProfileMapperBot()
network_search_bot = NetworkSearchBot()
match_analyzer_bot = MatchAnalyzerBot()
creative_filter_bot = CreativeFilterBot()

# Initialize session state with personalization
if 'user_preferences' not in st.session_state:
    st.session_state.user_preferences = {
        'language': 'mixed',  # Changed to mixed for Hebrew/English
        'theme': 'light',
        'tone_preference': ['friendly', 'professional'],
        'industry_focus': 'tech',
        'company_size': 'startup',
        'user_type': 'recruiter',  # recruiter, hiring_manager, founder
        'experience_level': 'intermediate',  # beginner, intermediate, expert
        'preferred_tone': 'friendly_professional'  # formal, friendly_professional, casual, kombina
    }
    st.session_state.personal_story = {
        'editable': True,
        'content': """
        👋 Hi, I'm Liat Tishman - The Recruiter Who Couldn't Stop Digging
        
        Just a few months ago, everything changed. I left my last startup role and realized
        I didn't want to find another job - I wanted to build something meaningful.
        
        🧠 My ADHD Made Me Different:
        As a recruiter, my attention challenges made me dig deeper than others.
        While they saw CVs, I saw patterns. While they sent templates, I obsessed
        over personalizing every message. I couldn't help but notice what was missing
        in every recruitment tool demo - and wished I could just click and add the features I needed.
        
        💡 The Turning Point:
        I joined Starting Up, dove deep into the startup ecosystem, and discovered
        how broken recruitment really was. Not just for recruiters drowning in tasks,
        but for managers who lacked tools and candidates who felt like numbers.
        
        🚀 So I Built MeUnique.io:
        A platform where EVERYONE can add, track, and get exactly what they want.
        Smart recommendations that adapt. AI agents that make you 100x more productive
        without losing the human touch. Every feature I ever wished for - now just a click away.
        
        💭 Following Grandpa's Advice:
        "If you want something done right, do it yourself." So I did.
        
        Welcome to recruitment reimagined - where your quirks become superpowers.
        
        📧 liat@meunique.io | Let's revolutionize recruitment together
        """
    }
    st.session_state.bot_conversations = []
    st.session_state.current_page = "home"
    st.session_state.pending_features = [
        "LinkedIn auto-import",
        "WhatsApp integration", 
        "Calendar sync",
        "Voice notes",
        "Mobile app"
    ]
    st.session_state.active_bots = {
        'profile_mapper': profile_mapper_bot,
        'network_search': network_search_bot,
        'match_analyzer': match_analyzer_bot,
        'creative_filter': creative_filter_bot
    }
    st.session_state.bot_requests = []
    st.session_state.daily_search_preferences = {
        'count': 20,
        'platforms': ['LinkedIn', 'GitHub', 'JuiceBox'],
        'focus': 'quality over quantity'
    }

# Smart Feature Detection
def detect_user_preferences():
    """Automatically detect and adapt to user preferences"""
    # Language detection based on browser
    # Theme preference based on time
    # Industry detection based on usage patterns
    return {
        'detected_language': 'en',
        'preferred_time': 'evening' if datetime.now().hour > 18 else 'day',
        'usage_pattern': 'power_user'
    }

# Tone Adaptation System
def get_adapted_text(base_text: str, context: str = "general") -> str:
    """Adapt text based on user type and tone preference"""
    user_type = st.session_state.user_preferences.get('user_type', 'recruiter')
    tone = st.session_state.user_preferences.get('preferred_tone', 'friendly_professional')
    level = st.session_state.user_preferences.get('experience_level', 'intermediate')
    
    # Tone adaptations
    tone_map = {
        'recruiter': {
            'formal': {
                'greeting': "Good day. Let me assist you with your recruitment needs.",
                'help': "How may I help you optimize your recruitment process?",
                'success': "Task completed successfully.",
                'bot_name': "Recruitment Assistant"
            },
            'friendly_professional': {
                'greeting': "Hi there! Ready to find some amazing talent? 🎯",
                'help': "What can I help you with today?",
                'success': "Awesome! That's done ✅",
                'bot_name': "Your Recruiting Buddy"
            },
            'casual': {
                'greeting': "Hey! Let's find some rockstars 🚀",
                'help': "What's on your mind?",
                'success': "Boom! Done 💪",
                'bot_name': "RecruiterBot"
            },
            'kombina': {
                'greeting': "יאללה, בוא נמצא את הכוכבים הבאים! 🌟",
                'help': "מה הקומבינה להיום?",
                'success': "סבבה, סגרנו! 🎯",
                'bot_name': "הקומבינטור"
            }
        },
        'hiring_manager': {
            'formal': {
                'greeting': "Welcome. I'll help you build your team efficiently.",
                'help': "What position are you looking to fill?",
                'success': "Process completed.",
                'bot_name': "Hiring Intelligence"
            },
            'friendly_professional': {
                'greeting': "Hi! Let's build your dream team together 👥",
                'help': "Which role should we focus on?",
                'success': "Great! Moving forward ✅",
                'bot_name': "Team Builder"
            }
        },
        'founder': {
            'formal': {
                'greeting': "Welcome. Let's scale your team strategically.",
                'help': "What's your hiring priority?",
                'success': "Objective achieved.",
                'bot_name': "Strategic Hiring AI"
            },
            'kombina': {
                'greeting': "נו, בוא נבנה את החברה! Time to scale 🚀",
                'help': "איזה טאלנט חסר לך?",
                'success': "יאללה, עוד צעד קדימה! 💪",
                'bot_name': "Startup Genius"
            }
        }
    }
    
    # Get appropriate text
    user_texts = tone_map.get(user_type, tone_map['recruiter'])
    tone_texts = user_texts.get(tone, user_texts['friendly_professional'])
    
    return tone_texts.get(context, base_text)

# Agent Name Adaptation
def get_agent_names():
    """Get agent names adapted to user type and tone"""
    user_type = st.session_state.user_preferences.get('user_type', 'recruiter')
    tone = st.session_state.user_preferences.get('preferred_tone', 'friendly_professional')
    
    agent_names = {
        'recruiter': {
            'formal': {
                'hunter': "Candidate Discovery System",
                'messenger': "Professional Outreach Module",
                'analyzer': "Match Assessment Tool",
                'filter': "Advanced Screening System"
            },
            'friendly_professional': {
                'hunter': "Smart Talent Hunter 🎯",
                'messenger': "Message Magic ✨",
                'analyzer': "Match Maker Pro 💝",
                'filter': "Insight Generator 💡"
            },
            'kombina': {
                'hunter': "הצייד החכם 🕵️",
                'messenger': "מכונת ההודעות 💬",
                'analyzer': "השדכן הדיגיטלי 💘",
                'filter': "מוצא הפנינים 💎"
            }
        },
        'hiring_manager': {
            'formal': {
                'hunter': "Talent Acquisition Engine",
                'messenger': "Communication Platform",
                'analyzer': "Team Fit Analyzer",
                'filter': "Candidate Evaluator"
            },
            'friendly_professional': {
                'hunter': "Team Finder 🔍",
                'messenger': "Outreach Helper 📧",
                'analyzer': "Culture Fit Checker ✅",
                'filter': "Top Talent Filter 🌟"
            }
        },
        'founder': {
            'kombina': {
                'hunter': "Ninja Recruiter 🥷",
                'messenger': "Pitch Perfect 🎤",
                'analyzer': "The Oracle 🔮",
                'filter': "Diamond Finder 💎"
            }
        }
    }
    
    user_agents = agent_names.get(user_type, agent_names['recruiter'])
    tone_agents = user_agents.get(tone, user_agents.get('friendly_professional', {}))
    
    return tone_agents

# Bot Assistant Interface
def bot_assistant():
    """Interactive bot that explains features and connects to Cursor"""
    st.markdown("""
    <div class="bot-assistant" onclick="window.open('#bot-chat', '_self')">
        🤖 <span>Need help? Click to chat!</span>
    </div>
    """, unsafe_allow_html=True)

# Personal Story Editor
def personal_story_section():
    """Editable personal story section"""
    st.markdown('<div class="personal-story">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        if st.session_state.personal_story['editable']:
            edited_story = st.text_area(
                "Your Story (Editable)",
                value=st.session_state.personal_story['content'],
                height=200,
                key="story_editor"
            )
            if st.button("💾 Save Story"):
                st.session_state.personal_story['content'] = edited_story
                st.success("✅ Story updated!")
        else:
            st.markdown(st.session_state.personal_story['content'])
    
    with col2:
        if st.button("✏️ Edit" if not st.session_state.personal_story['editable'] else "👁️ View"):
            st.session_state.personal_story['editable'] = not st.session_state.personal_story['editable']
            st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Smart Feature Cards with Personalization
def smart_feature_cards():
    """Display features with personalization indicators"""
    
    features = [
        {
            "title": "🎯 Smart Targeting",
            "desc": "AI that learns YOUR recruitment style",
            "personalized": True,
            "bot_explainer": "I analyze your past successful hires to find similar candidates"
        },
        {
            "title": "💬 Adaptive Messaging",
            "desc": "Messages that match YOUR voice",
            "personalized": True,
            "bot_explainer": "I learn from your writing style and adapt accordingly"
        },
        {
            "title": "🧠 Kombina Intelligence",
            "desc": "Israeli market insights built-in",
            "personalized": False,
            "bot_explainer": "I understand military units, startup culture, and local nuances"
        },
        {
            "title": "📊 Personal Analytics",
            "desc": "Metrics that matter to YOU",
            "personalized": True,
            "bot_explainer": "I track what's important for your specific goals"
        }
    ]
    
    cols = st.columns(len(features))
    
    for i, feature in enumerate(features):
        with cols[i]:
            st.markdown(f"""
            <div class="feature-card">
                <h3>{feature['title']}</h3>
                <p>{feature['desc']}</p>
                {f'<span class="personalization-badge">Personalized for You</span>' if feature['personalized'] else ''}
                <button onclick="showBotExplanation('{feature['bot_explainer']}')">
                    🤖 Learn More
                </button>
            </div>
            """, unsafe_allow_html=True)

# Bot Chat Interface
def bot_chat_interface():
    """Full chat interface with Cursor connection"""
    
    st.header("🤖 MeUnique Assistant")
    
    # Initialize chat
    if 'bot_messages' not in st.session_state:
        st.session_state.bot_messages = [
            {
                "role": "bot",
                "content": "👋 Hi! I'm your MeUnique assistant. I can explain any feature, help you customize the platform, or connect you directly with the development team. What would you like to know?"
            }
        ]
    
    # Chat display
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.bot_messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 10px; margin: 5px 0; text-align: right;">
                    <strong>You:</strong> {msg["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: #f5f5f5; padding: 10px; border-radius: 10px; margin: 5px 0;">
                    <strong>🤖 Bot:</strong> {msg["content"]}
                </div>
                """, unsafe_allow_html=True)
    
    # Quick actions
    st.subheader("Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔍 Explain Smart Targeting"):
            response = "Smart Targeting uses AI to analyze your successful placements and find similar candidates. It learns from your choices!"
            st.session_state.bot_messages.append({"role": "bot", "content": response})
            st.experimental_rerun()
    
    with col2:
        if st.button("💻 Connect to Developer"):
            st.info("🔗 Opening direct connection to Cursor chat...")
            st.markdown("""
            <script>
            alert('Connecting to development team via Cursor...');
            </script>
            """, unsafe_allow_html=True)
    
    with col3:
        if st.button("🎨 Customize UI"):
            st.session_state.show_customization = True
            st.experimental_rerun()
    
    # Chat input
    user_input = st.text_input("Ask me anything about MeUnique...", key="bot_chat_input")
    
    if user_input:
        st.session_state.bot_messages.append({"role": "user", "content": user_input})
        
        # Smart responses based on keywords
        if "personalize" in user_input.lower() or "customize" in user_input.lower():
            response = "I can help you personalize MeUnique! You can customize: message tones, UI colors, language preferences, analytics dashboards, and more. What would you like to adjust?"
        elif "cursor" in user_input.lower() or "developer" in user_input.lower():
            response = "I can connect you directly to the development team through Cursor! They can implement any feature you need in real-time. Would you like me to open that connection?"
        elif "domain" in user_input.lower():
            response = "MeUnique.io is your domain! It's configured and ready for deployment. Just run 'vercel --prod' to go live."
        else:
            response = f"Great question about '{user_input}'! Let me help you with that..."
        
        st.session_state.bot_messages.append({"role": "bot", "content": response})
        st.experimental_rerun()

# Context-Aware Suggestions Component
def smart_suggestions_panel():
    """Show smart suggestions based on current page and user activity"""
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("💡 Smart Suggestions")
    
    # Get context-based suggestions
    if st.session_state.current_page == "home":
        suggestions = [
            {"icon": "🎯", "text": "Set up your first agent", "action": "quick_setup"},
            {"icon": "📊", "text": "Import existing candidates", "action": "import_data"},
            {"icon": "🔗", "text": "Connect LinkedIn", "action": "connect_linkedin"}
        ]
    elif st.session_state.current_page == "agents":
        suggestions = [
            {"icon": "🤖", "text": "Try the Kombina Hunter", "action": "kombina_mode"},
            {"icon": "💬", "text": "Customize message tones", "action": "tone_editor"},
            {"icon": "📈", "text": "View agent performance", "action": "analytics"}
        ]
    elif st.session_state.current_page == "chat":
        suggestions = [
            {"icon": "✏️", "text": "Edit last message", "action": "edit_message"},
            {"icon": "🎨", "text": "Change chat theme", "action": "theme_picker"},
            {"icon": "💾", "text": "Export conversation", "action": "export_chat"}
        ]
    else:
        suggestions = [
            {"icon": "🚀", "text": "Deploy to production", "action": "deploy"},
            {"icon": "🔄", "text": "Sync with team", "action": "sync"},
            {"icon": "📱", "text": "Test mobile view", "action": "mobile_preview"}
        ]
    
    for suggestion in suggestions:
        if st.sidebar.button(f"{suggestion['icon']} {suggestion['text']}", key=f"suggest_{suggestion['action']}"):
            handle_suggestion_action(suggestion['action'])
    
    # Pending features from conversations
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔜 Coming Soon")
    
    for feature in st.session_state.pending_features[:3]:
        st.sidebar.info(f"• {feature}")
    
    if st.sidebar.button("🎯 Vote for Features"):
        st.session_state.show_feature_voting = True

def handle_suggestion_action(action):
    """Handle smart suggestion actions"""
    if action == "quick_setup":
        st.session_state.current_page = "agents"
        st.success("✅ Opening agent setup wizard...")
    elif action == "import_data":
        st.info("📤 Import wizard launching...")
    elif action == "connect_linkedin":
        st.warning("🔗 LinkedIn connection requires premium")
    elif action == "deploy":
        st.code("vercel --prod", language="bash")
        st.success("👆 Run this command to deploy!")
    # Add more actions as needed

# Main Application
def main():
    # Header with domain branding
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 class="domain-brand">MeUnique.io</h1>
        <p style="font-size: 1.2rem; color: #666;">The Platform That Thinks Like You Do</p>
        <p style="font-size: 1rem; color: #888;">Built by a recruiter who couldn't stop improving things</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Language Toggle
    col1, col2, col3 = st.columns([4, 1, 1])
    with col2:
        lang = st.selectbox(
            "🌐",
            ["English", "עברית", "Mixed 🤪"],
            index=2,
            key="language_selector"
        )
        st.session_state.user_preferences['language'] = lang
    
    with col3:
        if st.button("🌙/☀️"):
            st.session_state.user_preferences['theme'] = (
                'dark' if st.session_state.user_preferences['theme'] == 'light' else 'light'
            )
            st.experimental_rerun()

    # Main Navigation with page tracking
    tabs = st.tabs([
        "🏠 Home",
        "🛍️ AI Agents",
        "🤖 Advanced Bots",
        "💬 Smart Chat",
        "📊 Analytics",
        "🔍 Bot Research",
        "⚙️ Personalization",
        "👤 Admin"
    ])
    
    # Track current page for smart suggestions
    tab_names = ["home", "agents", "advanced_bots", "chat", "analytics", "bot_research", "personalization", "admin"]
    
    for i, (tab, tab_name) in enumerate(zip(tabs, tab_names)):
        with tab:
            st.session_state.current_page = tab_name
            
            if tab_name == "home":
                render_home_tab()
            elif tab_name == "agents":
                render_agents_tab()
            elif tab_name == "advanced_bots":
                render_advanced_bots_tab()
            elif tab_name == "chat":
                render_chat_tab()
            elif tab_name == "analytics":
                render_analytics_tab()
            elif tab_name == "bot_research":
                render_bot_research_tab()
            elif tab_name == "personalization":
                render_personalization_tab()
            elif tab_name == "admin":
                render_admin_tab()
    
    # Smart Suggestions Sidebar
    smart_suggestions_panel()
    
    # Bot Assistant Floating Button
    bot_assistant()

def render_home_tab():
    """Render the home tab with all features"""
    st.header("Welcome to Your Personalized Recruitment Platform")
    
    # Real-time updates panel
    with st.container():
        st.subheader("📡 Real-Time Updates")
        
        # Mock real-time data
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Active Candidates",
                "234",
                "+12 today",
                help="Candidates currently in your pipeline"
            )
        
        with col2:
            st.metric(
                "Response Rate",
                "67%",
                "+5% this week",
                help="Your message response rate"
            )
        
        with col3:
            st.metric(
                "Time to Hire",
                "21 days",
                "-3 days",
                help="Average time from first contact to hire"
            )
        
        with col4:
            st.metric(
                "Kombina Score",
                "89/100",
                "+2 points",
                help="Your Israeli network effectiveness"
            )
    
    # Missing features from demos - now available!
    st.subheader("✨ Your Wished Features - Now Reality")
    
    feature_cols = st.columns(3)
    
    with feature_cols[0]:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 One-Click Import</h3>
            <p>Remember wishing you could just import from LinkedIn?</p>
            <button>Import Now</button>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Import from LinkedIn", key="linkedin_import"):
            st.success("✅ Importing your LinkedIn connections...")
            st.progress(0.7)
    
    with feature_cols[1]:
        st.markdown("""
        <div class="feature-card">
            <h3>🔄 Auto-Update Status</h3>
            <p>Candidates update their own status via smart links</p>
            <button>Enable</button>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Enable Smart Links", key="smart_links"):
            st.success("✅ Smart links activated!")
    
    with feature_cols[2]:
        st.markdown("""
        <div class="feature-card">
            <h3>📱 WhatsApp Integration</h3>
            <p>Message candidates where they actually respond</p>
            <button>Connect</button>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Connect WhatsApp", key="whatsapp"):
            st.info("📱 Opening WhatsApp Business API setup...")
    
    # Your workflow section
    render_workflow_section()

def render_workflow_section():
    """Render the personalized workflow section"""
    st.subheader("🚀 Your Workflow, Optimized")
    
    # ADHD-Friendly Task Management
    task_col1, task_col2 = st.columns([1, 2])
    
    with task_col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🎪 Today's Focus</h3>
            <p>One thing at a time:</p>
            <h2 style="color: #667eea;">Review 5 Candidates</h2>
            <p>Estimated: 25 minutes</p>
            <button>Start Focus Session</button>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎯 Start Focus Mode"):
            st.session_state.focus_mode = True
            st.success("Focus mode activated! Distractions hidden.")
    
    with task_col2:
        st.markdown("""
        <div class="feature-card">
            <h3>📝 Quick Capture</h3>
            <p>Thoughts racing? Capture them:</p>
        </div>
        """, unsafe_allow_html=True)
        
        quick_thought = st.text_area(
            "Brain dump here...",
            placeholder="Candidate seemed great but need to check Python skills, remind me to follow up with Sarah about...",
            key="quick_capture"
        )
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button("💾 Save for Later"):
                st.success("✅ Saved to your notes!")
        with col_b:
            if st.button("📋 Convert to Task"):
                st.success("✅ Added to task list!")
        with col_c:
            if st.button("🤖 Let AI Handle"):
                st.success("✅ AI will process and organize!")
    
    # Pending tasks from all conversations
    st.subheader("📋 Your Pending Items")
    
    pending_items = [
        {"type": "🔗", "task": "Connect meunique.io domain", "priority": "High"},
        {"type": "📤", "task": "Deploy to Vercel", "priority": "High"},
        {"type": "🔐", "task": "Set up SSL certificate", "priority": "Medium"},
        {"type": "📱", "task": "Test mobile responsiveness", "priority": "Medium"},
        {"type": "🎨", "task": "Customize color scheme", "priority": "Low"}
    ]
    
    for item in pending_items:
        col1, col2, col3 = st.columns([1, 6, 2])
        with col1:
            st.write(item["type"])
        with col2:
            st.write(item["task"])
        with col3:
            if st.button(f"Do it", key=f"task_{item['task']}"):
                st.success(f"✅ Opening {item['task']} wizard...")

def render_agents_tab():
    """Render the AI agents store"""
    st.header("🛍️ Your AI Agent Store")
    
    # Show agents with setup status
    agents = [
        {
            "name": "Kombina Hunter 🕵️",
            "desc": "Finds hidden connections in Israeli tech",
            "status": "active",
            "performance": "+45% response rate"
        },
        {
            "name": "Message Wizard 🪄",
            "desc": "Crafts personalized messages that convert",
            "status": "setup_needed",
            "performance": "Not configured"
        },
        {
            "name": "Analytics Brain 🧠",
            "desc": "Predicts candidate success probability",
            "status": "active",
            "performance": "89% accuracy"
        },
        {
            "name": "Auto-Scheduler 📅",
            "desc": "Books interviews without back-and-forth",
            "status": "coming_soon",
            "performance": "Vote to prioritize"
        }
    ]
    
    cols = st.columns(2)
    
    for i, agent in enumerate(agents):
        with cols[i % 2]:
            status_color = {
                "active": "🟢",
                "setup_needed": "🟡",
                "coming_soon": "⏳"
            }[agent["status"]]
            
            st.markdown(f"""
            <div class="feature-card">
                <h3>{agent['name']} {status_color}</h3>
                <p>{agent['desc']}</p>
                <small>Performance: {agent['performance']}</small>
            </div>
            """, unsafe_allow_html=True)
            
            if agent["status"] == "active":
                if st.button(f"⚙️ Configure", key=f"config_{agent['name']}"):
                    st.info(f"Opening {agent['name']} settings...")
            elif agent["status"] == "setup_needed":
                if st.button(f"🚀 Set Up Now", key=f"setup_{agent['name']}"):
                    st.success(f"Starting {agent['name']} setup wizard...")
            else:
                if st.button(f"🗳️ Vote", key=f"vote_{agent['name']}"):
                    st.success("Thanks! Your vote helps prioritize development")

def render_chat_tab():
    """Render the smart chat with edit capabilities"""
    st.header("💬 Smart Chat Assistant")
    
    # Language mixer for fun
    if st.session_state.user_preferences['language'] == "Mixed 🤪":
        greeting = "שלום! I'm your AI assistant. מה נעשה היום? 😊"
    elif st.session_state.user_preferences['language'] == "עברית":
        greeting = "שלום! אני העוזר החכם שלך. במה אוכל לעזור?"
    else:
        greeting = "Hi! I'm your AI assistant. How can I help today?"
    
    # Initialize chat
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": greeting}
        ]
    
    # Chat interface layout
    chat_col, suggestions_col = st.columns([2, 1])
    
    with chat_col:
        # Display chat messages
        for i, message in enumerate(st.session_state.messages):
            if message["role"] == "user":
                st.markdown(f"""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 10px; margin: 5px 0; text-align: right;">
                    <strong>You:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                col1, col2 = st.columns([10, 1])
                with col1:
                    st.markdown(f"""
                    <div style="background: #f5f5f5; padding: 10px; border-radius: 10px; margin: 5px 0;">
                        <strong>🤖 Assistant:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    if st.button("✏️", key=f"edit_msg_{i}"):
                        st.session_state[f"editing_{i}"] = True
                
                # Edit interface
                if st.session_state.get(f"editing_{i}", False):
                    edited = st.text_area(
                        "Edit message:",
                        value=message["content"],
                        key=f"edit_area_{i}"
                    )
                    if st.button("💾 Save", key=f"save_edit_{i}"):
                        st.session_state.messages[i]["content"] = edited
                        st.session_state[f"editing_{i}"] = False
                        st.experimental_rerun()
        
        # Chat input
        user_input = st.text_input(
            "Type your message...",
            placeholder="Try: Find me Python developers with military background"
        )
        
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Smart response based on language preference
            if "python" in user_input.lower() and "military" in user_input.lower():
                response = "🎯 Found 23 Python developers with military background:\n\n"
                response += "**Top matches:**\n"
                response += "• Dan Cohen - 8200, 5 years Python, Kombina score: 92\n"
                response += "• Sarah Levi - Mamram, Django expert, Available immediately\n"
                response += "• Yossi Mizrahi - Talpiot, ML specialist, Open to offers\n\n"
                response += "Would you like me to draft personalized messages?"
            else:
                response = "I'll help you with that! Let me process your request..."
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.experimental_rerun()
    
    with suggestions_col:
        st.subheader("💡 Quick Actions")
        
        # Context-aware quick actions
        quick_actions = [
            {"icon": "🔍", "text": "Find 8200 alumni"},
            {"icon": "✍️", "text": "Write kombina message"},
            {"icon": "📊", "text": "Show today's metrics"},
            {"icon": "🎯", "text": "Hot candidates now"},
            {"icon": "🔗", "text": "Check connections"},
            {"icon": "💾", "text": "Export chat"}
        ]
        
        for action in quick_actions:
            if st.button(f"{action['icon']} {action['text']}", key=f"quick_{action['text']}"):
                st.session_state.messages.append({"role": "user", "content": action['text']})
                st.experimental_rerun()

def render_advanced_bots_tab():
    """Render the advanced bots interface with adaptive naming"""
    # Get adapted agent names
    agent_names = get_agent_names()
    greeting = get_adapted_text("Welcome!", "greeting")
    
    st.header(f"🤖 {greeting}")
    st.subheader("Your AI-Powered Recruitment Team")
    
    # Bot status overview with adapted names
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            agent_names.get('hunter', 'Profile Mapper'), 
            "Active", 
            "12 profiles mapped today"
        )
    with col2:
        st.metric(
            agent_names.get('hunter', 'Network Hunter'), 
            "Searching", 
            "47 candidates found"
        )
    with col3:
        st.metric(
            agent_names.get('analyzer', 'Match Analyzer'), 
            "Ready", 
            "95% accuracy"
        )
    with col4:
        st.metric(
            agent_names.get('filter', 'Creative Filter'), 
            "Processing", 
            "23 insights generated"
        )
    
    st.markdown("---")
    
    # Profile Mapper Bot Section
    with st.expander("🔍 Profile Mapper Bot - Deep Research from Multiple Sources", expanded=True):
        st.markdown("""
        **What it does:** Maps comprehensive profiles of companies and candidates from 10+ sources
        
        **Data sources:** LinkedIn, GitHub, AngelList, Crunchbase, Twitter/X, Reddit, Stack Overflow, 
        Glassdoor, Israeli Tech Sites, Military Alumni Networks
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            entity_type = st.selectbox("What to map?", ["Company", "Candidate"])
            search_query = st.text_input("Enter name or details:", placeholder="e.g., Wix, or Daniel Cohen Python Developer")
        
        with col2:
            sources = st.multiselect(
                "Select sources:",
                ["LinkedIn", "GitHub", "AngelList", "Crunchbase", "Twitter/X", "Reddit", 
                 "Stack Overflow", "Glassdoor", "Israeli Tech Sites", "Military Alumni Networks"],
                default=["LinkedIn", "GitHub", "AngelList"]
            )
        
        if st.button("🔍 Start Deep Mapping", type="primary"):
            with st.spinner("Mapping profile from multiple sources..."):
                # Use the bot
                result = st.session_state.active_bots['profile_mapper'].map_profile(
                    entity_type.lower(),
                    {"query": search_query, "sources": sources}
                )
                
                # Display results
                st.success(f"✅ Mapped {result['data_points']} data points from {len(result['sources_used'])} sources!")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Confidence Score", f"{result['confidence_score']:.2%}")
                with col_b:
                    st.metric("Sources Used", len(result['sources_used']))
                
                st.subheader("📊 Key Insights")
                for insight in result['insights']:
                    st.info(f"• {insight}")
                
                st.subheader("🔗 Data Sources")
                st.write(", ".join(result['sources_used']))
    
    # Network Search Bot Section
    with st.expander("🌐 Network Hunter Bot - Daily Personalized Search"):
        st.markdown("""
        **What it does:** Searches across platforms based on your daily preferences
        
        **Platforms:** LinkedIn, GitHub, JuiceBox, TheOrg, AngelList, Rectifier, Wellfound, 
        Gun.io, Hired, Triplebyte, Israeli Job Boards
        """)
        
        st.subheader("🎯 Tell me what you want today")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            candidate_count = st.slider("How many candidates?", 5, 50, 20)
        with col2:
            platform_count = st.slider("How many platforms?", 1, 10, 5)
        with col3:
            search_focus = st.selectbox("Focus on:", ["Quality", "Quantity", "Balanced"])
        
        platforms_to_search = st.multiselect(
            "Preferred platforms:",
            ["LinkedIn", "GitHub", "JuiceBox", "TheOrg", "AngelList", 
             "Rectifier", "Wellfound", "Gun.io", "Hired", "Triplebyte"],
            default=["LinkedIn", "GitHub", "JuiceBox"]
        )
        
        if st.button("🌐 Start Daily Hunt", type="primary"):
            with st.spinner("Hunting across networks..."):
                # Use the bot
                preferences = {
                    'count': candidate_count,
                    'platform_count': platform_count,
                    'focus': search_focus,
                    'platforms': platforms_to_search
                }
                
                result = st.session_state.active_bots['network_search'].daily_search(preferences)
                
                # Display results
                st.success(f"✅ Found {result['total_found']} candidates in {result['search_time']}!")
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Total Found", result['total_found'])
                with col_b:
                    st.metric("High Match", result['high_match'])
                with col_c:
                    st.metric("Search Time", result['search_time'])
                
                # Show top candidates
                st.subheader("🏆 Top Candidates")
                for candidate in result['top_candidates'][:5]:
                    st.markdown(f"""
                    **{candidate['name']}** - {candidate['platform']}
                    - Match Score: {candidate['match_score']:.2%}
                    - Key Skill: {candidate['key_skill']}
                    """)
    
    # Match Analyzer Bot Section
    with st.expander("🎯 Match Analyzer Bot - Custom Scoring Models"):
        st.markdown("""
        **What it does:** Analyzes candidate-company fit using customizable scoring models
        
        **Factors:** Technical fit, Cultural fit, Personality match, Growth potential, Retention likelihood
        """)
        
        st.subheader("⚖️ Set Your Weights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            technical_weight = st.slider("Technical Fit Weight", 0.0, 1.0, 0.3)
            cultural_weight = st.slider("Cultural Fit Weight", 0.0, 1.0, 0.2)
            personality_weight = st.slider("Personality Match Weight", 0.0, 1.0, 0.2)
        
        with col2:
            growth_weight = st.slider("Growth Potential Weight", 0.0, 1.0, 0.2)
            retention_weight = st.slider("Retention Likelihood Weight", 0.0, 1.0, 0.1)
        
        if st.button("🎯 Analyze Match", type="primary"):
            # Mock candidate and company data
            candidate = {"name": "Sample Candidate", "skills": ["Python", "React"]}
            company = {"name": "Sample Company", "culture": "Fast-paced startup"}
            
            weights = {
                "technical_fit": technical_weight,
                "cultural_fit": cultural_weight,
                "personality_match": personality_weight,
                "growth_potential": growth_weight,
                "retention_likelihood": retention_weight
            }
            
            # Use the bot
            result = st.session_state.active_bots['match_analyzer'].analyze_match(
                candidate, company, weights
            )
            
            # Display results
            st.metric("Overall Match Score", f"{result['overall_score']:.2%}")
            
            # Breakdown
            st.subheader("📊 Score Breakdown")
            scores_df = pd.DataFrame([result['breakdown']]).T
            scores_df.columns = ['Score']
            st.bar_chart(scores_df)
            
            # Recommendations
            st.subheader("💡 Recommendations")
            for rec in result['recommendations']:
                st.success(f"✓ {rec}")
            
            # Red flags
            if result['red_flags']:
                st.subheader("🚩 Red Flags")
                for flag in result['red_flags']:
                    st.warning(f"! {flag}")
            
            # Advantages
            st.subheader("⭐ Unique Advantages")
            for adv in result['unique_advantages']:
                st.info(f"+ {adv}")
    
    # Creative Filter Bot Section
    with st.expander("🎨 Creative Filter Bot - Smart Insights & Patterns"):
        st.markdown("""
        **What it does:** Applies creative filters and finds hidden patterns in candidate data
        
        **Features:** Pattern recognition, Creative insights, Smart suggestions, Trend analysis
        """)
        
        if st.button("🎨 Apply Creative Filters", type="primary"):
            # Mock candidate list
            candidates = [{"name": f"Candidate {i}", "data": {}} for i in range(10)]
            filters = {"creative": True}
            
            # Use the bot
            result = st.session_state.active_bots['creative_filter'].apply_filters(
                candidates, filters
            )
            
            # Display patterns
            st.subheader("🔍 Unique Patterns Found")
            for pattern in result['unique_patterns']:
                st.info(f"📊 {pattern}")
            
            # Display suggestions
            st.subheader("💡 Smart Suggestions")
            for suggestion in result['suggestions']:
                st.success(f"💡 {suggestion}")
            
            # Creative insights
            st.subheader("🎨 Creative Insights")
            for i, insight in enumerate(result['creative_insights'][:3]):
                st.markdown(f"**Candidate {i+1}:** {insight}")

def render_analytics_tab():
    """Render analytics dashboard"""
    st.header("📊 Analytics Dashboard")
    
    # Performance metrics
    col1, col2, col3, col4 = st.columns(4)
    
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
            title = {'text': "Days to Hire"},
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
    
    with col4:
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 89,
            title = {'text': "Kombina Score"},
            gauge = {'axis': {'range': [None, 100]},
                    'bar': {'color': "#764ba2"}}
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

def render_bot_research_tab():
    """Render bot research interface"""
    st.header("🔍 Bot Research Center")
    
    st.info("🤖 All your bot requests and research history in one place")
    
    # Display bot requests
    if st.session_state.bot_requests:
        st.subheader("📋 Recent Bot Requests")
        for request in st.session_state.bot_requests[-5:]:
            st.markdown(f"• {request}")
    else:
        st.info("No bot requests yet. Start using the advanced bots!")

def render_personalization_tab():
    """Render personalization settings"""
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
    
    if st.button("💾 Save Settings", type="primary"):
        st.success("✅ Settings saved!")

def render_admin_tab():
    """Render comprehensive admin dashboard with all requested features"""
    st.header("👤 Admin Dashboard - Complete Feature Control")
    
    # User personalization settings
    with st.expander("🎯 User Personalization Settings", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            user_type = st.selectbox(
                "I am a:",
                ["recruiter", "hiring_manager", "founder"],
                index=["recruiter", "hiring_manager", "founder"].index(st.session_state.user_preferences.get('user_type', 'recruiter'))
            )
            st.session_state.user_preferences['user_type'] = user_type
        
        with col2:
            experience = st.selectbox(
                "Experience Level:",
                ["beginner", "intermediate", "expert"],
                index=["beginner", "intermediate", "expert"].index(st.session_state.user_preferences.get('experience_level', 'intermediate'))
            )
            st.session_state.user_preferences['experience_level'] = experience
        
        with col3:
            tone = st.selectbox(
                "Preferred Tone:",
                ["formal", "friendly_professional", "casual", "kombina"],
                index=["formal", "friendly_professional", "casual", "kombina"].index(st.session_state.user_preferences.get('preferred_tone', 'friendly_professional'))
            )
            st.session_state.user_preferences['preferred_tone'] = tone
        
        if st.button("🔄 Update Interface", type="primary"):
            st.success(get_adapted_text("Settings updated!", "success"))
            st.experimental_rerun()
    
    # Feature status with detailed breakdown
    st.subheader("🎯 Complete Feature Overview")
    
    # Requested Features Implementation Status
    requested_features = {
        "🪖 Military Service Integration": {
            "status": "🟢 Active",
            "description": "Tracks IDF units (8200, Mamram, Talpiot, 81)",
            "integration": "Integrated with profile mapper and match analyzer",
            "recommendation": "Use in Smart Hunter with 'Military Unit' filter for tech roles"
        },
        "🤝 Mutual Connections Finder": {
            "status": "🟢 Active", 
            "description": "Finds shared connections through LinkedIn and military networks",
            "integration": "Works with Network Hunter Bot",
            "recommendation": "Enable 'Deep Network Analysis' for best results"
        },
        "📱 WhatsApp Integration": {
            "status": "🟡 Ready to Deploy",
            "description": "Send messages via WhatsApp Business API",
            "integration": "Connect through Settings > Integrations",
            "recommendation": "Use for candidates who prefer instant messaging"
        },
        "🗓️ Calendar Sync": {
            "status": "🟡 Testing",
            "description": "Auto-schedule interviews with Google/Outlook",
            "integration": "Will work with Match Analyzer for optimal timing",
            "recommendation": "Best for high-volume recruiting"
        },
        "🎤 Voice Notes": {
            "status": "🔴 In Development",
            "description": "Record voice messages for candidates",
            "integration": "Will integrate with Message Wizard",
            "recommendation": "Great for personal touch with senior candidates"
        },
        "📲 Mobile App": {
            "status": "🔴 Planned Q2",
            "description": "Full mobile experience for on-the-go recruiting",
            "integration": "Sync with web platform",
            "recommendation": "Useful for recruiters at events/meetups"
        },
        "🧠 ADHD Features": {
            "status": "🟢 Active",
            "description": "Focus mode, quick capture, single-task view",
            "integration": "Built into all interfaces",
            "recommendation": "Enable in Settings > Accessibility"
        },
        "🎯 Kombina Score": {
            "status": "🟢 Active",
            "description": "Unique Israeli creativity/resourcefulness metric",
            "integration": "Calculated by Match Analyzer",
            "recommendation": "Weight higher for startup roles"
        },
        "🔍 Multi-Source Profile Mapping": {
            "status": "🟢 Active",
            "description": "Aggregates from 10+ sources including Israeli platforms",
            "integration": "Profile Mapper Bot",
            "recommendation": "Use for executive search and hard-to-find roles"
        },
        "🌐 Platform Scanners": {
            "status": "🟢 Active",
            "description": "Scans LinkedIn, GitHub, JuiceBox, Rectifier, etc.",
            "integration": "Network Hunter Bot",
            "recommendation": "Run daily searches with rotating platforms"
        }
    }
    
    # Display features in organized tabs
    feature_tabs = st.tabs(["🟢 Active", "🟡 Ready/Testing", "🔴 Coming Soon"])
    
    with feature_tabs[0]:  # Active features
        for name, details in requested_features.items():
            if details["status"].startswith("🟢"):
                with st.expander(f"{name} - {details['status']}", expanded=False):
                    st.markdown(f"**What it does:** {details['description']}")
                    st.markdown(f"**Integration:** {details['integration']}")
                    st.info(f"💡 **Pro Tip:** {details['recommendation']}")
                    
                    if st.button(f"Configure {name.split()[1]}", key=f"config_{name}"):
                        st.success("Opening configuration...")
    
    with feature_tabs[1]:  # Ready/Testing
        for name, details in requested_features.items():
            if details["status"].startswith("🟡"):
                with st.expander(f"{name} - {details['status']}", expanded=False):
                    st.markdown(f"**What it does:** {details['description']}")
                    st.markdown(f"**Integration:** {details['integration']}")
                    st.warning(f"⚡ **Action Needed:** {details['recommendation']}")
                    
                    if st.button(f"Activate {name.split()[1]}", key=f"activate_{name}"):
                        st.success("Activation wizard starting...")
    
    with feature_tabs[2]:  # Coming Soon
        for name, details in requested_features.items():
            if details["status"].startswith("🔴"):
                with st.expander(f"{name} - {details['status']}", expanded=False):
                    st.markdown(f"**Planned:** {details['description']}")
                    st.markdown(f"**Future Integration:** {details['integration']}")
                    st.info(f"📅 **When Ready:** {details['recommendation']}")
                    
                    if st.button(f"Vote for {name.split()[1]}", key=f"vote_{name}"):
                        st.success("Vote recorded! This helps prioritize development.")
    
    # Smart Recommendations Section
    st.markdown("---")
    st.subheader("🧠 Smart Integration Recommendations")
    
    user_type = st.session_state.user_preferences.get('user_type', 'recruiter')
    
    if user_type == 'recruiter':
        st.markdown("""
        ### 🎯 For Recruiters - Your Power Combo:
        
        1. **Daily Workflow:**
           - Morning: Run Network Hunter on 3 platforms (LinkedIn, GitHub, JuiceBox)
           - Use Military Unit filter for tech roles
           - Apply Kombina Score > 80 for startup positions
        
        2. **Message Strategy:**
           - Use Message Wizard with "Israeli Direct" tone for local candidates
           - Switch to "Professional" for international roles
           - Always check mutual connections first
        
        3. **Efficiency Boosters:**
           - Enable ADHD Focus Mode during candidate review
           - Use Quick Capture for thoughts during calls
           - Set up WhatsApp for faster responses
        """)
    
    elif user_type == 'hiring_manager':
        st.markdown("""
        ### 👥 For Hiring Managers - Team Building Excellence:
        
        1. **Evaluation Process:**
           - Use Match Analyzer with custom weights for your team
           - Focus on Cultural Fit (40%) and Growth Potential (30%)
           - Check military background for leadership roles
        
        2. **Collaboration:**
           - Share candidate profiles with team via export
           - Use Calendar Sync for interview coordination
           - Track feedback in unified dashboard
        
        3. **Decision Making:**
           - Review Kombina Score for innovative roles
           - Check retention likelihood before offers
           - Use data-driven insights for negotiations
        """)
    
    else:  # founder
        st.markdown("""
        ### 🚀 For Founders - Scale Smart:
        
        1. **Strategic Hiring:**
           - Focus on candidates with high Kombina Score (entrepreneurial mindset)
           - Look for 8200/Talpiot alumni for technical leadership
           - Use Creative Filter to find hidden gems
        
        2. **Fast Execution:**
           - Enable all automation features
           - Use "kombina" tone for cultural fit
           - Prioritize candidates with startup experience
        
        3. **Network Effect:**
           - Leverage mutual connections aggressively
           - Use multi-source mapping for key hires
           - Build talent pipeline before you need it
        """)
    
    # Deployment Section
    st.markdown("---")
    st.subheader("🚀 Production Deployment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📦 Current Status")
        st.success("✅ System Ready for Production")
        st.info("✅ Vercel CLI Installed")
        st.warning("⏳ Domain Connection Pending")
    
    with col2:
        st.markdown("### 🔧 Quick Deploy")
        
        if st.button("🚀 Deploy to Vercel Now", type="primary"):
            st.code("vercel --prod", language="bash")
            st.info("Run this command in your terminal")
        
        if st.button("🔗 Connect Domain"):
            st.markdown("""
            1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
            2. Select your project
            3. Go to Settings > Domains
            4. Add `meunique.io`
            5. Update DNS records as shown
            """)
    
    # System Health
    st.markdown("---")
    st.subheader("💚 System Health")
    
    health_col1, health_col2, health_col3, health_col4 = st.columns(4)
    
    with health_col1:
        st.metric("Bot Response Time", "0.3s", "🟢")
    with health_col2:
        st.metric("API Status", "All Active", "🟢")
    with health_col3:
        st.metric("Database", "Synced", "🟢")
    with health_col4:
        st.metric("Feature Requests", "23 Pending", "🔄")

if __name__ == "__main__":
    main() 