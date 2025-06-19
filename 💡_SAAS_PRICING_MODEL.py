#!/usr/bin/env python3
"""
💡 MeUnique SaaS - Pricing & Tenant Management System
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
from typing import Dict, List, Optional

# SaaS Configuration
PRICING_TIERS = {
    "free": {
        "name": "Free Trial",
        "price": 0,
        "currency": "₪",
        "limits": {
            "searches_per_month": 50,
            "messages_per_month": 100,
            "candidates_in_db": 100,
            "ai_agents": 1,
            "api_calls_per_day": 100
        },
        "features": [
            "Basic search",
            "1 message tone",
            "Basic analytics"
        ]
    },
    "starter": {
        "name": "Starter",
        "price": 299,
        "currency": "₪",
        "per": "month",
        "limits": {
            "searches_per_month": 500,
            "messages_per_month": 1000,
            "candidates_in_db": 1000,
            "ai_agents": 3,
            "api_calls_per_day": 1000
        },
        "features": [
            "All Free features",
            "3 message tones",
            "LinkedIn integration",
            "Basic Kombina scoring",
            "Email support"
        ]
    },
    "professional": {
        "name": "Professional",
        "price": 899,
        "currency": "₪",
        "per": "month",
        "limits": {
            "searches_per_month": 2000,
            "messages_per_month": 5000,
            "candidates_in_db": 10000,
            "ai_agents": 10,
            "api_calls_per_day": 5000
        },
        "features": [
            "All Starter features",
            "All 5 message tones",
            "Advanced analytics",
            "Military network analysis",
            "API access",
            "Priority support",
            "Custom branding"
        ]
    },
    "enterprise": {
        "name": "Enterprise",
        "price": "Custom",
        "currency": "",
        "limits": {
            "searches_per_month": "Unlimited",
            "messages_per_month": "Unlimited",
            "candidates_in_db": "Unlimited",
            "ai_agents": "Unlimited",
            "api_calls_per_day": "Unlimited"
        },
        "features": [
            "All Professional features",
            "Dedicated instance",
            "Custom integrations",
            "White label option",
            "SLA guarantee",
            "Dedicated success manager",
            "Custom AI training"
        ]
    }
}

class TenantManager:
    """Manages multi-tenant functionality"""
    
    def __init__(self):
        self.tenants = {}
        self.usage_tracking = {}
    
    def create_tenant(self, company_name: str, email: str, tier: str = "free"):
        """Create new tenant account"""
        tenant_id = f"tenant_{len(self.tenants) + 1}"
        
        self.tenants[tenant_id] = {
            "id": tenant_id,
            "company_name": company_name,
            "email": email,
            "tier": tier,
            "created_at": datetime.now(),
            "settings": {
                "language": "he",
                "timezone": "Asia/Jerusalem",
                "features": {
                    "military_networks": True,
                    "kombina_scoring": True,
                    "hebrew_support": True
                }
            },
            "database": {
                "candidates": [],
                "companies": [],
                "messages": []
            },
            "usage": {
                "searches_this_month": 0,
                "messages_this_month": 0,
                "api_calls_today": 0
            }
        }
        
        return tenant_id
    
    def track_usage(self, tenant_id: str, action: str, cost: float = 0):
        """Track usage and costs per tenant"""
        if tenant_id not in self.usage_tracking:
            self.usage_tracking[tenant_id] = {
                "actions": [],
                "total_cost": 0
            }
        
        self.usage_tracking[tenant_id]["actions"].append({
            "action": action,
            "timestamp": datetime.now(),
            "cost": cost
        })
        
        self.usage_tracking[tenant_id]["total_cost"] += cost
        
        # Update usage counters
        tenant = self.tenants.get(tenant_id)
        if tenant:
            if "search" in action:
                tenant["usage"]["searches_this_month"] += 1
            elif "message" in action:
                tenant["usage"]["messages_this_month"] += 1
            tenant["usage"]["api_calls_today"] += 1
    
    def check_limits(self, tenant_id: str, action: str) -> bool:
        """Check if tenant has reached usage limits"""
        tenant = self.tenants.get(tenant_id)
        if not tenant:
            return False
        
        tier_limits = PRICING_TIERS[tenant["tier"]]["limits"]
        usage = tenant["usage"]
        
        if "search" in action:
            return usage["searches_this_month"] < tier_limits["searches_per_month"]
        elif "message" in action:
            return usage["messages_this_month"] < tier_limits["messages_per_month"]
        elif "api" in action:
            return usage["api_calls_today"] < tier_limits["api_calls_per_day"]
        
        return True

def pricing_page():
    """Display SaaS pricing page"""
    st.title("💰 MeUnique Pricing - Built for Israeli Recruiters")
    
    st.markdown("""
    <style>
    .pricing-card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        height: 100%;
        position: relative;
    }
    .pricing-card.recommended {
        border: 3px solid #667eea;
    }
    .price-tag {
        font-size: 48px;
        font-weight: bold;
        color: #667eea;
    }
    .currency {
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Pricing cards
    cols = st.columns(4)
    
    for i, (tier_key, tier_info) in enumerate(PRICING_TIERS.items()):
        with cols[i]:
            recommended = tier_key == "professional"
            
            st.markdown(f"""
            <div class="pricing-card {'recommended' if recommended else ''}">
                {f'<div style="background: #667eea; color: white; padding: 5px; margin: -30px -30px 20px -30px; border-radius: 15px 15px 0 0;">🌟 MOST POPULAR</div>' if recommended else ''}
                <h3>{tier_info['name']}</h3>
                <div class="price-tag">
                    {f"<span class='currency'>{tier_info['currency']}</span>{tier_info['price']}" if tier_info['price'] != 'Custom' else 'Custom'}
                </div>
                {f"<p>per {tier_info.get('per', '')}</p>" if tier_info.get('per') else ''}
            </div>
            """, unsafe_allow_html=True)
            
            # Features
            st.markdown("### Features:")
            for feature in tier_info["features"]:
                st.write(f"✅ {feature}")
            
            # Limits
            with st.expander("Usage Limits"):
                for limit_key, limit_value in tier_info["limits"].items():
                    st.write(f"• {limit_key.replace('_', ' ').title()}: **{limit_value}**")
            
            # CTA Button
            if tier_key == "free":
                st.button("🚀 Start Free Trial", key=f"cta_{tier_key}", type="primary")
            elif tier_key == "enterprise":
                st.button("📞 Contact Sales", key=f"cta_{tier_key}")
            else:
                st.button(f"💳 Subscribe - ₪{tier_info['price']}/mo", key=f"cta_{tier_key}")

def usage_dashboard(tenant_id: str):
    """Display usage dashboard for tenant"""
    st.header("📊 Your Usage Dashboard")
    
    # Mock usage data
    usage_data = {
        "searches_today": 45,
        "searches_limit": 2000,
        "messages_sent": 156,
        "messages_limit": 5000,
        "api_calls": 1234,
        "api_limit": 5000,
        "candidates_db": 3456,
        "candidates_limit": 10000
    }
    
    # Usage metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        usage_pct = (usage_data["searches_today"] / usage_data["searches_limit"]) * 100
        st.metric(
            "🔍 Searches", 
            f"{usage_data['searches_today']}/{usage_data['searches_limit']}",
            f"{usage_pct:.1f}% used"
        )
        st.progress(usage_pct / 100)
    
    with col2:
        usage_pct = (usage_data["messages_sent"] / usage_data["messages_limit"]) * 100
        st.metric(
            "💬 Messages", 
            f"{usage_data['messages_sent']}/{usage_data['messages_limit']}",
            f"{usage_pct:.1f}% used"
        )
        st.progress(usage_pct / 100)
    
    with col3:
        usage_pct = (usage_data["api_calls"] / usage_data["api_limit"]) * 100
        st.metric(
            "🔌 API Calls", 
            f"{usage_data['api_calls']}/{usage_data['api_limit']}",
            f"{usage_pct:.1f}% used"
        )
        st.progress(usage_pct / 100)
    
    with col4:
        usage_pct = (usage_data["candidates_db"] / usage_data["candidates_limit"]) * 100
        st.metric(
            "👥 Database", 
            f"{usage_data['candidates_db']}/{usage_data['candidates_limit']}",
            f"{usage_pct:.1f}% used"
        )
        st.progress(usage_pct / 100)
    
    # Cost breakdown
    st.subheader("💸 Cost Breakdown (This Month)")
    
    cost_data = pd.DataFrame({
        'Service': ['OpenAI API', 'Database Queries', 'Email Sending', 'SMS (Optional)'],
        'Usage': [1234, 5678, 156, 0],
        'Cost per Unit': ['₪0.15', '₪0.01', '₪0.05', '₪0.25'],
        'Total': ['₪185.10', '₪56.78', '₪7.80', '₪0']
    })
    
    st.dataframe(cost_data, use_container_width=True)
    
    total_cost = 185.10 + 56.78 + 7.80
    your_price = 899  # Professional tier
    profit_margin = ((your_price - total_cost) / your_price) * 100
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Costs", f"₪{total_cost:.2f}")
    with col2:
        st.metric("Your Price", f"₪{your_price}")
    with col3:
        st.metric("Profit Margin", f"{profit_margin:.1f}%", "Healthy")

def tenant_isolation_demo():
    """Demo tenant isolation and data separation"""
    st.header("🔒 Tenant Isolation Demo")
    
    st.info("""
    **How Multi-Tenancy Works:**
    - Each customer gets isolated data
    - Separate candidate databases
    - Individual usage tracking
    - Custom settings & branding
    """)
    
    # Show example tenants
    example_tenants = {
        "tenant_1": {
            "company": "TechRecruit IL",
            "tier": "professional",
            "candidates": 3456,
            "active_searches": 23
        },
        "tenant_2": {
            "company": "StartupHunters",
            "tier": "starter",
            "candidates": 567,
            "active_searches": 8
        },
        "tenant_3": {
            "company": "Enterprise Staffing",
            "tier": "enterprise",
            "candidates": 15678,
            "active_searches": 156
        }
    }
    
    selected_tenant = st.selectbox(
        "Select tenant to view:",
        options=list(example_tenants.keys()),
        format_func=lambda x: example_tenants[x]["company"]
    )
    
    tenant_info = example_tenants[selected_tenant]
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Company:** {tenant_info['company']}")
        st.write(f"**Tier:** {tenant_info['tier'].title()}")
    with col2:
        st.write(f"**Candidates:** {tenant_info['candidates']:,}")
        st.write(f"**Active Searches:** {tenant_info['active_searches']}")
    
    st.success(f"✅ Viewing isolated data for {tenant_info['company']}")

# Main SaaS demo
def main():
    st.set_page_config(
        page_title="MeUnique SaaS Platform",
        page_icon="💰",
        layout="wide"
    )
    
    st.title("💡 MeUnique - SaaS Platform Overview")
    
    tabs = st.tabs([
        "💰 Pricing",
        "📊 Usage Dashboard",
        "🔒 Multi-Tenancy",
        "💸 Revenue Model"
    ])
    
    with tabs[0]:
        pricing_page()
    
    with tabs[1]:
        usage_dashboard("tenant_1")
    
    with tabs[2]:
        tenant_isolation_demo()
    
    with tabs[3]:
        st.header("💸 Revenue Projections")
        
        # Revenue calculator
        st.subheader("Revenue Calculator")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            free_users = st.number_input("Free Trial Users", value=100)
            starter_users = st.number_input("Starter Users", value=50)
        
        with col2:
            pro_users = st.number_input("Professional Users", value=20)
            enterprise_users = st.number_input("Enterprise Users", value=5)
        
        with col3:
            enterprise_avg_price = st.number_input("Avg Enterprise Price (₪)", value=5000)
        
        # Calculate revenue
        monthly_revenue = (
            starter_users * 299 +
            pro_users * 899 +
            enterprise_users * enterprise_avg_price
        )
        
        yearly_revenue = monthly_revenue * 12
        
        # Display projections
        st.markdown("---")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Monthly Revenue", f"₪{monthly_revenue:,.0f}")
        with col2:
            st.metric("Yearly Revenue", f"₪{yearly_revenue:,.0f}")
        with col3:
            total_users = free_users + starter_users + pro_users + enterprise_users
            st.metric("Total Users", total_users)
        with col4:
            paying_users = starter_users + pro_users + enterprise_users
            conversion_rate = (paying_users / total_users) * 100 if total_users > 0 else 0
            st.metric("Conversion Rate", f"{conversion_rate:.1f}%")
        
        # Growth projection
        st.subheader("📈 Growth Projection")
        
        months = list(range(1, 13))
        growth_rate = 1.15  # 15% monthly growth
        
        revenues = [monthly_revenue * (growth_rate ** i) for i in range(12)]
        
        df = pd.DataFrame({
            'Month': months,
            'Revenue (₪)': revenues
        })
        
        st.line_chart(df.set_index('Month'))

if __name__ == "__main__":
    main() 