%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
int es_capicua(char *cadena); /* Prototipo */

extern FILE *yyin; /* Para que Flex use el archivo */
%}

%union {
    char* str;
}

%token <str> CADENA

%%

input:
    /* vacío */
    | input CADENA {
        if (es_capicua($2)) {
            printf("%s -> Acepta\n", $2);
        } else {
            printf("%s -> No acepta\n", $2);
        }
        free($2);
    }
;

%%

int es_capicua(char *cadena) {
    int len = strlen(cadena);
    for (int i = 0; i < len / 2; i++) {
        if (cadena[i] != cadena[len - i - 1])
            return 0;
    }
    return 1;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }

    yyin = fopen(argv[1], "r");
    if (!yyin) {
        perror("No se pudo abrir el archivo");
        return 1;
    }

    yyparse();
    fclose(yyin);
    return 0;
}

