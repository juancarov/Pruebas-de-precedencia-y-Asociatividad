grammar ExprFuncAlt;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr: expr op=('+'|'-') expr      # AddSub
    | expr op=('*'|'/') expr      # MulDiv
    | func '(' expr ')'           # FuncExpr
    | expr '!'                    # FactorialExpr
    | INT                         # Int
    | FLOAT                       # Float
    | ID                          # Id
    | '(' expr ')'                # Parens
    ;

func:   'sin'
    |   'cos'
    |   'tan'
    |   'sqrt'
    |   'log'
    |   'ln'
    ;

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
FLOAT:	[0-9]+'.'[0-9]+;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;

