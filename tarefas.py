import dados
import utils

def cadastrar_aluno():
    # cadastrar os alunos pedindo às informações necessárias para o treino.
    utils.exibir_menu('👤 CADASTRO ALUNO(A) 👤')

    nome_aluno = input('Informe o seu nome: ')
    modalidade = input('Informe a Modalidade (ex: Musculação, Cárdio): ')

    dias_semana = utils.ler_inteiro('Dias por Semana (1-7): ')
    objetivo = input('Informe Seu Objetivo: ')
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

    print(f'\n- ✅ Aluno(a) {nome_aluno} Cadastrado(a) Com Sucesso!')

def listar_alunos():
    utils.exibir_menu('📋 LISTA DE ALUNOS 📋')

    if len(dados.lista_aluno) == 0:
        print('\n- 📭 Nenhum Aluno(a) Cadastrado no Sistema!')
        return
    # exibir os dados formatados na tela acessando as chaves do dicionário.
    for aluno in dados.lista_aluno:
        print(f'- Nome: {aluno['nome']}')
        print(f'- Modalidade: {aluno['modalidade']}')
        print(f'- Treinos por Semana: {aluno['dias_semana']}x')
        print(f'Objetivo: {aluno['objetivo']}')
        print(f'Status: {aluno['status']}')
        print('=' * 40)

def entrar_fila():
    utils.exibir_menu('📥 ENTRAR NA FILA DE ATENDIMENTO 📥')
    nome_atendimento = input('Informe o Nome do Aluno Que Chegou: ')

    # adiciona o aluno no FINAL da fila (fifo).
    dados.fila_atendimento.append(nome_atendimento)
    print(f'\n- {nome_atendimento} Foi Adicionado(a) à Fila!')

def atender_aluno():
    utils.exibir_menu('🛎 ATENDER PRÓXIMO ALUNO 🛎')

    # validar: se a fila estiver vazia não terá ninguém para atender.
    if len(dados.fila_atendimento) == 0:
        print('\n- 📭 A Fila de Atendimento Está Vazia!')
        return
    
    proximo = dados.fila_atendimento.pop(0)
    print(f'\n- 🗣 Atendendo Agora: {proximo}')

def registrar_treino():
    utils.exibir_menu('🏋️‍♂️ REGISTRAR CHECK-IN DE TREINO 🏋️‍♂️')

    # se não tiver alunos cadastrados irá avisar e sair.
    if len(dados.lista_aluno) == 0:
        print('\n- 📭 Nenhum Aluno Cadastrado Para Registrar Treino!')
        return
    
    nome_busca = input('Digite o Nome do Aluno Para o Check-in: ')
    aluno_encontrado = None

    # loop para procurar o aluno pelo nome.
    for aluno in dados.lista_aluno:
        if aluno ['nome'].lower() == nome_busca.lower():
            aluno_encontrado = aluno
            break
        
    if aluno_encontrado is None:
        print(f'\n- ❌ Aluno(a) "{nome_busca}" Não Foi Encontrado(a)!')
        return
    
    # a var 'aluno_encontrado' guarda o dicionário daquele aluno específico.
    print(f'Aluno Selecionado {aluno_encontrado['nome']}')
    data_treino = input('Digite a Data do Treino (ex: 01/01/2026): ')

    aluno_encontrado['sessoes'].append(data_treino)
    print(f'\n- ✅ Check-in Realizado Com Suecsso! Treino do Dia {data_treino} Adicionado ao Histórico.')

def visualizar_historico():
    utils.exibir_menu('📁 HISTÓRICO DE TREINOS 📁')

    if len(dados.lista_aluno) == 0:
        print(f'\n- 📭 Nenhum Aluno(a) Cadastrado no Sistema!')
        return
    
    nome_busca = input('Digiet o Nome do Aluno (Histórico): ')
    aluno_encontrado = None

    for aluno in dados.lista_aluno:
        if aluno['nome'].lower() == nome_busca.lower():
            aluno_encontrado = aluno
            break
    if aluno_encontrado is None:
        print(f'\n- ❌ Aluno(a) "`{nome_busca}" Não foi Encontrado(a)!')
        return
    
    utils.exibir_menu(f'Treinos de {aluno_encontrado['nome']}')

    # validação da pilha: se a lista de sessões estiver vazia.
    if len(aluno_encontrado['sessoes']) == 0:
        print('\n- 🏋️‍♂️ Este Aluno Ainda Não Realizou Nenhum Treino!')
        return

    # exibição em lifo: assim lendo a pilha do topo para baixo (no caso maiss recente primeiro).
    print('\n📆 Hisórico do Mais Recente ao Mais Antigo:\n')
    for treino in reversed(aluno_encontrado['sessoes']):
        print(f'- 📅 Treino Realizado em: {treino}')
    
    print('=' * 40)