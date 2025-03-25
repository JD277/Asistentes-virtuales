print("introduzca la edad de su perro")

def edad_de_tu_perro(años_humanos):

    if años_humanos < 0:
        print("eres subnormal o te caiste de chiquito")
    
    if años_humanos <= 0:
        print("0")
    
    if años_humanos == 1:
        print("10.5")
    
    if años_humanos == 2:
        return 21
    
    if años_humanos >= 3:
        return 21 + (años_humanos - 2) *4