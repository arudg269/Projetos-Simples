def decimal_para_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario

def binario_para_decimal(binario_str):
    decimal = 0
    for i, digito in enumerate(reversed(binario_str)):
        if digito == '1':
            decimal += 2**i
        elif digito != '0':
            raise ValueError("Entrada inválida. Apenas '0' e '1' são permitidos.")
    return decimal

def conversor_binario():
    while True:
        print("\n--- Conversor Binário ---")
        print("1 - Decimal para Binário")
        print("2 - Binário para Decimal")
        print("3 - Voltar ao Menu Principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == '3':
            print("Voltando ao menu principal...")
            break

        try:
            if opcao == '1':
                decimal_valor = int(input("Digite um número decimal: "))
                if decimal_valor < 0:
                    raise ValueError("Apenas números inteiros não-negativos são suportados.")
                
                resultado = decimal_para_binario(decimal_valor)
                print(f"O número {decimal_valor} em binário é: {resultado}")
            
            elif opcao == '2':
                binario_valor = input("Digite um número binário: ")
                resultado = binario_para_decimal(binario_valor)
                print(f"O número binário {binario_valor} em decimal é: {resultado}")

            else:
                print("Opção inválida. Por favor, tente novamente.")
        
        except ValueError as e:
            print(f"\nErro: {e}")