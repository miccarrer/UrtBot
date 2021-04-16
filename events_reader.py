from antlr4 import *
from events_parser.EventsLexer import EventsLexer
from events_parser.EventsParser import EventsParser


def read_one(str):
  parser = create_parser(InputStream(str))
  return parser.event().value

def read_one_from_file(filepath):
  parser = create_parser(FileStream(filepath))
  return parser.event().value

def read_all(str):
  parser = create_parser(InputStream(str))
  return parser.events().value

def read_all_from_file(filepath):
  parser = create_parser(FileStream(filepath))
  return parser.events().value

def create_parser(stream):
  lexer = EventsLexer(stream)
  token_stream = CommonTokenStream(lexer)
  return EventsParser(token_stream)