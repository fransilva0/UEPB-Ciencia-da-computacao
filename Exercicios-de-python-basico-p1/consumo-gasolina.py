#Faça um programa que calcule a média de consumo (em km/l) de combustível de um veículo. O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.

km01 = float(input("Qual foi o seu KM inícial? "))
km02 = float(input("Qual foi o seu KM final? "))
litros = float(input("Agora, quantos KM por Litro de gasolina? "))

km_medio = km02 - km01

consumo = km_medio / litros

print(f"No percurso de {km_medio :.2f} Kilomêtros, foram consumidos {consumo :.2f}, aproximadamente, de gasolina!")