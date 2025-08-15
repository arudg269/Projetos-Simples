def horas_para_minutos(horas):
    return horas * 60

def minutos_para_horas(minutos):
    return minutos / 60

def horas_para_segundos(horas):
    return horas * 3600

def segundos_para_horas(segundos):
    return segundos / 3600

def minutos_para_segundos(minutos):
    return minutos * 60

def segundos_para_minutos(segundos):
    return segundos / 60

def convertorde24para12(hora24):
    if not isinstance(hora24, int) or hora24 < 0 or hora24 > 23:
        raise ValueError("Hora inválida. Deve ser um número inteiro entre 0 e 23.")
    
    periodo = "AM" if hora24 < 12 else "PM"
    hora12 = hora24 % 12
    if hora12 == 0:
        hora12 = 12
    return f"{hora12} {periodo}"

def conversor_horas():
    while True:
        print("\nBem-vindo ao Conversor de Horas!")
        print("Selecione a conversão desejada:")
        print("1 - Horas para Minutos")
        print("2 - Minutos para Horas")
        print("3 - Horas para Segundos")
        print("4 - Segundos para Horas")
        print("5 - Minutos para Segundos")
        print("6 - Segundos para Minutos")
        print("7 - Conversor de 24h para 12h")
        print("8 - Sair")

        operacao = input("Digite o número da operação desejada: ")

        if operacao == "8":
            print("Saindo do conversor de horas...")
            break

        try:
            if operacao == '7':
                valor = int(input("Digite a hora (0-23): "))
                resultado = convertorde24para12(valor)
                print(f"Resultado: {resultado}")
                
            elif operacao in ('1', '2', '3', '4', '5', '6'):
                valor = float(input("Digite o valor: "))
                
                if operacao == "1":
                    resultado = horas_para_minutos(valor)
                    unidade = "minutos"
                elif operacao == "2":
                    resultado = minutos_para_horas(valor)
                    unidade = "horas"
                elif operacao == "3":
                    resultado = horas_para_segundos(valor)
                    unidade = "segundos"
                elif operacao == "4":
                    resultado = segundos_para_horas(valor)
                    unidade = "horas"
                elif operacao == "5":
                    resultado = minutos_para_segundos(valor)
                    unidade = "segundos"
                elif operacao == "6":
                    resultado = segundos_para_minutos(valor)
                    unidade = "minutos"
                    
                print(f"Resultado: {resultado} {unidade}")

            else:
                print("Opção inválida. Por favor, tente novamente.")
                
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira um número válido.")
            
if __name__ == "__main__":
    conversor_horas()