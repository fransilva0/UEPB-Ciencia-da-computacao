# 3. Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original da dívida (ex 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).

valor_original = float(input("Digite o valor original da dívida: "))
dias_atraso = int(input("Digite a quantidade de dias em atraso: "))
valor_multa = float(input("Digite o valor por dia de atraso: "))

juros_multa = valor_multa * dias_atraso 
valor_a_ser_pago = valor_original + juros_multa

print(f"O valor da dívida a ser pago agora é de {valor_a_ser_pago :.2f}")