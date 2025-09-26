# Generated from ExprFunc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprFuncParser import ExprFuncParser
else:
    from ExprFuncParser import ExprFuncParser

# This class defines a complete generic visitor for a parse tree produced by ExprFuncParser.

class ExprFuncVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprFuncParser#prog.
    def visitProg(self, ctx:ExprFuncParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#printExpr.
    def visitPrintExpr(self, ctx:ExprFuncParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#assign.
    def visitAssign(self, ctx:ExprFuncParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#blank.
    def visitBlank(self, ctx:ExprFuncParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#Float.
    def visitFloat(self, ctx:ExprFuncParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#MulDiv.
    def visitMulDiv(self, ctx:ExprFuncParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#AddSub.
    def visitAddSub(self, ctx:ExprFuncParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#Parens.
    def visitParens(self, ctx:ExprFuncParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#Id.
    def visitId(self, ctx:ExprFuncParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#FuncExpr.
    def visitFuncExpr(self, ctx:ExprFuncParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#Int.
    def visitInt(self, ctx:ExprFuncParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#FactorialExpr.
    def visitFactorialExpr(self, ctx:ExprFuncParser.FactorialExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprFuncParser#func.
    def visitFunc(self, ctx:ExprFuncParser.FuncContext):
        return self.visitChildren(ctx)



del ExprFuncParser