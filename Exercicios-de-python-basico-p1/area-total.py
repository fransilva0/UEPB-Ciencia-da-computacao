# 4. Faça um programa que calcule a área total (m2) de uma casa com 4 cômodos. O usuário deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.

print("---------Comôdo 1------------")
largura1 = float(input("Insira a largura do 1º comôdo: "))
comprimento1 = float(input("Insira o comprimento do 1º comôdo: "))

area1 = largura1 * comprimento1

print("---------Comôdo 2------------")
largura2 = float(input("Insira a largura do 2º comôdo: "))
comprimento2 = float(input("Insira o comprimento do 2º comôdo: "))

area2 = largura2 * comprimento2

print("---------Comôdo 3------------")
largura3 = float(input("Insira a largura do 3º comôdo: "))
comprimento3 = float(input("Insira o comprimento do 3º comôdo: "))

area3 = largura3 * comprimento3

print("---------Comôdo 4------------")
largura4 = float(input("Insira a largura do 4º comôdo: "))
comprimento4 = float(input("Insira o comprimento do 4º comôdo: "))

area4 = largura4 * comprimento4

area_total = area1 + area2 + area3 + area4 

print(f"A área total da casa é: {area_total}m²")