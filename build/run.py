import sys, os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyverilog.vparser.lexer import VerilogLexer
#from examples.example_parser import main

class ParseError(Exception):
    pass

def _coord(lex, lineno, column=None):
    ret = [lex.filename]
    ret.append('line:%s' % lineno)
    if column is not None:
        ret.append('column:%s' % column)
    return ' '.join(ret)

def _lexer_error_func(lex, msg, line, column):
    coord = _coord(lex, line, column)
    raise ParseError('%s: %s' % (coord, msg))

lexer = VerilogLexer(error_func=_lexer_error_func)
lexer.build()
with open("verilogcode/fsm.sv", 'r') as fin:
    lines = fin.read()
lexer.lexer.input(lines)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
#main("vrilogcode/fsm.sv")
#os.system("examples/example_parser.py verilogcode/fsm.sv")
