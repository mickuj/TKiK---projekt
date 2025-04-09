grammar PythonMelody;

program        : stmt_list EOF ;
stmt_list      : stmt stmt_list | /* epsilon */ ;
stmt           : if_stmt
               | while_stmt
               | for_stmt
               | func_def
               | assign_stmt
               | expr_stmt
               | print_stmt
               | import_stmt
               | break_stmt
               | continue_stmt
               | return_stmt
               | false_val
               | true_val
               | none_val ;

if_stmt        : 'if' expr ':' stmt_list 'else' ':' stmt_list ;
while_stmt     : 'while' expr ':' stmt_list ;
for_stmt       : 'for' ID 'in' expr ':' stmt_list ;
print_stmt     : 'print' '(' expr ')' ;
import_stmt    : 'import' module ('as' alias)?
               | 'from' module 'import' name ;
func_def       : 'def' ID '(' param_list? ')' ':' stmt_list ;
assign_stmt    : ID '=' expr ;
expr_stmt      : expr ;
break_stmt     : 'break' ;
continue_stmt  : 'continue' ;
return_stmt    : 'return' expr ;
false_val      : 'false' ;
true_val       : 'true' ;
none_val       : 'none' ;

param_list     : ID (',' ID)* ;
expr           : expr op=('*'|'/') expr
               | expr op=('+'|'-') expr
               | expr op=('%'|'=='|'!='|'<'|'>'|'<='|'>=') expr
               | '(' expr ')'
               | ID
               | NUM ;

module         : ID ('.' ID)* ;
alias          : ID ;
name           : ID ;

// === LEXER RULES ===

ID             : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM            : [0-9]+ ;
WS             : [ \t\r\n]+ -> skip ;
