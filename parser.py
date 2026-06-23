import icalendar
from pathlib import Path

def parse_ics_file(ics_file_path):    
    calendar = icalendar.Calendar.from_ical(ics_file_path)
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

print(parse_ics_file(Path("C:\\Users\\patel\\Downloads\\ASync (py)\\ASync\\user_z9rQL7Ko05ms2NrNU42RWzQyZ0w8fkX4SD6CbNBV.ics")))
