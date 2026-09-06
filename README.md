# 🏋️ Sistema de Gestão de Academia — CLI

Projetado e desenvolvido como projeto acadêmico de conclusão do **1º Semestre** do curso de Ciência da Computação / Análise e Desenvolvimento de Sistemas. 

O projeto consiste em um software de terminal (CLI) em Python que simula o fluxo operacional de uma academia, integrando cadastro de alunos, controle de atendimento recepção, registro de check-ins de treinos e consulta de históricos.

---

## 📌 Sumário
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Conceitos de Ciência da Computação Aplicados](#-conceitos-de-ciência-da-computação-aplicados)
- [Arquitetura do Projeto](#-arquitetura-do-projeto)
- [Funcionalidades Principais](#-funcionalidades-principais)
- [Como Executar o Projeto](#-como-executar-o-projeto)

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/)** — Linguagem principal do projeto.
- **[Colorama](https://pypi.org/project/colorama/)** — Estilização visual no terminal (cores, destaques e formatação).

---

## 💡 Conceitos de Ciência da Computação Aplicados

O objetivo principal deste projeto foi a aplicação prática dos pilares da programação estruturada e estruturas de dados fundamentais:

* **Estruturas de Dados Primárias (Dicionários & Listas):**
  Cada aluno é representado como um **dicionário** contendo chave-valor (`nome`, `modalidade`, `dias_semana`, `objetivo`, `status`, `sessoes`), mantidos dentro de uma **lista global**.
  
* **Fila / FIFO (*First-In, First-Out*):**
  Implementação da fila de atendimento da recepção. O primeiro aluno que entra na fila (`append()`) é o primeiro a ser atendido e removido do fluxo (`pop(0)`).

* **Pilha / LIFO (*Last-In, First-Out*):**
  O histórico de sessões de treino é inserido ao final da lista de cada aluno. A leitura utiliza o conceito de pilha via `reversed()`, garantindo que o treino mais recentemente registrado apareça no topo da exibição.

* **Tratamento de Strings & Buscas:**
  Algoritmos de busca linear com conversão *case-insensitive* (`.lower()`) para busca e localização de registros pelo nome do aluno.

* **Modularização & Separação de Conceitos:**
  Divisão da aplicação em módulos distintos para lógica principal (`main.py` / `operacoes.py`), manipulação de memória (`dados.py`) e rotinas reutilizáveis de I/O (`utils.py`).

---

## 📂 Arquitetura do Projeto

```text
├── main.py          # Ponto de entrada do sistema e controle do menu principal
├── tarefas.py       # Lógica das funções de negócio (cadastro, fila, treino, histórico)
├── dados.py         # Módulo responsável pelo armazenamento de dados em memória
└── utils.py         # Funções utilitárias (exibição de telas, leitura e validação de inputs)
_____________________________________________________________________________________________

Código por: Matheus A. Antunes Pentogennis'

<img width="1810" height="1394" alt="code" src="https://github.com/user-attachments/assets/95dd0626-4d3a-4664-863f-b29ca6c68af0" />

