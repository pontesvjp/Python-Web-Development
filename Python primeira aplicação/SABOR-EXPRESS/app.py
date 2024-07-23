import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]


def exibir_nome_do_programa():
    print('Sabor Express\n')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')
    print('5. Recomeçar')


def finalizar_app():
    exibir_subtitulo('finalizando app')


def voltar_ao_menu_principal():
    input('\ndigite uma tecla para voltar')
    main()


def recomeçar():
    os.system('cls')
    os.system('python app.py')


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


def opcao_invalida():
    print('opcao invalida\n')
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():

    exibir_subtitulo('cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'deseje o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'digite o nome da categoria do restaurante {
                      nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'\no restaurante {
          nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('listando os restuarante')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()


def altenar_estado_do_restaurante():
    exibir_subtitulo('alterando estado do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alternar o estado: ')
    rastaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {
                nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('restaurante não encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if (opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            altenar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        elif opcao_escolhida == 5:
            recomeçar()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
