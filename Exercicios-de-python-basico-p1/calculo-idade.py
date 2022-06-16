## 9. Crie um programa que pergunta o nome do usuário e o ano de nascimento do usuário e calcula qual idade ele tem (ou terá, se ainda não fez aniversário neste ano). Ex.: Nome = Carlos, Ano = 1999. O programa mostra a mensagem: “Carlos tem 20 anos”.

nome = str(input("Digite seu nome: "))
nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - nascimento

print(f"{nome} tem {idade} ano(s)")