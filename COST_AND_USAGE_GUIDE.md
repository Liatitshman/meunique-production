# MeUnique – Cost & Usage Guide  
*Version 2025-06*

This document explains **every recurring or one-off cost** in your stack, shows where to monitor usage, and lists simple no-code actions to prevent surprise bills.

---
## 1. Hosting / Deployment
| Item | Plan | Cost | Notes |
|------|------|------|-------|
| Streamlit Cloud | Community (Free) | **$0 / month** | Up to 3 apps, 1 GB RAM, 1 vCPU, sleep after 15 min idle |
| Custom Domain via Streamlit | Included | $0 | SSL certificate auto-renewed |
| Optional: Streamlit Pro | $25 / month | Wakes on traffic, 5 GB, email support |

### How to check usage
1. Streamlit Dashboard → *Usage* tab (CPU hours & visitors).  
2. Email alerts every time a build fails or exceeds limits.

---
## 2. Domain & DNS
| Domain | Registrar | Renewal | One-off |
|--------|-----------|---------|---------|
| **MeUniqueSourcer.ai** | Namecheap | ~$69 / year | First year already paid |
| **meuniqueai.io** (optional redirect) | Box | ~$30 / year | Redirect to `.ai` domain |

> Budget tip – keep only one domain live; use the other as 301 redirect to avoid duplicate SEO cost.

---
## 3. Email / SMTP
| Solution | Cost | Purpose |
|-----------|------|---------|
| Gmail Workspace Starter | $6 / user / month | `liat@meunique.ai` transactional & team email |
| **Free alternative** – Gmail alias | $0 | Forward to personal inbox, no branding |

### SMTP Setup
1. Workspace Admin → Security → *App passwords* → create  
2. Streamlit Secrets → add:
```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=465
SMTP_USER=liat@meunique.ai
SMTP_PASS=********
```

---
## 4. OpenAI API
| Model | Price per 1K tokens | Est. tokens / candidate | Est. cost / 100 candidates |
|-------|--------------------|-------------------------|-----------------------------|
| gpt-3.5-turbo | **$0.0015** | ~1 K | $0.15 |
| gpt-4o (optional) | $0.005 | ~1 K | $0.50 |

### Monthly Scenarios
| Users / month | Avg. candidates / user | Model | Monthly cost |
|---------------|-----------------------|-------|--------------|
| 10 (beta) | 20 | gpt-3.5 | **<$5** |
| 100 (launch) | 50 | 3.5 & occasional 4 | $40–60 |

### Hard budget
OpenAI dashboard → *Usage → Usage limits* → set **$70** hard limit and email alert at **$50**.

---
## 5. Third-party APIs
| API | Mandatory? | Free tier | Upgrade |
|-----|------------|----------|---------|
| LinkedIn Partner API | **Yes** (no scraping) |  8 | Pay-as-you-go (contact sales) |
| GitHub GraphQL | Optional | 5K req / hr | Free |
| AngelList API | Optional | Free |  |  

> Until Partner status is approved, disable LinkedIn calls in Settings → *show_israeli_features = False* to avoid errors.

---
## 6. DevOps / Security
| Tool | Cost | Why |
|------|------|-----|
| GitHub (private repo) | **$0** (no CI minutes) | Version control |
| Snyk Free | 200 scans / month | Open-source license & vuln scan |
| OWASP ZAP (manual) | Free | Quick DAST scan before releases |

---
## 7. One-page Budget Dashboard (Google Sheet)
A ready-made sheet sits in Google Drive → *MeUnique/Finance/BudgetDashboard.xlsx*.

Columns:
1. **Category** (OpenAI, SMTP, Domain…)  
2. **Plan**  
3. **Qty / month**  
4. **Unit cost**  
5. **Monthly total** (auto)  
6. **Owner** (e.g. Liat, DevOps)  
7. **Billing URL** – link to provider portal

The `TOTAL` row changes colour to **orange** when > ₪250.

---
## 8. No-Code How-To (Step by Step)
### Update code & deploy
1. GitHub → open file → ✏️ Edit → Make change.  
2. Scroll → "Commit directly to *main*".  
3. Wait ~1 min → Streamlit shows green "✓ Healthy".  
4. Refresh `www.MeUniqueSourcer.ai`.

### Pause the app
Settings → Manage app → **Stop** (freezes compute, keeps site).  
Restart: **▶ Run**.

### Roll back version
History → choose previous hash → **Roll back** → Confirm.

### Add a secret key
Settings → Secrets → + New Secret → Name & value → **Save**.  
App rebuilds automatically.

---
## 9. Typical Monthly Budget (production launch)
| Item | Cost |
|------|------|
| Streamlit Pro | $25 |
| Domain renewal | $5 │ (prorated) |
| OpenAI tokens | $40 |
| SMTP (1 user) | $6 |
| LinkedIn API | $19 |
| Misc (API / Tool buffer) | $10 |
| **Total** | **≈ $105 / month** |

*Beta stage (Free hosting + low usage) ≈ $20 / month.*

---
## 10. Questions & Next Steps
• Need a different model mix? ping me in GitHub Issues.  
• Want automated alerts in Slack/Email? open Issue #cost-alerts.  
• Ask ChatGPT in the repo discussions with tag **#cost-help**.

**Enjoy building without bill-shock!** 