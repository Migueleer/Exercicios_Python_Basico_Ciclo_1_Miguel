# Escreva um programa que pede ao usuário o valor atual da cotação do dollar e a quantidade de dólares para ser convertido em reais. 
# Depois mostre na tela a conversão.

# OUTPUT ESPERADO:

# Digite a cotação do dollar: 5.60
# Digite o valor em dollar a ser convetido para real: 100
# O valor em reais é:  560.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dollar_atual = float(input("Digite a cotação do dollar hoje em dia: "))
converter = float(input("Quantos dollars deseja converter em reais? "))
convertendo = (dollar_atual * converter)

print(f"A cotaçãodo dollar é: {dollar_atual}")
print(f"O dollar convertido é: {converter}")
print(f"O valor em reais é: {convertendo:.2f}")