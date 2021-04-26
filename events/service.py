from typing import List
from events.models import GameEvent
import logging
from events.utils.antlr import parse_events_from_file, parse_event
from utils.file import observe


class EventService:
    log_file: str = None
    events: List[GameEvent] = []

    def __init__(self, log_file):
        self.log_file = log_file

    def load(self):
        logging.info('Loading existing events from log file..')
        existing_events = parse_events_from_file(self.log_file)
        existing_events_count = len(existing_events)
        logging.info(f'Parsed {existing_events_count} existing events')

        self.events = existing_events

    def listen(self, on_new_event=None):
        logging.info('Listening to new events from log file..')
        existing_events_count = len(self.events)

        def on_new_line(line):
            event = parse_event(line)
            self.events.append(event)
            if(on_new_event):
                on_new_event(event)

        observe(self.log_file, on_new_line, existing_events_count)
