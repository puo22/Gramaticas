import re
import sys

# ------------------------------
# Archivo por defecto
# ------------------------------
archivo_por_defecto = "entrada2.txt"

# ------------------------------
# Función que verifica la gramática
# ------------------------------
def pertenece_lenguaje(cadena):
    cadena = cadena.strip()
    if cadena == "":
        # Cadena vacía (ε) válida
        return True
    # Verificar que la cadena tenga solo a* b+
    if not re.fullmatch(r'a*b+', cadena):
        return False
    # Contar 'a' y 'b'
    a_count = cadena.count('a')
    b_count = cadena.count('b')
    # Validar que b_count = a_count + 1
    return b_count == a_count + 1

# ------------------------------
# Función que valida líneas
# ------------------------------
def validar_lineas(lineas):
    for linea in lineas:
        linea_clean = linea.strip()
        resultado = pertenece_lenguaje(linea_clean)
        print(f'{linea_clean} -> {"acepta" if resultado else "NO acepta"}')

# ------------------------------
# Función que valida archivo
# ------------------------------
def validar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            lineas = f.read().splitlines()
        validar_lineas(lineas)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_archivo}")

# ------------------------------
# Programa principal
# ------------------------------
def main():
    # Si hay un argumento, usarlo como archivo
    if len(sys.argv) == 2:
        validar_archivo(sys.argv[1])
    else:
        # Intentar abrir archivo por defecto
        try:
            validar_archivo(archivo_por_defecto)
        except FileNotFoundError:
            # Si no existe, leer desde stdin
            print("Ingrese cadenas (Ctrl+D para terminar):")
            lineas = sys.stdin.read().splitlines()
            validar_lineas(lineas)

if __name__ == "__main__":
    main()
