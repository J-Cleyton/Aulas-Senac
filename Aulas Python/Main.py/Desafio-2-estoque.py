# Desafio prático estoque
produtos = ['TV', 'Computador', 'Geladeira', 'Liquidificador', 'Luneta', 'bicicleta']
estoque = (65, 230, 20, 80, 179, 50)

# Estoque mínimo
estoque_minimo = 100

# Variavel para contagem
acima_do_minimo = 0
abaixo_do_minimo = 0

for i, estoque in enumerate(estoque):
    if estoque >= estoque_minimo:
                   acima_do_minimo += 1
    else:
        abaixo_do_minimo += 1

# Exebindo a contagem final
print(f'Produtos acima do mínimo: {acima_do_minimo}')
print(f'Produtos abaixo do minimo {abaixo_do_minimo}')