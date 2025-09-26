from ExprFuncVisitor import ExprFuncVisitor
from ExprFuncParser import ExprFuncParser
import math

class EvalVisitor(ExprFuncVisitor):
    def __init__(self):
        self.memory = {}
        self.use_degrees = True

    def angle(self, x):
        return math.radians(x) if self.use_degrees else x

    def visitAssign(self, ctx:ExprFuncParser.AssignContext):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    def visitPrintExpr(self, ctx:ExprFuncParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0.0

    def visitInt(self, ctx:ExprFuncParser.IntContext):
        return float(ctx.INT().getText())

    def visitFloat(self, ctx:ExprFuncParser.FloatContext):
        return float(ctx.FLOAT().getText())

    def visitId(self, ctx:ExprFuncParser.IdContext):
        id_ = ctx.ID().getText()
        return self.memory.get(id_, 0.0)

    def visitMulDiv(self, ctx:ExprFuncParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ExprFuncParser.MUL:
            return left * right
        return left / right

    def visitAddSub(self, ctx:ExprFuncParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ExprFuncParser.ADD:
            return left + right
        return left - right

    def visitParens(self, ctx:ExprFuncParser.ParensContext):
        return self.visit(ctx.expr())

    def visitFuncExpr(self, ctx:ExprFuncParser.FuncExprContext):
        value = self.visit(ctx.expr())
        func = ctx.func().getText()
        if func == "sin": return math.sin(self.angle(value))
        if func == "cos": return math.cos(self.angle(value))
        if func == "tan": return math.tan(self.angle(value))
        if func == "sqrt": return math.sqrt(value)
        if func == "log": return math.log10(value)
        if func == "ln": return math.log(value)
        raise Exception(f"Función desconocida: {func}")

    def visitFactorialExpr(self, ctx:ExprFuncParser.FactorialExprContext):
        value = self.visit(ctx.expr())
        if not value.is_integer():
            raise Exception(f"Factorial solo definido para enteros: {value}")
        return self.factorial(int(value))

    def factorial(self, n: int):
        if n < 0:
            raise Exception(f"Factorial no definido para negativos: {n}")
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

