n = int(input("ingrese un numero: "))
divisores = 0
def get_prime(n):
    global divisores
    for i in range(1, n):
        if n % i == 0:
            divisores += 1
        if divisores > 3:
            print(f"{n}No es primo")
            return
    print(f"{n} Es primo")
get_prime(n)