# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
opcao = int(input("Escolha uma das opções de 1 a 4: "))

if opcao == 1:
    numero_1 = int (input("Me fale um número:"))
    numero_2 = int (input("Me fale um número:"))
    soma = numero_1 + numero_2
    print (f"o resultado de {numero_1} + {numero_2} = {soma}")

elif opcao == 2:
    numero_1 = int (input("Me fale um número:"))
    numero_2 = int (input("Me fale um número:"))
    soma = numero_1 - numero_2
    print(f"o resultado de {numero_1} - {numero_2} = {soma}")

elif opcao == 3:
    numero_1 = int (input("Me fale um número:"))
    numero_2 = int (input("Me fale um número:"))
    soma = numero_1 * numero_2
    print(f"o resultado de {numero_1} * {numero_2} = {soma}")

elif opcao == 4:
    numero_1 = int (input("Me fale um número:"))
    numero_2 = int (input("Me fale um número:"))
    soma = numero_1 / numero_2
    print(f"o resultado de {numero_1} / {numero_2} = {soma}")

else:
    print("Número inválido")



    




























# numero_1 = int (input("me fale um numero:"))
# numero_2 = int (input("me fale um numero:"))
# operacao = input("digite um tipo de conta que voce quer fazer:")

# if operacao == "somar" or operacao == "+":
#     soma = numero_1 + numero_2
#     print (f"o resultado de {numero_1} + {numero_2} = {soma}")
    
# elif operacao == "subtrair" or operacao == "-":
#     soma = numero_1 - numero_2
#     print(f"o resultado de {numero_1} - {numero_2} = {soma}")
    
# elif operacao == "multiplicar" or operacao == "*":
#     soma = numero_1 * numero_2
#     print(f"o resultado de {numero_1} * {numero_2} = {soma}")
    
# elif operacao == "dividir" or operacao == "/":
#     soma = numero_1 / numero_2
#     print(f"o resultado de {numero_1} / {numero_2} = {soma}")
    
# else:
#     print("operação invalida")