from typing import Any
from utils.parser import create_parser
from antlr4 import *
from plugins.commands.parser.CommandsLexer import CommandsLexer
from plugins.commands.parser.CommandsParser import CommandsParser


def parse_command(str, on_syntax_error: Any = None):
  parser = create_parser(CommandsLexer, CommandsParser, InputStream(str), on_syntax_error)
  return parser.command().value