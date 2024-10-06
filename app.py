import os

def exibir_nome_do_programa():

  print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
  
def exibir_opcoes():
      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurante')
      print('3. Ativar Restaurante')
      print('4. Sair\n')

def finalizar_app():
    os.system('cls') #clear
    print('Finalizando o app')

def escolher_opcao():
   try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
       cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
       opcao_invalida()
   except:
    opcao_invalida()


def opcao_invalida():
    print('Opção inválida')
    input('Digite uma tecla para voltar ao Menu Principal\n')
    main()

def cadastrar_novo_restaurante():
    pass

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    

    
if __name__ == '__main__':
    main()