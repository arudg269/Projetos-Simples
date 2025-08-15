def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Raiz quadrada de número negativo não é permitida.")
    return a ** 0.5

def calculadora():
    while True:
        print("\nBem-vindo à Calculadora!")
        print("Selecione a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potência")
        print("6 - Raiz Quadrada")
        print("7 - Sair")

        operacao = input("Digite o número da operação desejada: ")

        if operacao == "7":
            print("Saindo da calculadora...")
            break  

        try:

            if operacao in ('1', '2', '3', '4', '5'):
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            elif operacao == '6':
                a = float(input("Digite o número: "))
            else:
                print("Opção inválida. Por favor, tente novamente.")
                continue 

            if operacao == "1":
                resultado = soma(a, b)
            elif operacao == "2":
                resultado = subtracao(a, b)
            elif operacao == "3":
                resultado = multiplicacao(a, b)
            elif operacao == "4":
                resultado = divisao(a, b)
            elif operacao == "5":
                resultado = potencia(a, b)
            elif operacao == "6":
                resultado = raiz_quadrada(a)
            
            print(f"\nO resultado é: {resultado}")

        except ValueError as e:
            print(f"\nErro: {e}")
        
if __name__ == "__main__":
    calculadora()