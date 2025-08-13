%{
#include <stdio.h>
#include <stdlib.h>

extern char yyline[];  // buffer definido en el lexer
void yyerror(const char *s);
int yylex(void);
%}

%token A B

%%

input:
      | input line
;

line:
      S '\n' { printf("%s -> acepta\n", yyline); }
    | error '\n' { yyerrok; printf("%s -> NO acepta\n", yyline); }
;

S:
      B
    | A S B
    | /* vacío */
;

%%

void yyerror(const char *s) {
    /* No hacer nada aquí, la acción del parser imprime NO acepta */
}

int main(int argc, char **argv) {
    extern FILE *yyin;

    if (argc == 2) {
        yyin = fopen(argv[1], "r");
        if (!yyin) { perror(argv[1]); return 1; }
    } else {
        yyin = stdin;
    }

    yyparse();

    if (argc == 2) fclose(yyin);

    return 0;
}
