import math

def calcular_raizes(a, b, c):
    if a == 0:
        print("A equação não é do segundo grau.")
        return
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print("A equação possui uma raiz real:", raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print("A equação possui duas raízes reais:", raiz1, "e", raiz2)

def main():
    a = float(input("Digite o valor de a: "))
    if a == 0:
        print("O valor de 'a' não pode ser zero para uma equação do segundo grau.")
        return
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    calcular_raizes(a, b, c)

if __name__ == "__main__":
    main()

