# Operaciones Matemáticas básicas

def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print(sumar(5, 3))


def restar(a, b):
    return a - b

if __name__ == "__main__":
    print(restar(5, 3))


def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    print(multiplicar(5, 3))


def dividir(a, b):
    try:
        return round((a / b), 3)
    except ZeroDivisionError:
        print("Error. No se puede dividir entre cero")

if __name__ == "__main__":
    print(dividir(5, 3))