## 7. Faça um programa que calcula o tempo (em anos) que uma pessoa irá demorar para poupar R$ 1.000.000,00 (Um Milhão de Reais). O usuário informa o salário mensal e o total de despesas mensais.

salario_mes = float(input("Qual o seu salário mensal?: "))
despesas = float(input("Qual o gasto mensal(despesas)?: "))

poupanca_anual = (salario_mes - despesas) *12
anos = (1000000 / poupanca_anual)+ 0.5

print(f"Você vai demorar {anos :.2f} anos para conseguir seu 1º milhão!")