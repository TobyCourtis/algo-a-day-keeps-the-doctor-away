import csv
import os
from ics import Calendar, Event
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'tides.csv')

calendar = Calendar()


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y%m%dT%H%M%SZ")


with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        event = Event()
        event.name = f"High Tide ({row['name']})"
        event.begin = parse_date(row['date_time'])
        calendar.events.add(event)

ics_path = os.path.join(script_dir, 'events.ics')
with open(ics_path, 'w') as file:
    file.writelines(calendar)
