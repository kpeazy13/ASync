import icalendar
from pathlib import Path

ics_path = Path("C:\\Users\\patel\\Downloads\\ASync (py)\\ASync\\user_z9rQL7Ko05ms2NrNU42RWzQyZ0w8fkX4SD6CbNBV.ics")
calendar = icalendar.Calendar.from_ical(ics_path)
for event in calendar.events:
    print(event.get("SUMMARY"))
    print(event.get("DTSTART").dt)
    print(event.get("UID"))
