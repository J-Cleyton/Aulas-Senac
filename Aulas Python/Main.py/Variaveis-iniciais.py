produtos = []  # Lista para armazenar os nomes dos produtos
precos = []    #Lista para armazenar os preços dos produtos
estoques = []  #Lista para armazenar a quantidade em estoque de cada produto
vendas = []    #Lista para armazenar a quantidade vendida de cada produto

# Boas-Vindas
print("Bem-Vindo ao sistema de controle de estoque e vendas.")
print("VocÊ pode adicionar produtos, inserir preços, quantidades em estoque e quantidades vendidas.")
print("para sair, basta deixar o nome do produto em branco e pressionar enter")

# Loop para coletar os dados dos produtos
while True:
    # Solicita os dados do produto
    nome_produto = input('n'"Digite o nome do produto/item (ou pressione enter para sair do programa): ")

    # Se o usuário deixar o nome do produto em branco, o loop é interrompido
    if nome_produto == "":
        break  # Sai do loop se a entrada estiver vazia

    # Solicita o preço do produto
    try:
        preco_produto = float(input(f"Qual o preço unitário? {nome_produto}: R$ "))
    except ValueError:
            # Se o valor informado não for um número válido, exibe uma mensagem de erro
            print("Entrada inválida! O preço deve ser um número.")
            continue

    # Solicita quantidade vendida
    try:
        quantidade_vendida = int(input(f"Digite a quantidade vendida do {nome_produto}: "))
    except ValueError:
            # Se o valor informado não for um número inteiro válido, exibe uma mensagem de erro
            print("Entrada inválida! A quantidade vendida deve ser um número inteiro.")
            continue

        # Verifica se o produto já existe na lista de produtos
    if nome_produto in produtos:
            # Se o produto já estiver na lista, adiciona os dados ás listas
            index = produtos.index(nome_produto)
            estoques[index] += estoque_produto
            vendas[index] += quantidade_vendida
    else:
            # Se for um produto novo, adiciona os dados ás listas
            produtos.append(nome_produto)
            precos.append(preco_produto)
            estoques.append(estoque_produto)
            vendas.append(quantidade_vendida)

    # Cálculos
    valor_total_vendas = 0
    produto_mais_vendido = None
    maior_quantidade_vendida = 0

    # Exibe o estoque e o valor total das vendas para cada produto
    for i in range(len(produtos)):
        # Cálculo do valor total de vendas
        valor_vendas_produto = vendas[i] * precos[i] # Multiplica a quantidade vendida pelo preço unitário
        valor_total_vendas += valor_vendas_produto # Acumula o valor total das vendas

        # Verifica qual produto tem maior demanda
        if vendas[i] > maior_quantidade_vendida:
            maior_quantidade_vemdida = vendas[i] # Atualiza a maior quantidade vendida
            produto_mais_vendido = produtos[i] # Atualiza o nome do produto mais vendodp

        # Exibe o estoque e o valor das vendas do produto
        print(f"\nProduto: {produtos[i]}")
        print(f"Estoque: {estoques[i]}") # Exibe a quantidade em estoque
        print(f"Quantidade vendida: {vendas[i]}") # Exibe a quantidade vendida
        print(f"Valor total das vendas: R$ {valor_vendas_produto:.2f}") # Exibe o valor total das vendas do produto

    # Exibe o valor total de vendas e o produto mais vendido
    print(f"\nValor total de vendas de todos os produtos: R$ {valor_total_vendas:.2f}")
    print(f"O produto mais vendido foi: {produto_mais_vendido}, com {maior_qwuantidade_vendida} unidades vendidas.")

    # Finalização
    print('\n'"Obrigado por utilizar nosso programa! Em breve iremos ter interface.")    