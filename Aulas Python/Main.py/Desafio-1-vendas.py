# Desafio Prático
vendedores = ['João', 'Maria', 'José', 'Marcos', 'Daniel']
vendas = [15000, 30000, 21000, 11000, 9500]

#Meta mínima
meta_vendas = 20000

for i, vendas in enumerate(vendas):
    if vendas >= 20000:
        print(f'O vendedor {vendedores[i]} Teve excelente desempenho nas vendas!')

    elif meta_vendas >= 15000:
        print(f'O vendedor  {vendedores[i]} Teve boas vendas')
    else:
        print(f'O vendedor {vendedores[i]} Precisa vender mais.')