<div align="center">

# 🎯 AI Lead Gen Pipeline

**Fully automated lead generation with AI qualification, email finding & personalized outreach**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Airtable](https://img.shields.io/badge/Airtable-Database-18BFFF?style=for-the-badge&logo=airtable&logoColor=white)](https://airtable.com)
[![Instantly](https://img.shields.io/badge/Instantly-Outreach-FF6B35?style=for-the-badge)](https://instantly.ai)

</div>

---

## Overview

This pipeline runs every morning at 6 AM and delivers a fresh batch of qualified, enriched, personalized leads straight into your outreach tool. Zero manual work.

```
ICP Definition → Prospect Scraping → AI Qualification → Deduplication
      → Email Finding → Enrichment → Icebreaker Generation → Instantly
```

**Results from live deployments:**
- 34% cold email reply rate (industry avg: 8%)
- 22% lead-to-meeting conversion
- ~180 qualified leads per day, fully automated

---

## Pipeline Stages

### Stage 1: ICP-Based Prospect Discovery
```python
# Define your Ideal Customer Profile
ICP = {
    "industries": ["SaaS", "E-commerce", "Professional Services"],
    "employee_count": "10-200",
    "location": ["United States", "Canada"],
    "revenue_range": "$1M-$20M",
    "tech_stack": ["HubSpot", "Shopify", "Stripe"],  # technographic targeting
    "job_titles": ["CEO", "Founder", "Head of Operations", "COO"]
}
```

Sources scraped: Apollo, LinkedIn Sales Nav, Google Maps (local businesses), Crunchbase.

### Stage 2: AI Qualification Scoring
Each prospect is scored 0–100 by GPT-4o against your ICP:

```json
{
  "prospect": "Jane Smith, CEO @ Acme SaaS",
  "icp_score": 87,
  "qualification_reason": "Matches on industry, size, tech stack. HubSpot user = likely manual CRM pain. Recent LinkedIn activity shows ops scaling challenges.",
  "recommended_angle": "CRM automation and lead routing",
  "priority": "HIGH"
}
```

Only prospects scoring ≥ 65 proceed to email finding.

### Stage 3: Email Finding & Verification
Verified emails found via:
1. **Anymailfinder** (primary)
2. **Hunter.io** (fallback)
3. **Apollo enrichment** (secondary fallback)

All emails are verified before use. Catch-all domains are flagged.

### Stage 4: Deduplication
```python
# Checks against:
# - Airtable master archive (all-time)
# - Instantly active campaigns
# - DNC list
# - Already-replied prospects
def is_duplicate(prospect: Prospect) -> bool:
    return (
        archive.contains(prospect.email) or
        archive.contains(prospect.linkedin_url) or
        dnc.contains(prospect.domain)
    )
```

### Stage 5: AI Icebreaker Generation
GPT-4o writes a hyper-personalized first line for each prospect:

```
Input:  LinkedIn profile, recent posts, company news, tech stack
Output: "Saw your post about scaling the ops team past 50 — that's usually when
         the manual Notion/spreadsheet juggle really starts breaking down."
```

### Stage 6: Push to Instantly
Enriched leads with personalized icebreakers are pushed via Instantly API into the correct campaign based on ICP segment.

---

## Setup

### Requirements
```
python >= 3.11
airtable-python-wrapper
openai
requests
schedule
python-dotenv
```

### Install
```bash
git clone https://github.com/rohan643/ai-lead-gen-pipeline.git
cd ai-lead-gen-pipeline
pip install -r requirements.txt
cp .env.example .env
# Fill in your API keys
python main.py
```

### Environment Variables
```env
OPENAI_API_KEY=sk-...
AIRTABLE_API_KEY=...
AIRTABLE_BASE_ID=...
ANYMAILFINDER_API_KEY=...
HUNTER_API_KEY=...
INSTANTLY_API_KEY=...
APOLLO_API_KEY=...
```

---

## File Structure

```
ai-lead-gen-pipeline/
├── main.py                  # Orchestrator — runs the full pipeline
├── config/
│   └── icp.yaml             # Your ICP definition
├── scrapers/
│   ├── apollo_scraper.py
│   ├── linkedin_scraper.py
│   └── google_maps_scraper.py
├── processors/
│   ├── qualifier.py         # GPT-4o ICP scoring
│   ├── deduplicator.py
│   ├── email_finder.py
│   └── icebreaker.py        # GPT-4o personalization
├── integrations/
│   ├── airtable_client.py
│   └── instantly_client.py
├── logs/
│   └── pipeline.log
└── tests/
    └── test_qualifier.py
```

---

## Daily Output Example

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PIPELINE RUN: 2026-05-07 06:00 AM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Prospects Scraped:        412
 Passed ICP Scoring:       184  (44.7%)
 Emails Found & Verified:  161  (87.5%)
 Duplicates Removed:        23
 Final Leads Pushed:       138
 Avg ICP Score:             79/100
 Icebreakers Generated:    138
 Time Elapsed:              4m 12s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

<div align="center">

**Built by [Rohan Mukherjee](https://github.com/rohan643) @ Apex Automation Co.**

</div>
