from colorama import Style, Fore, Back, init
init(autoreset=True)

# essa função ira ocorrer um erro caso não informe um número inteiro.
def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print(Style.BRIGHT + Fore.RED + '=' * 40)
            print('❌ ERRO: Digite um número válido ❌'.center (40))
            print(Style.BRIGHT + Fore.RED + '=' * 40)

# função que irá exibir o menu no main.py
def exibir_menu(texto):
    print(Style.BRIGHT + '=' * 40)
    print(Style.BRIGHT + texto.center(40))
    print(Style.BRIGHT + '=' * 40)

exibir_menu('CADASTRO ALUNO(A)')
