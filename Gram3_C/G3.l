%{
#include "G3.tab.h"
#include <string.h>
%}

%%

a   { return A; }
b   { return B; }
\n  { return '\n'; }
[ \t]+  { /* ignorar espacios */ }
.   { return yytext[0]; }

%%
int yywrap(void) { return 1; }

