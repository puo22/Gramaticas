import re

archivo = "entrada3.txt"

def pertenece_g3(cadena):
    cadena = cadena.strip()
    if cadena == "":
        return False

    a_count = cadena.count('a')
    b_count = cadena.count('b')

    # Debe ser solo a y b
    if not re.fullmatch(r'[ab]+', cadena):
        return False

    # Cadena mínima "b" válida
    if cadena == "b":
        return True

    # Verificar regla de G3: b_count = a_count + 1
    if b_count == a_count + 1:
        return True

    return False

def validar_lineas(lineas):
    for linea in lineas:
        linea_clean = linea.strip()
        resultado = pertenece_g3(linea_clean)
        print(f'{linea_clean} -> {"acepta" if resultado else "NO acepta"}')

def validar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            lineas = f.read().splitlines()
        validar_lineas(lineas)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_archivo}")

def main():
    validar_archivo(archivo)

if __name__ == "__main__":
    main()
