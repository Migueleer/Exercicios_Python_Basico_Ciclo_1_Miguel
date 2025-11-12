# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto_porcentagem = float(input("Digite o valor do desconto: "))
valor_final = preco * (desconto_porcentagem/100)
total = preco - valor_final

print(f"O produto é: {produto}")
print(f"O preço é: R${preco:.2f}")
print(f"O desconto é de: {desconto_porcentagem}")
print(f"O valor final é: R${total:.2f}")
