%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex(void);
extern FILE *yyin;

void yyerror(const char *s);
%}

%token A B

%%

input:
      | input line
      ;

line:
      S '\n' { printf("acepta\n"); }
    | error '\n' { yyerrok; printf("NO acepta\n"); }
    ;

S:
      B
    | A S B
    | A B
    ;

%%

void yyerror(const char *s) {
    printf("NO acepta\n");
}

int main(int argc, char **argv) {
    if(argc != 2) {
        fprintf(stderr, "Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if(!f) { perror(argv[1]); return 1; }
    yyin = f;

    yyparse();

    fclose(f);
    return 0;
}
