import icalendar
from pathlib import Path

ics_path = Path("C:\\Users\\patel\\Downloads\\ASync (py)\\ASync\\user_z9rQL7Ko05ms2NrNU42RWzQyZ0w8fkX4SD6CbNBV.ics")
calendar = icalendar.Calendar.from_ical(ics_path)
for event in calendar.events:
    uid = str(event.get('UID'))
    if "assignment" in uid.lower():
        print(f"Event UID: {uid}")
        print(f"Summary: {event.get('SUMMARY')}")
        print(f"Start Time: {event.get('DTSTART').dt}")
        print(f"Description: {event.get('DESCRIPTION')}")
        print("-" * 40)