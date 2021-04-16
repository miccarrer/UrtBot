# Generated from events_parser\Events.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

from events import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("\u01af\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\5")
        buf.write("\2=\n\2\7\2?\n\2\f\2\16\2B\13\2\3\3\7\3E\n\3\f\3\16\3")
        buf.write("H\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u0090\n\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\6\5\u00a1\n\5\r\5")
        buf.write("\16\5\u00a2\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\6\6\u00ae")
        buf.write("\n\6\r\6\16\6\u00af\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\6\7\u00bb\n\7\r\7\16\7\u00bc\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\6\17\u00f4\n\17\r\17\16\17\u00f5\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00ff\n\20\3\20\3\20\3\20\5\20\u0104")
        buf.write("\n\20\3\20\3\20\6\20\u0108\n\20\r\20\16\20\u0109\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u0117\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u0123\n\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\5\32\u019d\n\32\3\32\6\32\u01a0\n")
        buf.write("\32\r\32\16\32\u01a1\3\33\6\33\u01a5\n\33\r\33\16\33\u01a6")
        buf.write("\3\34\3\34\6\34\u01ab\n\34\r\34\16\34\u01ac\3\34\2\2\35")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\66\2\3\5\2\32#%(+,\2\u01b9\28\3\2\2\2\4F\3\2\2\2\6")
        buf.write("\u0094\3\2\2\2\b\u0097\3\2\2\2\n\u00a4\3\2\2\2\f\u00b1")
        buf.write("\3\2\2\2\16\u00be\3\2\2\2\20\u00c1\3\2\2\2\22\u00c4\3")
        buf.write("\2\2\2\24\u00cf\3\2\2\2\26\u00d5\3\2\2\2\30\u00db\3\2")
        buf.write("\2\2\32\u00e1\3\2\2\2\34\u00e7\3\2\2\2\36\u00f7\3\2\2")
        buf.write("\2 \u010b\3\2\2\2\"\u0128\3\2\2\2$\u0135\3\2\2\2&\u0145")
        buf.write("\3\2\2\2(\u0152\3\2\2\2*\u0161\3\2\2\2,\u017b\3\2\2\2")
        buf.write(".\u0184\3\2\2\2\60\u0191\3\2\2\2\62\u019c\3\2\2\2\64\u01a4")
        buf.write("\3\2\2\2\66\u01aa\3\2\2\28@\b\2\1\29:\5\4\3\2:<\b\2\1")
        buf.write("\2;=\7*\2\2<;\3\2\2\2<=\3\2\2\2=?\3\2\2\2>9\3\2\2\2?B")
        buf.write("\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\3\3\2\2\2B@\3\2\2\2CE\7")
        buf.write(")\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2")
        buf.write("\2HF\3\2\2\2IJ\5\62\32\2JK\7\36\2\2KL\5\62\32\2L\u008f")
        buf.write("\7)\2\2MN\5\6\4\2NO\b\3\1\2O\u0090\3\2\2\2PQ\5\b\5\2Q")
        buf.write("R\b\3\1\2R\u0090\3\2\2\2ST\5\n\6\2TU\b\3\1\2U\u0090\3")
        buf.write("\2\2\2VW\5\f\7\2WX\b\3\1\2X\u0090\3\2\2\2YZ\5\16\b\2Z")
        buf.write("[\b\3\1\2[\u0090\3\2\2\2\\]\5\20\t\2]^\b\3\1\2^\u0090")
        buf.write("\3\2\2\2_`\5\22\n\2`a\b\3\1\2a\u0090\3\2\2\2bc\5\24\13")
        buf.write("\2cd\b\3\1\2d\u0090\3\2\2\2ef\5\26\f\2fg\b\3\1\2g\u0090")
        buf.write("\3\2\2\2hi\5\30\r\2ij\b\3\1\2j\u0090\3\2\2\2kl\5\32\16")
        buf.write("\2lm\b\3\1\2m\u0090\3\2\2\2no\5\34\17\2op\b\3\1\2p\u0090")
        buf.write("\3\2\2\2qr\5\36\20\2rs\b\3\1\2s\u0090\3\2\2\2tu\5 \21")
        buf.write("\2uv\b\3\1\2v\u0090\3\2\2\2wx\5\"\22\2xy\b\3\1\2y\u0090")
        buf.write("\3\2\2\2z{\5$\23\2{|\b\3\1\2|\u0090\3\2\2\2}~\5&\24\2")
        buf.write("~\177\b\3\1\2\177\u0090\3\2\2\2\u0080\u0081\5(\25\2\u0081")
        buf.write("\u0082\b\3\1\2\u0082\u0090\3\2\2\2\u0083\u0084\5*\26\2")
        buf.write("\u0084\u0085\b\3\1\2\u0085\u0090\3\2\2\2\u0086\u0087\5")
        buf.write(",\27\2\u0087\u0088\b\3\1\2\u0088\u0090\3\2\2\2\u0089\u008a")
        buf.write("\5.\30\2\u008a\u008b\b\3\1\2\u008b\u0090\3\2\2\2\u008c")
        buf.write("\u008d\5\60\31\2\u008d\u008e\b\3\1\2\u008e\u0090\3\2\2")
        buf.write("\2\u008fM\3\2\2\2\u008fP\3\2\2\2\u008fS\3\2\2\2\u008f")
        buf.write("V\3\2\2\2\u008fY\3\2\2\2\u008f\\\3\2\2\2\u008f_\3\2\2")
        buf.write("\2\u008fb\3\2\2\2\u008fe\3\2\2\2\u008fh\3\2\2\2\u008f")
        buf.write("k\3\2\2\2\u008fn\3\2\2\2\u008fq\3\2\2\2\u008ft\3\2\2\2")
        buf.write("\u008fw\3\2\2\2\u008fz\3\2\2\2\u008f}\3\2\2\2\u008f\u0080")
        buf.write("\3\2\2\2\u008f\u0083\3\2\2\2\u008f\u0086\3\2\2\2\u008f")
        buf.write("\u0089\3\2\2\2\u008f\u008c\3\2\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\u0092\b\3\1\2\u0092\u0093\b\3\1\2\u0093\5\3\2\2")
        buf.write("\2\u0094\u0095\7\3\2\2\u0095\u0096\b\4\1\2\u0096\7\3\2")
        buf.write("\2\2\u0097\u0098\7\4\2\2\u0098\u0099\7)\2\2\u0099\u00a0")
        buf.write("\b\5\1\2\u009a\u009b\7\31\2\2\u009b\u009c\5\64\33\2\u009c")
        buf.write("\u009d\7\31\2\2\u009d\u009e\5\66\34\2\u009e\u009f\b\5")
        buf.write("\1\2\u009f\u00a1\3\2\2\2\u00a0\u009a\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\t\3\2\2\2\u00a4\u00a5\7\5\2\2\u00a5\u00a6\7)\2\2\u00a6")
        buf.write("\u00ad\b\6\1\2\u00a7\u00a8\7\31\2\2\u00a8\u00a9\5\64\33")
        buf.write("\2\u00a9\u00aa\7\31\2\2\u00aa\u00ab\5\66\34\2\u00ab\u00ac")
        buf.write("\b\6\1\2\u00ac\u00ae\3\2\2\2\u00ad\u00a7\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\13\3\2\2\2\u00b1\u00b2\7\6\2\2\u00b2\u00b3\7)\2")
        buf.write("\2\u00b3\u00ba\b\7\1\2\u00b4\u00b5\7\31\2\2\u00b5\u00b6")
        buf.write("\5\64\33\2\u00b6\u00b7\7\31\2\2\u00b7\u00b8\5\66\34\2")
        buf.write("\u00b8\u00b9\b\7\1\2\u00b9\u00bb\3\2\2\2\u00ba\u00b4\3")
        buf.write("\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd")
        buf.write("\3\2\2\2\u00bd\r\3\2\2\2\u00be\u00bf\7\7\2\2\u00bf\u00c0")
        buf.write("\b\b\1\2\u00c0\17\3\2\2\2\u00c1\u00c2\7\b\2\2\u00c2\u00c3")
        buf.write("\b\t\1\2\u00c3\21\3\2\2\2\u00c4\u00c5\7\t\2\2\u00c5\u00c6")
        buf.write("\7)\2\2\u00c6\u00c7\5\62\32\2\u00c7\u00c8\7)\2\2\u00c8")
        buf.write("\u00c9\5\64\33\2\u00c9\u00ca\7)\2\2\u00ca\u00cb\5\62\32")
        buf.write("\2\u00cb\u00cc\b\n\1\2\u00cc\u00cd\b\n\1\2\u00cd\u00ce")
        buf.write("\b\n\1\2\u00ce\23\3\2\2\2\u00cf\u00d0\7\n\2\2\u00d0\u00d1")
        buf.write("\7)\2\2\u00d1\u00d2\5\62\32\2\u00d2\u00d3\b\13\1\2\u00d3")
        buf.write("\u00d4\b\13\1\2\u00d4\25\3\2\2\2\u00d5\u00d6\7\13\2\2")
        buf.write("\u00d6\u00d7\7)\2\2\u00d7\u00d8\5\62\32\2\u00d8\u00d9")
        buf.write("\b\f\1\2\u00d9\u00da\b\f\1\2\u00da\27\3\2\2\2\u00db\u00dc")
        buf.write("\7\f\2\2\u00dc\u00dd\7)\2\2\u00dd\u00de\5\62\32\2\u00de")
        buf.write("\u00df\b\r\1\2\u00df\u00e0\b\r\1\2\u00e0\31\3\2\2\2\u00e1")
        buf.write("\u00e2\7\r\2\2\u00e2\u00e3\7)\2\2\u00e3\u00e4\5\62\32")
        buf.write("\2\u00e4\u00e5\b\16\1\2\u00e5\u00e6\b\16\1\2\u00e6\33")
        buf.write("\3\2\2\2\u00e7\u00e8\7\16\2\2\u00e8\u00e9\7)\2\2\u00e9")
        buf.write("\u00ea\5\62\32\2\u00ea\u00eb\7)\2\2\u00eb\u00ec\b\17\1")
        buf.write("\2\u00ec\u00f3\b\17\1\2\u00ed\u00ee\7\31\2\2\u00ee\u00ef")
        buf.write("\5\64\33\2\u00ef\u00f0\7\31\2\2\u00f0\u00f1\5\66\34\2")
        buf.write("\u00f1\u00f2\b\17\1\2\u00f2\u00f4\3\2\2\2\u00f3\u00ed")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\35\3\2\2\2\u00f7\u00f8\7\17\2\2\u00f8")
        buf.write("\u00f9\7)\2\2\u00f9\u00fa\5\62\32\2\u00fa\u00fb\7)\2\2")
        buf.write("\u00fb\u00fc\b\20\1\2\u00fc\u0107\b\20\1\2\u00fd\u00ff")
        buf.write("\7\31\2\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100\u0101\5\64\33\2\u0101\u0103\7\31")
        buf.write("\2\2\u0102\u0104\5\66\34\2\u0103\u0102\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\b\20\1\2\u0106")
        buf.write("\u0108\3\2\2\2\u0107\u00fe\3\2\2\2\u0108\u0109\3\2\2\2")
        buf.write("\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\37\3\2")
        buf.write("\2\2\u010b\u010c\b\21\1\2\u010c\u010d\7\20\2\2\u010d\u010e")
        buf.write("\7)\2\2\u010e\u010f\5\62\32\2\u010f\u0110\7)\2\2\u0110")
        buf.write("\u0111\7\"\2\2\u0111\u0116\7)\2\2\u0112\u0113\5\64\33")
        buf.write("\2\u0113\u0114\b\21\1\2\u0114\u0115\7)\2\2\u0115\u0117")
        buf.write("\3\2\2\2\u0116\u0112\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u0119\7\"\2\2\u0119\u011a\7)\2\2")
        buf.write("\u011a\u011b\5\62\32\2\u011b\u011c\7)\2\2\u011c\u011d")
        buf.write("\7\"\2\2\u011d\u011e\7)\2\2\u011e\u0122\7$\2\2\u011f\u0120")
        buf.write("\5\64\33\2\u0120\u0121\b\21\1\2\u0121\u0123\3\2\2\2\u0122")
        buf.write("\u011f\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2")
        buf.write("\u0124\u0125\7$\2\2\u0125\u0126\b\21\1\2\u0126\u0127\b")
        buf.write("\21\1\2\u0127!\3\2\2\2\u0128\u0129\7\21\2\2\u0129\u012a")
        buf.write("\7)\2\2\u012a\u012b\5\62\32\2\u012b\u012c\7)\2\2\u012c")
        buf.write("\u012d\5\64\33\2\u012d\u012e\7\36\2\2\u012e\u012f\7)\2")
        buf.write("\2\u012f\u0130\5\66\34\2\u0130\u0131\b\22\1\2\u0131\u0132")
        buf.write("\b\22\1\2\u0132\u0133\b\22\1\2\u0133\u0134\b\22\1\2\u0134")
        buf.write("#\3\2\2\2\u0135\u0136\7\22\2\2\u0136\u0137\7)\2\2\u0137")
        buf.write("\u0138\5\62\32\2\u0138\u0139\7)\2\2\u0139\u013a\5\62\32")
        buf.write("\2\u013a\u013b\7)\2\2\u013b\u013c\5\64\33\2\u013c\u013d")
        buf.write("\7\36\2\2\u013d\u013e\7)\2\2\u013e\u013f\5\66\34\2\u013f")
        buf.write("\u0140\b\23\1\2\u0140\u0141\b\23\1\2\u0141\u0142\b\23")
        buf.write("\1\2\u0142\u0143\b\23\1\2\u0143\u0144\b\23\1\2\u0144%")
        buf.write("\3\2\2\2\u0145\u0146\7\22\2\2\u0146\u0147\7)\2\2\u0147")
        buf.write("\u0148\5\62\32\2\u0148\u0149\7)\2\2\u0149\u014a\5\64\33")
        buf.write("\2\u014a\u014b\7\36\2\2\u014b\u014c\7)\2\2\u014c\u014d")
        buf.write("\5\66\34\2\u014d\u014e\b\24\1\2\u014e\u014f\b\24\1\2\u014f")
        buf.write("\u0150\b\24\1\2\u0150\u0151\b\24\1\2\u0151\'\3\2\2\2\u0152")
        buf.write("\u0153\7\24\2\2\u0153\u0154\7)\2\2\u0154\u0155\5\64\33")
        buf.write("\2\u0155\u0156\7)\2\2\u0156\u0157\5\64\33\2\u0157\u0158")
        buf.write("\7)\2\2\u0158\u0159\5\64\33\2\u0159\u015a\7\36\2\2\u015a")
        buf.write("\u015b\7)\2\2\u015b\u015c\5\66\34\2\u015c\u015d\b\25\1")
        buf.write("\2\u015d\u015e\b\25\1\2\u015e\u015f\b\25\1\2\u015f\u0160")
        buf.write("\b\25\1\2\u0160)\3\2\2\2\u0161\u0162\7\25\2\2\u0162\u0163")
        buf.write("\7)\2\2\u0163\u0164\5\62\32\2\u0164\u0165\7)\2\2\u0165")
        buf.write("\u0166\5\62\32\2\u0166\u0167\7)\2\2\u0167\u0168\5\62\32")
        buf.write("\2\u0168\u0169\7\36\2\2\u0169\u016a\7)\2\2\u016a\u016b")
        buf.write("\5\64\33\2\u016b\u016c\7)\2\2\u016c\u016d\5\64\33\2\u016d")
        buf.write("\u016e\7)\2\2\u016e\u016f\5\64\33\2\u016f\u0170\7)\2\2")
        buf.write("\u0170\u0171\5\64\33\2\u0171\u0172\7)\2\2\u0172\u0173")
        buf.write("\5\64\33\2\u0173\u0174\b\26\1\2\u0174\u0175\b\26\1\2\u0175")
        buf.write("\u0176\b\26\1\2\u0176\u0177\b\26\1\2\u0177\u0178\b\26")
        buf.write("\1\2\u0178\u0179\b\26\1\2\u0179\u017a\b\26\1\2\u017a+")
        buf.write("\3\2\2\2\u017b\u017c\7\26\2\2\u017c\u017d\7)\2\2\u017d")
        buf.write("\u017e\5\62\32\2\u017e\u017f\7)\2\2\u017f\u0180\5\64\33")
        buf.write("\2\u0180\u0181\b\27\1\2\u0181\u0182\b\27\1\2\u0182\u0183")
        buf.write("\b\27\1\2\u0183-\3\2\2\2\u0184\u0185\7\27\2\2\u0185\u0186")
        buf.write("\7)\2\2\u0186\u0187\5\62\32\2\u0187\u0188\7)\2\2\u0188")
        buf.write("\u0189\5\62\32\2\u0189\u018a\7\36\2\2\u018a\u018b\7)\2")
        buf.write("\2\u018b\u018c\5\64\33\2\u018c\u018d\b\30\1\2\u018d\u018e")
        buf.write("\b\30\1\2\u018e\u018f\b\30\1\2\u018f\u0190\b\30\1\2\u0190")
        buf.write("/\3\2\2\2\u0191\u0192\7\30\2\2\u0192\u0193\7)\2\2\u0193")
        buf.write("\u0194\5\62\32\2\u0194\u0195\7\36\2\2\u0195\u0196\7)\2")
        buf.write("\2\u0196\u0197\5\62\32\2\u0197\u0198\b\31\1\2\u0198\u0199")
        buf.write("\b\31\1\2\u0199\u019a\b\31\1\2\u019a\61\3\2\2\2\u019b")
        buf.write("\u019d\7\"\2\2\u019c\u019b\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019d\u019f\3\2\2\2\u019e\u01a0\7,\2\2\u019f\u019e\3")
        buf.write("\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\63\3\2\2\2\u01a3\u01a5\t\2\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\65\3\2\2\2\u01a8\u01ab\5\64\33\2")
        buf.write("\u01a9\u01ab\7)\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3")
        buf.write("\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad")
        buf.write("\3\2\2\2\u01ad\67\3\2\2\2\24<@F\u008f\u00a2\u00af\u00bc")
        buf.write("\u00f5\u00fe\u0103\u0109\u0116\u0122\u019c\u01a1\u01a6")
        buf.write("\u01aa\u01ac")
        return buf.getvalue()


class EventsParser ( Parser ):

    grammarFileName = "Events.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'------------------------------------------------------------'", 
                     "'InitGame:'", "'InitRound:'", "'InitAuth:'", "'ShutdownGame:'", 
                     "'Warmup:'", "'Session data initialised for client on slot'", 
                     "'ClientConnect:'", "'ClientDisconnect:'", "'ClientBegin:'", 
                     "'ClientSpawn:'", "'ClientUserinfo:'", "'ClientUserinfoChanged:'", 
                     "'AccountValidated:'", "'say:'", "'saytell:'", "'sayteam:'", 
                     "'tell:'", "'Kill:'", "'Item:'", "'Flag:'", "'FlagCaptureTime:'", 
                     "'\\'", "'/'", "','", "'<'", "'>'", "':'", "';'", "'.'", 
                     "'_'", "'-'", "'+'", "'\"'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "SEPARATOR", "INITGAME", "INITROUND", 
                      "INITAUTH", "SHUTDOWNGAME", "WARMUP", "SESSION_DATA_INITIALISED", 
                      "CLIENTCONNECT", "CLIENTDISCONNECT", "CLIENTBEGIN", 
                      "CLIENTSPAWN", "CLIENTUSERINFO", "CLIENTUSERINFOCHANGED", 
                      "ACCOUNTVALIDATED", "SAY", "SAYTELL", "SAYTEAM", "TELL", 
                      "KILL", "ITEM", "FLAG", "FLAGCAPTURETIME", "BACK_SLASH", 
                      "SLASH", "COMMA", "INFERIOR", "SUPERIOR", "COLON", 
                      "SEMICOLON", "DOT", "UNDERSCORE", "MINUS", "PLUS", 
                      "DOUBLE_QUOTE", "ROUND_BRACKET_LEFT", "ROUND_BRACKET_RIGHT", 
                      "SQUARE_BRACKET_LEFT", "SQUARE_BRACKET_RIGHT", "WHITESPACE", 
                      "NEWLINE", "LETTER", "DIGIT" ]

    RULE_events = 0
    RULE_event = 1
    RULE_separatorEvent = 2
    RULE_initGameEvent = 3
    RULE_initRoundEvent = 4
    RULE_initAuthEvent = 5
    RULE_shutdownGameEvent = 6
    RULE_warmupEvent = 7
    RULE_sessionDataInitEvent = 8
    RULE_clientConnectEvent = 9
    RULE_clientDisconnectEvent = 10
    RULE_clientBeginEvent = 11
    RULE_clientSpawnEvent = 12
    RULE_clientUserinfoEvent = 13
    RULE_clientUserinfoChangedEvent = 14
    RULE_accountValidatedEvent = 15
    RULE_sayEvent = 16
    RULE_sayTellEvent = 17
    RULE_sayTeamEvent = 18
    RULE_tellEvent = 19
    RULE_killEvent = 20
    RULE_itemEvent = 21
    RULE_flagEvent = 22
    RULE_flagCaptureTimeEvent = 23
    RULE_intValue = 24
    RULE_wordValue = 25
    RULE_sentenceValue = 26

    ruleNames =  [ "events", "event", "separatorEvent", "initGameEvent", 
                   "initRoundEvent", "initAuthEvent", "shutdownGameEvent", 
                   "warmupEvent", "sessionDataInitEvent", "clientConnectEvent", 
                   "clientDisconnectEvent", "clientBeginEvent", "clientSpawnEvent", 
                   "clientUserinfoEvent", "clientUserinfoChangedEvent", 
                   "accountValidatedEvent", "sayEvent", "sayTellEvent", 
                   "sayTeamEvent", "tellEvent", "killEvent", "itemEvent", 
                   "flagEvent", "flagCaptureTimeEvent", "intValue", "wordValue", 
                   "sentenceValue" ]

    EOF = Token.EOF
    SEPARATOR=1
    INITGAME=2
    INITROUND=3
    INITAUTH=4
    SHUTDOWNGAME=5
    WARMUP=6
    SESSION_DATA_INITIALISED=7
    CLIENTCONNECT=8
    CLIENTDISCONNECT=9
    CLIENTBEGIN=10
    CLIENTSPAWN=11
    CLIENTUSERINFO=12
    CLIENTUSERINFOCHANGED=13
    ACCOUNTVALIDATED=14
    SAY=15
    SAYTELL=16
    SAYTEAM=17
    TELL=18
    KILL=19
    ITEM=20
    FLAG=21
    FLAGCAPTURETIME=22
    BACK_SLASH=23
    SLASH=24
    COMMA=25
    INFERIOR=26
    SUPERIOR=27
    COLON=28
    SEMICOLON=29
    DOT=30
    UNDERSCORE=31
    MINUS=32
    PLUS=33
    DOUBLE_QUOTE=34
    ROUND_BRACKET_LEFT=35
    ROUND_BRACKET_RIGHT=36
    SQUARE_BRACKET_LEFT=37
    SQUARE_BRACKET_RIGHT=38
    WHITESPACE=39
    NEWLINE=40
    LETTER=41
    DIGIT=42

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
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.MINUS) | (1 << EventsParser.WHITESPACE) | (1 << EventsParser.DIGIT))) != 0):
                self.state = 55
                localctx.a = self.event()
                localctx.value.append(localctx.a.value)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==EventsParser.NEWLINE:
                    self.state = 57
                    self.match(EventsParser.NEWLINE)


                self.state = 64
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
            self.a = None # IntValueContext
            self.b = None # IntValueContext
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
            self.killEvt = None # KillEventContext
            self.itemEvt = None # ItemEventContext
            self.flagEvt = None # FlagEventContext
            self.flagCaptureTimeEvt = None # FlagCaptureTimeEventContext

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


        def killEvent(self):
            return self.getTypedRuleContext(EventsParser.KillEventContext,0)


        def itemEvent(self):
            return self.getTypedRuleContext(EventsParser.ItemEventContext,0)


        def flagEvent(self):
            return self.getTypedRuleContext(EventsParser.FlagEventContext,0)


        def flagCaptureTimeEvent(self):
            return self.getTypedRuleContext(EventsParser.FlagCaptureTimeEventContext,0)


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
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EventsParser.WHITESPACE:
                self.state = 65
                self.match(EventsParser.WHITESPACE)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            localctx.a = self.intValue()
            self.state = 72
            self.match(EventsParser.COLON)
            self.state = 73
            localctx.b = self.intValue()
            self.state = 74
            self.match(EventsParser.WHITESPACE)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 75
                localctx.separatorEvt = self.separatorEvent()
                localctx.value = localctx.separatorEvt.value
                pass

            elif la_ == 2:
                self.state = 78
                localctx.initGameEvt = self.initGameEvent()
                localctx.value = localctx.initGameEvt.value
                pass

            elif la_ == 3:
                self.state = 81
                localctx.initRoundEvt = self.initRoundEvent()
                localctx.value = localctx.initRoundEvt.value
                pass

            elif la_ == 4:
                self.state = 84
                localctx.initAuthEvt = self.initAuthEvent()
                localctx.value = localctx.initAuthEvt.value
                pass

            elif la_ == 5:
                self.state = 87
                localctx.shutdownGameEvt = self.shutdownGameEvent()
                localctx.value = localctx.shutdownGameEvt.value
                pass

            elif la_ == 6:
                self.state = 90
                localctx.warmupEvt = self.warmupEvent()
                localctx.value = localctx.warmupEvt.value
                pass

            elif la_ == 7:
                self.state = 93
                localctx.sessionDataInitEvt = self.sessionDataInitEvent()
                localctx.value = localctx.sessionDataInitEvt.value
                pass

            elif la_ == 8:
                self.state = 96
                localctx.clientConnectEvt = self.clientConnectEvent()
                localctx.value = localctx.clientConnectEvt.value
                pass

            elif la_ == 9:
                self.state = 99
                localctx.clientDisconnectEvt = self.clientDisconnectEvent()
                localctx.value = localctx.clientDisconnectEvt.value
                pass

            elif la_ == 10:
                self.state = 102
                localctx.clientBeginEvt = self.clientBeginEvent()
                localctx.value = localctx.clientBeginEvt.value
                pass

            elif la_ == 11:
                self.state = 105
                localctx.clientSpawnEvt = self.clientSpawnEvent()
                localctx.value = localctx.clientSpawnEvt.value
                pass

            elif la_ == 12:
                self.state = 108
                localctx.clientUserinfoEvt = self.clientUserinfoEvent()
                localctx.value = localctx.clientUserinfoEvt.value
                pass

            elif la_ == 13:
                self.state = 111
                localctx.clientUserinfoChangedEvt = self.clientUserinfoChangedEvent()
                localctx.value = localctx.clientUserinfoChangedEvt.value
                pass

            elif la_ == 14:
                self.state = 114
                localctx.accountValidatedEvt = self.accountValidatedEvent()
                localctx.value = localctx.accountValidatedEvt.value
                pass

            elif la_ == 15:
                self.state = 117
                localctx.sayEvt = self.sayEvent()
                localctx.value = localctx.sayEvt.value
                pass

            elif la_ == 16:
                self.state = 120
                localctx.sayTellEvt = self.sayTellEvent()
                localctx.value = localctx.sayTellEvt.value
                pass

            elif la_ == 17:
                self.state = 123
                localctx.sayTeamEvt = self.sayTeamEvent()
                localctx.value = localctx.sayTeamEvt.value
                pass

            elif la_ == 18:
                self.state = 126
                localctx.tellEvt = self.tellEvent()
                localctx.value = localctx.tellEvt.value
                pass

            elif la_ == 19:
                self.state = 129
                localctx.killEvt = self.killEvent()
                localctx.value = localctx.killEvt.value
                pass

            elif la_ == 20:
                self.state = 132
                localctx.itemEvt = self.itemEvent()
                localctx.value = localctx.itemEvt.value
                pass

            elif la_ == 21:
                self.state = 135
                localctx.flagEvt = self.flagEvent()
                localctx.value = localctx.flagEvt.value
                pass

            elif la_ == 22:
                self.state = 138
                localctx.flagCaptureTimeEvt = self.flagCaptureTimeEvent()
                localctx.value = localctx.flagCaptureTimeEvt.value
                pass


            localctx.value.minutes = int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.seconds = int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
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
        self.enterRule(localctx, 4, self.RULE_separatorEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
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
            self.a = None # WordValueContext
            self.b = None # SentenceValueContext

        def INITGAME(self):
            return self.getToken(EventsParser.INITGAME, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


        def sentenceValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.SentenceValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.SentenceValueContext,i)


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
        self.enterRule(localctx, 6, self.RULE_initGameEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(EventsParser.INITGAME)
            self.state = 150
            self.match(EventsParser.WHITESPACE)
            localctx.value = InitGameEvent()
            self.state = 158 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self.match(EventsParser.BACK_SLASH)
                self.state = 153
                localctx.a = self.wordValue()
                self.state = 154
                self.match(EventsParser.BACK_SLASH)
                self.state = 155
                localctx.b = self.sentenceValue()
                localctx.value.parameters[(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))]=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
                self.state = 160 
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
            self.a = None # WordValueContext
            self.b = None # SentenceValueContext

        def INITROUND(self):
            return self.getToken(EventsParser.INITROUND, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


        def sentenceValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.SentenceValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.SentenceValueContext,i)


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
        self.enterRule(localctx, 8, self.RULE_initRoundEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(EventsParser.INITROUND)
            self.state = 163
            self.match(EventsParser.WHITESPACE)
            localctx.value = InitRoundEvent()
            self.state = 171 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 165
                self.match(EventsParser.BACK_SLASH)
                self.state = 166
                localctx.a = self.wordValue()
                self.state = 167
                self.match(EventsParser.BACK_SLASH)
                self.state = 168
                localctx.b = self.sentenceValue()
                localctx.value.parameters[(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))]=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
                self.state = 173 
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
            self.a = None # WordValueContext
            self.b = None # SentenceValueContext

        def INITAUTH(self):
            return self.getToken(EventsParser.INITAUTH, 0)

        def WHITESPACE(self):
            return self.getToken(EventsParser.WHITESPACE, 0)

        def BACK_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.BACK_SLASH)
            else:
                return self.getToken(EventsParser.BACK_SLASH, i)

        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


        def sentenceValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.SentenceValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.SentenceValueContext,i)


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
        self.enterRule(localctx, 10, self.RULE_initAuthEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(EventsParser.INITAUTH)
            self.state = 176
            self.match(EventsParser.WHITESPACE)
            localctx.value = InitAuthEvent()
            self.state = 184 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.match(EventsParser.BACK_SLASH)
                self.state = 179
                localctx.a = self.wordValue()
                self.state = 180
                self.match(EventsParser.BACK_SLASH)
                self.state = 181
                localctx.b = self.sentenceValue()
                localctx.value.parameters[(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))]=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
                self.state = 186 
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
        self.enterRule(localctx, 12, self.RULE_shutdownGameEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(EventsParser.SHUTDOWNGAME)
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
        self.enterRule(localctx, 14, self.RULE_warmupEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(EventsParser.WARMUP)
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

        def wordValue(self):
            return self.getTypedRuleContext(EventsParser.WordValueContext,0)


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
        self.enterRule(localctx, 16, self.RULE_sessionDataInitEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(EventsParser.SESSION_DATA_INITIALISED)
            self.state = 195
            self.match(EventsParser.WHITESPACE)
            self.state = 196
            localctx.a = self.intValue()
            self.state = 197
            self.match(EventsParser.WHITESPACE)
            self.state = 198
            self.wordValue()
            self.state = 199
            self.match(EventsParser.WHITESPACE)
            self.state = 200
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
        self.enterRule(localctx, 18, self.RULE_clientConnectEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(EventsParser.CLIENTCONNECT)
            self.state = 206
            self.match(EventsParser.WHITESPACE)
            self.state = 207
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
        self.enterRule(localctx, 20, self.RULE_clientDisconnectEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(EventsParser.CLIENTDISCONNECT)
            self.state = 212
            self.match(EventsParser.WHITESPACE)
            self.state = 213
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
        self.enterRule(localctx, 22, self.RULE_clientBeginEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(EventsParser.CLIENTBEGIN)
            self.state = 218
            self.match(EventsParser.WHITESPACE)
            self.state = 219
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
        self.enterRule(localctx, 24, self.RULE_clientSpawnEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(EventsParser.CLIENTSPAWN)
            self.state = 224
            self.match(EventsParser.WHITESPACE)
            self.state = 225
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
            self.b = None # WordValueContext
            self.c = None # SentenceValueContext

        def CLIENTUSERINFO(self):
            return self.getToken(EventsParser.CLIENTUSERINFO, 0)

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

        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


        def sentenceValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.SentenceValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.SentenceValueContext,i)


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
        self.enterRule(localctx, 26, self.RULE_clientUserinfoEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(EventsParser.CLIENTUSERINFO)
            self.state = 230
            self.match(EventsParser.WHITESPACE)
            self.state = 231
            localctx.a = self.intValue()
            self.state = 232
            self.match(EventsParser.WHITESPACE)
            localctx.value=ClientUserinfoEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 235
                self.match(EventsParser.BACK_SLASH)
                self.state = 236
                localctx.b = self.wordValue()
                self.state = 237
                self.match(EventsParser.BACK_SLASH)
                self.state = 238
                localctx.c = self.sentenceValue()
                localctx.value.parameters[(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))]=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
                self.state = 243 
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
            self.b = None # WordValueContext
            self.c = None # SentenceValueContext

        def CLIENTUSERINFOCHANGED(self):
            return self.getToken(EventsParser.CLIENTUSERINFOCHANGED, 0)

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

        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


        def sentenceValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.SentenceValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.SentenceValueContext,i)


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
        self.enterRule(localctx, 28, self.RULE_clientUserinfoChangedEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(EventsParser.CLIENTUSERINFOCHANGED)
            self.state = 246
            self.match(EventsParser.WHITESPACE)
            self.state = 247
            localctx.a = self.intValue()
            self.state = 248
            self.match(EventsParser.WHITESPACE)
            localctx.value=ClientUserinfoChangedEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            self.state = 261 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 252
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==EventsParser.BACK_SLASH:
                        self.state = 251
                        self.match(EventsParser.BACK_SLASH)


                    self.state = 254
                    localctx.b = self.wordValue()
                    self.state = 255
                    self.match(EventsParser.BACK_SLASH)
                    self.state = 257
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 256
                        localctx.c = self.sentenceValue()


                    localctx.value.parameters[(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))]=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))

                else:
                    raise NoViableAltException(self)
                self.state = 263 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            self.b = None # WordValueContext
            self.c = None # IntValueContext
            self.d = None # WordValueContext

        def ACCOUNTVALIDATED(self):
            return self.getToken(EventsParser.ACCOUNTVALIDATED, 0)

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


        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


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
        self.enterRule(localctx, 30, self.RULE_accountValidatedEvent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.value=AccountValidatedEvent()
            self.state = 266
            self.match(EventsParser.ACCOUNTVALIDATED)
            self.state = 267
            self.match(EventsParser.WHITESPACE)
            self.state = 268
            localctx.a = self.intValue()
            self.state = 269
            self.match(EventsParser.WHITESPACE)
            self.state = 270
            self.match(EventsParser.MINUS)
            self.state = 271
            self.match(EventsParser.WHITESPACE)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 272
                localctx.b = self.wordValue()
                localctx.value.account=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
                self.state = 274
                self.match(EventsParser.WHITESPACE)


            self.state = 278
            self.match(EventsParser.MINUS)
            self.state = 279
            self.match(EventsParser.WHITESPACE)
            self.state = 280
            localctx.c = self.intValue()
            self.state = 281
            self.match(EventsParser.WHITESPACE)
            self.state = 282
            self.match(EventsParser.MINUS)
            self.state = 283
            self.match(EventsParser.WHITESPACE)
            self.state = 284
            self.match(EventsParser.DOUBLE_QUOTE)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SLASH) | (1 << EventsParser.COMMA) | (1 << EventsParser.INFERIOR) | (1 << EventsParser.SUPERIOR) | (1 << EventsParser.COLON) | (1 << EventsParser.SEMICOLON) | (1 << EventsParser.DOT) | (1 << EventsParser.UNDERSCORE) | (1 << EventsParser.MINUS) | (1 << EventsParser.PLUS) | (1 << EventsParser.ROUND_BRACKET_LEFT) | (1 << EventsParser.ROUND_BRACKET_RIGHT) | (1 << EventsParser.SQUARE_BRACKET_LEFT) | (1 << EventsParser.SQUARE_BRACKET_RIGHT) | (1 << EventsParser.LETTER) | (1 << EventsParser.DIGIT))) != 0):
                self.state = 285
                localctx.d = self.wordValue()
                localctx.value.role=(None if localctx.d is None else self._input.getText(localctx.d.start,localctx.d.stop))


            self.state = 290
            self.match(EventsParser.DOUBLE_QUOTE)
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.level=int((None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop)))
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
            self.b = None # WordValueContext
            self.c = None # SentenceValueContext

        def SAY(self):
            return self.getToken(EventsParser.SAY, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def wordValue(self):
            return self.getTypedRuleContext(EventsParser.WordValueContext,0)


        def sentenceValue(self):
            return self.getTypedRuleContext(EventsParser.SentenceValueContext,0)


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
        self.enterRule(localctx, 32, self.RULE_sayEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(EventsParser.SAY)
            self.state = 295
            self.match(EventsParser.WHITESPACE)
            self.state = 296
            localctx.a = self.intValue()
            self.state = 297
            self.match(EventsParser.WHITESPACE)
            self.state = 298
            localctx.b = self.wordValue()
            self.state = 299
            self.match(EventsParser.COLON)
            self.state = 300
            self.match(EventsParser.WHITESPACE)
            self.state = 301
            localctx.c = self.sentenceValue()
            localctx.value=SayEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.sender=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
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
            self.c = None # WordValueContext
            self.d = None # SentenceValueContext

        def SAYTELL(self):
            return self.getToken(EventsParser.SAYTELL, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def wordValue(self):
            return self.getTypedRuleContext(EventsParser.WordValueContext,0)


        def sentenceValue(self):
            return self.getTypedRuleContext(EventsParser.SentenceValueContext,0)


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
        self.enterRule(localctx, 34, self.RULE_sayTellEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(EventsParser.SAYTELL)
            self.state = 308
            self.match(EventsParser.WHITESPACE)
            self.state = 309
            localctx.a = self.intValue()
            self.state = 310
            self.match(EventsParser.WHITESPACE)
            self.state = 311
            localctx.b = self.intValue()
            self.state = 312
            self.match(EventsParser.WHITESPACE)
            self.state = 313
            localctx.c = self.wordValue()
            self.state = 314
            self.match(EventsParser.COLON)
            self.state = 315
            self.match(EventsParser.WHITESPACE)
            self.state = 316
            localctx.d = self.sentenceValue()
            localctx.value=SayTellEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.sender_slot=int((None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop)))
            localctx.value.sender=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
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
            self.b = None # WordValueContext
            self.c = None # SentenceValueContext

        def SAYTELL(self):
            return self.getToken(EventsParser.SAYTELL, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def wordValue(self):
            return self.getTypedRuleContext(EventsParser.WordValueContext,0)


        def sentenceValue(self):
            return self.getTypedRuleContext(EventsParser.SentenceValueContext,0)


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
        self.enterRule(localctx, 36, self.RULE_sayTeamEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(EventsParser.SAYTELL)
            self.state = 324
            self.match(EventsParser.WHITESPACE)
            self.state = 325
            localctx.a = self.intValue()
            self.state = 326
            self.match(EventsParser.WHITESPACE)
            self.state = 327
            localctx.b = self.wordValue()
            self.state = 328
            self.match(EventsParser.COLON)
            self.state = 329
            self.match(EventsParser.WHITESPACE)
            self.state = 330
            localctx.c = self.sentenceValue()
            localctx.value=SayTeamEvent()
            localctx.value.slot=int((None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop)))
            localctx.value.sender=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
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
            self.a = None # WordValueContext
            self.b = None # WordValueContext
            self.c = None # SentenceValueContext

        def TELL(self):
            return self.getToken(EventsParser.TELL, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def sentenceValue(self):
            return self.getTypedRuleContext(EventsParser.SentenceValueContext,0)


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
        self.enterRule(localctx, 38, self.RULE_tellEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(EventsParser.TELL)
            self.state = 337
            self.match(EventsParser.WHITESPACE)
            self.state = 338
            localctx.a = self.wordValue()
            self.state = 339
            self.match(EventsParser.WHITESPACE)
            self.state = 340
            self.wordValue()
            self.state = 341
            self.match(EventsParser.WHITESPACE)
            self.state = 342
            localctx.b = self.wordValue()
            self.state = 343
            self.match(EventsParser.COLON)
            self.state = 344
            self.match(EventsParser.WHITESPACE)
            self.state = 345
            localctx.c = self.sentenceValue()
            localctx.value=TellEvent()
            localctx.value.sender=(None if localctx.a is None else self._input.getText(localctx.a.start,localctx.a.stop))
            localctx.value.target=(None if localctx.b is None else self._input.getText(localctx.b.start,localctx.b.stop))
            localctx.value.message=(None if localctx.c is None else self._input.getText(localctx.c.start,localctx.c.stop))
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
            self.d = None # WordValueContext
            self.e = None # WordValueContext
            self.f = None # WordValueContext

        def KILL(self):
            return self.getToken(EventsParser.KILL, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


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
        self.enterRule(localctx, 40, self.RULE_killEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(EventsParser.KILL)
            self.state = 352
            self.match(EventsParser.WHITESPACE)
            self.state = 353
            localctx.a = self.intValue()
            self.state = 354
            self.match(EventsParser.WHITESPACE)
            self.state = 355
            localctx.b = self.intValue()
            self.state = 356
            self.match(EventsParser.WHITESPACE)
            self.state = 357
            localctx.c = self.intValue()
            self.state = 358
            self.match(EventsParser.COLON)
            self.state = 359
            self.match(EventsParser.WHITESPACE)
            self.state = 360
            localctx.d = self.wordValue()
            self.state = 361
            self.match(EventsParser.WHITESPACE)
            self.state = 362
            self.wordValue()
            self.state = 363
            self.match(EventsParser.WHITESPACE)
            self.state = 364
            localctx.e = self.wordValue()
            self.state = 365
            self.match(EventsParser.WHITESPACE)
            self.state = 366
            self.wordValue()
            self.state = 367
            self.match(EventsParser.WHITESPACE)
            self.state = 368
            localctx.f = self.wordValue()
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
            self.b = None # WordValueContext

        def ITEM(self):
            return self.getToken(EventsParser.ITEM, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def intValue(self):
            return self.getTypedRuleContext(EventsParser.IntValueContext,0)


        def wordValue(self):
            return self.getTypedRuleContext(EventsParser.WordValueContext,0)


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
        self.enterRule(localctx, 42, self.RULE_itemEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(EventsParser.ITEM)
            self.state = 378
            self.match(EventsParser.WHITESPACE)
            self.state = 379
            localctx.a = self.intValue()
            self.state = 380
            self.match(EventsParser.WHITESPACE)
            self.state = 381
            localctx.b = self.wordValue()
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
            self.c = None # WordValueContext

        def FLAG(self):
            return self.getToken(EventsParser.FLAG, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

        def intValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.IntValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.IntValueContext,i)


        def wordValue(self):
            return self.getTypedRuleContext(EventsParser.WordValueContext,0)


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
        self.enterRule(localctx, 44, self.RULE_flagEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(EventsParser.FLAG)
            self.state = 387
            self.match(EventsParser.WHITESPACE)
            self.state = 388
            localctx.a = self.intValue()
            self.state = 389
            self.match(EventsParser.WHITESPACE)
            self.state = 390
            localctx.b = self.intValue()
            self.state = 391
            self.match(EventsParser.COLON)
            self.state = 392
            self.match(EventsParser.WHITESPACE)
            self.state = 393
            localctx.c = self.wordValue()
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

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def COLON(self):
            return self.getToken(EventsParser.COLON, 0)

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
        self.enterRule(localctx, 46, self.RULE_flagCaptureTimeEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(EventsParser.FLAGCAPTURETIME)
            self.state = 400
            self.match(EventsParser.WHITESPACE)
            self.state = 401
            localctx.a = self.intValue()
            self.state = 402
            self.match(EventsParser.COLON)
            self.state = 403
            self.match(EventsParser.WHITESPACE)
            self.state = 404
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
        self.enterRule(localctx, 48, self.RULE_intValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EventsParser.MINUS:
                self.state = 409
                self.match(EventsParser.MINUS)


            self.state = 413 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 412
                    self.match(EventsParser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 415 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.LETTER)
            else:
                return self.getToken(EventsParser.LETTER, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.DIGIT)
            else:
                return self.getToken(EventsParser.DIGIT, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.UNDERSCORE)
            else:
                return self.getToken(EventsParser.UNDERSCORE, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.MINUS)
            else:
                return self.getToken(EventsParser.MINUS, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.PLUS)
            else:
                return self.getToken(EventsParser.PLUS, i)

        def ROUND_BRACKET_LEFT(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.ROUND_BRACKET_LEFT)
            else:
                return self.getToken(EventsParser.ROUND_BRACKET_LEFT, i)

        def ROUND_BRACKET_RIGHT(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.ROUND_BRACKET_RIGHT)
            else:
                return self.getToken(EventsParser.ROUND_BRACKET_RIGHT, i)

        def SQUARE_BRACKET_LEFT(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.SQUARE_BRACKET_LEFT)
            else:
                return self.getToken(EventsParser.SQUARE_BRACKET_LEFT, i)

        def SQUARE_BRACKET_RIGHT(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.SQUARE_BRACKET_RIGHT)
            else:
                return self.getToken(EventsParser.SQUARE_BRACKET_RIGHT, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.SLASH)
            else:
                return self.getToken(EventsParser.SLASH, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.COMMA)
            else:
                return self.getToken(EventsParser.COMMA, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.COLON)
            else:
                return self.getToken(EventsParser.COLON, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.SEMICOLON)
            else:
                return self.getToken(EventsParser.SEMICOLON, i)

        def INFERIOR(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.INFERIOR)
            else:
                return self.getToken(EventsParser.INFERIOR, i)

        def SUPERIOR(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.SUPERIOR)
            else:
                return self.getToken(EventsParser.SUPERIOR, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.DOT)
            else:
                return self.getToken(EventsParser.DOT, i)

        def getRuleIndex(self):
            return EventsParser.RULE_wordValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWordValue" ):
                listener.enterWordValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWordValue" ):
                listener.exitWordValue(self)




    def wordValue(self):

        localctx = EventsParser.WordValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_wordValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 417
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EventsParser.SLASH) | (1 << EventsParser.COMMA) | (1 << EventsParser.INFERIOR) | (1 << EventsParser.SUPERIOR) | (1 << EventsParser.COLON) | (1 << EventsParser.SEMICOLON) | (1 << EventsParser.DOT) | (1 << EventsParser.UNDERSCORE) | (1 << EventsParser.MINUS) | (1 << EventsParser.PLUS) | (1 << EventsParser.ROUND_BRACKET_LEFT) | (1 << EventsParser.ROUND_BRACKET_RIGHT) | (1 << EventsParser.SQUARE_BRACKET_LEFT) | (1 << EventsParser.SQUARE_BRACKET_RIGHT) | (1 << EventsParser.LETTER) | (1 << EventsParser.DIGIT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 420 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wordValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EventsParser.WordValueContext)
            else:
                return self.getTypedRuleContext(EventsParser.WordValueContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(EventsParser.WHITESPACE)
            else:
                return self.getToken(EventsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return EventsParser.RULE_sentenceValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenceValue" ):
                listener.enterSentenceValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenceValue" ):
                listener.exitSentenceValue(self)




    def sentenceValue(self):

        localctx = EventsParser.SentenceValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_sentenceValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 424
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [EventsParser.SLASH, EventsParser.COMMA, EventsParser.INFERIOR, EventsParser.SUPERIOR, EventsParser.COLON, EventsParser.SEMICOLON, EventsParser.DOT, EventsParser.UNDERSCORE, EventsParser.MINUS, EventsParser.PLUS, EventsParser.ROUND_BRACKET_LEFT, EventsParser.ROUND_BRACKET_RIGHT, EventsParser.SQUARE_BRACKET_LEFT, EventsParser.SQUARE_BRACKET_RIGHT, EventsParser.LETTER, EventsParser.DIGIT]:
                        self.state = 422
                        self.wordValue()
                        pass
                    elif token in [EventsParser.WHITESPACE]:
                        self.state = 423
                        self.match(EventsParser.WHITESPACE)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 426 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





