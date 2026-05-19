from colorama import Style, Fore, Back, init
init(autoreset=True)
import dados
import utils

def cadastrar_aluno():
    # cadastrar os alunos pedindo às informações necessárias para o treino.
    utils.exibir_menu('CADASTRO ALUNO(A)')

    nome_aluno = input(Style.BRIGHT + 'Informe o seu nome: ')
    modalidade = input(Style.BRIGHT + 'Informe a modalidade (ex: musculação, pernas): ')
    dias_semana = utils.ler_inteiro(Style.BRIGHT + 'Dias por semana (1-7): ')
    objetivo = input(Style.BRIGHT + 'Informe seu objetivo: ')
    
    # montar o dicionário do aluno com as regras do pdf.
    novo_aluno = {
    'nome': nome_aluno,
    'modalidade': modalidade,
    'dias_semana': dias_semana,
    'objetivo': objetivo,
    'status': 'Ativo',
    'sessoes': []
    }

    dados.lista_aluno.append(novo_aluno)

    print(Style.BRIGHT + Fore.GREEN + f'\n- ✅ Aluno(a) {nome_aluno} Cadastrado(a) Com Sucesso!')
    input(Style.BRIGHT + '\nAperte ENTER para voltar ao menu...')

def listar_alunos():
    utils.exibir_menu('LISTA DE ALUNOS')

    if len(dados.lista_aluno) == 0:
        print(Style.BRIGHT + Fore.RED + '\n- 📭 Nenhum aluno(a) cadastrado no sistema!')
        input(Style.BRIGHT + '\nPressione ENTER para voltar ao menu...')
        return

    # exibir os dados formatados na tela acessando as chaves do dicionário.
    for aluno in dados.lista_aluno:
        print(f'- Nome: {aluno['nome']}')
        print(f'- Modalidade: {aluno['modalidade']}')
        print(f'- Treinos por Semana: {aluno['dias_semana']}x')
        print(f'Objetivo: {aluno['objetivo']}')
        print(f'Status: {aluno['status']}')
        print('=' * 40)

        input('\nPressione ENTER para voltar ao menu...')

def entrar_fila():
    utils.exibir_menu('ENTRAR NA FILA DE ATENDIMENTO')
    nome_atendimento = input(Style.BRIGHT + 'Informe o nome do aluno que chegou: ')

    # adiciona o aluno no FINAL da fila (fifo).
    dados.fila_atendimento.append(nome_atendimento)
    print(Style.BRIGHT +Fore.GREEN + f'\n- {nome_atendimento} foi adicionado(a) à fila!')
    input(Style.BRIGHT + '\nPressione ENTER para voltar ao menu...')

def atender_aluno():
    utils.exibir_menu('ATENDER PRÓXIMO ALUNO')

    # validar: se a fila estiver vazia não terá ninguém para atender.
    if len(dados.fila_atendimento) == 0:
        print(Style.BRIGHT + Fore.RED + '\n- 📭 Fila de atendimento vazia!')
        return
    
    proximo = dados.fila_atendimento.pop(0)
    print(Style.BRIGHT + f'\n- Atendendo agora: {proximo}')

def registrar_treino():
    utils.exibir_menu('REGISTRAR CHECK-IN DE TREINO')

    # se não tiver alunos cadastrados irá avisar e sair.
    if len(dados.lista_aluno) == 0:
        print(Style.BRIGHT + Fore.RED + '\n- 📭 Nenhum aluno cadastrado para registrar treino!')
        return
    
    nome_busca = input('Digite o nome do aluno para o check-in: ')
    aluno_encontrado = None

    # loop para procurar o aluno pelo nome.
    for aluno in dados.lista_aluno:
        if aluno ['nome'].lower() == nome_busca.lower():
            aluno_encontrado = aluno
            break
        
    if aluno_encontrado is None:
        print(Style.BRIGHT + Fore.RED + f'\n- ❌ Aluno(a) "{nome_busca}" não foi encontrado(a)!')
        return
    
    # a var 'aluno_encontrado' guarda o dicionário daquele aluno específico.
    print(Style.BRIGHT + f'Aluno selecionado {aluno_encontrado['nome']}')
    data_treino = input(Style.BRIGHT + 'Digite a data do treino (ex: 01/01/2026): ')

    aluno_encontrado['sessoes'].append(data_treino)
    print(Style.BRIGHT + Fore.GREEN + f'\n- ✅ Check-in realizado com sucesso! Treino do dia {data_treino} adicionado ao histórico.')

def visualizar_historico():
    utils.exibir_menu('HISTÓRICO DE TREINOS')

    if len(dados.lista_aluno) == 0:
        print(f'\n- 📭 Nenhum Aluno(a) Cadastrado no Sistema!')
        return
    
    nome_busca = input(Style.BRIGHT + 'Digite o nome do aluno (histórico): ')
    aluno_encontrado = None

    for aluno in dados.lista_aluno:
        if aluno['nome'].lower() == nome_busca.lower():
            aluno_encontrado = aluno
            break
    if aluno_encontrado is None:
        print(Style.BRIGHT + Fore.RED + f'\n- ❌ Aluno(a) "{nome_busca}" não foi encontrado(a)!')
        return
    
    utils.exibir_menu(Style.BRIGHT + f'Treinos de {aluno_encontrado['nome']}')

    # validação da pilha: se a lista de sessões estiver vazia.
    if len(aluno_encontrado['sessoes']) == 0:
        print(Style.BRIGHT + Fore.RED + '\n- Este aluno não realizou nenhum treino!')
        return

    # exibição em lifo: assim lendo a pilha do topo para baixo (no caso mas recente primeiro).
    print(Style.BRIGHT + '\n- Hisórico do mais recente ao mais antigo:\n')
    for treino in reversed(aluno_encontrado['sessoes']):
        print(Style.BRIGHT + f'- Treino realizado em: {treino}')
    
    print('=' * 40)
