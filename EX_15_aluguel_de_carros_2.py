# Atualize o código de aluguel de carros feito anteriormente. 
# Crie um programa em Python que simule o cálculo do valor total a ser pago pelo aluguel de um carro. O programa deve:
# 1- Perguntar ao usuário qual foi o modelo do carro alugado.
# 2- Perguntar por quantos dias o carro foi alugado.
# 3- Perguntar quantos quilômetros foram percorridos com o carro.
# 4- Usar uma tabela de preços (pré-definida pelo próprio aluno) para determinar o valor diário de aluguel de acordo com o modelo do carro.
# 5- Calcular o custo total com base:
# 6- No número de dias alugados × valor por dia
# 7- No total de quilômetros rodados × R$0,15 por km
# 8- Exibir o valor total a ser pago, com duas casas decimais.

# Os alunos são livres para definir quais modelos de carro o programa aceitará e o valor por dia de cada um.

# Se o modelo inserido pelo usuário não estiver na lista, o programa deve aplicar um valor padrão por dia.

# OUTPUT ESPERADO: 

# ----------------------------------------------------- EXEMPLO 1

# Qual foi o modelo do carro alugado? uno
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100
# Você andou 100.0km por 10 dias, então o preço a pagar é R$415.00.

# ----------------------------------------------------- EXEMPLO 2

# Qual foi o modelo do carro alugado? bmw
# Por quantos dias o carro foi alugado: 10 
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$10015.00.

# ----------------------------------------------------- EXEMPLO 3(PREÇO PADRÃO)

# Qual foi o modelo do carro alugado? fox
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$615.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
precos_diarias = {
    "Civic": 150.00,
    "Fox": 130.00,
    "Hb20": 120.00,
    "I30": 150.00,
    "Azera": 300.00,
    "Corolla": 220.00,
    "Kombi": 110.00
}

carro_alugado = input("Digite o carro que você alugou: ")
diaria = float(input("Digite a diaria do carro alugado: "))
dias = int(input(f'Por quantos dias o {carro_alugado} foi alugado? '))
km = float(input(f'Quantos kms você rodou com o {carro_alugado}? '))

total_dias = dias * diaria
total_km = km * 0.15
aluguel_total = total_dias+total_km

if carro_alugado == 'Civic':
    print(f"Você alugou o carro: {carro_alugado}.")
    print(f"Você alugou o carro por {dias} dias.")
    print(f"Você andou {km} km com o {carro_alugado}.")
    print(f"O valor final a pagar é {aluguel_total}.")

elif carro_alugado == 'Fox':
    print(f"Você alugou o carro: {carro_alugado}.")
    print(f"Você alugou o carro por {dias} dias.")
    print(f"Você andou {km} km com o {carro_alugado}.")
    print(f"O valor final a pagar é {aluguel_total}.")

elif carro_alugado == 'Hb20':
    print(f"Você alugou o carro: {carro_alugado}.")
    print(f"Você alugou o carro por {dias} dias.")
    print(f"Você andou {km} km com o {carro_alugado}.")
    print(f"O valor final a pagar é {aluguel_total}.")

elif carro_alugado == 'I30':
    print(f"Você alugou o carro: {carro_alugado}.")
    print(f"Você alugou o carro por {dias} dias.")
    print(f"Você andou {km} km com o {carro_alugado}.")
    print(f"O valor final a pagar é {aluguel_total}.")

elif carro_alugado == 'Azera':
    print(f"Você alugou o carro: {carro_alugado}.")
    print(f"Você alugou o carro por {dias} dias.")
    print(f"Você andou {km} km com o {carro_alugado}.")
    print(f"O valor final a pagar é {aluguel_total}.")

elif carro_alugado == 'Corolla':
    print(f"Você alugou o carro: {carro_alugado}.")
    print(f"Você alugou o carro por {dias} dias.")
    print(f"Você andou {km} km com o {carro_alugado}.")
    print(f"O valor final a pagar é {aluguel_total}.")

elif carro_alugado == 'Kombi':
    print(f"Você alugou o carro: {carro_alugado}.")
    print(f"Você alugou o carro por {dias} dias.")
    print(f"Você andou {km} km com o {carro_alugado}.")
    print(f"O valor final a pagar é {aluguel_total}.")

else:
    print("Modelo invalido")