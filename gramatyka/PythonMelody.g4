grammar PythonMelody;

tokens { INDENT, DEDENT }

@lexer::header {
from antlr_denter.DenterHelper import DenterHelper
from PythonMelodyParser import PythonMelodyParser
}

@lexer::members {
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
}

// Parser rules
program     : stmt+ EOF;

stmt        : simple_stmt | compound_stmt;

simple_stmt : (assign_stmt | expr_stmt | print_stmt | import_stmt | return_stmt) NEWLINE;
compound_stmt: (func_def | if_stmt | while_stmt | for_stmt);

func_def    : 'def' ID '(' param_list? ')' ':' block;
if_stmt     : 'if' expr ':' block ('elif' expr ':' block)* ('else' ':' block)?;
while_stmt  : 'while' expr ':' block;
for_stmt    : 'for' ID 'in' expr ':' block;

block       : INDENT stmt+ DEDENT
                | simple_stmt;

assign_stmt : ID assign_op expr;
assign_op   : '='| '+=' | '-=' | '*=' | '/=';
expr_stmt   : function_call;
print_stmt  : 'print' '(' expr (',' expr)*')';
import_stmt : 'import' module ('as' alias)?
            | 'from' module 'import' name;
return_stmt : 'return' expr?;

param_list  : ID (',' ID)*;

expr            : arith_expr
                | bool_expr
                | logic_const
                | list_expr
                | dict_expr
                | STRING
                | function_call ;

dotted_name : ID ('.' ID)* ;

function_call : dotted_name '(' (expr (',' expr)*)? ')';

arith_expr      : ID
                | NUM
                | STRING
                | arith_expr '+' arith_expr
                | arith_expr '-' arith_expr
                | arith_expr '*' arith_expr
                | arith_expr '/' arith_expr
                | arith_expr '%' arith_expr
                | '(' arith_expr ')'
                | dotted_name;

bool_expr       : arith_expr rel_op arith_expr
                | bool_expr log_op bool_expr
                | '(' bool_expr ')' ;

logic_const     : 'true' | 'false' | 'none' ;

list_expr   : '[' elements? ']';
elements    : expr (',' expr)*;
dict_expr   : '{' kv_pairs? '}';
kv_pairs    : expr ':' expr (',' expr ':' expr)*;

module      : ID ('.' ID)*;
alias       : ID;
name        : ID;

rel_op      : '==' | '!=' | '<' | '>' | '<=' | '>=';
log_op      : 'and' | 'or'| 'not';

// Lexer rules
NEWLINE     : ('\r'? '\n' [ \t]*);
INDENT      : ;
DEDENT      : ;
WS          : [ \t\r]+ -> skip;
COMMENT     : '#' ~[\r\n]* -> skip;

DEF     : 'def';
IF      : 'if';
ELSE    : 'else';
ELIF    : 'elif';
WHILE   : 'while';
FOR     : 'for';
IN      : 'in';
PRINT   : 'print';
IMPORT  : 'import';
FROM    : 'from';
AS      : 'as';
RETURN  : 'return';
PASS    : 'pass';
TRUE    : 'true';
FALSE   : 'false';
NONE    : 'none';
AND     : 'and';
OR      : 'or';
NOT     : 'not';

PLUS    : '+';
MINUS   : '-';
STAR    : '*';
SLASH   : '/';
PERCENT : '%';

EQ      : '=';
EQEQ    : '==';
NEQ     : '!=';
LT      : '<';
GT      : '>';
LE      : '<=';
GE      : '>=';
PLUSEQ   : '+=';
MINUSEQ  : '-=';
STAREQ   : '*=';
SLASHEQ  : '/=';

LPAREN  : '(';
RPAREN  : ')';
LBRACK  : '[';
RBRACK  : ']';
LBRACE  : '{';
RBRACE  : '}';
COLON   : ':';
COMMA   : ',';
DOT     : '.';
SEMICOLON : ';';

fragment LETTER : [a-zA-Z\u0100-\u017F_];
fragment ESC    : '\\' .;

ID      : LETTER (LETTER | [0-9])*;
NUM     : [0-9]+ ('.' [0-9]+)? ([eE][+-]?[0-9]+)?;
STRING  : '"' (~["\\\r\n] | ESC)* '"'
        | '\'' (~['\\\r\n] | ESC)* '\'';