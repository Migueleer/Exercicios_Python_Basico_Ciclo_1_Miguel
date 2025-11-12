# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
carro_alugado = input("Digite o carro que você alugou: ")
diaria = float(input("Digite a diaria do carro alugado: "))
dias = int(input(f'Por quantos dias o {carro_alugado} foi alugado? '))
km = float(input(f'Quantos kms você rodou com o {carro_alugado}? '))

total_dias = dias * diaria
total_km = km * 0.15
aluguel_total = total_dias+total_km

print(f"Você alugou o carro: {carro_alugado}.")
print(f"Você alugou o carro por {dias} dias.")
print(f"Você andou {km} km com o carro.")
print(f"O valor final a pagar é {aluguel_total}.")
