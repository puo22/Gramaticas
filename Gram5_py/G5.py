archivo = "entrada5.txt"

def pertenece_g5(cadena):
    cadena = cadena.strip()
    if cadena == "":
        return False

    if cadena == "ab":
        return True

    if cadena[0] == 'a' and cadena[-1] == 'b':
        interior = cadena[1:-1]
        if interior == "":
            return True  # Caso n=0
        if interior.count("ab") * 2 == len(interior):
            i = 0
            while i < len(interior):
                if interior[i:i+2] != "ab":
                    return False
                i += 2
            return True
    return False

def validar_lineas(lineas):
    for linea in lineas:
        linea_clean = linea.strip()
        resultado = pertenece_g5(linea_clean)
        print(f'{linea_clean} -> {"acepta" if resultado else "NO acepta"}')

def validar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            lineas = f.read().split()
        validar_lineas(lineas)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_archivo}")

def main():
    validar_archivo(archivo)

if __name__ == "__main__":
    main()
