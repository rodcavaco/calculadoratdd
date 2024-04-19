
def subtract(a, b):
    return a - b 


def divide(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por 0")
    return a / b

if __name__ == "__main__":
    while True:
        print("Selecione a operação:")
        print("1. Subtração")
        print("2. Divisão")
        print("3. Adição")
        print("4. Multiplicação")
        print("5. Sair")

        choice = input("Digite a opção (1/2/3/4/5): ")

        if choice == '5':
            print("Adeus.")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print("Resultado:", subtract(num1, num2))
        elif choice == '2':
            try:
                print("Resultado:", divide(num1, num2))
            except ValueError as e:
                print("Erro:", e)
        else:
            print("Opção inválida. Por favor, digite novamente.")
