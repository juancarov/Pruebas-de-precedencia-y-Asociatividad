# Generated from ExprFuncAlt.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprFuncAltParser import ExprFuncAltParser
else:
    from ExprFuncAltParser import ExprFuncAltParser

# This class defines a complete generic visitor for a parse tree produced by ExprFuncAltParser.

class ExprFuncAltVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprFuncAltParser#prog.
    def visitProg(self, ctx:ExprFuncAltParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#printExpr.
    def visitPrintExpr(self, ctx:ExprFuncAltParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#assign.
    def visitAssign(self, ctx:ExprFuncAltParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#blank.
    def visitBlank(self, ctx:ExprFuncAltParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#Float.
    def visitFloat(self, ctx:ExprFuncAltParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#AddSub.
    def visitAddSub(self, ctx:ExprFuncAltParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#MulDiv.
    def visitMulDiv(self, ctx:ExprFuncAltParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#Parens.
    def visitParens(self, ctx:ExprFuncAltParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#Id.
    def visitId(self, ctx:ExprFuncAltParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#FuncExpr.
    def visitFuncExpr(self, ctx:ExprFuncAltParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#Int.
    def visitInt(self, ctx:ExprFuncAltParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#FactorialExpr.
    def visitFactorialExpr(self, ctx:ExprFuncAltParser.FactorialExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncAltParser#func.
    def visitFunc(self, ctx:ExprFuncAltParser.FuncContext):
        return self.visitChildren(ctx)



del ExprFuncAltParser