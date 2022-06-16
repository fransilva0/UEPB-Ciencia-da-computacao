# 6. Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %)

salario_atual = float(input("Informe o seu salário atual: "))
reajuste = float(input("Informe a porcentagem de reajuste: "))

converter_porcentagem = reajuste / 100

salario_reajustado = salario_atual + (salario_atual * converter_porcentagem)

print(f"O seu salário com reajuste é de: {salario_reajustado}")