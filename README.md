---

# **Implementación en Python**

## Librerías necesarias

* Python 3 (ya trae `re` integrado, no hay que instalarlo)
* No requiere librerías externas

Verificar instalación:

```bash
python3 --version
```

---

## Paso a paso

**Ejemplo con G1 (`S -> 00 | 11 | 0 | 1`)**

1. **Crear archivo de código**

```bash
nano G1.py
```

2. **Pegar el código** (usa `re` para expresiones regulares):

```python
import sys, re

def acepta(s: str) -> bool:
    return re.fullmatch(r'(0|1|00|11)', s) is not None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python3 G1.py <archivo.txt>"); sys.exit(1)
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            if not s: continue
            print(f"{s} -> {'Acepta' if acepta(s) else 'No acepta'}")
```

3. **Crear archivo de entrada**

```bash
nano entrada1.txt
```

Ejemplo de contenido:

```
0
1
00
11
10
101
```

4. **Ejecutar**

```bash
python3 G1.py entrada1.txt
```

---

Repite lo mismo para **G2–G5** usando el código que te pasé antes, cambiando la función `acepta()`.

---

# **Implementación en C con Flex y Bison**

## Librerías necesarias

Instalar Flex y Bison (si no los tienes):

```bash
sudo apt update
sudo apt install flex bison gcc
```

Verificar:

```bash
flex --version
bison --version
gcc --version
```

---

## Paso a paso

**Ejemplo con G1 (`S -> 00 | 11 | 0 | 1`)**

1. **Crear directorio**

```bash
mkdir Gram1_C
cd Gram1_C
```

2. **Crear archivo lexer (`G1.l`)**

```bash
nano G1.l
```

Contenido:

```c
%{
#include "G1.tab.h"
#include <string.h>
#include <stdlib.h>
%}

%%
[01]+   { yylval.str = strdup(yytext); return CADENA; }
\n      { /* ignorar */ }
.       { /* ignorar */ }
%%
```

3. **Crear archivo parser (`G1.y`)**

```bash
nano G1.y
```

Contenido:

```c
%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
int acepta(const char *s);
%}

%union { char *str; }
%token <str> CADENA

%%
input:
      /* vacío */
    | input CADENA {
        printf("%s -> %s\n", $2, acepta($2) ? "Acepta" : "No acepta");
        free($2);
      }
    ;
%%

int acepta(const char *s) {
    return (strcmp(s,"0")==0) || (strcmp(s,"1")==0) ||
           (strcmp(s,"00")==0) || (strcmp(s,"11")==0);
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
```

4. **Crear archivo de entrada**

```bash
nano entrada1c.txt
```

Contenido:

```
0
1
00
11
10
101
```

5. **Compilar**

```bash
bison -d G1.y
flex G1.l
gcc G1.tab.c lex.yy.c -o G1 -lfl
```

6. **Ejecutar**

```bash
./G1 < entrada1c.txt
```

---

## Resumen de comandos en C

```bash
# Compilar parser
bison -d G1.y
# Compilar lexer
flex G1.l
# Generar ejecutable
gcc G1.tab.c lex.yy.c -o G1 -lfl
# Ejecutar con archivo de entrada
./G1 < entrada1c.txt
```

---

**Notas importantes:**

* En C, el archivo `.l` y `.y` deben coincidir en nombre (`G1.l` / `G1.y`).
* Para **G2–G5** solo cambias:

  * Regla de tokens en `.l` (`[01]+` → `[ab]+`)
  * Función `acepta()` en `.y`

---

Si quieres, ahora te puedo hacer un **README.md listo para tu práctica** con estos pasos explicados para G1–G5.
