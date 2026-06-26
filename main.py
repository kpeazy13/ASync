import os
from dotenv import load_dotenv
from fetch import fetch_ics
from parser import parse_ics_file
from notion_client import Client



load_dotenv()
notion = Client(auth=os.getenv("NOTION_SECRET_KEY"))
db_id = os.getenv("NOTION_DATABASE_ID")
db = notion.databases.retrieve(database_id=db_id)
response = notion.pages.create(
    parent={"database_id": db_id},
    properties={
        "Name": {
        "title": [{"text": {"content": "History Essay" } }]
        },
        "URL": {
            "url": "https://wikipedia.org"
        }
    }
)

feed_url = os.getenv("CANVAS_FEED_URL")
if not feed_url:
    raise ValueError("CANVAS_FEED_URL not set — check your .env file")

ics_text = fetch_ics(feed_url)
assignments = parse_ics_file(ics_text)
print(assignments)


#idea: for assignments that the user has completed, after a certain amount of time, delete them from the database. This will keep the database clean and prevent it from getting too large.
