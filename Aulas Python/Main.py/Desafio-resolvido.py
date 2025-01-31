# Listas de produtos e suas avaliaçoes
produtos = ['Teclado', 'Monitor', 'Mouse', 'Impressora', 'Cadeira']
avaliacoes = [4.5, 3.2, 4.8, 2.9, 4.0]

#Avaliação mínima para qualidade
avaliacao_minima = 3.5

# Percorre as avaliações e verifica a qualidade dos produtos
for i, avaliacao in enumerate(avaliacoes):
    if avaliacao >= 4.5:
        print(f'O produto {produtos[i]} Tem excelente qualidade!')

    elif avaliacao >= 3.5:
        print(f'O produto {produtos[i]} Tem boa qualidade')
    else:
        print(f'O produto {produtos[i]} Precisa de melhorias na qualidadee.')