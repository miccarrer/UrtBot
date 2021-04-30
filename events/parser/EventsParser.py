# Generated from events/parser/Events.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

from events.models import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%")
        buf.write("\u0212\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\5\2H\n\2\3")
        buf.write("\2\3\2\7\2L\n\2\f\2\16\2O\13\2\3\3\7\3R\n\3\f\3\16\3U")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00a1\n\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\6\6\u00b7\n\6\r\6\16\6\u00b8\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7\u00c5\n\7\r\7\16")
        buf.write("\7\u00c6\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00d1\n\b")
        buf.write("\3\b\3\b\6\b\u00d5\n\b\r\b\16\b\u00d6\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\6\20\u0115")
        buf.write("\n\20\r\20\16\20\u0116\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u0123\n\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u012b\n\21\3\21\3\21\7\21\u012f\n\21\f")
        buf.write("\21\16\21\u0132\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u013c\n\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u0147\n\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u019a\n\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u01a2")
        buf.write("\n\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\5\35\u01f2\n\35\3\35\6\35\u01f5\n\35\r\35\16")
        buf.write("\35\u01f6\3\36\6\36\u01fa\n\36\r\36\16\36\u01fb\3\37\6")
        buf.write("\37\u01ff\n\37\r\37\16\37\u0200\3 \6 \u0204\n \r \16 ")
        buf.write("\u0205\3!\6!\u0209\n!\r!\16!\u020a\3\"\6\"\u020e\n\"\r")
        buf.write("\"\16\"\u020f\3\"\2\2#\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@B\2\7\3\2\37\37\3\2\36")
        buf.write("\36\3\2  \3\2\37 \3\2##\2\u021d\2D\3\2\2\2\4S\3\2\2\2")
        buf.write("\6\u00a4\3\2\2\2\b\u00a9\3\2\2\2\n\u00ac\3\2\2\2\f\u00ba")
        buf.write("\3\2\2\2\16\u00c8\3\2\2\2\20\u00d8\3\2\2\2\22\u00dc\3")
        buf.write("\2\2\2\24\u00e0\3\2\2\2\26\u00eb\3\2\2\2\30\u00f2\3\2")
        buf.write("\2\2\32\u00f9\3\2\2\2\34\u0100\3\2\2\2\36\u0107\3\2\2")
        buf.write("\2 \u0118\3\2\2\2\"\u0133\3\2\2\2$\u014f\3\2\2\2&\u015c")
        buf.write("\3\2\2\2(\u016c\3\2\2\2*\u0179\3\2\2\2,\u0188\3\2\2\2")
        buf.write(".\u01ab\3\2\2\2\60\u01c6\3\2\2\2\62\u01d0\3\2\2\2\64\u01de")
        buf.write("\3\2\2\2\66\u01e9\3\2\2\28\u01f1\3\2\2\2:\u01f9\3\2\2")
        buf.write("\2<\u01fe\3\2\2\2>\u0203\3\2\2\2@\u0208\3\2\2\2B\u020d")
        buf.write("\3\2\2\2DM\b\2\1\2EG\5\4\3\2FH\7\37\2\2GF\3\2\2\2GH\3")
        buf.write("\2\2\2HI\3\2\2\2IJ\b\2\1\2JL\3\2\2\2KE\3\2\2\2LO\3\2\2")
        buf.write("\2MK\3\2\2\2MN\3\2\2\2N\3\3\2\2\2OM\3\2\2\2PR\7\36\2\2")
        buf.write("QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2US\3")
        buf.write("\2\2\2VW\5\6\4\2W\u00a0\7\36\2\2XY\5\b\5\2YZ\b\3\1\2Z")
        buf.write("\u00a1\3\2\2\2[\\\5\n\6\2\\]\b\3\1\2]\u00a1\3\2\2\2^_")
        buf.write("\5\f\7\2_`\b\3\1\2`\u00a1\3\2\2\2ab\5\16\b\2bc\b\3\1\2")
        buf.write("c\u00a1\3\2\2\2de\5\20\t\2ef\b\3\1\2f\u00a1\3\2\2\2gh")
        buf.write("\5\22\n\2hi\b\3\1\2i\u00a1\3\2\2\2jk\5\24\13\2kl\b\3\1")
        buf.write("\2l\u00a1\3\2\2\2mn\5\26\f\2no\b\3\1\2o\u00a1\3\2\2\2")
        buf.write("pq\5\30\r\2qr\b\3\1\2r\u00a1\3\2\2\2st\5\32\16\2tu\b\3")
        buf.write("\1\2u\u00a1\3\2\2\2vw\5\34\17\2wx\b\3\1\2x\u00a1\3\2\2")
        buf.write("\2yz\5\36\20\2z{\b\3\1\2{\u00a1\3\2\2\2|}\5 \21\2}~\b")
        buf.write("\3\1\2~\u00a1\3\2\2\2\177\u0080\5\"\22\2\u0080\u0081\b")
        buf.write("\3\1\2\u0081\u00a1\3\2\2\2\u0082\u0083\5$\23\2\u0083\u0084")
        buf.write("\b\3\1\2\u0084\u00a1\3\2\2\2\u0085\u0086\5&\24\2\u0086")
        buf.write("\u0087\b\3\1\2\u0087\u00a1\3\2\2\2\u0088\u0089\5(\25\2")
        buf.write("\u0089\u008a\b\3\1\2\u008a\u00a1\3\2\2\2\u008b\u008c\5")
        buf.write("*\26\2\u008c\u008d\b\3\1\2\u008d\u00a1\3\2\2\2\u008e\u008f")
        buf.write("\5,\27\2\u008f\u0090\b\3\1\2\u0090\u00a1\3\2\2\2\u0091")
        buf.write("\u0092\5.\30\2\u0092\u0093\b\3\1\2\u0093\u00a1\3\2\2\2")
        buf.write("\u0094\u0095\5\60\31\2\u0095\u0096\b\3\1\2\u0096\u00a1")
        buf.write("\3\2\2\2\u0097\u0098\5\62\32\2\u0098\u0099\b\3\1\2\u0099")
        buf.write("\u00a1\3\2\2\2\u009a\u009b\5\64\33\2\u009b\u009c\b\3\1")
        buf.write("\2\u009c\u00a1\3\2\2\2\u009d\u009e\5\66\34\2\u009e\u009f")
        buf.write("\b\3\1\2\u009f\u00a1\3\2\2\2\u00a0X\3\2\2\2\u00a0[\3\2")
        buf.write("\2\2\u00a0^\3\2\2\2\u00a0a\3\2\2\2\u00a0d\3\2\2\2\u00a0")
        buf.write("g\3\2\2\2\u00a0j\3\2\2\2\u00a0m\3\2\2\2\u00a0p\3\2\2\2")
        buf.write("\u00a0s\3\2\2\2\u00a0v\3\2\2\2\u00a0y\3\2\2\2\u00a0|\3")
        buf.write("\2\2\2\u00a0\177\3\2\2\2\u00a0\u0082\3\2\2\2\u00a0\u0085")
        buf.write("\3\2\2\2\u00a0\u0088\3\2\2\2\u00a0\u008b\3\2\2\2\u00a0")
        buf.write("\u008e\3\2\2\2\u00a0\u0091\3\2\2\2\u00a0\u0094\3\2\2\2")
        buf.write("\u00a0\u0097\3\2\2\2\u00a0\u009a\3\2\2\2\u00a0\u009d\3")
        buf.write("\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\b\3\1\2\u00a3\5")
        buf.write("\3\2\2\2\u00a4\u00a5\58\35\2\u00a5\u00a6\7!\2\2\u00a6")
        buf.write("\u00a7\58\35\2\u00a7\u00a8\b\4\1\2\u00a8\7\3\2\2\2\u00a9")
        buf.write("\u00aa\7\3\2\2\u00aa\u00ab\b\5\1\2\u00ab\t\3\2\2\2\u00ac")
        buf.write("\u00ad\7\4\2\2\u00ad\u00ae\7!\2\2\u00ae\u00af\7\36\2\2")
        buf.write("\u00af\u00b6\b\6\1\2\u00b0\u00b1\7 \2\2\u00b1\u00b2\5")
        buf.write("> \2\u00b2\u00b3\7 \2\2\u00b3\u00b4\5@!\2\u00b4\u00b5")
        buf.write("\b\6\1\2\u00b5\u00b7\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\13\3\2\2\2\u00ba\u00bb\7\5\2\2\u00bb\u00bc\7!\2")
        buf.write("\2\u00bc\u00bd\7\36\2\2\u00bd\u00c4\b\7\1\2\u00be\u00bf")
        buf.write("\7 \2\2\u00bf\u00c0\5> \2\u00c0\u00c1\7 \2\2\u00c1\u00c2")
        buf.write("\5@!\2\u00c2\u00c3\b\7\1\2\u00c3\u00c5\3\2\2\2\u00c4\u00be")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\r\3\2\2\2\u00c8\u00c9\7\6\2\2\u00c9")
        buf.write("\u00ca\7!\2\2\u00ca\u00cb\7\36\2\2\u00cb\u00d4\b\b\1\2")
        buf.write("\u00cc\u00cd\7 \2\2\u00cd\u00ce\5> \2\u00ce\u00d0\7 \2")
        buf.write("\2\u00cf\u00d1\5@!\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3")
        buf.write("\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\b\b\1\2\u00d3\u00d5")
        buf.write("\3\2\2\2\u00d4\u00cc\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\17\3\2\2\2\u00d8")
        buf.write("\u00d9\7\7\2\2\u00d9\u00da\7!\2\2\u00da\u00db\b\t\1\2")
        buf.write("\u00db\21\3\2\2\2\u00dc\u00dd\7\b\2\2\u00dd\u00de\7!\2")
        buf.write("\2\u00de\u00df\b\n\1\2\u00df\23\3\2\2\2\u00e0\u00e1\7")
        buf.write("\t\2\2\u00e1\u00e2\7\36\2\2\u00e2\u00e3\58\35\2\u00e3")
        buf.write("\u00e4\7\36\2\2\u00e4\u00e5\7\n\2\2\u00e5\u00e6\7\36\2")
        buf.write("\2\u00e6\u00e7\58\35\2\u00e7\u00e8\b\13\1\2\u00e8\u00e9")
        buf.write("\b\13\1\2\u00e9\u00ea\b\13\1\2\u00ea\25\3\2\2\2\u00eb")
        buf.write("\u00ec\7\13\2\2\u00ec\u00ed\7!\2\2\u00ed\u00ee\7\36\2")
        buf.write("\2\u00ee\u00ef\58\35\2\u00ef\u00f0\b\f\1\2\u00f0\u00f1")
        buf.write("\b\f\1\2\u00f1\27\3\2\2\2\u00f2\u00f3\7\f\2\2\u00f3\u00f4")
        buf.write("\7!\2\2\u00f4\u00f5\7\36\2\2\u00f5\u00f6\58\35\2\u00f6")
        buf.write("\u00f7\b\r\1\2\u00f7\u00f8\b\r\1\2\u00f8\31\3\2\2\2\u00f9")
        buf.write("\u00fa\7\r\2\2\u00fa\u00fb\7!\2\2\u00fb\u00fc\7\36\2\2")
        buf.write("\u00fc\u00fd\58\35\2\u00fd\u00fe\b\16\1\2\u00fe\u00ff")
        buf.write("\b\16\1\2\u00ff\33\3\2\2\2\u0100\u0101\7\16\2\2\u0101")
        buf.write("\u0102\7!\2\2\u0102\u0103\7\36\2\2\u0103\u0104\58\35\2")
        buf.write("\u0104\u0105\b\17\1\2\u0105\u0106\b\17\1\2\u0106\35\3")
        buf.write("\2\2\2\u0107\u0108\7\17\2\2\u0108\u0109\7!\2\2\u0109\u010a")
        buf.write("\7\36\2\2\u010a\u010b\58\35\2\u010b\u010c\7\36\2\2\u010c")
        buf.write("\u010d\b\20\1\2\u010d\u0114\b\20\1\2\u010e\u010f\7 \2")
        buf.write("\2\u010f\u0110\5> \2\u0110\u0111\7 \2\2\u0111\u0112\5")
        buf.write("@!\2\u0112\u0113\b\20\1\2\u0113\u0115\3\2\2\2\u0114\u010e")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0114\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\37\3\2\2\2\u0118\u0119\7\20\2\2\u0119")
        buf.write("\u011a\7!\2\2\u011a\u011b\7\36\2\2\u011b\u011c\58\35\2")
        buf.write("\u011c\u011d\7\36\2\2\u011d\u011e\b\21\1\2\u011e\u011f")
        buf.write("\b\21\1\2\u011f\u0120\5> \2\u0120\u0122\7 \2\2\u0121\u0123")
        buf.write("\5@!\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124")
        buf.write("\3\2\2\2\u0124\u0125\b\21\1\2\u0125\u0130\3\2\2\2\u0126")
        buf.write("\u0127\7 \2\2\u0127\u0128\5> \2\u0128\u012a\7 \2\2\u0129")
        buf.write("\u012b\5@!\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\u012c\3\2\2\2\u012c\u012d\b\21\1\2\u012d\u012f\3\2\2")
        buf.write("\2\u012e\u0126\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131!\3\2\2\2\u0132\u0130")
        buf.write("\3\2\2\2\u0133\u0134\7\21\2\2\u0134\u0135\7!\2\2\u0135")
        buf.write("\u0136\7\36\2\2\u0136\u0137\58\35\2\u0137\u0138\7\36\2")
        buf.write("\2\u0138\u0139\7\"\2\2\u0139\u013b\7\36\2\2\u013a\u013c")
        buf.write("\5<\37\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u013e\7\36\2\2\u013e\u013f\7\"\2")
        buf.write("\2\u013f\u0140\7\36\2\2\u0140\u0141\58\35\2\u0141\u0142")
        buf.write("\7\36\2\2\u0142\u0143\7\"\2\2\u0143\u0144\7\36\2\2\u0144")
        buf.write("\u0146\7#\2\2\u0145\u0147\5B\"\2\u0146\u0145\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\7#\2\2")
        buf.write("\u0149\u014a\b\22\1\2\u014a\u014b\b\22\1\2\u014b\u014c")
        buf.write("\b\22\1\2\u014c\u014d\b\22\1\2\u014d\u014e\b\22\1\2\u014e")
        buf.write("#\3\2\2\2\u014f\u0150\7\22\2\2\u0150\u0151\7!\2\2\u0151")
        buf.write("\u0152\7\36\2\2\u0152\u0153\58\35\2\u0153\u0154\7\36\2")
        buf.write("\2\u0154\u0155\5<\37\2\u0155\u0156\7\36\2\2\u0156\u0157")
        buf.write("\5:\36\2\u0157\u0158\b\23\1\2\u0158\u0159\b\23\1\2\u0159")
        buf.write("\u015a\b\23\1\2\u015a\u015b\b\23\1\2\u015b%\3\2\2\2\u015c")
        buf.write("\u015d\7\23\2\2\u015d\u015e\7!\2\2\u015e\u015f\7\36\2")
        buf.write("\2\u015f\u0160\58\35\2\u0160\u0161\7\36\2\2\u0161\u0162")
        buf.write("\58\35\2\u0162\u0163\7\36\2\2\u0163\u0164\5<\37\2\u0164")
        buf.write("\u0165\7\36\2\2\u0165\u0166\5:\36\2\u0166\u0167\b\24\1")
        buf.write("\2\u0167\u0168\b\24\1\2\u0168\u0169\b\24\1\2\u0169\u016a")
        buf.write("\b\24\1\2\u016a\u016b\b\24\1\2\u016b\'\3\2\2\2\u016c\u016d")
        buf.write("\7\24\2\2\u016d\u016e\7!\2\2\u016e\u016f\7\36\2\2\u016f")
        buf.write("\u0170\58\35\2\u0170\u0171\7\36\2\2\u0171\u0172\5<\37")
        buf.write("\2\u0172\u0173\7\36\2\2\u0173\u0174\5:\36\2\u0174\u0175")
        buf.write("\b\25\1\2\u0175\u0176\b\25\1\2\u0176\u0177\b\25\1\2\u0177")
        buf.write("\u0178\b\25\1\2\u0178)\3\2\2\2\u0179\u017a\7\26\2\2\u017a")
        buf.write("\u017b\7!\2\2\u017b\u017c\7\36\2\2\u017c\u017d\5<\37\2")
        buf.write("\u017d\u017e\7\36\2\2\u017e\u017f\7\34\2\2\u017f\u0180")
        buf.write("\7\36\2\2\u0180\u0181\5<\37\2\u0181\u0182\7\36\2\2\u0182")
        buf.write("\u0183\5:\36\2\u0183\u0184\b\26\1\2\u0184\u0185\b\26\1")
        buf.write("\2\u0185\u0186\b\26\1\2\u0186\u0187\b\26\1\2\u0187+\3")
        buf.write("\2\2\2\u0188\u0189\7\25\2\2\u0189\u018a\7!\2\2\u018a\u018b")
        buf.write("\7\36\2\2\u018b\u018c\58\35\2\u018c\u018d\7\36\2\2\u018d")
        buf.write("\u018e\7\"\2\2\u018e\u018f\7\36\2\2\u018f\u0190\58\35")
        buf.write("\2\u0190\u0191\7\36\2\2\u0191\u0192\7\"\2\2\u0192\u0193")
        buf.write("\7\36\2\2\u0193\u0194\58\35\2\u0194\u0195\7\36\2\2\u0195")
        buf.write("\u0196\7\"\2\2\u0196\u0197\7\36\2\2\u0197\u0199\7#\2\2")
        buf.write("\u0198\u019a\5B\"\2\u0199\u0198\3\2\2\2\u0199\u019a\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\7#\2\2\u019c\u019d")
        buf.write("\7\36\2\2\u019d\u019e\7\"\2\2\u019e\u019f\7\36\2\2\u019f")
        buf.write("\u01a1\7#\2\2\u01a0\u01a2\5B\"\2\u01a1\u01a0\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\7#\2\2")
        buf.write("\u01a4\u01a5\b\27\1\2\u01a5\u01a6\b\27\1\2\u01a6\u01a7")
        buf.write("\b\27\1\2\u01a7\u01a8\b\27\1\2\u01a8\u01a9\b\27\1\2\u01a9")
        buf.write("\u01aa\b\27\1\2\u01aa-\3\2\2\2\u01ab\u01ac\7\27\2\2\u01ac")
        buf.write("\u01ad\7!\2\2\u01ad\u01ae\7\36\2\2\u01ae\u01af\58\35\2")
        buf.write("\u01af\u01b0\7\36\2\2\u01b0\u01b1\58\35\2\u01b1\u01b2")
        buf.write("\7\36\2\2\u01b2\u01b3\58\35\2\u01b3\u01b4\7!\2\2\u01b4")
        buf.write("\u01b5\7\36\2\2\u01b5\u01b6\5<\37\2\u01b6\u01b7\7\36\2")
        buf.write("\2\u01b7\u01b8\5<\37\2\u01b8\u01b9\7\36\2\2\u01b9\u01ba")
        buf.write("\5<\37\2\u01ba\u01bb\7\36\2\2\u01bb\u01bc\7\35\2\2\u01bc")
        buf.write("\u01bd\7\36\2\2\u01bd\u01be\5:\36\2\u01be\u01bf\b\30\1")
        buf.write("\2\u01bf\u01c0\b\30\1\2\u01c0\u01c1\b\30\1\2\u01c1\u01c2")
        buf.write("\b\30\1\2\u01c2\u01c3\b\30\1\2\u01c3\u01c4\b\30\1\2\u01c4")
        buf.write("\u01c5\b\30\1\2\u01c5/\3\2\2\2\u01c6\u01c7\7\30\2\2\u01c7")
        buf.write("\u01c8\7!\2\2\u01c8\u01c9\7\36\2\2\u01c9\u01ca\58\35\2")
        buf.write("\u01ca\u01cb\7\36\2\2\u01cb\u01cc\5:\36\2\u01cc\u01cd")
        buf.write("\b\31\1\2\u01cd\u01ce\b\31\1\2\u01ce\u01cf\b\31\1\2\u01cf")
        buf.write("\61\3\2\2\2\u01d0\u01d1\7\31\2\2\u01d1\u01d2\7!\2\2\u01d2")
        buf.write("\u01d3\7\36\2\2\u01d3\u01d4\58\35\2\u01d4\u01d5\7\36\2")
        buf.write("\2\u01d5\u01d6\58\35\2\u01d6\u01d7\7!\2\2\u01d7\u01d8")
        buf.write("\7\36\2\2\u01d8\u01d9\5:\36\2\u01d9\u01da\b\32\1\2\u01da")
        buf.write("\u01db\b\32\1\2\u01db\u01dc\b\32\1\2\u01dc\u01dd\b\32")
        buf.write("\1\2\u01dd\63\3\2\2\2\u01de\u01df\7\32\2\2\u01df\u01e0")
        buf.write("\7!\2\2\u01e0\u01e1\7\36\2\2\u01e1\u01e2\58\35\2\u01e2")
        buf.write("\u01e3\7!\2\2\u01e3\u01e4\7\36\2\2\u01e4\u01e5\58\35\2")
        buf.write("\u01e5\u01e6\b\33\1\2\u01e6\u01e7\b\33\1\2\u01e7\u01e8")
        buf.write("\b\33\1\2\u01e8\65\3\2\2\2\u01e9\u01ea\7\33\2\2\u01ea")
        buf.write("\u01eb\7!\2\2\u01eb\u01ec\7\36\2\2\u01ec\u01ed\5:\36\2")
        buf.write("\u01ed\u01ee\b\34\1\2\u01ee\u01ef\b\34\1\2\u01ef\67\3")
        buf.write("\2\2\2\u01f0\u01f2\7\"\2\2\u01f1\u01f0\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01f5\7$\2\2\u01f4")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f4\3\2\2\2")
        buf.write("\u01f6\u01f7\3\2\2\2\u01f79\3\2\2\2\u01f8\u01fa\n\2\2")
        buf.write("\2\u01f9\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc;\3\2\2\2\u01fd\u01ff")
        buf.write("\n\3\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200")
        buf.write("\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201=\3\2\2\2\u0202")
        buf.write("\u0204\n\4\2\2\u0203\u0202\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206?\3\2\2")
        buf.write("\2\u0207\u0209\n\5\2\2\u0208\u0207\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b")
        buf.write("A\3\2\2\2\u020c\u020e\n\6\2\2\u020d\u020c\3\2\2\2\u020e")
        buf.write("\u020f\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2")
        buf.write("\u0210C\3\2\2\2\31GMS\u00a0\u00b8\u00c6\u00d0\u00d6\u0116")
        buf.write("\u0122\u012a\u0130\u013b\u0146\u0199\u01a1\u01f1\u01f6")
        buf.write("\u01fb\u0200\u0205\u020a\u020f")
        return buf.getvalue()


class EventsParser ( Parser ):

    grammarFileName = "Events.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'------------------------------------------------------------'", 
                     "'InitGame'", "'InitRound'", "'InitAuth'", "'ShutdownGame'", 
                     "'Warmup'", "'Session data initialised for client on slot'", 
                     "'at'", "'ClientConnect'", "'ClientDisconnect'", "'ClientBegin'", 
                     "'ClientSpawn'", "'ClientUserinfo'", "'ClientUserinfoChanged'", 
                     "'AccountValidated'", "'say'", "'saytell'", "'sayteam'", 
                     "'Radio'", "'tell'", "'Kill'", "'Item'", "'Flag'", 
                     "'FlagCaptureTime'", "'Flag Return'", "'to'", "'by'", 
                     "<INVALID>", "<INVALID>", "'\\'", "':'", "'-'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "SEPARATOR", "INITGAME", "INITROUND", 
                      "INITAUTH", "SHUTDOWNGAME", "WARMUP", "SESSION_DATA_INITIALISED", 
                      "AT", "CLIENTCONNECT", "CLIENTDISCONNECT", "CLIENTBEGIN", 
                      "CLIENTSPAWN", "CLIENTUSERINFO", "CLIENTUSERINFOCHANGED", 
                      "ACCOUNTVALIDATED", "SAY", "SAYTELL", "SAYTEAM", "RADIO", 
                      "TELL", "KILL", "ITEM", "FLAG", "FLAGCAPTURETIME", 
                      "FLAGRETURN", "TO", "BY", "WHITESPACE", "NEWLINE", 
                      "BACK_SLASH", "COLON", "MINUS", "DOUBLE_QUOTE", "DIGIT", 
                      "ANY_CHAR" ]

    RULE_events = 0
    RULE_event = 1
    RULE_eventTime = 2
    RULE_separatorEvent = 3
    RULE_initGameEvent = 4
    RULE_initRoundEvent = 5
    RULE_initAuthEvent = 6
    RULE_shutdownGameEvent = 7
    RULE_warmupEvent = 8
    RULE_sessionDataInitEvent = 9
    RULE_clientConnectEvent = 10
    RULE_clientDisconnectEvent = 11
    RULE_clientBeginEvent = 12
    RULE_clientSpawnEvent = 13
    RULE_clientUserinfoEvent = 14
    RULE_clientUserinfoChangedEvent = 15
    RULE_accountValidatedEvent = 16
    RULE_sayEvent = 17
    RULE_sayTellEvent = 18
    RULE_sayTeamEvent = 19
    RULE_tellEvent = 20
    RULE_radioEvent = 21
    RULE_killEvent = 22
    RULE_itemEvent = 23
    RULE_flagEvent = 24
    RULE_flagCaptureTimeEvent = 25
    RULE_flagReturnEvent = 26
    RULE_intValue = 27
    RULE_manyButNewLine = 28
    RULE_manyButWhitespace = 29
    RULE_manyButBackSlash = 30
    RULE_manyButBackSlashOrNewLine = 31
    RULE_manyButDoubleQuote = 32

    ruleNames =  [ "events", "event", "eventTime", "separatorEvent", "initGameEvent", 
                   "initRoundEvent", "initAuthEvent", "shutdownGameEvent", 
                   "warmupEvent", "sessionDataInitEvent", "clientConnectEvent", 
                   "clientDisconnectEvent", "clientBeginEvent", "clientSpawnEvent", 
                   "clientUserinfoEvent", "clientUserinfoChangedEvent", 
                   "accountValidatedEvent", "sayEvent", "sayTellEvent", 
                   "sayTeamEvent", "tellEvent", "radioEvent", "killEvent", 
                   "itemEvent", "flagEvent", "flagCaptureTimeEvent", "flagReturnEvent", 
                   "intValue", "manyButNewLine", "manyButWhitespace", "manyButBackSlash", 
                   "manyButBackSlashOrNewLine", "manyButDoubleQuote" ]

    EOF = Token.EOF
    SEPARATOR=1
    INITGAME=2
    INITROUND=3
    INITAUTH=4
    SHUTDOWNGAME=5
    WARMUP=6
    SESSION_DATA_INITIALISED=7
    AT=8
    CLIENTCONNECT=9
    CLIENTDISCONNECT=10
    CLIENTBEGIN=11
    CLIENTSPAWN=12
    CLIENTUSERINFO=13
    CLIENTUSERINFOCHANGED=14
    ACCOUNTVALIDATED=15
    SAY=16
    SAYTELL=17
    SAYTEAM=18
    RADIO=19
    TELL=20
    KILL=21
    ITEM=22
    FLAG=23
    FLAGCAPTURETIME=24
    FLAGRETURN=25
    TO=26
    BY=27
    WHITESPACE=28
    NEWLINE=29
    BACK_SLASH=30
    COLON=31
    MINUS=32
    DOUBLE_QUOTE=33
    DIGIT=34
    ANY_CHAR=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EventsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # EventContext

        def event(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.EventContext)
            else:
                return self.getTypedRuleContext(EventsParser.EventContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.NEWLINE)
            else:
                return self.getToken(EventsParser.NEWLINE, i)

        def getRuleIndex(self):
            return EventsParser.RULE_events

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvents" ):
                listener.enterEvents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvents" ):
                listener.exitEvents(self)




    def events(self):

        localctx = EventsParser.EventsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_events)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.value = []
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.WHITESPACE) | (1 << EventsParser.MINUS) | (1 << EventsParser.DIGIT))) != 0):
                self.state = 67
                localctx.a = self.event()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==EventsParser.NEWLINE:
                    self.state = 68
                    self.match(EventsParser.NEWLINE)


                localctx.value.append(localctx.a.value)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.time = None # EventTimeContext
            self.separatorEvt = None # SeparatorEventContext
            self.initGameEvt = None # InitGameEventContext
            self.initRoundEvt = None # InitRoundEventContext
            self.initAuthEvt = None # InitAuthEventContext
            self.shutdownGameEvt = None # ShutdownGameEventContext
            self.warmupEvt = None # WarmupEventContext
            self.sessionDataInitEvt = None # SessionDataInitEventContext
            self.clientConnectEvt = None # ClientConnectEventContext
            self.clientDisconnectEvt = None # ClientDisconnectEventContext
            self.clientBeginEvt = None # ClientBeginEventContext
            self.clientSpawnEvt = None # ClientSpawnEventContext
            self.clientUserinfoEvt = None # ClientUserinfoEventContext
            self.clientUserinfoChangedEvt = None # ClientUserinfoChangedEventContext
            self.accountValidatedEvt = None # AccountValidatedEventContext
            self.sayEvt = None # SayEventContext
            self.sayTellEvt = None # SayTellEventContext
            self.sayTeamEvt = None # SayTeamEventContext
            self.tellEvt = None # TellEventContext
            self.radioEvt = None # RadioEventContext
            self.killEvt = None # KillEventContext
            self.itemEvt = None # ItemEventContext
            self.flagEvt = None # FlagEventContext
            self.flagCaptureTimeEvt = None # FlagCaptureTimeEventContext
            self.flagReturnEvt = None # FlagReturnEventContext

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def eventTime(self):
            return self.getTypedRuleContext(EventsParser.EventTimeContext,0)


        def separatorEvent(self):
            return self.getTypedRuleContext(EventsParser.SeparatorEventContext,0)


        def initGameEvent(self):
            return self.getTypedRuleContext(EventsParser.InitGameEventContext,0)


        def initRoundEvent(self):
            return self.getTypedRuleContext(EventsParser.InitRoundEventContext,0)


        def initAuthEvent(self):
            return self.getTypedRuleContext(EventsParser.InitAuthEventContext,0)


        def shutdownGameEvent(self):
            return self.getTypedRuleContext(EventsParser.ShutdownGameEventContext,0)


        def warmupEvent(self):
            return self.getTypedRuleContext(EventsParser.WarmupEventContext,0)


        def sessionDataInitEvent(self):
            return self.getTypedRuleContext(EventsParser.SessionDataInitEventContext,0)


        def clientConnectEvent(self):
            return self.getTypedRuleContext(EventsParser.ClientConnectEventContext,0)


        def clientDisconnectEvent(self):
            return self.getTypedRuleContext(EventsParser.ClientDisconnectEventContext,0)


        def clientBeginEvent(self):
            return self.getTypedRuleContext(EventsParser.ClientBeginEventContext,0)


        def clientSpawnEvent(self):
            return self.getTypedRuleContext(EventsParser.ClientSpawnEventContext,0)


        def clientUserinfoEvent(self):
            return self.getTypedRuleContext(EventsParser.ClientUserinfoEventContext,0)


        def clientUserinfoChangedEvent(self):
            return self.getTypedRuleContext(EventsParser.ClientUserinfoChangedEventContext,0)


        def accountValidatedEvent(self):
            return self.getTypedRuleContext(EventsParser.AccountValidatedEventContext,0)


        def sayEvent(self):
            return self.getTypedRuleContext(EventsParser.SayEventContext,0)


        def sayTellEvent(self):
            return self.getTypedRuleContext(EventsParser.SayTellEventContext,0)


        def sayTeamEvent(self):
            return self.getTypedRuleContext(EventsParser.SayTeamEventContext,0)


        def tellEvent(self):
            return self.getTypedRuleContext(EventsParser.TellEventContext,0)


        def radioEvent(self):
            return self.getTypedRuleContext(EventsParser.RadioEventContext,0)


        def killEvent(self):
            return self.getTypedRuleContext(EventsParser.KillEventContext,0)


        def itemEvent(self):
            return self.getTypedRuleContext(EventsParser.ItemEventContext,0)


        def flagEvent(self):
            return self.getTypedRuleContext(EventsParser.FlagEventContext,0)


        def flagCaptureTimeEvent(self):
            return self.getTypedRuleContext(EventsParser.FlagCaptureTimeEventContext,0)


        def flagReturnEvent(self):
            return self.getTypedRuleContext(EventsParser.FlagReturnEventContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_event

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent" ):
                listener.enterEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent" ):
                listener.exitEvent(self)




    def event(self):

        localctx = EventsParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EventsParser.WHITESPACE:
                self.state = 78
                self.match(EventsParser.WHITESPACE)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            localctx.time = self.eventTime()
            self.state = 85
            self.match(EventsParser.WHITESPACE)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EventsParser.SEPARATOR]:
                self.state = 86
                localctx.separatorEvt = self.separatorEvent()
                localctx.value = localctx.separatorEvt.value
                pass
            elif token in [EventsParser.INITGAME]:
                self.state = 89
                localctx.initGameEvt = self.initGameEvent()
                localctx.value = localctx.initGameEvt.value
                pass
            elif token in [EventsParser.INITROUND]:
                self.state = 92
                localctx.initRoundEvt = self.initRoundEvent()
                localctx.value = localctx.initRoundEvt.value
                pass
            elif token in [EventsParser.INITAUTH]:
                self.state = 95
                localctx.initAuthEvt = self.initAuthEvent()
                localctx.value = localctx.initAuthEvt.value
                pass
            elif token in [EventsParser.SHUTDOWNGAME]:
                self.state = 98
                localctx.shutdownGameEvt = self.shutdownGameEvent()
                localctx.value = localctx.shutdownGameEvt.value
                pass
            elif token in [EventsParser.WARMUP]:
                self.state = 101
                localctx.warmupEvt = self.warmupEvent()
                localctx.value = localctx.warmupEvt.value
                pass
            elif token in [EventsParser.SESSION_DATA_INITIALISED]:
                self.state = 104
                localctx.sessionDataInitEvt = self.sessionDataInitEvent()
                localctx.value = localctx.sessionDataInitEvt.value
                pass
            elif token in [EventsParser.CLIENTCONNECT]:
                self.state = 107
                localctx.clientConnectEvt = self.clientConnectEvent()
                localctx.value = localctx.clientConnectEvt.value
                pass
            elif token in [EventsParser.CLIENTDISCONNECT]:
                self.state = 110
                localctx.clientDisconnectEvt = self.clientDisconnectEvent()
                localctx.value = localctx.clientDisconnectEvt.value
                pass
            elif token in [EventsParser.CLIENTBEGIN]:
                self.state = 113
                localctx.clientBeginEvt = self.clientBeginEvent()
                localctx.value = localctx.clientBeginEvt.value
                pass
            elif token in [EventsParser.CLIENTSPAWN]:
                self.state = 116
                localctx.clientSpawnEvt = self.clientSpawnEvent()
                localctx.value = localctx.clientSpawnEvt.value
                pass
            elif token in [EventsParser.CLIENTUSERINFO]:
                self.state = 119
                localctx.clientUserinfoEvt = self.clientUserinfoEvent()
                localctx.value = localctx.clientUserinfoEvt.value
                pass
            elif token in [EventsParser.CLIENTUSERINFOCHANGED]:
                self.state = 122
                localctx.clientUserinfoChangedEvt = self.clientUserinfoChangedEvent()
                localctx.value = localctx.clientUserinfoChangedEvt.value
                pass
            elif token in [EventsParser.ACCOUNTVALIDATED]:
                self.state = 125
                localctx.accountValidatedEvt = self.accountValidatedEvent()
                localctx.value = localctx.accountValidatedEvt.value
                pass
            elif token in [EventsParser.SAY]:
                self.state = 128
                localctx.sayEvt = self.sayEvent()
                localctx.value = localctx.sayEvt.value
                pass
            elif token in [EventsParser.SAYTELL]:
                self.state = 131
                localctx.sayTellEvt = self.sayTellEvent()
                localctx.value = localctx.sayTellEvt.value
                pass
            elif token in [EventsParser.SAYTEAM]:
                self.state = 134
                localctx.sayTeamEvt = self.sayTeamEvent()
                localctx.value = localctx.sayTeamEvt.value
                pass
            elif token in [EventsParser.TELL]:
                self.state = 137
                localctx.tellEvt = self.tellEvent()
                localctx.value = localctx.tellEvt.value
                pass
            elif token in [EventsParser.RADIO]:
                self.state = 140
                localctx.radioEvt = self.radioEvent()
                localctx.value = localctx.radioEvt.value
                pass
            elif token in [EventsParser.KILL]:
                self.state = 143
                localctx.killEvt = self.killEvent()
                localctx.value = localctx.killEvt.value
                pass
            elif token in [EventsParser.ITEM]:
                self.state = 146
                localctx.itemEvt = self.itemEvent()
                localctx.value = localctx.itemEvt.value
                pass
            elif token in [EventsParser.FLAG]:
                self.state = 149
                localctx.flagEvt = self.flagEvent()
                localctx.value = localctx.flagEvt.value
                pass
            elif token in [EventsParser.FLAGCAPTURETIME]:
                self.state = 152
                localctx.flagCaptureTimeEvt = self.flagCaptureTimeEvent()
                localctx.value = localctx.flagCaptureTimeEvt.value
                pass
            elif token in [EventsParser.FLAGRETURN]:
                self.state = 155
                localctx.flagReturnEvt = self.flagReturnEvent()
                localctx.value = localctx.flagReturnEvt.value
                pass
            else:
                raise NoViableAltException(self)

            localctx.value.time = localctx.time.value
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventTimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # IntValueContext

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_eventTime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventTime" ):
                listener.enterEventTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventTime" ):
                listener.exitEventTime(self)




    def eventTime(self):

        localctx = EventsParser.EventTimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_eventTime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            localctx.a = self.intValue()
            self.state = 163
            self.match(EventsParser.COLON)
            self.state = 164
            localctx.b = self.intValue()
            localctx.value = int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))) * 60 + int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeparatorEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None

        def SEPARATOR(self):
            return self.getToken(EventsParser.SEPARATOR, 0)

        def getRuleIndex(self):
            return EventsParser.RULE_separatorEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeparatorEvent" ):
                listener.enterSeparatorEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeparatorEvent" ):
                listener.exitSeparatorEvent(self)




    def separatorEvent(self):

        localctx = EventsParser.SeparatorEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_separatorEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(EventsParser.SEPARATOR)
            localctx.value = SeparatorEvent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitGameEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # ManyButBackSlashContext
            self.b = None # ManyButBackSlashOrNewLineContext

        def INITGAME(self):
            return self.getToken(EventsParser.INITGAME, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def manyButBackSlash(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashContext,i)


        def manyButBackSlashOrNewLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashOrNewLineContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashOrNewLineContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_initGameEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitGameEvent" ):
                listener.enterInitGameEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitGameEvent" ):
                listener.exitInitGameEvent(self)




    def initGameEvent(self):

        localctx = EventsParser.InitGameEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_initGameEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(EventsParser.INITGAME)
            self.state = 171
            self.match(EventsParser.COLON)
            self.state = 172
            self.match(EventsParser.WHITESPACE)
            localctx.value = InitGameEvent()
            self.state = 180 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174
                self.match(EventsParser.BACK_SLASH)
                self.state = 175
                localctx.a = self.manyButBackSlash()
                self.state = 176
                self.match(EventsParser.BACK_SLASH)
                self.state = 177
                localctx.b = self.manyButBackSlashOrNewLine()
                localctx.value.parameters[(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))]=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
                self.state = 182 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EventsParser.BACK_SLASH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitRoundEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # ManyButBackSlashContext
            self.b = None # ManyButBackSlashOrNewLineContext

        def INITROUND(self):
            return self.getToken(EventsParser.INITROUND, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def manyButBackSlash(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashContext,i)


        def manyButBackSlashOrNewLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashOrNewLineContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashOrNewLineContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_initRoundEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitRoundEvent" ):
                listener.enterInitRoundEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitRoundEvent" ):
                listener.exitInitRoundEvent(self)




    def initRoundEvent(self):

        localctx = EventsParser.InitRoundEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_initRoundEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(EventsParser.INITROUND)
            self.state = 185
            self.match(EventsParser.COLON)
            self.state = 186
            self.match(EventsParser.WHITESPACE)
            localctx.value = InitRoundEvent()
            self.state = 194 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self.match(EventsParser.BACK_SLASH)
                self.state = 189
                localctx.a = self.manyButBackSlash()
                self.state = 190
                self.match(EventsParser.BACK_SLASH)
                self.state = 191
                localctx.b = self.manyButBackSlashOrNewLine()
                localctx.value.parameters[(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))]=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
                self.state = 196 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EventsParser.BACK_SLASH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitAuthEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # ManyButBackSlashContext
            self.b = None # ManyButBackSlashOrNewLineContext

        def INITAUTH(self):
            return self.getToken(EventsParser.INITAUTH, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def manyButBackSlash(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashContext,i)


        def manyButBackSlashOrNewLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashOrNewLineContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashOrNewLineContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_initAuthEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitAuthEvent" ):
                listener.enterInitAuthEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitAuthEvent" ):
                listener.exitInitAuthEvent(self)




    def initAuthEvent(self):

        localctx = EventsParser.InitAuthEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initAuthEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(EventsParser.INITAUTH)
            self.state = 199
            self.match(EventsParser.COLON)
            self.state = 200
            self.match(EventsParser.WHITESPACE)
            localctx.value = InitAuthEvent()
            self.state = 210 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 202
                self.match(EventsParser.BACK_SLASH)
                self.state = 203
                localctx.a = self.manyButBackSlash()
                self.state = 204
                self.match(EventsParser.BACK_SLASH)
                self.state = 206
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 205
                    localctx.b = self.manyButBackSlashOrNewLine()


                localctx.value.parameters[(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))]=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
                self.state = 212 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EventsParser.BACK_SLASH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShutdownGameEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None

        def SHUTDOWNGAME(self):
            return self.getToken(EventsParser.SHUTDOWNGAME, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def getRuleIndex(self):
            return EventsParser.RULE_shutdownGameEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShutdownGameEvent" ):
                listener.enterShutdownGameEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShutdownGameEvent" ):
                listener.exitShutdownGameEvent(self)




    def shutdownGameEvent(self):

        localctx = EventsParser.ShutdownGameEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_shutdownGameEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(EventsParser.SHUTDOWNGAME)
            self.state = 215
            self.match(EventsParser.COLON)
            localctx.value = ShutdownGameEvent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WarmupEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None

        def WARMUP(self):
            return self.getToken(EventsParser.WARMUP, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def getRuleIndex(self):
            return EventsParser.RULE_warmupEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWarmupEvent" ):
                listener.enterWarmupEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWarmupEvent" ):
                listener.exitWarmupEvent(self)




    def warmupEvent(self):

        localctx = EventsParser.WarmupEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_warmupEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(EventsParser.WARMUP)
            self.state = 219
            self.match(EventsParser.COLON)
            localctx.value = WarmUpEvent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SessionDataInitEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # IntValueContext

        def SESSION_DATA_INITIALISED(self):
            return self.getToken(EventsParser.SESSION_DATA_INITIALISED, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def AT(self):
            return self.getToken(EventsParser.AT, 0)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_sessionDataInitEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSessionDataInitEvent" ):
                listener.enterSessionDataInitEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSessionDataInitEvent" ):
                listener.exitSessionDataInitEvent(self)




    def sessionDataInitEvent(self):

        localctx = EventsParser.SessionDataInitEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sessionDataInitEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(EventsParser.SESSION_DATA_INITIALISED)
            self.state = 223
            self.match(EventsParser.WHITESPACE)
            self.state = 224
            localctx.a = self.intValue()
            self.state = 225
            self.match(EventsParser.WHITESPACE)
            self.state = 226
            self.match(EventsParser.AT)
            self.state = 227
            self.match(EventsParser.WHITESPACE)
            self.state = 228
            localctx.b = self.intValue()
            localctx.value = SessionDataInitialisedEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.unknown=int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClientConnectEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext

        def CLIENTCONNECT(self):
            return self.getToken(EventsParser.CLIENTCONNECT, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_clientConnectEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClientConnectEvent" ):
                listener.enterClientConnectEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClientConnectEvent" ):
                listener.exitClientConnectEvent(self)




    def clientConnectEvent(self):

        localctx = EventsParser.ClientConnectEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_clientConnectEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(EventsParser.CLIENTCONNECT)
            self.state = 234
            self.match(EventsParser.COLON)
            self.state = 235
            self.match(EventsParser.WHITESPACE)
            self.state = 236
            localctx.a = self.intValue()
            localctx.value=ClientConnectEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClientDisconnectEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext

        def CLIENTDISCONNECT(self):
            return self.getToken(EventsParser.CLIENTDISCONNECT, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_clientDisconnectEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClientDisconnectEvent" ):
                listener.enterClientDisconnectEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClientDisconnectEvent" ):
                listener.exitClientDisconnectEvent(self)




    def clientDisconnectEvent(self):

        localctx = EventsParser.ClientDisconnectEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_clientDisconnectEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(EventsParser.CLIENTDISCONNECT)
            self.state = 241
            self.match(EventsParser.COLON)
            self.state = 242
            self.match(EventsParser.WHITESPACE)
            self.state = 243
            localctx.a = self.intValue()
            localctx.value=ClientDisconnectEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClientBeginEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext

        def CLIENTBEGIN(self):
            return self.getToken(EventsParser.CLIENTBEGIN, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_clientBeginEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClientBeginEvent" ):
                listener.enterClientBeginEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClientBeginEvent" ):
                listener.exitClientBeginEvent(self)




    def clientBeginEvent(self):

        localctx = EventsParser.ClientBeginEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_clientBeginEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(EventsParser.CLIENTBEGIN)
            self.state = 248
            self.match(EventsParser.COLON)
            self.state = 249
            self.match(EventsParser.WHITESPACE)
            self.state = 250
            localctx.a = self.intValue()
            localctx.value=ClientBeginEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClientSpawnEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext

        def CLIENTSPAWN(self):
            return self.getToken(EventsParser.CLIENTSPAWN, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_clientSpawnEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClientSpawnEvent" ):
                listener.enterClientSpawnEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClientSpawnEvent" ):
                listener.exitClientSpawnEvent(self)




    def clientSpawnEvent(self):

        localctx = EventsParser.ClientSpawnEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_clientSpawnEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(EventsParser.CLIENTSPAWN)
            self.state = 255
            self.match(EventsParser.COLON)
            self.state = 256
            self.match(EventsParser.WHITESPACE)
            self.state = 257
            localctx.a = self.intValue()
            localctx.value=ClientSpawnEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClientUserinfoEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # ManyButBackSlashContext
            self.c = None # ManyButBackSlashOrNewLineContext

        def CLIENTUSERINFO(self):
            return self.getToken(EventsParser.CLIENTUSERINFO, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def manyButBackSlash(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashContext,i)


        def manyButBackSlashOrNewLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashOrNewLineContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashOrNewLineContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_clientUserinfoEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClientUserinfoEvent" ):
                listener.enterClientUserinfoEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClientUserinfoEvent" ):
                listener.exitClientUserinfoEvent(self)




    def clientUserinfoEvent(self):

        localctx = EventsParser.ClientUserinfoEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_clientUserinfoEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(EventsParser.CLIENTUSERINFO)
            self.state = 262
            self.match(EventsParser.COLON)
            self.state = 263
            self.match(EventsParser.WHITESPACE)
            self.state = 264
            localctx.a = self.intValue()
            self.state = 265
            self.match(EventsParser.WHITESPACE)
            localctx.value=ClientUserinfoEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            self.state = 274 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 268
                self.match(EventsParser.BACK_SLASH)
                self.state = 269
                localctx.b = self.manyButBackSlash()
                self.state = 270
                self.match(EventsParser.BACK_SLASH)
                self.state = 271
                localctx.c = self.manyButBackSlashOrNewLine()
                localctx.value.parameters[(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))]=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
                self.state = 276 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EventsParser.BACK_SLASH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClientUserinfoChangedEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # ManyButBackSlashContext
            self.c = None # ManyButBackSlashOrNewLineContext
            self.b2 = None # ManyButBackSlashContext
            self.c2 = None # ManyButBackSlashOrNewLineContext

        def CLIENTUSERINFOCHANGED(self):
            return self.getToken(EventsParser.CLIENTUSERINFOCHANGED, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def manyButBackSlash(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashContext,i)


        def manyButBackSlashOrNewLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButBackSlashOrNewLineContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButBackSlashOrNewLineContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_clientUserinfoChangedEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClientUserinfoChangedEvent" ):
                listener.enterClientUserinfoChangedEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClientUserinfoChangedEvent" ):
                listener.exitClientUserinfoChangedEvent(self)




    def clientUserinfoChangedEvent(self):

        localctx = EventsParser.ClientUserinfoChangedEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_clientUserinfoChangedEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(EventsParser.CLIENTUSERINFOCHANGED)
            self.state = 279
            self.match(EventsParser.COLON)
            self.state = 280
            self.match(EventsParser.WHITESPACE)
            self.state = 281
            localctx.a = self.intValue()
            self.state = 282
            self.match(EventsParser.WHITESPACE)
            localctx.value=ClientUserinfoChangedEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))

            self.state = 285
            localctx.b = self.manyButBackSlash()
            self.state = 286
            self.match(EventsParser.BACK_SLASH)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 287
                localctx.c = self.manyButBackSlashOrNewLine()


            localctx.value.parameters[(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))]=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EventsParser.BACK_SLASH:
                self.state = 292
                self.match(EventsParser.BACK_SLASH)
                self.state = 293
                localctx.b2 = self.manyButBackSlash()
                self.state = 294
                self.match(EventsParser.BACK_SLASH)
                self.state = 296
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 295
                    localctx.c2 = self.manyButBackSlashOrNewLine()


                localctx.value.parameters[(None if localctx.b2 is None else self._input.getText(localctx.b2.start,localctx.b2.stop))]=(None if localctx.c2 is None else self._input.getText(localctx.c2.start,localctx.c2.stop))
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccountValidatedEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # ManyButWhitespaceContext
            self.c = None # IntValueContext
            self.d = None # ManyButDoubleQuoteContext

        def ACCOUNTVALIDATED(self):
            return self.getToken(EventsParser.ACCOUNTVALIDATED, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.MINUS)
            else:
                return self.getToken(EventsParser.MINUS, i)

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.DOUBLE_QUOTE)
            else:
                return self.getToken(EventsParser.DOUBLE_QUOTE, i)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def manyButWhitespace(self):
            return self.getTypedRuleContext(EventsParser.ManyButWhitespaceContext,0)


        def manyButDoubleQuote(self):
            return self.getTypedRuleContext(EventsParser.ManyButDoubleQuoteContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_accountValidatedEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccountValidatedEvent" ):
                listener.enterAccountValidatedEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccountValidatedEvent" ):
                listener.exitAccountValidatedEvent(self)




    def accountValidatedEvent(self):

        localctx = EventsParser.AccountValidatedEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_accountValidatedEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(EventsParser.ACCOUNTVALIDATED)
            self.state = 306
            self.match(EventsParser.COLON)
            self.state = 307
            self.match(EventsParser.WHITESPACE)
            self.state = 308
            localctx.a = self.intValue()
            self.state = 309
            self.match(EventsParser.WHITESPACE)
            self.state = 310
            self.match(EventsParser.MINUS)
            self.state = 311
            self.match(EventsParser.WHITESPACE)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SEPARATOR) | (1 << EventsParser.INITGAME) | (1 << EventsParser.INITROUND) | (1 << EventsParser.INITAUTH) | (1 << EventsParser.SHUTDOWNGAME) | (1 << EventsParser.WARMUP) | (1 << EventsParser.SESSION_DATA_INITIALISED) | (1 << EventsParser.AT) | (1 << EventsParser.CLIENTCONNECT) | (1 << EventsParser.CLIENTDISCONNECT) | (1 << EventsParser.CLIENTBEGIN) | (1 << EventsParser.CLIENTSPAWN) | (1 << EventsParser.CLIENTUSERINFO) | (1 << EventsParser.CLIENTUSERINFOCHANGED) | (1 << EventsParser.ACCOUNTVALIDATED) | (1 << EventsParser.SAY) | (1 << EventsParser.SAYTELL) | (1 << EventsParser.SAYTEAM) | (1 << EventsParser.RADIO) | (1 << EventsParser.TELL) | (1 << EventsParser.KILL) | (1 << EventsParser.ITEM) | (1 << EventsParser.FLAG) | (1 << EventsParser.FLAGCAPTURETIME) | (1 << EventsParser.FLAGRETURN) | (1 << EventsParser.TO) | (1 << EventsParser.BY) | (1 << EventsParser.NEWLINE) | (1 << EventsParser.BACK_SLASH) | (1 << EventsParser.COLON) | (1 << EventsParser.MINUS) | (1 << EventsParser.DOUBLE_QUOTE) | (1 << EventsParser.DIGIT) | (1 << EventsParser.ANY_CHAR))) != 0):
                self.state = 312
                localctx.b = self.manyButWhitespace()


            self.state = 315
            self.match(EventsParser.WHITESPACE)
            self.state = 316
            self.match(EventsParser.MINUS)
            self.state = 317
            self.match(EventsParser.WHITESPACE)
            self.state = 318
            localctx.c = self.intValue()
            self.state = 319
            self.match(EventsParser.WHITESPACE)
            self.state = 320
            self.match(EventsParser.MINUS)
            self.state = 321
            self.match(EventsParser.WHITESPACE)
            self.state = 322
            self.match(EventsParser.DOUBLE_QUOTE)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SEPARATOR) | (1 << EventsParser.INITGAME) | (1 << EventsParser.INITROUND) | (1 << EventsParser.INITAUTH) | (1 << EventsParser.SHUTDOWNGAME) | (1 << EventsParser.WARMUP) | (1 << EventsParser.SESSION_DATA_INITIALISED) | (1 << EventsParser.AT) | (1 << EventsParser.CLIENTCONNECT) | (1 << EventsParser.CLIENTDISCONNECT) | (1 << EventsParser.CLIENTBEGIN) | (1 << EventsParser.CLIENTSPAWN) | (1 << EventsParser.CLIENTUSERINFO) | (1 << EventsParser.CLIENTUSERINFOCHANGED) | (1 << EventsParser.ACCOUNTVALIDATED) | (1 << EventsParser.SAY) | (1 << EventsParser.SAYTELL) | (1 << EventsParser.SAYTEAM) | (1 << EventsParser.RADIO) | (1 << EventsParser.TELL) | (1 << EventsParser.KILL) | (1 << EventsParser.ITEM) | (1 << EventsParser.FLAG) | (1 << EventsParser.FLAGCAPTURETIME) | (1 << EventsParser.FLAGRETURN) | (1 << EventsParser.TO) | (1 << EventsParser.BY) | (1 << EventsParser.WHITESPACE) | (1 << EventsParser.NEWLINE) | (1 << EventsParser.BACK_SLASH) | (1 << EventsParser.COLON) | (1 << EventsParser.MINUS) | (1 << EventsParser.DIGIT) | (1 << EventsParser.ANY_CHAR))) != 0):
                self.state = 323
                localctx.d = self.manyButDoubleQuote()


            self.state = 326
            self.match(EventsParser.DOUBLE_QUOTE)
            localctx.value=AccountValidatedEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.account=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
            localctx.value.level=int((None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop)))
            localctx.value.role=(None if localctx.d is None else self._input.getText(localctx.d.start,localctx.d.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SayEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # ManyButWhitespaceContext
            self.c = None # ManyButNewLineContext

        def SAY(self):
            return self.getToken(EventsParser.SAY, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def manyButWhitespace(self):
            return self.getTypedRuleContext(EventsParser.ManyButWhitespaceContext,0)


        def manyButNewLine(self):
            return self.getTypedRuleContext(EventsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_sayEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSayEvent" ):
                listener.enterSayEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSayEvent" ):
                listener.exitSayEvent(self)




    def sayEvent(self):

        localctx = EventsParser.SayEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sayEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(EventsParser.SAY)
            self.state = 334
            self.match(EventsParser.COLON)
            self.state = 335
            self.match(EventsParser.WHITESPACE)
            self.state = 336
            localctx.a = self.intValue()
            self.state = 337
            self.match(EventsParser.WHITESPACE)
            self.state = 338
            localctx.b = self.manyButWhitespace()
            self.state = 339
            self.match(EventsParser.WHITESPACE)
            self.state = 340
            localctx.c = self.manyButNewLine()
            localctx.value=SayEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.sender=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))[:-1]
            localctx.value.message=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SayTellEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # IntValueContext
            self.c = None # ManyButWhitespaceContext
            self.d = None # ManyButNewLineContext

        def SAYTELL(self):
            return self.getToken(EventsParser.SAYTELL, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def manyButWhitespace(self):
            return self.getTypedRuleContext(EventsParser.ManyButWhitespaceContext,0)


        def manyButNewLine(self):
            return self.getTypedRuleContext(EventsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_sayTellEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSayTellEvent" ):
                listener.enterSayTellEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSayTellEvent" ):
                listener.exitSayTellEvent(self)




    def sayTellEvent(self):

        localctx = EventsParser.SayTellEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_sayTellEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(EventsParser.SAYTELL)
            self.state = 347
            self.match(EventsParser.COLON)
            self.state = 348
            self.match(EventsParser.WHITESPACE)
            self.state = 349
            localctx.a = self.intValue()
            self.state = 350
            self.match(EventsParser.WHITESPACE)
            self.state = 351
            localctx.b = self.intValue()
            self.state = 352
            self.match(EventsParser.WHITESPACE)
            self.state = 353
            localctx.c = self.manyButWhitespace()
            self.state = 354
            self.match(EventsParser.WHITESPACE)
            self.state = 355
            localctx.d = self.manyButNewLine()
            localctx.value=SayTellEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.sender_slot=int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
            localctx.value.sender=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))[:-1]
            localctx.value.message=(None if localctx.d is None else self._input.getText(localctx.d.start,localctx.d.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SayTeamEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # ManyButWhitespaceContext
            self.c = None # ManyButNewLineContext

        def SAYTEAM(self):
            return self.getToken(EventsParser.SAYTEAM, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def manyButWhitespace(self):
            return self.getTypedRuleContext(EventsParser.ManyButWhitespaceContext,0)


        def manyButNewLine(self):
            return self.getTypedRuleContext(EventsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_sayTeamEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSayTeamEvent" ):
                listener.enterSayTeamEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSayTeamEvent" ):
                listener.exitSayTeamEvent(self)




    def sayTeamEvent(self):

        localctx = EventsParser.SayTeamEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sayTeamEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(EventsParser.SAYTEAM)
            self.state = 363
            self.match(EventsParser.COLON)
            self.state = 364
            self.match(EventsParser.WHITESPACE)
            self.state = 365
            localctx.a = self.intValue()
            self.state = 366
            self.match(EventsParser.WHITESPACE)
            self.state = 367
            localctx.b = self.manyButWhitespace()
            self.state = 368
            self.match(EventsParser.WHITESPACE)
            self.state = 369
            localctx.c = self.manyButNewLine()
            localctx.value=SayTeamEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.sender=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))[:-1]
            localctx.value.message=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TellEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # ManyButWhitespaceContext
            self.b = None # ManyButWhitespaceContext
            self.c = None # ManyButNewLineContext

        def TELL(self):
            return self.getToken(EventsParser.TELL, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def TO(self):
            return self.getToken(EventsParser.TO, 0)

        def manyButWhitespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButWhitespaceContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButWhitespaceContext,i)


        def manyButNewLine(self):
            return self.getTypedRuleContext(EventsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_tellEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTellEvent" ):
                listener.enterTellEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTellEvent" ):
                listener.exitTellEvent(self)




    def tellEvent(self):

        localctx = EventsParser.TellEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_tellEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(EventsParser.TELL)
            self.state = 376
            self.match(EventsParser.COLON)
            self.state = 377
            self.match(EventsParser.WHITESPACE)
            self.state = 378
            localctx.a = self.manyButWhitespace()
            self.state = 379
            self.match(EventsParser.WHITESPACE)
            self.state = 380
            self.match(EventsParser.TO)
            self.state = 381
            self.match(EventsParser.WHITESPACE)
            self.state = 382
            localctx.b = self.manyButWhitespace()
            self.state = 383
            self.match(EventsParser.WHITESPACE)
            self.state = 384
            localctx.c = self.manyButNewLine()
            localctx.value=TellEvent()
            localctx.value.sender=(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))
            localctx.value.target=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))[:-1]
            localctx.value.message=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RadioEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # IntValueContext
            self.c = None # IntValueContext
            self.d = None # ManyButDoubleQuoteContext
            self.e = None # ManyButDoubleQuoteContext

        def RADIO(self):
            return self.getToken(EventsParser.RADIO, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.MINUS)
            else:
                return self.getToken(EventsParser.MINUS, i)

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.DOUBLE_QUOTE)
            else:
                return self.getToken(EventsParser.DOUBLE_QUOTE, i)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def manyButDoubleQuote(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButDoubleQuoteContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButDoubleQuoteContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_radioEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRadioEvent" ):
                listener.enterRadioEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRadioEvent" ):
                listener.exitRadioEvent(self)




    def radioEvent(self):

        localctx = EventsParser.RadioEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_radioEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(EventsParser.RADIO)
            self.state = 391
            self.match(EventsParser.COLON)
            self.state = 392
            self.match(EventsParser.WHITESPACE)
            self.state = 393
            localctx.a = self.intValue()
            self.state = 394
            self.match(EventsParser.WHITESPACE)
            self.state = 395
            self.match(EventsParser.MINUS)
            self.state = 396
            self.match(EventsParser.WHITESPACE)
            self.state = 397
            localctx.b = self.intValue()
            self.state = 398
            self.match(EventsParser.WHITESPACE)
            self.state = 399
            self.match(EventsParser.MINUS)
            self.state = 400
            self.match(EventsParser.WHITESPACE)
            self.state = 401
            localctx.c = self.intValue()
            self.state = 402
            self.match(EventsParser.WHITESPACE)
            self.state = 403
            self.match(EventsParser.MINUS)
            self.state = 404
            self.match(EventsParser.WHITESPACE)
            self.state = 405
            self.match(EventsParser.DOUBLE_QUOTE)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SEPARATOR) | (1 << EventsParser.INITGAME) | (1 << EventsParser.INITROUND) | (1 << EventsParser.INITAUTH) | (1 << EventsParser.SHUTDOWNGAME) | (1 << EventsParser.WARMUP) | (1 << EventsParser.SESSION_DATA_INITIALISED) | (1 << EventsParser.AT) | (1 << EventsParser.CLIENTCONNECT) | (1 << EventsParser.CLIENTDISCONNECT) | (1 << EventsParser.CLIENTBEGIN) | (1 << EventsParser.CLIENTSPAWN) | (1 << EventsParser.CLIENTUSERINFO) | (1 << EventsParser.CLIENTUSERINFOCHANGED) | (1 << EventsParser.ACCOUNTVALIDATED) | (1 << EventsParser.SAY) | (1 << EventsParser.SAYTELL) | (1 << EventsParser.SAYTEAM) | (1 << EventsParser.RADIO) | (1 << EventsParser.TELL) | (1 << EventsParser.KILL) | (1 << EventsParser.ITEM) | (1 << EventsParser.FLAG) | (1 << EventsParser.FLAGCAPTURETIME) | (1 << EventsParser.FLAGRETURN) | (1 << EventsParser.TO) | (1 << EventsParser.BY) | (1 << EventsParser.WHITESPACE) | (1 << EventsParser.NEWLINE) | (1 << EventsParser.BACK_SLASH) | (1 << EventsParser.COLON) | (1 << EventsParser.MINUS) | (1 << EventsParser.DIGIT) | (1 << EventsParser.ANY_CHAR))) != 0):
                self.state = 406
                localctx.d = self.manyButDoubleQuote()


            self.state = 409
            self.match(EventsParser.DOUBLE_QUOTE)
            self.state = 410
            self.match(EventsParser.WHITESPACE)
            self.state = 411
            self.match(EventsParser.MINUS)
            self.state = 412
            self.match(EventsParser.WHITESPACE)
            self.state = 413
            self.match(EventsParser.DOUBLE_QUOTE)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SEPARATOR) | (1 << EventsParser.INITGAME) | (1 << EventsParser.INITROUND) | (1 << EventsParser.INITAUTH) | (1 << EventsParser.SHUTDOWNGAME) | (1 << EventsParser.WARMUP) | (1 << EventsParser.SESSION_DATA_INITIALISED) | (1 << EventsParser.AT) | (1 << EventsParser.CLIENTCONNECT) | (1 << EventsParser.CLIENTDISCONNECT) | (1 << EventsParser.CLIENTBEGIN) | (1 << EventsParser.CLIENTSPAWN) | (1 << EventsParser.CLIENTUSERINFO) | (1 << EventsParser.CLIENTUSERINFOCHANGED) | (1 << EventsParser.ACCOUNTVALIDATED) | (1 << EventsParser.SAY) | (1 << EventsParser.SAYTELL) | (1 << EventsParser.SAYTEAM) | (1 << EventsParser.RADIO) | (1 << EventsParser.TELL) | (1 << EventsParser.KILL) | (1 << EventsParser.ITEM) | (1 << EventsParser.FLAG) | (1 << EventsParser.FLAGCAPTURETIME) | (1 << EventsParser.FLAGRETURN) | (1 << EventsParser.TO) | (1 << EventsParser.BY) | (1 << EventsParser.WHITESPACE) | (1 << EventsParser.NEWLINE) | (1 << EventsParser.BACK_SLASH) | (1 << EventsParser.COLON) | (1 << EventsParser.MINUS) | (1 << EventsParser.DIGIT) | (1 << EventsParser.ANY_CHAR))) != 0):
                self.state = 414
                localctx.e = self.manyButDoubleQuote()


            self.state = 417
            self.match(EventsParser.DOUBLE_QUOTE)
            localctx.value=RadioEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.menu1=int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
            localctx.value.menu2=int((None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop)))
            localctx.value.location=(None if localctx.d is None else self._input.getText(localctx.d.start,localctx.d.stop))
            localctx.value.message=(None if localctx.e is None else self._input.getText(localctx.e.start,localctx.e.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KillEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # IntValueContext
            self.c = None # IntValueContext
            self.d = None # ManyButWhitespaceContext
            self.e = None # ManyButWhitespaceContext
            self.f = None # ManyButNewLineContext

        def KILL(self):
            return self.getToken(EventsParser.KILL, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.COLON)
            else:
                return self.getToken(EventsParser.COLON, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def manyButWhitespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.ManyButWhitespaceContext)
            else:
                return self.getTypedRuleContext(EventsParser.ManyButWhitespaceContext,i)


        def BY(self):
            return self.getToken(EventsParser.BY, 0)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def manyButNewLine(self):
            return self.getTypedRuleContext(EventsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_killEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKillEvent" ):
                listener.enterKillEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKillEvent" ):
                listener.exitKillEvent(self)




    def killEvent(self):

        localctx = EventsParser.KillEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_killEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(EventsParser.KILL)
            self.state = 426
            self.match(EventsParser.COLON)
            self.state = 427
            self.match(EventsParser.WHITESPACE)
            self.state = 428
            localctx.a = self.intValue()
            self.state = 429
            self.match(EventsParser.WHITESPACE)
            self.state = 430
            localctx.b = self.intValue()
            self.state = 431
            self.match(EventsParser.WHITESPACE)
            self.state = 432
            localctx.c = self.intValue()
            self.state = 433
            self.match(EventsParser.COLON)
            self.state = 434
            self.match(EventsParser.WHITESPACE)
            self.state = 435
            localctx.d = self.manyButWhitespace()
            self.state = 436
            self.match(EventsParser.WHITESPACE)
            self.state = 437
            self.manyButWhitespace()
            self.state = 438
            self.match(EventsParser.WHITESPACE)
            self.state = 439
            localctx.e = self.manyButWhitespace()
            self.state = 440
            self.match(EventsParser.WHITESPACE)
            self.state = 441
            self.match(EventsParser.BY)
            self.state = 442
            self.match(EventsParser.WHITESPACE)
            self.state = 443
            localctx.f = self.manyButNewLine()
            localctx.value=KillEvent()
            localctx.value.x=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.y=int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
            localctx.value.z=int((None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop)))
            localctx.value.killer=(None if localctx.d is None else self._input.getText(localctx.d.start,localctx.d.stop))
            localctx.value.killed=(None if localctx.e is None else self._input.getText(localctx.e.start,localctx.e.stop))
            localctx.value.how=(None if localctx.f is None else self._input.getText(localctx.f.start,localctx.f.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # ManyButNewLineContext

        def ITEM(self):
            return self.getToken(EventsParser.ITEM, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def manyButNewLine(self):
            return self.getTypedRuleContext(EventsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_itemEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemEvent" ):
                listener.enterItemEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemEvent" ):
                listener.exitItemEvent(self)




    def itemEvent(self):

        localctx = EventsParser.ItemEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_itemEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(EventsParser.ITEM)
            self.state = 453
            self.match(EventsParser.COLON)
            self.state = 454
            self.match(EventsParser.WHITESPACE)
            self.state = 455
            localctx.a = self.intValue()
            self.state = 456
            self.match(EventsParser.WHITESPACE)
            self.state = 457
            localctx.b = self.manyButNewLine()
            localctx.value=ItemEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.item=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # IntValueContext
            self.c = None # ManyButNewLineContext

        def FLAG(self):
            return self.getToken(EventsParser.FLAG, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.COLON)
            else:
                return self.getToken(EventsParser.COLON, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def manyButNewLine(self):
            return self.getTypedRuleContext(EventsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_flagEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagEvent" ):
                listener.enterFlagEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagEvent" ):
                listener.exitFlagEvent(self)




    def flagEvent(self):

        localctx = EventsParser.FlagEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_flagEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(EventsParser.FLAG)
            self.state = 463
            self.match(EventsParser.COLON)
            self.state = 464
            self.match(EventsParser.WHITESPACE)
            self.state = 465
            localctx.a = self.intValue()
            self.state = 466
            self.match(EventsParser.WHITESPACE)
            self.state = 467
            localctx.b = self.intValue()
            self.state = 468
            self.match(EventsParser.COLON)
            self.state = 469
            self.match(EventsParser.WHITESPACE)
            self.state = 470
            localctx.c = self.manyButNewLine()
            localctx.value=FlagEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.num=int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
            localctx.value.item=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagCaptureTimeEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # IntValueContext
            self.b = None # IntValueContext

        def FLAGCAPTURETIME(self):
            return self.getToken(EventsParser.FLAGCAPTURETIME, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.COLON)
            else:
                return self.getToken(EventsParser.COLON, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def getRuleIndex(self):
            return EventsParser.RULE_flagCaptureTimeEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagCaptureTimeEvent" ):
                listener.enterFlagCaptureTimeEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagCaptureTimeEvent" ):
                listener.exitFlagCaptureTimeEvent(self)




    def flagCaptureTimeEvent(self):

        localctx = EventsParser.FlagCaptureTimeEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_flagCaptureTimeEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(EventsParser.FLAGCAPTURETIME)
            self.state = 477
            self.match(EventsParser.COLON)
            self.state = 478
            self.match(EventsParser.WHITESPACE)
            self.state = 479
            localctx.a = self.intValue()
            self.state = 480
            self.match(EventsParser.COLON)
            self.state = 481
            self.match(EventsParser.WHITESPACE)
            self.state = 482
            localctx.b = self.intValue()
            localctx.value=FlagCaptureTimeEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.time=int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagReturnEventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.a = None # ManyButNewLineContext

        def FLAGRETURN(self):
            return self.getToken(EventsParser.FLAGRETURN, 0)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def manyButNewLine(self):
            return self.getTypedRuleContext(EventsParser.ManyButNewLineContext,0)


        def getRuleIndex(self):
            return EventsParser.RULE_flagReturnEvent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagReturnEvent" ):
                listener.enterFlagReturnEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagReturnEvent" ):
                listener.exitFlagReturnEvent(self)




    def flagReturnEvent(self):

        localctx = EventsParser.FlagReturnEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_flagReturnEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(EventsParser.FLAGRETURN)
            self.state = 488
            self.match(EventsParser.COLON)
            self.state = 489
            self.match(EventsParser.WHITESPACE)
            self.state = 490
            localctx.a = self.manyButNewLine()
            localctx.value=FlagReturnEvent()
            localctx.value.flag=(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(EventsParser.MINUS, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.DIGIT)
            else:
                return self.getToken(EventsParser.DIGIT, i)

        def getRuleIndex(self):
            return EventsParser.RULE_intValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntValue" ):
                listener.enterIntValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntValue" ):
                listener.exitIntValue(self)




    def intValue(self):

        localctx = EventsParser.IntValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_intValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EventsParser.MINUS:
                self.state = 494
                self.match(EventsParser.MINUS)


            self.state = 498 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 497
                    self.match(EventsParser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 500 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyButNewLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.NEWLINE)
            else:
                return self.getToken(EventsParser.NEWLINE, i)

        def getRuleIndex(self):
            return EventsParser.RULE_manyButNewLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManyButNewLine" ):
                listener.enterManyButNewLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManyButNewLine" ):
                listener.exitManyButNewLine(self)




    def manyButNewLine(self):

        localctx = EventsParser.ManyButNewLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_manyButNewLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 502
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==EventsParser.NEWLINE:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 505 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyButWhitespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return EventsParser.RULE_manyButWhitespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManyButWhitespace" ):
                listener.enterManyButWhitespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManyButWhitespace" ):
                listener.exitManyButWhitespace(self)




    def manyButWhitespace(self):

        localctx = EventsParser.ManyButWhitespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_manyButWhitespace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 507
                _la = self._input.LA(1)
                if _la <= 0 or _la==EventsParser.WHITESPACE:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 510 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SEPARATOR) | (1 << EventsParser.INITGAME) | (1 << EventsParser.INITROUND) | (1 << EventsParser.INITAUTH) | (1 << EventsParser.SHUTDOWNGAME) | (1 << EventsParser.WARMUP) | (1 << EventsParser.SESSION_DATA_INITIALISED) | (1 << EventsParser.AT) | (1 << EventsParser.CLIENTCONNECT) | (1 << EventsParser.CLIENTDISCONNECT) | (1 << EventsParser.CLIENTBEGIN) | (1 << EventsParser.CLIENTSPAWN) | (1 << EventsParser.CLIENTUSERINFO) | (1 << EventsParser.CLIENTUSERINFOCHANGED) | (1 << EventsParser.ACCOUNTVALIDATED) | (1 << EventsParser.SAY) | (1 << EventsParser.SAYTELL) | (1 << EventsParser.SAYTEAM) | (1 << EventsParser.RADIO) | (1 << EventsParser.TELL) | (1 << EventsParser.KILL) | (1 << EventsParser.ITEM) | (1 << EventsParser.FLAG) | (1 << EventsParser.FLAGCAPTURETIME) | (1 << EventsParser.FLAGRETURN) | (1 << EventsParser.TO) | (1 << EventsParser.BY) | (1 << EventsParser.NEWLINE) | (1 << EventsParser.BACK_SLASH) | (1 << EventsParser.COLON) | (1 << EventsParser.MINUS) | (1 << EventsParser.DOUBLE_QUOTE) | (1 << EventsParser.DIGIT) | (1 << EventsParser.ANY_CHAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyButBackSlashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def getRuleIndex(self):
            return EventsParser.RULE_manyButBackSlash

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManyButBackSlash" ):
                listener.enterManyButBackSlash(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManyButBackSlash" ):
                listener.exitManyButBackSlash(self)




    def manyButBackSlash(self):

        localctx = EventsParser.ManyButBackSlashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_manyButBackSlash)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 512
                _la = self._input.LA(1)
                if _la <= 0 or _la==EventsParser.BACK_SLASH:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 515 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SEPARATOR) | (1 << EventsParser.INITGAME) | (1 << EventsParser.INITROUND) | (1 << EventsParser.INITAUTH) | (1 << EventsParser.SHUTDOWNGAME) | (1 << EventsParser.WARMUP) | (1 << EventsParser.SESSION_DATA_INITIALISED) | (1 << EventsParser.AT) | (1 << EventsParser.CLIENTCONNECT) | (1 << EventsParser.CLIENTDISCONNECT) | (1 << EventsParser.CLIENTBEGIN) | (1 << EventsParser.CLIENTSPAWN) | (1 << EventsParser.CLIENTUSERINFO) | (1 << EventsParser.CLIENTUSERINFOCHANGED) | (1 << EventsParser.ACCOUNTVALIDATED) | (1 << EventsParser.SAY) | (1 << EventsParser.SAYTELL) | (1 << EventsParser.SAYTEAM) | (1 << EventsParser.RADIO) | (1 << EventsParser.TELL) | (1 << EventsParser.KILL) | (1 << EventsParser.ITEM) | (1 << EventsParser.FLAG) | (1 << EventsParser.FLAGCAPTURETIME) | (1 << EventsParser.FLAGRETURN) | (1 << EventsParser.TO) | (1 << EventsParser.BY) | (1 << EventsParser.WHITESPACE) | (1 << EventsParser.NEWLINE) | (1 << EventsParser.COLON) | (1 << EventsParser.MINUS) | (1 << EventsParser.DOUBLE_QUOTE) | (1 << EventsParser.DIGIT) | (1 << EventsParser.ANY_CHAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyButBackSlashOrNewLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.NEWLINE)
            else:
                return self.getToken(EventsParser.NEWLINE, i)

        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def getRuleIndex(self):
            return EventsParser.RULE_manyButBackSlashOrNewLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManyButBackSlashOrNewLine" ):
                listener.enterManyButBackSlashOrNewLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManyButBackSlashOrNewLine" ):
                listener.exitManyButBackSlashOrNewLine(self)




    def manyButBackSlashOrNewLine(self):

        localctx = EventsParser.ManyButBackSlashOrNewLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_manyButBackSlashOrNewLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 517
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==EventsParser.NEWLINE or _la==EventsParser.BACK_SLASH:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 520 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyButDoubleQuoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.DOUBLE_QUOTE)
            else:
                return self.getToken(EventsParser.DOUBLE_QUOTE, i)

        def getRuleIndex(self):
            return EventsParser.RULE_manyButDoubleQuote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManyButDoubleQuote" ):
                listener.enterManyButDoubleQuote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManyButDoubleQuote" ):
                listener.exitManyButDoubleQuote(self)




    def manyButDoubleQuote(self):

        localctx = EventsParser.ManyButDoubleQuoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_manyButDoubleQuote)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 522
                _la = self._input.LA(1)
                if _la <= 0 or _la==EventsParser.DOUBLE_QUOTE:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 525 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SEPARATOR) | (1 << EventsParser.INITGAME) | (1 << EventsParser.INITROUND) | (1 << EventsParser.INITAUTH) | (1 << EventsParser.SHUTDOWNGAME) | (1 << EventsParser.WARMUP) | (1 << EventsParser.SESSION_DATA_INITIALISED) | (1 << EventsParser.AT) | (1 << EventsParser.CLIENTCONNECT) | (1 << EventsParser.CLIENTDISCONNECT) | (1 << EventsParser.CLIENTBEGIN) | (1 << EventsParser.CLIENTSPAWN) | (1 << EventsParser.CLIENTUSERINFO) | (1 << EventsParser.CLIENTUSERINFOCHANGED) | (1 << EventsParser.ACCOUNTVALIDATED) | (1 << EventsParser.SAY) | (1 << EventsParser.SAYTELL) | (1 << EventsParser.SAYTEAM) | (1 << EventsParser.RADIO) | (1 << EventsParser.TELL) | (1 << EventsParser.KILL) | (1 << EventsParser.ITEM) | (1 << EventsParser.FLAG) | (1 << EventsParser.FLAGCAPTURETIME) | (1 << EventsParser.FLAGRETURN) | (1 << EventsParser.TO) | (1 << EventsParser.BY) | (1 << EventsParser.WHITESPACE) | (1 << EventsParser.NEWLINE) | (1 << EventsParser.BACK_SLASH) | (1 << EventsParser.COLON) | (1 << EventsParser.MINUS) | (1 << EventsParser.DIGIT) | (1 << EventsParser.ANY_CHAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





