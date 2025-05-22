# Interpreter kodu w Pythonie na melodię

## Autorki
Natalia Marcinkowska - natmar@student.agh.edu.pl

Michalina Kujawa - mkujawa@student.agh.edu.pl

## Założenia projektu 🎧
Celem projektu jest stworzenie interpretera, który analizuje kod napisany w języku Python i przekształca jego strukturę składniową na melodię. 
Program nie wymaga żadnych muzycznych komend w kodzie źródłowym – użytkownik podaje zwykły fragment Pythona (np. funkcję, pętlę, wyrażenia warunkowe), a interpreter automatycznie przekształca jego składniki na odpowiadające im elementy muzyczne.

Rodzaj translatora: Interpreter

Język implementacji: Python

Planowany wynik działania: Plik .midi

Skaner/parser: ANTLR4

Dodatkowe biblioteki w Pythonie: denterhelper, mido, pygame

### Jak działa? 🎤

Kod Pythona jest analizowany przez skaner, który dzieli go na tokeny (np. identyfikatory, liczby, operatory, słowa kluczowe). Parser oparty na własnej gramatyce rozpoznaje struktury takie jak pętle, funkcje, instrukcje warunkowe itp. Każdy element gramatyczny jest mapowany na odpowiedni motyw muzyczny.

Na podstawie rozpoznanych reguł produkcji generowana jest melodia za pomocą syntezatora dźwięku w Pythonie.
## Tokeny 🎶

[Lista tokenów](tokeny/tokeny)

## Gramatyka 🎼

G = (T, V, S, P)

T = {

        'def', 'if', 'else', 'elif', 'while', 'for', 'in', 'print', 'import', 
        'from', 'as', 'return', 'pass', 'true', 'false', 'none',
        '+', '-', '*', '/', '%', '=', '+=', '-=', '*=', '/=',
        '==', '!=', '<', '>', '<=', '>=',
        '(', ')', '[', ']', '{', '}', ':', ',', '.', ';',
        ID, NUM, STRING
        
}

V = {

        program, stmt, simple_stmt, compound_stmt, assign_stmt, assign_op, 
        expr_stmt, print_stmt, import_stmt, return_stmt,
        func_def, if_stmt, while_stmt, for_stmt, block,
        param_list, dotted_name, function_call, expr, arith_expr, bool_expr, 
        logic_const, list_expr, dict_expr, elements, kv_pairs,
        module, alias, name, rel_op, log_op
        
}

S = program

P = {

        program         → stmt+ EOF
    
        stmt            → simple_stmt | compound_stmt
    
        simple_stmt     → (assign_stmt | expr_stmt | print_stmt | import_stmt | return_stmt) NEWLINE
    
        compound_stmt   → func_def | if_stmt | while_stmt | for_stmt
    
        func_def        → 'def' ID '(' param_list? ')' ':' block
    
        if_stmt         → 'if' expr ':' block ('elif' expr ':' block)* ('else' ':' block)?
    
        while_stmt      → 'while' expr ':' block
    
        for_stmt        → 'for' ID 'in' expr ':' block
    
        block           → INDENT stmt+ DEDENT | simple_stmt
    
        assign_stmt     → ID assign_op expr
    
        assign_op       → '=' | '+=' | '-=' | '*=' | '/='
    
        expr_stmt       → function_call
    
        print_stmt      → 'print' '(' expr (',' expr)* ')'
    
        import_stmt     → 'import' module ('as' alias)? | 'from' module 'import' name
    
        return_stmt     → 'return' expr?
    
        param_list      → ID (',' ID)*
    
        function_call   → dotted_name '(' (expr (',' expr)*)? ')'
    
        expr            → arith_expr | bool_expr | logic_const | list_expr | dict_expr | STRING | function_call

        dotted_name     → ID ('.' ID)* ;
        
        arith_expr      → ID | NUM | STRING
                        | arith_expr '+' arith_expr | arith_expr '-' arith_expr
                        | arith_expr '*' arith_expr | arith_expr '/' arith_expr
                        | arith_expr '%' arith_expr | '(' arith_expr ')'
                        | dotted_name;
    
        bool_expr       → arith_expr rel_op arith_expr
                        | bool_expr log_op bool_expr
                        | '(' bool_expr ')'
    
        logic_const     → 'true' | 'false' | 'none'
    
        list_expr       → '[' elements? ']'
    
        elements        → expr (',' expr)*
    
        dict_expr       → '{' kv_pairs? '}'
    
        kv_pairs        → expr ':' expr (',' expr ':' expr)*
    
        module          → ID ('.' ID)*
    
        alias           → ID
    
        name            → ID
    
        rel_op          → '==' | '!=' | '<' | '>' | '<=' | '>='
    
        log_op          → 'and' | 'or' | 'not'
        
}


## Użyte generatory, skanery, parsery
ANTLR4

## Przykład użycia

##
