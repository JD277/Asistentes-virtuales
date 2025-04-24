def sumador_interactivo():
    suma_total = 0.0
    
    print("Sumador interactivo (ingrese una línea en blanco para terminar)")
    
    while True:
        entrada = input("Ingrese un número: ").strip()
        if entrada == "":
            print("Programa terminado. Suma final:", suma_total)
            break
        
        try:
            numero = float(entrada)
            if '.' not in entrada:
                numero = int(entrada)
            
            suma_total += numero
            print("Suma actual:", suma_total)
            
        except ValueError:
            print("Error: Entrada no válida. Por favor ingrese un número válido o línea en blanco para terminar.")
if __name__ == "__main__":
    sumador_interactivo()