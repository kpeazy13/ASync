import os
from dotenv import load_dotenv
from fetch import fetch_ics
from parser import parse_ics_file

load_dotenv()

feed_url = os.getenv("CANVAS_FEED_URL")
if not feed_url:
    raise ValueError("CANVAS_FEED_URL not set — check your .env file")

ics_text = fetch_ics(feed_url)
assignments = parse_ics_file(ics_text)
print(assignments)


