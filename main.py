# menu principal para rodar tudo do tarefas.py

import os
from colorama import Style, Fore, Back, init
import tarefas
import utils

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpar_tela()
        utils.exibir_menu('ACADEMIA - MENU PRINCIPAL')
        
        print(Style.BRIGHT + "1 - Cadastrar aluno(a)")
        print(Style.BRIGHT + "2 - Lista de alunos ativos")
        print(Style.BRIGHT + "3 - Entrar na fila de atendimento")
        print(Style.BRIGHT + "4 - Atender Próximo Aluno")
        print(Style.BRIGHT + "5 - Registrar check-in de treino")
        print(Style.BRIGHT + "6 - Visualizar histórico de treinos")
        print(Style.BRIGHT + Fore.RED + "0 - Encerrar programa")
        print(Style.BRIGHT + '=' * 40)
        
        opcao = int(input(Style.BRIGHT + "Escolha uma opção (1-6): "))
        
        # match para escolher alguma opção do menu.
        match opcao:
            case 1:
                limpar_tela()
                tarefas.cadastrar_aluno()
            case 2:
                limpar_tela()
                tarefas.listar_alunos()
            case 3:
                limpar_tela()
                tarefas.entrar_fila()
            case 4:
                limpar_tela()
                tarefas.atender_aluno()
            case 5:
                limpar_tela()
                tarefas.registrar_treino()
            case 6:
                limpar_tela()
                tarefas.visualizar_historico()
            case 0:
                limpar_tela()
                print(Style.BRIGHT + Fore.RED + '\nEncerrando programa...')
                break
            case _:
                print(Style.BRIGHT + Fore.RED + '\nOpção inválida! Tente novamente...')
                input(Style.BRIGHT + '\nPressione ENTER para confirmar...')

if __name__ == "__main__":
    menu_principal()
