# Generated from PythonMelody.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from PythonMelodyParser import PythonMelodyParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u015e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\5\2s\n\2")
        buf.write("\3\2\3\2\7\2w\n\2\f\2\16\2z\13\2\3\3\3\3\3\4\3\4\3\5\6")
        buf.write("\5\u0081\n\5\r\5\16\5\u0082\3\5\3\5\3\6\3\6\7\6\u0089")
        buf.write("\n\6\f\6\16\6\u008c\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(")
        buf.write("\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\7\66\u012e\n\66\f\66\16\66\u0131")
        buf.write("\13\66\3\67\6\67\u0134\n\67\r\67\16\67\u0135\3\67\3\67")
        buf.write("\6\67\u013a\n\67\r\67\16\67\u013b\5\67\u013e\n\67\3\67")
        buf.write("\3\67\5\67\u0142\n\67\3\67\6\67\u0145\n\67\r\67\16\67")
        buf.write("\u0146\5\67\u0149\n\67\38\38\38\78\u014e\n8\f8\168\u0151")
        buf.write("\138\38\38\38\38\78\u0157\n8\f8\168\u015a\138\38\58\u015d")
        buf.write("\n8\2\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write("I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\2i\2k\65m\66")
        buf.write("o\67\3\2\13\4\2\13\13\"\"\5\2\13\13\17\17\"\"\4\2\f\f")
        buf.write("\17\17\6\2C\\aac|\u0102\u0181\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\6\2\f\f\17\17$$^^\6\2\f\f\17\17))^^\2\u016c\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\3r\3\2\2\2\5{\3\2\2\2\7}\3\2\2\2\t")
        buf.write("\u0080\3\2\2\2\13\u0086\3\2\2\2\r\u008f\3\2\2\2\17\u0093")
        buf.write("\3\2\2\2\21\u0096\3\2\2\2\23\u009b\3\2\2\2\25\u00a0\3")
        buf.write("\2\2\2\27\u00a6\3\2\2\2\31\u00aa\3\2\2\2\33\u00ad\3\2")
        buf.write("\2\2\35\u00b3\3\2\2\2\37\u00ba\3\2\2\2!\u00bf\3\2\2\2")
        buf.write("#\u00c2\3\2\2\2%\u00c9\3\2\2\2\'\u00ce\3\2\2\2)\u00d3")
        buf.write("\3\2\2\2+\u00d9\3\2\2\2-\u00de\3\2\2\2/\u00e2\3\2\2\2")
        buf.write("\61\u00e5\3\2\2\2\63\u00e9\3\2\2\2\65\u00eb\3\2\2\2\67")
        buf.write("\u00ed\3\2\2\29\u00ef\3\2\2\2;\u00f1\3\2\2\2=\u00f3\3")
        buf.write("\2\2\2?\u00f5\3\2\2\2A\u00f8\3\2\2\2C\u00fb\3\2\2\2E\u00fd")
        buf.write("\3\2\2\2G\u00ff\3\2\2\2I\u0102\3\2\2\2K\u0105\3\2\2\2")
        buf.write("M\u0108\3\2\2\2O\u010b\3\2\2\2Q\u010e\3\2\2\2S\u0111\3")
        buf.write("\2\2\2U\u0113\3\2\2\2W\u0115\3\2\2\2Y\u0117\3\2\2\2[\u0119")
        buf.write("\3\2\2\2]\u011b\3\2\2\2_\u011d\3\2\2\2a\u011f\3\2\2\2")
        buf.write("c\u0121\3\2\2\2e\u0123\3\2\2\2g\u0125\3\2\2\2i\u0127\3")
        buf.write("\2\2\2k\u012a\3\2\2\2m\u0133\3\2\2\2o\u015c\3\2\2\2qs")
        buf.write("\7\17\2\2rq\3\2\2\2rs\3\2\2\2st\3\2\2\2tx\7\f\2\2uw\t")
        buf.write("\2\2\2vu\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y\4\3\2")
        buf.write("\2\2zx\3\2\2\2{|\3\2\2\2|\6\3\2\2\2}~\3\2\2\2~\b\3\2\2")
        buf.write("\2\177\u0081\t\3\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2")
        buf.write("\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\b\5\2\2\u0085\n\3\2\2\2\u0086\u008a")
        buf.write("\7%\2\2\u0087\u0089\n\4\2\2\u0088\u0087\3\2\2\2\u0089")
        buf.write("\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\u008d\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008e\b")
        buf.write("\6\2\2\u008e\f\3\2\2\2\u008f\u0090\7f\2\2\u0090\u0091")
        buf.write("\7g\2\2\u0091\u0092\7h\2\2\u0092\16\3\2\2\2\u0093\u0094")
        buf.write("\7k\2\2\u0094\u0095\7h\2\2\u0095\20\3\2\2\2\u0096\u0097")
        buf.write("\7g\2\2\u0097\u0098\7n\2\2\u0098\u0099\7u\2\2\u0099\u009a")
        buf.write("\7g\2\2\u009a\22\3\2\2\2\u009b\u009c\7g\2\2\u009c\u009d")
        buf.write("\7n\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2\u009f\24")
        buf.write("\3\2\2\2\u00a0\u00a1\7y\2\2\u00a1\u00a2\7j\2\2\u00a2\u00a3")
        buf.write("\7k\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7g\2\2\u00a5\26")
        buf.write("\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9")
        buf.write("\7t\2\2\u00a9\30\3\2\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac")
        buf.write("\7p\2\2\u00ac\32\3\2\2\2\u00ad\u00ae\7r\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\34\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7o\2\2\u00b5\u00b6\7r\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7t\2\2\u00b8\u00b9\7v\2\2\u00b9\36\3\2\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write("\7o\2\2\u00be \3\2\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1")
        buf.write("\7u\2\2\u00c1\"\3\2\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7")
        buf.write("\7t\2\2\u00c7\u00c8\7p\2\2\u00c8$\3\2\2\2\u00c9\u00ca")
        buf.write("\7r\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7u\2\2\u00cd&\3\2\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2\7g\2\2\u00d2(\3")
        buf.write("\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7n\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8\7g\2\2\u00d8*\3")
        buf.write("\2\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7g\2\2\u00dd,\3\2\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7f\2\2\u00e1.\3")
        buf.write("\2\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4\60")
        buf.write("\3\2\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\62\3\2\2\2\u00e9\u00ea\7-\2\2\u00ea\64\3")
        buf.write("\2\2\2\u00eb\u00ec\7/\2\2\u00ec\66\3\2\2\2\u00ed\u00ee")
        buf.write("\7,\2\2\u00ee8\3\2\2\2\u00ef\u00f0\7\61\2\2\u00f0:\3\2")
        buf.write("\2\2\u00f1\u00f2\7\'\2\2\u00f2<\3\2\2\2\u00f3\u00f4\7")
        buf.write("?\2\2\u00f4>\3\2\2\2\u00f5\u00f6\7?\2\2\u00f6\u00f7\7")
        buf.write("?\2\2\u00f7@\3\2\2\2\u00f8\u00f9\7#\2\2\u00f9\u00fa\7")
        buf.write("?\2\2\u00faB\3\2\2\2\u00fb\u00fc\7>\2\2\u00fcD\3\2\2\2")
        buf.write("\u00fd\u00fe\7@\2\2\u00feF\3\2\2\2\u00ff\u0100\7>\2\2")
        buf.write("\u0100\u0101\7?\2\2\u0101H\3\2\2\2\u0102\u0103\7@\2\2")
        buf.write("\u0103\u0104\7?\2\2\u0104J\3\2\2\2\u0105\u0106\7-\2\2")
        buf.write("\u0106\u0107\7?\2\2\u0107L\3\2\2\2\u0108\u0109\7/\2\2")
        buf.write("\u0109\u010a\7?\2\2\u010aN\3\2\2\2\u010b\u010c\7,\2\2")
        buf.write("\u010c\u010d\7?\2\2\u010dP\3\2\2\2\u010e\u010f\7\61\2")
        buf.write("\2\u010f\u0110\7?\2\2\u0110R\3\2\2\2\u0111\u0112\7*\2")
        buf.write("\2\u0112T\3\2\2\2\u0113\u0114\7+\2\2\u0114V\3\2\2\2\u0115")
        buf.write("\u0116\7]\2\2\u0116X\3\2\2\2\u0117\u0118\7_\2\2\u0118")
        buf.write("Z\3\2\2\2\u0119\u011a\7}\2\2\u011a\\\3\2\2\2\u011b\u011c")
        buf.write("\7\177\2\2\u011c^\3\2\2\2\u011d\u011e\7<\2\2\u011e`\3")
        buf.write("\2\2\2\u011f\u0120\7.\2\2\u0120b\3\2\2\2\u0121\u0122\7")
        buf.write("\60\2\2\u0122d\3\2\2\2\u0123\u0124\7=\2\2\u0124f\3\2\2")
        buf.write("\2\u0125\u0126\t\5\2\2\u0126h\3\2\2\2\u0127\u0128\7^\2")
        buf.write("\2\u0128\u0129\13\2\2\2\u0129j\3\2\2\2\u012a\u012f\5g")
        buf.write("\64\2\u012b\u012e\5g\64\2\u012c\u012e\t\6\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012d\u012c\3\2\2\2\u012e\u0131\3\2\2\2\u012f")
        buf.write("\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130l\3\2\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0132\u0134\t\6\2\2\u0133\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3")
        buf.write("\2\2\2\u0136\u013d\3\2\2\2\u0137\u0139\7\60\2\2\u0138")
        buf.write("\u013a\t\6\2\2\u0139\u0138\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013e\3")
        buf.write("\2\2\2\u013d\u0137\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0148")
        buf.write("\3\2\2\2\u013f\u0141\t\7\2\2\u0140\u0142\t\b\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2")
        buf.write("\u0143\u0145\t\6\2\2\u0144\u0143\3\2\2\2\u0145\u0146\3")
        buf.write("\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149")
        buf.write("\3\2\2\2\u0148\u013f\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("n\3\2\2\2\u014a\u014f\7$\2\2\u014b\u014e\n\t\2\2\u014c")
        buf.write("\u014e\5i\65\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u015d")
        buf.write("\7$\2\2\u0153\u0158\7)\2\2\u0154\u0157\n\n\2\2\u0155\u0157")
        buf.write("\5i\65\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015d\7")
        buf.write(")\2\2\u015c\u014a\3\2\2\2\u015c\u0153\3\2\2\2\u015dp\3")
        buf.write("\2\2\2\24\2rx\u0082\u008a\u012d\u012f\u0135\u013b\u013d")
        buf.write("\u0141\u0146\u0148\u014d\u014f\u0156\u0158\u015c\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class PythonMelodyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NEWLINE = 1
    INDENT = 2
    DEDENT = 3
    WS = 4
    COMMENT = 5
    DEF = 6
    IF = 7
    ELSE = 8
    ELIF = 9
    WHILE = 10
    FOR = 11
    IN = 12
    PRINT = 13
    IMPORT = 14
    FROM = 15
    AS = 16
    RETURN = 17
    PASS = 18
    TRUE = 19
    FALSE = 20
    NONE = 21
    AND = 22
    OR = 23
    NOT = 24
    PLUS = 25
    MINUS = 26
    STAR = 27
    SLASH = 28
    PERCENT = 29
    EQ = 30
    EQEQ = 31
    NEQ = 32
    LT = 33
    GT = 34
    LE = 35
    GE = 36
    PLUSEQ = 37
    MINUSEQ = 38
    STAREQ = 39
    SLASHEQ = 40
    LPAREN = 41
    RPAREN = 42
    LBRACK = 43
    RBRACK = 44
    LBRACE = 45
    RBRACE = 46
    COLON = 47
    COMMA = 48
    DOT = 49
    SEMICOLON = 50
    ID = 51
    NUM = 52
    STRING = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'if'", "'else'", "'elif'", "'while'", "'for'", "'in'", 
            "'print'", "'import'", "'from'", "'as'", "'return'", "'pass'", 
            "'true'", "'false'", "'none'", "'and'", "'or'", "'not'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'='", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'+='", "'-='", "'*='", "'/='", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "':'", "','", "'.'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "INDENT", "DEDENT", "WS", "COMMENT", "DEF", "IF", 
            "ELSE", "ELIF", "WHILE", "FOR", "IN", "PRINT", "IMPORT", "FROM", 
            "AS", "RETURN", "PASS", "TRUE", "FALSE", "NONE", "AND", "OR", 
            "NOT", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", "EQ", "EQEQ", 
            "NEQ", "LT", "GT", "LE", "GE", "PLUSEQ", "MINUSEQ", "STAREQ", 
            "SLASHEQ", "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", 
            "RBRACE", "COLON", "COMMA", "DOT", "SEMICOLON", "ID", "NUM", 
            "STRING" ]

    ruleNames = [ "NEWLINE", "INDENT", "DEDENT", "WS", "COMMENT", "DEF", 
                  "IF", "ELSE", "ELIF", "WHILE", "FOR", "IN", "PRINT", "IMPORT", 
                  "FROM", "AS", "RETURN", "PASS", "TRUE", "FALSE", "NONE", 
                  "AND", "OR", "NOT", "PLUS", "MINUS", "STAR", "SLASH", 
                  "PERCENT", "EQ", "EQEQ", "NEQ", "LT", "GT", "LE", "GE", 
                  "PLUSEQ", "MINUSEQ", "STAREQ", "SLASHEQ", "LPAREN", "RPAREN", 
                  "LBRACK", "RBRACK", "LBRACE", "RBRACE", "COLON", "COMMA", 
                  "DOT", "SEMICOLON", "LETTER", "ESC", "ID", "NUM", "STRING" ]

    grammarFileName = "PythonMelody.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class PythonMelodyDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer = lexer

        def pull_token(self):
            return super(PythonMelodyLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.PythonMelodyDenter(
                self, self.NEWLINE, PythonMelodyParser.INDENT, PythonMelodyParser.DEDENT, False
            )
        return self.denter.next_token()


