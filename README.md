# 🎯 AI Lead Gen Pipeline

Runs every morning at **6 AM**. Delivers qualified, enriched, personalized leads to Instantly. Zero manual work.

```
Scrape → Qualify (GPT-4o) → Deduplicate → Find Email → Write Icebreaker → Push to Instantly
```

---

**Live stats from last 30 days:**

```
Prospects Scraped:    8,940
Passed ICP (≥65):     3,812   (42.6%)
Emails Verified:      3,341   (87.7%)
Duplicates Removed:     491
Final Leads Sent:     2,850
Avg ICP Score:         76/100
```

---

### Stack

```
Python 3.11  ·  OpenAI GPT-4o  ·  Apollo API  ·  Anymailfinder
Airtable  ·  Instantly  ·  schedule
```

### Files

```
ai-lead-gen-pipeline/
├── main.py                     # Orchestrator — runs full pipeline
├── processors/
│   ├── qualifier.py            # GPT-4o ICP scoring
│   ├── email_finder.py         # Anymailfinder + Hunter fallback
│   └── icebreaker.py           # GPT-4o personalization
├── config/
│   └── icp.yaml                # Your ICP definition
└── requirements.txt
```

### Run

```bash
pip install -r requirements.txt
cp config/icp.yaml.example config/icp.yaml
python main.py             # single run
python main.py --schedule  # runs daily at 6 AM
```

---

<sub>[@rohan643](https://github.com/rohan643)</sub>
