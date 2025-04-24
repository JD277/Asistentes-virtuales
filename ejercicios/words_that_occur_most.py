import string

def procesar_palabra(palabra):
    palabra = palabra.strip(string.punctuation)
    return palabra.lower()

def encontrar_palabra_mas_frecuente(nombre_archivo):
    frecuencia_palabras = {}
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras = linea.split()
                for palabra in palabras:
                    palabra_procesada = procesar_palabra(palabra)
                    if palabra_procesada:
                        if palabra_procesada in frecuencia_palabras:
                            frecuencia_palabras[palabra_procesada] += 1
                        else:
                            frecuencia_palabras[palabra_procesada] = 1
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
    
    if not frecuencia_palabras:
        print("El archivo está vacío o no contiene palabras válidas.")
        return None
    
    palabra_mas_frecuente = max(frecuencia_palabras.items(), key=lambda x: x[1])
    return palabra_mas_frecuente

def main():
    nombre_archivo = input("Por favor, ingrese el nombre del archivo: ")
    resultado = encontrar_palabra_mas_frecuente(nombre_archivo)
    
    if resultado:
        palabra, frecuencia = resultado
        print(f"La palabra más frecuente es '{palabra}' que aparece {frecuencia} veces.")

if __name__ == "__main__":
    main()