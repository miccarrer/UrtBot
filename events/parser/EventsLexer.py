# Generated from events/parser/Events.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2%")
        buf.write("\u01b7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\36\5\36\u01a6\n\36\3\36\3\36\5\36\u01aa")
        buf.write("\n\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\2\2%\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%\3\2\3\4\2\13")
        buf.write("\13\"\"\2\u01b8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\3I\3\2\2\2\5\u0086\3\2\2\2\7\u008f\3\2\2\2\t\u0099")
        buf.write("\3\2\2\2\13\u00a2\3\2\2\2\r\u00af\3\2\2\2\17\u00b6\3\2")
        buf.write("\2\2\21\u00e2\3\2\2\2\23\u00e5\3\2\2\2\25\u00f3\3\2\2")
        buf.write("\2\27\u0104\3\2\2\2\31\u0110\3\2\2\2\33\u011c\3\2\2\2")
        buf.write("\35\u012b\3\2\2\2\37\u0141\3\2\2\2!\u0152\3\2\2\2#\u0156")
        buf.write("\3\2\2\2%\u015e\3\2\2\2\'\u0166\3\2\2\2)\u016c\3\2\2\2")
        buf.write("+\u0171\3\2\2\2-\u0176\3\2\2\2/\u017b\3\2\2\2\61\u0180")
        buf.write("\3\2\2\2\63\u0190\3\2\2\2\65\u019c\3\2\2\2\67\u019f\3")
        buf.write("\2\2\29\u01a2\3\2\2\2;\u01a9\3\2\2\2=\u01ab\3\2\2\2?\u01ad")
        buf.write("\3\2\2\2A\u01af\3\2\2\2C\u01b1\3\2\2\2E\u01b3\3\2\2\2")
        buf.write("G\u01b5\3\2\2\2IJ\7/\2\2JK\7/\2\2KL\7/\2\2LM\7/\2\2MN")
        buf.write("\7/\2\2NO\7/\2\2OP\7/\2\2PQ\7/\2\2QR\7/\2\2RS\7/\2\2S")
        buf.write("T\7/\2\2TU\7/\2\2UV\7/\2\2VW\7/\2\2WX\7/\2\2XY\7/\2\2")
        buf.write("YZ\7/\2\2Z[\7/\2\2[\\\7/\2\2\\]\7/\2\2]^\7/\2\2^_\7/\2")
        buf.write("\2_`\7/\2\2`a\7/\2\2ab\7/\2\2bc\7/\2\2cd\7/\2\2de\7/\2")
        buf.write("\2ef\7/\2\2fg\7/\2\2gh\7/\2\2hi\7/\2\2ij\7/\2\2jk\7/\2")
        buf.write("\2kl\7/\2\2lm\7/\2\2mn\7/\2\2no\7/\2\2op\7/\2\2pq\7/\2")
        buf.write("\2qr\7/\2\2rs\7/\2\2st\7/\2\2tu\7/\2\2uv\7/\2\2vw\7/\2")
        buf.write("\2wx\7/\2\2xy\7/\2\2yz\7/\2\2z{\7/\2\2{|\7/\2\2|}\7/\2")
        buf.write("\2}~\7/\2\2~\177\7/\2\2\177\u0080\7/\2\2\u0080\u0081\7")
        buf.write("/\2\2\u0081\u0082\7/\2\2\u0082\u0083\7/\2\2\u0083\u0084")
        buf.write("\7/\2\2\u0084\u0085\7/\2\2\u0085\4\3\2\2\2\u0086\u0087")
        buf.write("\7K\2\2\u0087\u0088\7p\2\2\u0088\u0089\7k\2\2\u0089\u008a")
        buf.write("\7v\2\2\u008a\u008b\7I\2\2\u008b\u008c\7c\2\2\u008c\u008d")
        buf.write("\7o\2\2\u008d\u008e\7g\2\2\u008e\6\3\2\2\2\u008f\u0090")
        buf.write("\7K\2\2\u0090\u0091\7p\2\2\u0091\u0092\7k\2\2\u0092\u0093")
        buf.write("\7v\2\2\u0093\u0094\7T\2\2\u0094\u0095\7q\2\2\u0095\u0096")
        buf.write("\7w\2\2\u0096\u0097\7p\2\2\u0097\u0098\7f\2\2\u0098\b")
        buf.write("\3\2\2\2\u0099\u009a\7K\2\2\u009a\u009b\7p\2\2\u009b\u009c")
        buf.write("\7k\2\2\u009c\u009d\7v\2\2\u009d\u009e\7C\2\2\u009e\u009f")
        buf.write("\7w\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1\7j\2\2\u00a1\n")
        buf.write("\3\2\2\2\u00a2\u00a3\7U\2\2\u00a3\u00a4\7j\2\2\u00a4\u00a5")
        buf.write("\7w\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7y\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab")
        buf.write("\7I\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7o\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\f\3\2\2\2\u00af\u00b0\7Y\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7o\2\2\u00b3\u00b4")
        buf.write("\7w\2\2\u00b4\u00b5\7r\2\2\u00b5\16\3\2\2\2\u00b6\u00b7")
        buf.write("\7U\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba")
        buf.write("\7u\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\u00be\7\"\2\2\u00be\u00bf\7f\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3")
        buf.write("\7\"\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6")
        buf.write("\7k\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7u\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7f\2\2\u00ce\u00cf")
        buf.write("\7\"\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\u00d3\7\"\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7\"\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7\"\2\2\u00dd\u00de")
        buf.write("\7u\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\20\3\2\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\22\3\2\2\2\u00e5\u00e6\7E\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7E\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2\7v\2\2\u00f2\24")
        buf.write("\3\2\2\2\u00f3\u00f4\7E\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6")
        buf.write("\7k\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9\u00fa\7F\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc")
        buf.write("\7u\2\2\u00fc\u00fd\7e\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7e\2\2\u0102\u0103\7v\2\2\u0103\26\3\2\2\2\u0104\u0105")
        buf.write("\7E\2\2\u0105\u0106\7n\2\2\u0106\u0107\7k\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\u0109\7p\2\2\u0109\u010a\7v\2\2\u010a\u010b")
        buf.write("\7D\2\2\u010b\u010c\7g\2\2\u010c\u010d\7i\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7p\2\2\u010f\30\3\2\2\2\u0110\u0111")
        buf.write("\7E\2\2\u0111\u0112\7n\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\u0115\7p\2\2\u0115\u0116\7v\2\2\u0116\u0117")
        buf.write("\7U\2\2\u0117\u0118\7r\2\2\u0118\u0119\7c\2\2\u0119\u011a")
        buf.write("\7y\2\2\u011a\u011b\7p\2\2\u011b\32\3\2\2\2\u011c\u011d")
        buf.write("\7E\2\2\u011d\u011e\7n\2\2\u011e\u011f\7k\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7p\2\2\u0121\u0122\7v\2\2\u0122\u0123")
        buf.write("\7W\2\2\u0123\u0124\7u\2\2\u0124\u0125\7g\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128\u0129")
        buf.write("\7h\2\2\u0129\u012a\7q\2\2\u012a\34\3\2\2\2\u012b\u012c")
        buf.write("\7E\2\2\u012c\u012d\7n\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7g\2\2\u012f\u0130\7p\2\2\u0130\u0131\7v\2\2\u0131\u0132")
        buf.write("\7W\2\2\u0132\u0133\7u\2\2\u0133\u0134\7g\2\2\u0134\u0135")
        buf.write("\7t\2\2\u0135\u0136\7k\2\2\u0136\u0137\7p\2\2\u0137\u0138")
        buf.write("\7h\2\2\u0138\u0139\7q\2\2\u0139\u013a\7E\2\2\u013a\u013b")
        buf.write("\7j\2\2\u013b\u013c\7c\2\2\u013c\u013d\7p\2\2\u013d\u013e")
        buf.write("\7i\2\2\u013e\u013f\7g\2\2\u013f\u0140\7f\2\2\u0140\36")
        buf.write("\3\2\2\2\u0141\u0142\7C\2\2\u0142\u0143\7e\2\2\u0143\u0144")
        buf.write("\7e\2\2\u0144\u0145\7q\2\2\u0145\u0146\7w\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\u0148\7v\2\2\u0148\u0149\7X\2\2\u0149\u014a")
        buf.write("\7c\2\2\u014a\u014b\7n\2\2\u014b\u014c\7k\2\2\u014c\u014d")
        buf.write("\7f\2\2\u014d\u014e\7c\2\2\u014e\u014f\7v\2\2\u014f\u0150")
        buf.write("\7g\2\2\u0150\u0151\7f\2\2\u0151 \3\2\2\2\u0152\u0153")
        buf.write("\7u\2\2\u0153\u0154\7c\2\2\u0154\u0155\7{\2\2\u0155\"")
        buf.write("\3\2\2\2\u0156\u0157\7u\2\2\u0157\u0158\7c\2\2\u0158\u0159")
        buf.write("\7{\2\2\u0159\u015a\7v\2\2\u015a\u015b\7g\2\2\u015b\u015c")
        buf.write("\7n\2\2\u015c\u015d\7n\2\2\u015d$\3\2\2\2\u015e\u015f")
        buf.write("\7u\2\2\u015f\u0160\7c\2\2\u0160\u0161\7{\2\2\u0161\u0162")
        buf.write("\7v\2\2\u0162\u0163\7g\2\2\u0163\u0164\7c\2\2\u0164\u0165")
        buf.write("\7o\2\2\u0165&\3\2\2\2\u0166\u0167\7T\2\2\u0167\u0168")
        buf.write("\7c\2\2\u0168\u0169\7f\2\2\u0169\u016a\7k\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016b(\3\2\2\2\u016c\u016d\7v\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e\u016f\7n\2\2\u016f\u0170\7n\2\2\u0170*\3")
        buf.write("\2\2\2\u0171\u0172\7M\2\2\u0172\u0173\7k\2\2\u0173\u0174")
        buf.write("\7n\2\2\u0174\u0175\7n\2\2\u0175,\3\2\2\2\u0176\u0177")
        buf.write("\7K\2\2\u0177\u0178\7v\2\2\u0178\u0179\7g\2\2\u0179\u017a")
        buf.write("\7o\2\2\u017a.\3\2\2\2\u017b\u017c\7H\2\2\u017c\u017d")
        buf.write("\7n\2\2\u017d\u017e\7c\2\2\u017e\u017f\7i\2\2\u017f\60")
        buf.write("\3\2\2\2\u0180\u0181\7H\2\2\u0181\u0182\7n\2\2\u0182\u0183")
        buf.write("\7c\2\2\u0183\u0184\7i\2\2\u0184\u0185\7E\2\2\u0185\u0186")
        buf.write("\7c\2\2\u0186\u0187\7r\2\2\u0187\u0188\7v\2\2\u0188\u0189")
        buf.write("\7w\2\2\u0189\u018a\7t\2\2\u018a\u018b\7g\2\2\u018b\u018c")
        buf.write("\7V\2\2\u018c\u018d\7k\2\2\u018d\u018e\7o\2\2\u018e\u018f")
        buf.write("\7g\2\2\u018f\62\3\2\2\2\u0190\u0191\7H\2\2\u0191\u0192")
        buf.write("\7n\2\2\u0192\u0193\7c\2\2\u0193\u0194\7i\2\2\u0194\u0195")
        buf.write("\7\"\2\2\u0195\u0196\7T\2\2\u0196\u0197\7g\2\2\u0197\u0198")
        buf.write("\7v\2\2\u0198\u0199\7w\2\2\u0199\u019a\7t\2\2\u019a\u019b")
        buf.write("\7p\2\2\u019b\64\3\2\2\2\u019c\u019d\7v\2\2\u019d\u019e")
        buf.write("\7q\2\2\u019e\66\3\2\2\2\u019f\u01a0\7d\2\2\u01a0\u01a1")
        buf.write("\7{\2\2\u01a18\3\2\2\2\u01a2\u01a3\t\2\2\2\u01a3:\3\2")
        buf.write("\2\2\u01a4\u01a6\7\17\2\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01aa\7\f\2\2\u01a8")
        buf.write("\u01aa\7\17\2\2\u01a9\u01a5\3\2\2\2\u01a9\u01a8\3\2\2")
        buf.write("\2\u01aa<\3\2\2\2\u01ab\u01ac\7^\2\2\u01ac>\3\2\2\2\u01ad")
        buf.write("\u01ae\7<\2\2\u01ae@\3\2\2\2\u01af\u01b0\7/\2\2\u01b0")
        buf.write("B\3\2\2\2\u01b1\u01b2\7$\2\2\u01b2D\3\2\2\2\u01b3\u01b4")
        buf.write("\4\62;\2\u01b4F\3\2\2\2\u01b5\u01b6\13\2\2\2\u01b6H\3")
        buf.write("\2\2\2\5\2\u01a5\u01a9\2")
        return buf.getvalue()


class EventsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SEPARATOR = 1
    INITGAME = 2
    INITROUND = 3
    INITAUTH = 4
    SHUTDOWNGAME = 5
    WARMUP = 6
    SESSION_DATA_INITIALISED = 7
    AT = 8
    CLIENTCONNECT = 9
    CLIENTDISCONNECT = 10
    CLIENTBEGIN = 11
    CLIENTSPAWN = 12
    CLIENTUSERINFO = 13
    CLIENTUSERINFOCHANGED = 14
    ACCOUNTVALIDATED = 15
    SAY = 16
    SAYTELL = 17
    SAYTEAM = 18
    RADIO = 19
    TELL = 20
    KILL = 21
    ITEM = 22
    FLAG = 23
    FLAGCAPTURETIME = 24
    FLAGRETURN = 25
    TO = 26
    BY = 27
    WHITESPACE = 28
    NEWLINE = 29
    BACK_SLASH = 30
    COLON = 31
    MINUS = 32
    DOUBLE_QUOTE = 33
    DIGIT = 34
    ANY_CHAR = 35

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'------------------------------------------------------------'", 
            "'InitGame'", "'InitRound'", "'InitAuth'", "'ShutdownGame'", 
            "'Warmup'", "'Session data initialised for client on slot'", 
            "'at'", "'ClientConnect'", "'ClientDisconnect'", "'ClientBegin'", 
            "'ClientSpawn'", "'ClientUserinfo'", "'ClientUserinfoChanged'", 
            "'AccountValidated'", "'say'", "'saytell'", "'sayteam'", "'Radio'", 
            "'tell'", "'Kill'", "'Item'", "'Flag'", "'FlagCaptureTime'", 
            "'Flag Return'", "'to'", "'by'", "'\\'", "':'", "'-'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "SEPARATOR", "INITGAME", "INITROUND", "INITAUTH", "SHUTDOWNGAME", 
            "WARMUP", "SESSION_DATA_INITIALISED", "AT", "CLIENTCONNECT", 
            "CLIENTDISCONNECT", "CLIENTBEGIN", "CLIENTSPAWN", "CLIENTUSERINFO", 
            "CLIENTUSERINFOCHANGED", "ACCOUNTVALIDATED", "SAY", "SAYTELL", 
            "SAYTEAM", "RADIO", "TELL", "KILL", "ITEM", "FLAG", "FLAGCAPTURETIME", 
            "FLAGRETURN", "TO", "BY", "WHITESPACE", "NEWLINE", "BACK_SLASH", 
            "COLON", "MINUS", "DOUBLE_QUOTE", "DIGIT", "ANY_CHAR" ]

    ruleNames = [ "SEPARATOR", "INITGAME", "INITROUND", "INITAUTH", "SHUTDOWNGAME", 
                  "WARMUP", "SESSION_DATA_INITIALISED", "AT", "CLIENTCONNECT", 
                  "CLIENTDISCONNECT", "CLIENTBEGIN", "CLIENTSPAWN", "CLIENTUSERINFO", 
                  "CLIENTUSERINFOCHANGED", "ACCOUNTVALIDATED", "SAY", "SAYTELL", 
                  "SAYTEAM", "RADIO", "TELL", "KILL", "ITEM", "FLAG", "FLAGCAPTURETIME", 
                  "FLAGRETURN", "TO", "BY", "WHITESPACE", "NEWLINE", "BACK_SLASH", 
                  "COLON", "MINUS", "DOUBLE_QUOTE", "DIGIT", "ANY_CHAR" ]

    grammarFileName = "Events.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


