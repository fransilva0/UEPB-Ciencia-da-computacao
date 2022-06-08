#1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e
#quanto em dinheiro ele deseja abastecer (ex. 50,00).
#Calcule quantos litros de combustível o usuário obterá com esses valores.

litro = float(input("Digite o valor do litro de combustível atualmente: "))
abastecimento = float(input("Agora, digite o valor em dinheiro que você deseja abastecer: "))

calculo = abastecimento / litro

print(f"Com R$ {abastecimento} você poderá adicionar, aproximadamente, {calculo :.2f} litros no carro")