
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None

    return a / b


print("=== CALCULADORA PYTHON ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha uma operação: ")

if opcao not in ("1", "2", "3", "4"):
    print("Opção inválida.")
else:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = somar(numero1, numero2)

        elif opcao == "2":
            resultado = subtrair(numero1, numero2)

        elif opcao == "3":
            resultado = multiplicar(numero1, numero2)

        else:
            resultado = dividir(numero1, numero2)

        if resultado is None:
            print("Erro: divisão por zero não é permitida.")
        else:
            print(f"Resultado: {resultado:g}")

    except ValueError:
        print("Erro: digite apenas números válidos.")
