%{
#include "G5.tab.h"
#include <stdio.h>
#include <string.h>
%}

%%

a(ab)*b  { return CADENA; }  // Reconoce cadenas válidas
[ \t\n]+ { /* ignorar espacios y saltos de línea */ }
.       { return yytext[0]; }

%%
int yywrap(void) { return 1; }
