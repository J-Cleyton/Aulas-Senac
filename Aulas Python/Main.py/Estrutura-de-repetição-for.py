#Mostrar indices de uma lista durante 5 vezes em um print

#Listas de marcas e quantidades
marcas = ['Ford', 'Toyota', 'Ferrari', 'McLaren']
qtd_disponivel = [500, 2000, 6, 2]

#Verificando o comprimento das listas (quantidade de elementos)
qtd = len(marcas)

    #Loop para mostrar a marca e quantidade
for indice in range(qtd):
    print(f'A marca: {marcas[indice]}), teve {qtd_disponivel[indice]} fabricados')

    #Verificar valores

    vendas_mensais = [100, 500, 500, 1500, 3000, 600, 900, 8000, 6000, 100, 102]
    meta = 1000

    contador = 0
    for maior_venda in vendas_mensais:
        if maior_venda >= meta:
            contador += 1
print('\n' + 'Quantidade de vendedores que atingiram a meta:' '\n')
print('Apenas', contador, 'conseguiram bater a meta')         

 
 #Utilizando FOR para verificações em uma lista

qtd_estoque = [40, 50, 600, 700, 500]
produtos = ['Golf', 'Parati', 'Fusca', 'Vespa', 'Gol']
estoque_minimo = 500

#Iterando sobre a lista de quantidade de estoque
for i, qtd_atual in enumerate(qtd_estoque):
    if qtd_atual < estoque_minimo:
        #Usando f-string para formatar a mensagem de forma mais legivel
        print(f'O produto{produtos[i]} está abaixo do minimo, com {qtd_atual} unidades.')