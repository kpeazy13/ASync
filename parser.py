import icalendar
from pathlib import Path

def parse_ics_file(ics_text):
    calendar = icalendar.Calendar.from_ical(ics_text)
    assignment_list = []
    for event in calendar.events:
        assignment = {}
        uid = str(event.get('UID'))
        if "assignment" in uid.lower():
            assignment['uid'] = uid
            assignment['summary'] = str(event.get('SUMMARY'))
            assignment['description'] = str(event.get('DESCRIPTION'))
            assignment['due'] = event.get('DTSTART').dt
            assignment_list.append(assignment)
    return assignment_list

