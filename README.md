🏋️ Sistema de Gestão de Academia (Projeto Acadêmico - 1º Semestre)
Este projeto foi desenvolvido como trabalho de conclusão do 1º semestre da faculdade, com o objetivo de consolidar os conceitos fundamentais da programação estruturada, manipulação de dados e introdução a Estruturas de Dados em Python.

O sistema simula o funcionamento do terminal de uma academia, permitindo o cadastro de alunos, gerenciamento da fila de recepção, check-in de treinos e consulta ao histórico de atividades.

🛠️ Tecnologias e Bibliotecas
Python 3: Linguagem base utilizada na implementação da lógica e estruturas.
Colorama: Biblioteca utilizada para estilizar a interface de linha de comando (CLI) com cores e formatação textual, tornando a navegação mais amigável.
Modularização: Organização do projeto em diferentes arquivos (dados.py, utils.py e rotinas principais).

💡 Conceitos de Programação & Estruturas de Dados Aplicados
Estruturas Primárias (Listas e Dicionários): Mapeamento dos dados do aluno (nome, modalidade, objetivo, status e sessões) em dicionários armazenados dentro de uma lista principal.
Fila (FIFO - First-In, First-Out): Gerenciamento da chegada de alunos no atendimento via append() e remoção do primeiro da fila com pop(0).
Pilha (LIFO - Last-In, First-Out): Exibição do histórico de treinos do mais recente ao mais antigo utilizando a função reversed().
Busca e Trata de Strings: Tratamento de buscas por nome com .lower() para ignorar diferenças entre maiúsculas e minúsculas.
Validação e Controle de Fluxo: Checagens de segurança para evitar erros ao tentar operar em listas vazias ou buscar registros inexistentes.

🚀 Funcionalidades do Código
cadastrar_aluno(): Coleta informações do usuário e registra um novo perfil ativo no sistema.
listar_alunos(): Exibe a lista completa de alunos cadastrados e seus detalhes.
entrar_fila() e atender_aluno(): Controla a ordem de chegada na recepção utilizando o conceito de fila.
registrar_treino(): Realiza a busca pelo aluno e registra a data do treino realizado no seu histórico.
visualizar_historico(): Apresenta a ordem cronológica inversa dos treinos realizados por determinado aluno.

Código por: Matheus A. Antunes Pentogennis
___________________________________________________________________________________________________________

## Como Rodar o Programa

1. Requisitos: Python instalado na versão 3.10 ou superior.
2. Biblioteca externa: Este projeto utiliza a biblioteca 'colorama' para estilizar o terminal. Instale a biblioteca rodando o comando no terminal:

   pip install colorama
