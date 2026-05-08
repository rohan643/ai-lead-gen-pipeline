"""Lead generation pipeline orchestrator."""
import argparse, schedule, time, logging
from processors.qualifier import score_leads
from processors.email_finder import find_emails
from processors.icebreaker import generate_icebreakers
from integrations import airtable, instantly

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


def run_pipeline():
    log.info("Pipeline started")

    # 1. Fetch new prospects from Apollo
    from integrations.apollo import fetch_prospects
    prospects = fetch_prospects()
    log.info(f"Scraped {len(prospects)} prospects")

    # 2. Score against ICP
    scored = score_leads(prospects)
    qualified = [p for p in scored if p["icp_score"] >= 65]
    log.info(f"Qualified: {len(qualified)} (≥65 score)")

    # 3. Deduplicate
    from integrations.airtable import is_duplicate
    fresh = [p for p in qualified if not is_duplicate(p)]
    log.info(f"After dedup: {len(fresh)}")

    # 4. Find emails
    with_emails = find_emails(fresh)
    log.info(f"Emails found: {len(with_emails)}")

    # 5. Generate icebreakers
    final = generate_icebreakers(with_emails)

    # 6. Push to Instantly + archive in Airtable
    instantly.push_leads(final)
    airtable.archive_leads(final)
    log.info(f"Pipeline complete — {len(final)} leads pushed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--schedule", action="store_true", help="Run on schedule")
    args = parser.parse_args()

    if args.schedule:
        schedule.every().day.at("06:00").do(run_pipeline)
        log.info("Scheduler running — next run at 06:00")
        while True:
            schedule.run_pending()
            time.sleep(60)
    else:
        run_pipeline()
