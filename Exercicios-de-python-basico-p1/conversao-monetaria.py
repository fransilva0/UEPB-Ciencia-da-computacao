## 5. Faça um programa que calcule a conversão monetária de Real para Dólar. O usuário informa o valor da cotação do dólar (ex.: 3,78) e quanto em real deseja converter (ex. 150,00). O programa exibe quantos dólares valem os reais informados.

dolar = float(input("Qual a cotação do dolar?: "))
real = float(input("Quantos reais você quer converter?: "))

resultado = real / dolar

print(f"Seus R$ {real} valem ${resultado :.2f}, na cotação mensionada")