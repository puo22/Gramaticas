%{
#include "G4.tab.h"
#include <string.h>
#include <stdio.h>
%}

%%

abb     { return CADENA; }
ab      { return CADENA; }
a       { return CADENA; }
b       { return CADENA; }
[ \t\n]+  { /* ignorar espacios y saltos de línea */ }

%%
int yywrap(void) { return 1; }
