def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

def conversor_temperatura():
    while True:
        print("\nBem-vindo ao Conversor de Temperatura!")
        print("Selecione a conversão desejada:")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        print("3 - Celsius para Kelvin")
        print("4 - Kelvin para Celsius")
        print("5 - Fahrenheit para Kelvin")
        print("6 - Kelvin para Fahrenheit")
        print("7 - Sair")

        operacao = input("Digite o número da operação desejada: ")

        if operacao == "7":
            print("Saindo do conversor de temperatura...")
            break

        try:
            if operacao in ('1', '2', '3', '4', '5', '6'):
                temperatura = float(input("Digite a temperatura: "))
            else:
                print("Opção inválida. Por favor, tente novamente.")
                continue

            if operacao == "1":
                resultado = celsius_para_fahrenheit(temperatura)
                unidade = "Fahrenheit"
            elif operacao == "2":
                resultado = fahrenheit_para_celsius(temperatura)
                unidade = "Celsius"
            elif operacao == "3":
                resultado = celsius_para_kelvin(temperatura)
                unidade = "Kelvin"
            elif operacao == "4":
                resultado = kelvin_para_celsius(temperatura)
                unidade = "Celsius"
            elif operacao == "5":
                resultado = fahrenheit_para_kelvin(temperatura)
                unidade = "Kelvin"
            elif operacao == "6":
                resultado = kelvin_para_fahrenheit(temperatura)
                unidade = "Fahrenheit"
                
            print(f"Resultado: {resultado} {unidade}")
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira um número válido.")
            
if __name__ == "__main__":
    conversor_temperatura()