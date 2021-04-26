from typing import Any
from utils.parser import create_parser
from antlr4 import *
from events.parser.EventsLexer import EventsLexer
from events.parser.EventsParser import EventsParser


def parse_event(str: str, on_syntax_error: Any = None):
    parser = create_parser(EventsLexer, EventsParser, InputStream(str), on_syntax_error)
    return parser.event().value


def parse_events(str: str, on_syntax_error: Any = None):
    parser = create_parser(EventsLexer, EventsParser, InputStream(str), on_syntax_error)
    return parser.events().value


def parse_events_from_file(filepath: str, on_syntax_error: Any = None):
    parser = create_parser(EventsLexer, EventsParser, FileStream(filepath), on_syntax_error)
    return parser.events().value
