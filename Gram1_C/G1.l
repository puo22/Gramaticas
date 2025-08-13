%{
#include "G1.tab.h"
#include <string.h>
%}

%%
[01]+   { yylval.str = strdup(yytext); return CADENA; }
\n      { /* ignorar salto de línea */ }
.       { /* ignorar cualquier otro caracter */ }
%%
