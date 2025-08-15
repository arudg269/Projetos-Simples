from calculadora import calculadora
from conversor import conversor_temperatura
from horas import conversor_horas
from binario import conversor_binario
from doom_game import run_doom_game

def menu():
    
    print(" _______  _______  _        _______           _        _______  ______   _______  _______  _______   ")
    print("(  ____ \(  ___  )( \      (  ____ \|\     /|( \      (  ___  )(  __  \ (  ___  )(  ____ )(  ___  )  ")
    print("| (    \/| (   ) || (      | (    \/| )   ( || (      | (   ) || (  \  )| (   ) || (    )|| (   ) |  ")
    print("| |      | (___) || |      | |      | |   | || |      | (___) || |   ) || |   | || (____)|| (___) |  ")
    print("| |      |  ___  || |      | |      | |   | || |      |  ___  || |   | || |   | ||     __)|  ___  |  ")
    print("| |      | (   ) || |      | |      | |   | || |      | (   ) || |   ) || |   | || (\ (   | (   ) |  ")
    print("| (____/\| )   ( || (____/\| (____/\| (___) || (____/\| )   ( || (__/  )| (___) || ) \ \__| )   ( |  ")
    print("(_______/|/     \|(_______/(_______/(_______)(_______/|/     \|(______/ (_______)|/   \__/|/     \|  ")
    print("                                                                                                     ")
    
    while True:
        print("\nSelecione uma opção:")
        print("1 - Calculadora")
        print("2 - Conversor de Temperatura")
        print("3 - Conversor de Horas")
        print("4 - binario")
        print("5 - Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            print("Iniciando a Calculadora...")
            print("-" * 30)
            calculadora()

        elif opcao == "2":
            print("Iniciando o Conversor de Temperatura...")
            print("-" * 30)
            conversor_temperatura()

        elif opcao == "3":
            print("Iniciando o Conversor de Horas...")
            print("-" * 30)
            conversor_horas()
            
        elif opcao == "4":
            print ("iniciando o conversor binário...")
            print("-" * 30)
            conversor_binario()
            
        elif opcao == "doom":
            print("Iniciando o Jogo Doom (Pygame)...")
            print("-" * 30)
            run_doom_game()
                
        elif opcao == "5":
            print("Saindo do programa...")
            break  # Interrompe o loop
        else:
            print("Opção inválida. Por favor, tente novamente.")
            
if __name__ == "__main__":
    menu()