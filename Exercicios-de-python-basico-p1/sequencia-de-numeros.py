## 8. Faça um programa que leia um valor inteiro e mostre na tela uma sequência incluindo os dois números que vem antes, o número digitado, e os dois números que vem depois dele. Ex.: digitou 5; o programa mostra 3 4 5 6 7.

numero = int(input("Digite um número inteiro: "))

anterior = numero-1
ante_anterior= numero-2
posterior= numero+1
pos_posterior= numero+2

print(f"{ante_anterior} - {anterior} -- {numero} -- {posterior} - {pos_posterior}")