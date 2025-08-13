import sys
import re

def gramatica1(cadena):
    # Solo acepta cadenas formadas por 0 y 1
    if not re.fullmatch(r"[01]+", cadena):
        return False
    # Comprueba si es palíndromo
    return cadena == cadena[::-1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 G1.py <entrada1.txt>")
        sys.exit(1)

    ruta_archivo = sys.argv[1]

    try:
        with open(ruta_archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()
                if cadena:  # Ignorar líneas vacías
                    if gramatica1(cadena):
                        print(f"{cadena} -> Acepta")
                    else:
                        print(f"{cadena} -> No acepta")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
