# Generated from plugins/commands/parser/Commands.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

from plugins.commands.models import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("\67\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\5\2\31\n\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3 \n\3\3\4\3\4\3\4\3\4\3\4\5\4\'\n")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\5\b\60\n\b\3\b\3\b\5\b")
        buf.write("\64\n\b\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\3\2\3\4\2\13\13\"\"\2;\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\3\30\3\2\2\2\5\37\3\2\2\2\7&\3\2\2\2")
        buf.write("\t(\3\2\2\2\13*\3\2\2\2\r,\3\2\2\2\17\63\3\2\2\2\21\65")
        buf.write("\3\2\2\2\23\24\7t\2\2\24\25\7e\2\2\25\26\7q\2\2\26\31")
        buf.write("\7p\2\2\27\31\7t\2\2\30\23\3\2\2\2\30\27\3\2\2\2\31\4")
        buf.write("\3\2\2\2\32\33\7j\2\2\33\34\7g\2\2\34\35\7n\2\2\35 \7")
        buf.write("r\2\2\36 \7j\2\2\37\32\3\2\2\2\37\36\3\2\2\2 \6\3\2\2")
        buf.write("\2!\"\7m\2\2\"#\7k\2\2#$\7n\2\2$\'\7n\2\2%\'\7m\2\2&!")
        buf.write("\3\2\2\2&%\3\2\2\2\'\b\3\2\2\2()\4\62;\2)\n\3\2\2\2*+")
        buf.write("\7$\2\2+\f\3\2\2\2,-\t\2\2\2-\16\3\2\2\2.\60\7\17\2\2")
        buf.write("/.\3\2\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\64\7\f\2\2\62")
        buf.write("\64\7\17\2\2\63/\3\2\2\2\63\62\3\2\2\2\64\20\3\2\2\2\65")
        buf.write("\66\13\2\2\2\66\22\3\2\2\2\b\2\30\37&/\63\2")
        return buf.getvalue()


class CommandsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RCON = 1
    HELP = 2
    KILL = 3
    DIGIT = 4
    DOUBLE_QUOTE = 5
    WHITESPACE = 6
    NEWLINE = 7
    ANY_CHAR = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "RCON", "HELP", "KILL", "DIGIT", "DOUBLE_QUOTE", "WHITESPACE", 
            "NEWLINE", "ANY_CHAR" ]

    ruleNames = [ "RCON", "HELP", "KILL", "DIGIT", "DOUBLE_QUOTE", "WHITESPACE", 
                  "NEWLINE", "ANY_CHAR" ]

    grammarFileName = "Commands.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


