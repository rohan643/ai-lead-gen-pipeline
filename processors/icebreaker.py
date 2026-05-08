"""Generate hyper-personalized opening lines using GPT-4o."""
import os, json
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = """You write hyper-personalized cold email opening lines.
Rules:
- 1-2 sentences max
- Reference something SPECIFIC and REAL about the prospect (post, company news, hiring, etc.)
- Sound like a human, not a marketer
- No compliments. No "I noticed". Get straight to the observation.
- Connect the observation to a pain point naturally"""


def generate_icebreakers(leads: list[dict]) -> list[dict]:
    for lead in leads:
        try:
            lead["icebreaker"] = _generate_one(lead)
        except Exception as e:
            lead["icebreaker"] = ""
    return leads


def _generate_one(lead: dict) -> str:
    context = {
        "name": lead.get("first_name"),
        "company": lead.get("company"),
        "title": lead.get("title"),
        "recent_posts": lead.get("recent_linkedin_posts", [])[:2],
        "company_news": lead.get("company_news", ""),
        "job_postings": lead.get("open_roles", [])[:3],
        "tech_stack": lead.get("tech_stack", [])
    }
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Write an icebreaker for: {json.dumps(context)}"}
        ],
        temperature=0.9,
        max_tokens=100
    )
    return resp.choices[0].message.content.strip()
