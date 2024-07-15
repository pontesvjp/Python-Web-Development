import os 
def exibir_nome_do_programa():
    print('Sabor Express')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finalizar_app():
    os.system('cls')
    print('finalizando app\n')
    
def opcao_invalida():
        print('opcao invalida\n')
        input('digite uma tecla para voltar')
        main()
        

def escolher_opcao(): 
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if (opcao_escolhida == 1):
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('listar restaurantes')
        elif opcao_escolhida == 3:
            print('ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    
