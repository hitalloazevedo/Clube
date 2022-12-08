from interface import *
from calculos import *
from sys import exit

author = 'Alunos do Clube'
version = 'v0.0.2'

# Muito obrigado pela preferência Github: @HitalloAzevedo

def main():
    while True:
        cabecalho(f'MENU ESCOLAR {version}')
        print(f'Criado por {author}')
        print('=' * 60)

        opcao = menu('Progressão Aritmética',
        'Progressão Geométrica',
        'Fibonacci',
        'Função Primeiro Grau',
        'Função Segundo Grau',
        'Logaritmo')


        match opcao:
            case 99:
                print('Obrigado por usar!')
                input('Pressione ENTER para sair!')
                exit()

            case 1:
                limpar()
                PA()
                while True:
                    r = resposta()
                    if r == 'n':
                        limpar()
                        main()
                    else:
                        limpar()
                        PA()

            case 2:
                limpar()
                PG()
                while True:
                    r = resposta()
                    if r == 'n':
                        limpar()
                        main()
                    else:
                        limpar()
                        PG()

            case 3:
                limpar()
                fibonacci()
                while True:
                    r = resposta()
                    if r == 'n':
                        limpar()
                        main()
                    else:
                        limpar()
                        fibonacci()

            case 4:
                limpar()
                funcao_primeiro()
                while True:
                    r = resposta()
                    if r == 'n':
                        limpar()
                        main()
                    else:
                        limpar()
                        funcao_primeiro()

            case 5:
                limpar()
                funcao_segundo()
                while True:
                    r = resposta()
                    if r == 'n':
                        limpar()
                        main()
                    else:
                        limpar()
                        funcao_segundo()

            case 6:
                limpar()
                logaritmo()
                while True:
                    r = resposta()
                    if r == 'n':
                        limpar()
                        main()
                    else:
                        limpar()
                        logaritmo()


if __name__ == '__main__':
    main()
