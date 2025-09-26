import sys
from antlr4 import *
from ExprFuncAltLexer import ExprFuncAltLexer as ExprFuncLexer
from ExprFuncAltParser import ExprFuncAltParser as ExprFuncParser
from EvalVisitor import EvalVisitor

def main(argv):
    input_stream = FileStream(argv[1] if len(argv) > 1 else None or sys.stdin.fileno())
    lexer = ExprFuncLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprFuncParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
