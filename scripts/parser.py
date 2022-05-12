import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, default, words, combined
from pygments.util import get_bool_opt, shebang_matches
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Generic, Other
from .uni import xid_start, xid_continue

__all__ = ['ChimeraLexer']

line_re = re.compile('.*?\n')


class ChimeraLexer(RegexLexer):
    name = 'Chimera'
    aliases = ['chimera','chi']
    filenames = ['*.chi']
    mimetypes = ['text/x-chimera', 'application/x-chimera']

    flags = re.MULTILINE | re.UNICODE

    uni_name = "[%s][%s-]*[\?!]?" % (xid_start, xid_continue)
    name_first_upper = "[A-Z][%s-]*" % xid_continue
    op_chars = r"=!\?><\+\|~/\*%&^\.\\:`"+"\u2200\u2201\u2203-\u220d\u220f-\u2214\u2217-\u2222\u2224\u2226\u2227-\u2235\u2238-\u22d7\u22da-\u22ff"

    def innerstring_rules(ttype):
        return [
            # the new style '{}'.format(...) string formatting
            (r'\{'
             r'((\w+)((\.\w+)|(\[[^\]]+\]))*)?'  # field name
             r'(\:(.?[<>=\^])?[-+ ]?#?0?(\d+)?,?(\.\d+)?[E-GXb-gnosx%]?)?'
             r'\}', String.Interpol),

            # backslashes, quotes and formatting signs must be parsed one at a time
            (r'[^\\\'"%{\n]+', ttype),
            (r'[\'"\\]', ttype),
            # unhandled string formatting sign
            (r'%|(\{{1,2})', ttype)
            # newlines are an error (use "nl" state)
        ]

    tokens = {
        'root': [
            (r'\nC>|^C>', Name.Label),
            (r'\n', Text),
            (r'#{', Comment.Multiline, 'comment'),
            (r'#\?.+$', Comment.Special),
            (r'#.*$', Comment.Single),
            (r'(fn|gen)(\s+)', bygroups(Keyword, Text), 'funcname'),
            include('expr'),
        ],
        'comment': [
            (r'[^}]+', Comment.Multiline),
            (r'#{', Comment.Multiline, '#push'),
            (r'}*', Comment.Multiline, '#pop'),
        ],
        'expr': [
            ('(""")', bygroups(String.Double), combined('stringescape', 'tdqs')),
            ("(''')", bygroups(String.Single), combined('stringescape', 'tsqs')),
            ('(")', bygroups(String.Double), combined('stringescape', 'dqs')),
            ("(')", bygroups(String.Single), combined('stringescape', 'sqs')),
            (r'\s+', Text),
            include('numbers'),
            (r'[%s]+' % op_chars, Operator),
            (r'[{}:()\[\],;]', Punctuation),
            include('keywords'),
            include('builtins'),
            (r'Error\b', Name.Exception),
            (name_first_upper, Name.Class),
            (uni_name, Name.Variable),
            (r'(in|is|and|or|not)\b', Operator.Word),
            ("-", Operator)
        ],
        'keywords': [
            (words((
                'assert', 'async', 'await', 'break', 'continue', 'else', 'for', 'then', 'raise',
                'if', 'return', 'while', 'yield', 'as', 'with', 'self'), suffix=r'[\s\n$]'),
             Keyword),
            (words(('true', 'false'), suffix=r'[\s\n$]'), Keyword.Constant)
        ],
        'builtins': [
            (words(( 'abs', 'all', 'any', 'eval', 'filter', 'iter', 'list', 'map', 'max', 'min', 'next', 'pow', 'print', 'property',
                'range', 'reverse', 'round', 'slice', 'sort', 'sum', 'super', 'tuple', 'type', 'zip'), prefix=r'!?', suffix=r'[\s\n$]'),
             Name.Builtin)
        ],
        'funcname': [
            include('builtins'),
            (uni_name, Name.Function, '#pop'),
            default('#pop'),
        ],
        'numbers': [
            (r'\d(?:_?\d)*\.\d(?:_?\d)*[eE][+-]?\d*', Number.Float),
            (r'\d(?:_?\d)*[eE][+-]?\d*', Number.Float),
            (r'0[oO](?:_?[0-7])+', Number.Oct),
            (r'0[bB](?:_?[01])+', Number.Bin),
            (r'0[xX](?:_?[a-fA-F0-9])+', Number.Hex),
            (r'\d(?:_?\d)*', Number.Integer),
        ],
        'stringescape': [
            (r'\\([\\abfnrtv"\']|\n|N\{.*?\}|u[a-fA-F0-9]{4}|'
             r'U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})', String.Escape)
        ],
        'strings-single': innerstring_rules(String.Single),
        'strings-double': innerstring_rules(String.Double),
        'dqs': [
            (r'"', String.Double, '#pop'),
            (r'\\\\|\\"|\\\n', String.Escape),  # included here for raw strings
            include('strings-double')
        ],
        'sqs': [
            (r"'", String.Single, '#pop'),
            (r"\\\\|\\'|\\\n", String.Escape),  # included here for raw strings
            include('strings-single')
        ],
        'tdqs': [
            (r'"""', String.Double, '#pop'),
            include('strings-double'),
            (r'\n', String.Double)
        ],
        'tsqs': [
            (r"'''", String.Single, '#pop'),
            include('strings-single'),
            (r'\n', String.Single)
        ],
    }

    def analyse_text(text):
        return True
