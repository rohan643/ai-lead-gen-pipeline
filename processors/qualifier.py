"""GPT-4o ICP scoring for prospects."""
import os, json, yaml
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

with open(Path("config/icp.yaml")) as f:
    ICP = yaml.safe_load(f)


def score_leads(prospects: list[dict]) -> list[dict]:
    scored = []
    for p in prospects:
        try:
            result = _score_one(p)
            p.update(result)
        except Exception as e:
            p["icp_score"] = 0
            p["icp_reason"] = f"Scoring failed: {e}"
        scored.append(p)
    return scored


def _score_one(prospect: dict) -> dict:
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "system",
            "content": f"You are an ICP scoring engine. Score prospects against this ICP: {json.dumps(ICP)}"
        }, {
            "role": "user",
            "content": f"Score this prospect 0-100. Return JSON with: score, reason, angle, priority (HIGH/MED/LOW). Prospect: {json.dumps(prospect)}"
        }],
        response_format={"type": "json_object"},
        temperature=0.1
    )
    return json.loads(resp.choices[0].message.content)
