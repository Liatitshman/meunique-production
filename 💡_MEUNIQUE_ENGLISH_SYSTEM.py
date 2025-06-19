#!/usr/bin/env python3
"""
💡 MeUnique.io - AI Recruitment Revolution (English Version)
Full English interface with Israeli innovation DNA
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
from streamlit.components.v1 import iframe
import gspread
from google.oauth2.service_account import Credentials

# Page config
st.set_page_config(
    page_title="MeUnique.io - AI Recruitment Revolution",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced Bot Classes with English Interface
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
            "insights": self._generate_insights(entity_type),
            "kombina_score": random.uniform(0.7, 0.95)  # Israeli creativity metric
        }
    
    def _generate_insights(self, entity_type: str) -> List[str]:
        if entity_type == "company":
            return [
                "Growing 40% YoY in engineering team",
                "Strong preference for Unit 8200 alumni",
                "Remote-first culture with quarterly meetups in Tel Aviv",
                "Uses cutting-edge tech stack with Israeli innovations"
            ]
        else:
            return [
                "Active open-source contributor",
                "Speaks at tech conferences globally",
                "Startup experience in Israeli fintech",
                "Strong Python + ML background from Technion"
            ]

@dataclass
class NetworkHunterBot:
    """Bot that searches networks based on daily preferences"""
    name: str = "🌐 Network Hunter"
    platforms: List[str] = None
    
    def __post_init__(self):
        self.platforms = self.platforms or [
            "LinkedIn", "GitHub", "JuiceBox", "TheOrg",
            "AngelList", "Wellfound", "Gun.io", "Hired",
            "Triplebyte", "Israeli Job Boards", "Unit Networks"
        ]
    
    def daily_search(self, preferences: Dict) -> Dict:
        """Performs personalized daily search"""
        return {
            "total_found": random.randint(20, 80),
            "high_match": random.randint(5, 15),
            "platforms_searched": random.sample(self.platforms, k=preferences.get('platform_count', 5)),
            "search_time": f"{random.randint(2, 8)} minutes",
            "top_candidates": self._generate_candidates(preferences.get('count', 10)),
            "israeli_connections": random.randint(3, 10)
        }
    
    def _generate_candidates(self, count: int) -> List[Dict]:
        units = ["8200", "Mamram", "Talpiot", "81", "Shayetet", "669"]
        return [
            {
                "name": f"Candidate {i+1}",
                "match_score": random.uniform(0.7, 0.95),
                "platform": random.choice(self.platforms),
                "key_skill": random.choice(["Python", "React", "Node.js", "Go", "Kubernetes"]),
                "military_unit": random.choice(units + [None, None, None])  # 25% chance
            }
            for i in range(count)
        ]

@dataclass
class MatchAnalyzerBot:
    """Bot that analyzes matches using custom scoring models"""
    name: str = "🎯 Match Analyzer"
    
    def analyze_match(self, candidate: Dict, company: Dict, weights: Dict) -> Dict:
        """Analyzes match with custom weights including Israeli factors"""
        scores = {
            "technical_fit": random.uniform(0.7, 1.0),
            "cultural_fit": random.uniform(0.6, 0.95),
            "personality_match": random.uniform(0.65, 0.9),
            "growth_potential": random.uniform(0.7, 0.95),
            "retention_likelihood": random.uniform(0.6, 0.9),
            "israeli_network_strength": random.uniform(0.5, 1.0)
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
            "unique_advantages": self._find_advantages(candidate, company),
            "kombina_factor": self._calculate_kombina(candidate, company)
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
            "Previous successful exit in Israel",
            "Strong referral from team member"
        ][:random.randint(1, 3)]
    
    def _calculate_kombina(self, candidate: Dict, company: Dict) -> float:
        """Calculate Israeli 'kombina' score - creative problem-solving ability"""
        return random.uniform(0.6, 0.95)

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
            "suggestions": self._generate_suggestions(filtered),
            "israeli_innovation_score": random.uniform(0.8, 0.98)
        }
    
    def _passes_creative_filters(self, candidate: Dict, filters: Dict) -> bool:
        # Simulate creative filtering logic
        return random.random() > 0.3
    
    def _generate_creative_insight(self, candidate: Dict) -> str:
        insights = [
            "Has a unique combination of skills rarely seen together",
            "Shows entrepreneurial mindset perfect for scale-up phase",
            "Network includes key Israeli tech influencers",
            "Background suggests high adaptability - classic Israeli trait",
            "Side projects show 'chutzpah' and innovation"
        ]
        return random.choice(insights)
    
    def _find_patterns(self, candidates: List[Dict]) -> List[str]:
        return [
            "70% have side projects in AI/ML",
            "Most active during Tel Aviv evening hours",
            "Strong correlation between military service and leadership",
            "Preference for async communication with bursts of collaboration"
        ][:random.randint(2, 4)]
    
    def _generate_suggestions(self, candidates: List[Dict]) -> List[str]:
        return [
            "Try reaching out on Tuesday mornings (Israel time) for best response",
            "Mention specific GitHub projects in outreach",
            "Highlight remote work flexibility with Tel Aviv HQ visits",
            "Use direct, no-nonsense approach - Israelis appreciate it"
        ]

# Enhanced CSS with English UI and Israeli design elements
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&family=Space+Grotesk:wght@400;500;700&display=swap');
    
    /* Modern Design System */
    :root {
        --primary-gradient: linear-gradient(135deg, #0066cc 0%, #004494 100%);
        --israeli-blue: #0066cc;
        --success-color: #00c851;
        --warning-color: #ffbb33;
        --danger-color: #ff4444;
        --dark-bg: #1a1a2e;
        --light-bg: #ffffff;
        --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
        --shadow-md: 0 4px 8px rgba(0,0,0,0.15);
        --shadow-lg: 0 8px 16px rgba(0,0,0,0.2);
        --shadow-xl: 0 16px 32px rgba(0,0,0,0.25);
    }
    
    /* Typography System */
    * {
        font-family: 'Inter', 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    h1 { 
        font-size: 2.5rem;
        font-weight: 900;
        letter-spacing: -0.02em;
    }
    
    h2 { 
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: -0.01em;
    }
    
    h3 { 
        font-size: 1.5rem;
        font-weight: 600;
    }
    
    /* Hero Section */
    .hero-section {
        background: var(--primary-gradient);
        color: white;
        padding: 3rem;
        border-radius: 24px;
        margin: 2rem 0;
        box-shadow: var(--shadow-xl);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: "💡";
        position: absolute;
        top: -30px;
        right: -30px;
        font-size: 150px;
        opacity: 0.1;
        transform: rotate(-15deg);
    }
    
    /* Feature Cards */
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: var(--shadow-md);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(0,102,204,0.1);
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--shadow-xl);
        border-color: var(--israeli-blue);
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
        transform-origin: left;
    }
    
    .feature-card:hover::after {
        transform: scaleX(1);
    }
    
    /* Interactive Elements */
    .cta-button {
        background: var(--primary-gradient);
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
        box-shadow: var(--shadow-md);
    }
    
    .cta-button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
    }
    
    /* Bot Chat Interface */
    .bot-chat-container {
        background: #f8f9fa;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-sm);
    }
    
    .bot-message {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        box-shadow: var(--shadow-sm);
        position: relative;
    }
    
    .bot-message.user {
        background: var(--israeli-blue);
        color: white;
        margin-left: 20%;
    }
    
    .bot-message.assistant {
        background: white;
        margin-right: 20%;
        border: 1px solid #e0e0e0;
    }
    
    /* Personalization Indicators */
    .personalization-badge {
        background: var(--success-color);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        display: inline-block;
        margin: 0 4px;
    }
    
    .kombina-score {
        background: linear-gradient(135deg, #ff6b6b, #ffd93d);
        color: white;
        padding: 8px 16px;
        border-radius: 24px;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Responsive Grid */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    /* Edit Mode */
    .edit-mode {
        border: 2px dashed var(--israeli-blue);
        padding: 1rem;
        border-radius: 8px;
        background: rgba(0,102,204,0.05);
    }
    
    /* Domain Branding */
    .domain-brand {
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.5rem;
        letter-spacing: -0.03em;
    }
    
    /* Chat Widget Style */
    .embedded-chat {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 380px;
        height: 500px;
        background: white;
        border-radius: 16px;
        box-shadow: var(--shadow-xl);
        display: flex;
        flex-direction: column;
        z-index: 1000;
        transition: all 0.3s;
    }
    
    .chat-header {
        background: var(--primary-gradient);
        color: white;
        padding: 1rem;
        border-radius: 16px 16px 0 0;
        font-weight: 600;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .chat-body {
        flex: 1;
        overflow-y: auto;
        padding: 1rem;
        background: #f8f9fa;
    }
    
    .chat-input {
        padding: 1rem;
        border-top: 1px solid #e0e0e0;
        display: flex;
        gap: 8px;
    }
    
    /* Floating Action Button */
    .fab {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 60px;
        height: 60px;
        background: var(--primary-gradient);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 24px;
        cursor: pointer;
        box-shadow: var(--shadow-lg);
        transition: all 0.3s;
        z-index: 999;
    }
    
    .fab:hover {
        transform: scale(1.1);
        box-shadow: var(--shadow-xl);
    }
    
    /* Mobile Responsive */
    @media (max-width: 768px) {
        .hero-section {
            padding: 2rem;
        }
        
        h1 {
            font-size: 2rem;
        }
        
        .feature-grid {
            grid-template-columns: 1fr;
            gap: 1rem;
        }
        
        .embedded-chat {
            width: 100%;
            height: 100%;
            bottom: 0;
            right: 0;
            border-radius: 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state with English defaults
if 'user_preferences' not in st.session_state:
    st.session_state.user_preferences = {
        'language': 'en',
        'theme': 'light',
        'industry_focus': 'tech',
        'company_size': 'startup',
        'user_type': 'recruiter',
        'experience_level': 'intermediate',
        'preferred_tone': 'friendly_professional',
        'show_israeli_features': True,
        'enable_kombina_mode': True
    }

if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []

if 'embedded_chat_open' not in st.session_state:
    st.session_state.embedded_chat_open = False

if 'current_bot' not in st.session_state:
    st.session_state.current_bot = None

if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

# Tone and Personalization System
TONE_STYLES = {
    'formal': {
        'greeting': "Welcome to MeUnique. How may I assist you today?",
        'success': "Task completed successfully.",
        'error': "An error occurred. Please try again.",
        'suggestion': "I recommend the following action:",
        'bot_intro': "I am your professional recruitment assistant."
    },
    'friendly_professional': {
        'greeting': "Hi there! Ready to revolutionize your recruiting? 🚀",
        'success': "Awesome! That's done ✅",
        'error': "Oops! Let's try that again 🔄",
        'suggestion': "Here's what I'd suggest:",
        'bot_intro': "I'm your friendly recruitment partner!"
    },
    'casual': {
        'greeting': "Hey! Let's find some amazing people! 🎯",
        'success': "Boom! Nailed it 💪",
        'error': "Uh oh, something went wrong 😅",
        'suggestion': "Check this out:",
        'bot_intro': "I'm here to make recruiting fun!"
    },
    'kombina': {
        'greeting': "Let's do some recruiting magic! ✨",
        'success': "Bang! Another win 🎯",
        'error': "No worries, we'll figure it out 💡",
        'suggestion': "Here's a creative idea:",
        'bot_intro': "I'm your secret weapon for smart recruiting!"
    }
}

def get_tone_text(text_key: str, tone: str = None) -> str:
    """Get text in the appropriate tone"""
    if tone is None:
        tone = st.session_state.user_preferences.get('preferred_tone', 'friendly_professional')
    return TONE_STYLES.get(tone, TONE_STYLES['friendly_professional']).get(text_key, "")

# Embedded Chat Component
def render_embedded_chat():
    """Render the embedded chat interface"""
    if st.session_state.embedded_chat_open:
        st.markdown("""
        <div class="embedded-chat">
            <div class="chat-header">
                <span>💬 MeUnique Assistant</span>
                <span style="cursor: pointer;" onclick="closeChat()">✖️</span>
            </div>
            <div class="chat-body" id="chatBody">
                <!-- Chat messages will appear here -->
            </div>
            <div class="chat-input">
                <input type="text" placeholder="Type your message..." style="flex: 1; padding: 8px; border: 1px solid #ddd; border-radius: 8px;">
                <button class="cta-button" style="padding: 8px 16px;">Send</button>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Main Header
def render_header():
    """Render the main header with branding"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<h1 class="domain-brand" style="text-align: center;">MeUnique.io</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">AI Recruitment Revolution</p>', unsafe_allow_html=True)
    
    with col3:
        if st.button("🔧 Settings", key="settings_btn"):
            st.session_state.current_page = 'settings'

# Personal Story Section
def render_personal_story():
    """Render Liat's personal story"""
    with st.container():
        st.markdown("""
        <div class="hero-section">
            <h2>The Story Behind MeUnique</h2>
            <p style="font-size: 1.1rem; line-height: 1.8;">
                👋 Hi, I'm Liat Tishman - The Recruiter Who Couldn't Stop Digging
                <br><br>
                Just a few months ago, everything changed. I left my last startup role and realized
                I didn't want to find another job - I wanted to build something meaningful.
                <br><br>
                <strong>🧠 My ADHD Made Me Different:</strong><br>
                As a recruiter, my attention challenges made me dig deeper than others.
                While they saw CVs, I saw patterns. While they sent templates, I obsessed
                over personalizing every message. I couldn't help but notice what was missing
                in every recruitment tool demo.
                <br><br>
                <strong>💡 The Turning Point:</strong><br>
                I joined Starting Up, dove deep into the startup ecosystem, and discovered
                how broken recruitment really was. Not just for recruiters drowning in tasks,
                but for managers who lacked tools and candidates who felt like numbers.
                <br><br>
                <strong>🚀 So I Built MeUnique.io:</strong><br>
                A platform where EVERYONE can add, track, and get exactly what they want.
                Smart recommendations that adapt. AI agents that make you 100x more productive
                without losing the human touch.
                <br><br>
                <em>"If you want something done right, do it yourself."</em> - My Grandpa
                <br><br>
                Welcome to recruitment reimagined - where your quirks become superpowers.
            </p>
        </div>
        """, unsafe_allow_html=True)

# Feature Cards
def render_feature_cards():
    """Render the main feature cards"""
    st.markdown("<h2>Transform Your Recruitment Process</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🔍 Smart Profile Mapping</h3>
            <p>AI-powered profile analysis from 10+ sources. Find hidden gems with our multi-platform search.</p>
            <div class="personalization-badge">Unit 8200 Network</div>
            <div class="personalization-badge">GitHub Activity</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 Intelligent Bots</h3>
            <p>4 specialized bots working 24/7 to find, analyze, and engage top talent automatically.</p>
            <div class="personalization-badge">Auto-personalize</div>
            <div class="personalization-badge">Creative Insights</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Precision Matching</h3>
            <p>Beyond keywords - understand culture fit, growth potential, and that special 'kombina' factor.</p>
            <div class="kombina-score">🔥 Kombina Score</div>
        </div>
        """, unsafe_allow_html=True)

# Bot Interaction Panel
def render_bot_panel():
    """Render the bot interaction panel"""
    st.markdown("<h2>Your AI Recruitment Team</h2>", unsafe_allow_html=True)
    
    tabs = st.tabs(["🔍 Profile Mapper", "🌐 Network Hunter", "🎯 Match Analyzer", "🎨 Creative Filter"])
    
    with tabs[0]:
        st.markdown("### Profile Mapper Bot")
        company_name = st.text_input("Company/Candidate Name:", placeholder="e.g., Wix, Monday.com")
        if st.button("Map Profile", key="map_profile"):
            with st.spinner("Mapping profile across platforms..."):
                time.sleep(2)
                bot = st.session_state.active_bots['profile_mapper']
                result = bot.map_profile("company", {"name": company_name})
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Data Points", result['data_points'])
                    st.metric("Confidence", f"{result['confidence_score']:.0%}")
                with col2:
                    st.metric("Sources Used", len(result['sources_used']))
                    st.metric("Kombina Score", f"{result['kombina_score']:.0%}")
                
                st.success("✅ Profile mapped successfully!")
                with st.expander("View Insights"):
                    for insight in result['insights']:
                        st.write(f"• {insight}")
    
    with tabs[1]:
        st.markdown("### Network Hunter Bot")
        search_count = st.slider("Daily search limit:", 10, 100, 20)
        platforms = st.multiselect("Platforms to search:", 
                                 ["LinkedIn", "GitHub", "JuiceBox", "AngelList", "Israeli Job Boards"],
                                 default=["LinkedIn", "GitHub"])
        
        if st.button("Start Daily Hunt", key="daily_hunt"):
            with st.spinner("Hunting across networks..."):
                time.sleep(2)
                bot = st.session_state.active_bots['network_search']
                result = bot.daily_search({
                    'count': search_count,
                    'platform_count': len(platforms)
                })
                
                st.success(f"Found {result['total_found']} candidates!")
                st.info(f"🎯 {result['high_match']} high-quality matches")
                st.info(f"🇮🇱 {result['israeli_connections']} with Israeli connections")
                
                # Show sample candidates
                st.markdown("### Top Matches")
                for candidate in result['top_candidates'][:5]:
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        unit = candidate.get('military_unit')
                        unit_badge = f" • Unit {unit}" if unit else ""
                        st.write(f"**{candidate['name']}** - {candidate['key_skill']}{unit_badge}")
                    with col2:
                        st.write(f"Match: {candidate['match_score']:.0%}")
                    with col3:
                        st.write(f"via {candidate['platform']}")
    
    with tabs[2]:
        st.markdown("### Match Analyzer Bot")
        st.markdown("Adjust matching weights:")
        
        col1, col2 = st.columns(2)
        with col1:
            tech_weight = st.slider("Technical Skills", 0.0, 1.0, 0.3)
            culture_weight = st.slider("Culture Fit", 0.0, 1.0, 0.25)
            personality_weight = st.slider("Personality", 0.0, 1.0, 0.2)
        with col2:
            growth_weight = st.slider("Growth Potential", 0.0, 1.0, 0.15)
            retention_weight = st.slider("Retention Likelihood", 0.0, 1.0, 0.1)
            network_weight = st.slider("Israeli Network", 0.0, 1.0, 0.2)
        
        if st.button("Analyze Match", key="analyze"):
            bot = st.session_state.active_bots['match_analyzer']
            weights = {
                'technical_fit': tech_weight,
                'cultural_fit': culture_weight,
                'personality_match': personality_weight,
                'growth_potential': growth_weight,
                'retention_likelihood': retention_weight,
                'israeli_network_strength': network_weight
            }
            
            result = bot.analyze_match({}, {}, weights)
            
            st.markdown("### Match Analysis Results")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Overall Match", f"{result['overall_score']:.0%}")
                st.metric("Kombina Factor", f"{result['kombina_factor']:.0%}")
            
            with col2:
                st.markdown("**Score Breakdown:**")
                for key, value in result['breakdown'].items():
                    st.write(f"• {key.replace('_', ' ').title()}: {value:.0%}")
            
            if result['unique_advantages']:
                st.success("✨ Unique Advantages:")
                for advantage in result['unique_advantages']:
                    st.write(f"• {advantage}")
    
    with tabs[3]:
        st.markdown("### Creative Filter Bot")
        st.markdown("Apply creative filters to find non-obvious matches")
        
        filter_type = st.selectbox("Filter Type:", 
                                 ["Side Project Enthusiasts", "Career Switchers", 
                                  "Hidden Gems", "Israeli Innovation Leaders"])
        
        if st.button("Apply Creative Filter", key="creative"):
            bot = st.session_state.active_bots['creative_filter']
            result = bot.apply_filters([], {'type': filter_type})
            
            st.metric("Innovation Score", f"{result['israeli_innovation_score']:.0%}")
            
            st.markdown("### Creative Insights")
            for pattern in result['unique_patterns']:
                st.info(f"💡 {pattern}")
            
            st.markdown("### Recommendations")
            for suggestion in result['suggestions']:
                st.write(f"• {suggestion}")

# Edit Mode Toggle
def render_edit_mode():
    """Render edit mode controls"""
    if st.session_state.edit_mode:
        st.markdown("""
        <div class="edit-mode">
            <h3>🔧 Edit Mode Active</h3>
            <p>Click on any element to edit directly. Changes are saved automatically.</p>
        </div>
        """, unsafe_allow_html=True)

# Chat Integration
def render_chat_integration():
    """Render the chat integration component"""
    with st.container():
        css = """
        <style>
        .help-fab{position:fixed;bottom:20px;right:20px;width:60px;
                  height:60px;background:#0066cc;border-radius:50%;
                  display:flex;align-items:center;justify-content:center;
                  color:white;font-size:26px;cursor:pointer;z-index:9999;}
        </style>"""
        st.markdown(css, unsafe_allow_html=True)
        st.markdown("<div class='help-fab' onClick='window.location.hash=\"#?help=1\"'>💬</div>",
                    unsafe_allow_html=True)

# Settings Page
def render_settings():
    """Render the settings page"""
    st.markdown("## ⚙️ Settings & Personalization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### User Profile")
        user_type = st.selectbox("I am a:", 
                               ["Recruiter", "Hiring Manager", "Founder", "HR Professional"],
                               index=["recruiter", "hiring_manager", "founder", "hr_professional"].index(
                                   st.session_state.user_preferences.get('user_type', 'recruiter')))
        
        experience = st.select_slider("Experience Level:",
                                    ["Beginner", "Intermediate", "Expert"],
                                    value=st.session_state.user_preferences.get('experience_level', 'intermediate').title())
        
        st.markdown("### Communication Style")
        tone = st.radio("Preferred Tone:",
                       ["Formal", "Friendly Professional", "Casual", "Kombina Mode 🚀"],
                       index=["formal", "friendly_professional", "casual", "kombina"].index(
                           st.session_state.user_preferences.get('preferred_tone', 'friendly_professional')))
    
    with col2:
        st.markdown("### Focus Areas")
        industry = st.selectbox("Industry:", 
                              ["Tech", "Finance", "Healthcare", "E-commerce", "Other"])
        
        company_size = st.select_slider("Company Size:",
                                      ["Startup", "Scale-up", "Mid-size", "Enterprise"],
                                      value="Startup")
        
        st.markdown("### Special Features")
        show_israeli = st.checkbox("Show Israeli network features", 
                                 value=st.session_state.user_preferences.get('show_israeli_features', True))
        
        enable_kombina = st.checkbox("Enable Kombina scoring", 
                                   value=st.session_state.user_preferences.get('enable_kombina_mode', True))
    
    if st.button("Save Settings", type="primary"):
        st.session_state.user_preferences.update({
            'user_type': user_type.lower().replace(' ', '_'),
            'experience_level': experience.lower(),
            'preferred_tone': tone.lower().replace(' mode', '').replace(' professional', '_professional'),
            'industry_focus': industry.lower(),
            'company_size': company_size.lower().replace('-', ''),
            'show_israeli_features': show_israeli,
            'enable_kombina_mode': enable_kombina
        })
        st.success("✅ Settings saved successfully!")
        st.rerun()

def handle_help_chat():
    if st.query_params.get("help") == "1":
        st.sidebar.title("🆘 Help Bot")
        option = st.sidebar.selectbox(
            "Quick actions",
            ["Ask a question",
             "Change Color Palette",
             "Edit Section Text",
             "Open Admin Panel"]
        )
        if option == "Ask a question":
            user_q = st.sidebar.chat_input("Type your question")
            if user_q:
                st.sidebar.write("🤖", "This is where I answer…")
        elif option == "Change Color Palette":
            new_primary = st.sidebar.color_picker("Pick primary color", "#0066cc")
            if st.sidebar.button("Apply"):
                st.session_state['primary_color'] = new_primary
                st.experimental_rerun()
        elif option == "Edit Section Text":
            section = st.sidebar.selectbox("Section", ["Hero Title", "Hero Body"])
            new_text = st.sidebar.text_area("New content")
            if st.sidebar.button("Save"):
                st.session_state[f'section_{section}'] = new_text
                st.experimental_rerun()
        else:  # Open Admin Panel
            st.session_state.current_page = 'admin'
            st.experimental_rerun()

@st.cache_resource
def load_usage():
    creds = Credentials.from_service_account_file("gcp_service.json",
            scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])
    sheet = gspread.authorize(creds).open("Cost_Usage_Dashboard")
    return sheet.worksheet("Summary").get_all_records()

# Main App
def main():
    render_header()
    
    # Navigation
    if st.session_state.get('current_page') == 'settings':
        render_settings()
        if st.button("← Back to Home"):
            st.session_state.current_page = 'home'
            st.rerun()
    else:
        # Edit mode toggle
        col1, col2 = st.columns([10, 1])
        with col2:
            if st.button("✏️" if not st.session_state.edit_mode else "💾"):
                st.session_state.edit_mode = not st.session_state.edit_mode
                st.rerun()
        
        render_edit_mode()
        render_personal_story()
        render_feature_cards()
        
        st.markdown("---")
        
        render_bot_panel()
        
        # Chat integration
        render_embedded_chat()
        render_chat_integration()
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; padding: 2rem;">
            <p>Made with ❤️ and 🧠 in Tel Aviv</p>
            <p>© 2024 MeUnique.io - Revolutionizing Recruitment with Israeli Innovation</p>
        </div>
        """, unsafe_allow_html=True)

    # Sidebar tools
    tools = ["🏠 Home", "🤖 Chatbot", "🧐 AI Detector", "📄 Resume Parser"]
    choice = st.sidebar.radio("🛠 Tools", tools)

    if choice == "🤖 Chatbot":
        iframe("https://chatbot-ui.vercel.app/?model=gpt-4o&theme=pastel", height=600)
    elif choice == "🧐 AI Detector":
        iframe("https://aidetector.streamlit.app", height=600, scrolling=True)
    elif choice == "📄 Resume Parser":
        uploaded = st.file_uploader("Upload CV (PDF)", type="pdf")
        if uploaded:
            import pyresparser, tempfile, json
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded.read())
                data = pyresparser.ResumeParser(tmp.name).get_extracted_data()
            st.json(data)

    st.sidebar.subheader("💸 Usage & Cost")
    st.sidebar.table(load_usage())

    if "AUTH" not in st.session_state:
        pwd = st.text_input("Password", type="password")
        if st.button("Enter") and pwd == ADMIN_PWD:
            st.session_state.AUTH = True
        st.stop()

if __name__ == "__main__":
    main() 