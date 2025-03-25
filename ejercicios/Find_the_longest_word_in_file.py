import os

def crear_archivo_txt(nombre_archivo, contenido):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print(f"Archivo '{nombre_archivo}' creado exitosamente.")

def encontrar_palabra_mas_larga(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    palabras = texto.split()

    palabra_mas_larga = max(palabras, key=len)

    print(f"La palabra más larga es: '{palabra_mas_larga}' con {len(palabra_mas_larga)} caracteres.")

def crear_y_abrir_archivo_txt(nombre_archivo, contenido):
    crear_archivo_txt(nombre_archivo, contenido)

    if os.name == "nt":  
        os.startfile(nombre_archivo)
    elif os.name == "posix":  
        os.system(f"open {nombre_archivo}")  
    else:
        print("Sistema operativo no compatible para abrir el archivo automáticamente.")

def main():
    contenido = """Este es el primer párrafo del archivo de texto. Contiene varias palabras de diferentes longitudes.
Este es el segundo párrafo. Aquí también hay palabras largas como 'esternocleidomastoideo' y 'electroencefalografía'.
El encefalografista de esternocleidomastoideo utiliza su acido desoxirribonucleico para idear una solucion para curarse de la hipopotomonstrosesquipedaliofobia
.
"""

    nombre_archivo = input("Ingresa el nombre del archivo (incluye la extensión .txt): ")

    crear_y_abrir_archivo_txt(nombre_archivo, contenido)

    encontrar_palabra_mas_larga(nombre_archivo)

    eliminar = input("¿Deseas eliminar el archivo? (s/n): ").lower()
    if eliminar == "s":
        os.remove(nombre_archivo)
        print(f"Archivo '{nombre_archivo}' eliminado exitosamente.")
    else:
        print("El archivo no fue eliminado.")

if __name__ == "__main__":
    main()