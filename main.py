#organizando o main.py ainda

from colorama import Style, Fore, Back, init
init(autoreset=True)

import tarefas
import utils

def menu_principal():
    print(Style.BRIGHT + '=' * 40)
    print(Style.BRIGHT + 'MENU PRINCIPAL ACADEMIA'.center(40))
    print(Style.BRIGHT + '=' * 40)
    print('- 1 Cadastrar Aluno(a)')
    print('- 2 Listar Alunos')
    print('- 3 Fila de Atendimento')
    print('- 4 Atender Próximo Aluno')
    print('- 5 Check-in de Treino')
    print('- 6 Histórico de Treinos')
    print(Style.BRIGHT + Fore.RED + '- 0 Encerrar ')
    print(Style.BRIGHT + '=' * 40)

def main():
    while True:
        menu_principal()
        opcoes = int(input('Escolha uma opção (1-6): '))

        match opcoes:
            case 1:
                tarefas.cadastrar_aluno()
            case 2:
                tarefas.listar_alunos()
            case 3:
                tarefas.entrar_fila()
            case 4:
                tarefas.atender_aluno()
            case 5:
                tarefas.registrar_treino()
            case 6:
                tarefas.visualizar_historico()
            case 0:
                print(Style.BRIGHT + Fore.RED + 'Encerrando Sistema...')

            case _:
                print(Style.BRIGHT + Fore.RED + 'Opção Inválida, Tente Novamente!')
    
if __name__ == '__main__':
    main()
