%{
#include "G2.tab.h"
#include <string.h>

char yyline[1024];  // buffer para la línea completa
int idx = 0;
%}

%%

a       { yyline[idx++] = 'a'; return A; }
b       { yyline[idx++] = 'b'; return B; }
\n      { yyline[idx] = '\0'; idx = 0; return '\n'; }
[ \t]+  { /* ignorar */ }
.       { /* ignorar otros caracteres */ }

%%
int yywrap(void) { return 1; }
