"""Generate 15 icebreakers using the OpenAI-powered icebreaker processor."""
import json
from processors.icebreaker import generate_icebreakers

SAMPLE_LEADS = [
    {
        "first_name": "Sarah",
        "company": "Bolt Logistics",
        "title": "CEO",
        "recent_linkedin_posts": ["Just opened our 3rd warehouse — ops team is stretched thin but we're making it work"],
        "company_news": "Raised $4M seed round last month",
        "open_roles": ["Operations Manager", "Dispatch Coordinator"],
        "tech_stack": ["Shopify", "Stripe"],
    },
    {
        "first_name": "Marcus",
        "company": "NestCraft Interiors",
        "title": "Founder",
        "recent_linkedin_posts": ["Hiring is the hardest part of scaling a design studio — 12 open reqs and counting"],
        "company_news": "",
        "open_roles": ["Interior Designer", "Project Manager", "Client Success"],
        "tech_stack": ["HubSpot"],
    },
    {
        "first_name": "Priya",
        "company": "CleanSlate HVAC",
        "title": "Owner",
        "recent_linkedin_posts": ["Summer rush is here — team is doing 40+ jobs a week. Scheduling is a nightmare."],
        "company_news": "Acquired a competitor in Phoenix",
        "open_roles": ["HVAC Technician", "Field Supervisor"],
        "tech_stack": ["Stripe"],
    },
    {
        "first_name": "Jordan",
        "company": "PeakFlow SaaS",
        "title": "COO",
        "recent_linkedin_posts": ["We went from 10 to 60 employees in 18 months — processes haven't kept up"],
        "company_news": "Launched enterprise tier",
        "open_roles": ["RevOps Manager", "Customer Success Lead"],
        "tech_stack": ["HubSpot", "Stripe"],
    },
    {
        "first_name": "Elena",
        "company": "Verdant Foods",
        "title": "VP Operations",
        "recent_linkedin_posts": ["Supply chain chaos is real — manual spreadsheets are killing us"],
        "company_news": "Expanded to 200 retail locations",
        "open_roles": ["Supply Chain Analyst", "Ops Coordinator"],
        "tech_stack": ["Shopify"],
    },
    {
        "first_name": "Tom",
        "company": "Ironclad Roofing",
        "title": "Owner",
        "recent_linkedin_posts": ["Running 8 crews now — communication between field and office is broken"],
        "company_news": "",
        "open_roles": ["Project Manager", "Estimator"],
        "tech_stack": [],
    },
    {
        "first_name": "Aisha",
        "company": "Luminary Digital",
        "title": "Founder",
        "recent_linkedin_posts": ["Agency life: trying to systematize delivery but every client is a snowflake"],
        "company_news": "Named top 50 fastest-growing agencies",
        "open_roles": ["Account Manager", "SEO Specialist"],
        "tech_stack": ["HubSpot"],
    },
    {
        "first_name": "Derek",
        "company": "SwiftMed Staffing",
        "title": "CEO",
        "recent_linkedin_posts": ["Healthcare staffing demand is up 30% — we're placing nurses faster than we can onboard them"],
        "company_news": "Partnered with 3 new hospital networks",
        "open_roles": ["Recruiter", "Compliance Officer"],
        "tech_stack": ["Stripe"],
    },
    {
        "first_name": "Camille",
        "company": "GreenLeaf Landscaping",
        "title": "Head of Operations",
        "recent_linkedin_posts": ["70 employees across 5 crews — tracking hours manually is embarrassing at this scale"],
        "company_news": "",
        "open_roles": ["Crew Lead", "Estimator"],
        "tech_stack": [],
    },
    {
        "first_name": "Noah",
        "company": "Stackline Commerce",
        "title": "Founder",
        "recent_linkedin_posts": ["We 3x'd GMV this year and our ops stack is basically duct tape and prayer"],
        "company_news": "Hit $10M ARR",
        "open_roles": ["Head of Ops", "Fulfillment Manager"],
        "tech_stack": ["Shopify", "Stripe"],
    },
    {
        "first_name": "Rachel",
        "company": "BrightPath Tutoring",
        "title": "CEO",
        "recent_linkedin_posts": ["Onboarding 50 new tutors this quarter — the manual checklist process doesn't scale"],
        "company_news": "Expanding to 5 new cities",
        "open_roles": ["Operations Coordinator", "Tutor Onboarding Specialist"],
        "tech_stack": ["HubSpot"],
    },
    {
        "first_name": "James",
        "company": "Apex Electrical",
        "title": "Owner",
        "recent_linkedin_posts": ["Missed a job because a tech didn't get the schedule update — costly lesson"],
        "company_news": "",
        "open_roles": ["Electrician", "Office Manager"],
        "tech_stack": [],
    },
    {
        "first_name": "Sofia",
        "company": "Meridian Consulting",
        "title": "COO",
        "recent_linkedin_posts": ["Client delivery is inconsistent — too much depends on individual consultants knowing the 'way we do things'"],
        "company_news": "Promoted 4 to partner",
        "open_roles": ["Senior Consultant", "Ops Analyst"],
        "tech_stack": ["HubSpot"],
    },
    {
        "first_name": "Liam",
        "company": "CrateBox Ecommerce",
        "title": "Founder",
        "recent_linkedin_posts": ["Black Friday nearly broke us — fulfillment SLAs slipped and we lost 200 customers"],
        "company_news": "Raised a $2M pre-seed",
        "open_roles": ["Fulfillment Lead", "Customer Support"],
        "tech_stack": ["Shopify", "Stripe"],
    },
    {
        "first_name": "Diana",
        "company": "ClearPath Insurance",
        "title": "VP Operations",
        "recent_linkedin_posts": ["Underwriting bottlenecks are stacking up — too many manual touchpoints in the workflow"],
        "company_news": "Launched small business product line",
        "open_roles": ["Underwriter", "Ops Specialist"],
        "tech_stack": ["Stripe"],
    },
]


def main():
    print(f"Generating icebreakers for {len(SAMPLE_LEADS)} leads...\n")
    results = generate_icebreakers(SAMPLE_LEADS)
    for i, lead in enumerate(results, 1):
        name = lead["first_name"]
        company = lead["company"]
        icebreaker = lead.get("icebreaker") or "(failed)"
        print(f"{i:>2}. [{name} @ {company}]")
        print(f"    {icebreaker}\n")


if __name__ == "__main__":
    main()
