archivo = "entrada4.txt"

def pertenece_g4(cadena):
    cadena = cadena.strip()
    return cadena in {"ab", "abb"}

def validar_lineas(lineas):
    for linea in lineas:
        linea_clean = linea.strip()
        resultado = pertenece_g4(linea_clean)
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
