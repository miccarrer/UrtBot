from typing import Any
from antlr4 import CommonTokenStream
from antlr4.Lexer import Lexer
from antlr4.error.ErrorListener import ErrorListener
from yaml.parser import Parser


def create_parser(lexerType: type, parserType: type, stream, on_syntax_error: Any = None):
    lexer: Lexer = lexerType(stream)
    lexer.removeErrorListeners()

    token_stream = CommonTokenStream(lexer)
    
    parser: Parser = parserType(token_stream)
    if(on_syntax_error):
        parser.addErrorListener(SyntaxErrorListener(on_syntax_error))

    return parser


class SyntaxErrorListener(ErrorListener):
    on_syntax_error: Any

    def __init__(self, on_syntax_error):
        super(SyntaxErrorListener, self).__init__()
        self.on_syntax_error = on_syntax_error

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.on_syntax_error(recognizer, offendingSymbol, line, column, msg, e)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass