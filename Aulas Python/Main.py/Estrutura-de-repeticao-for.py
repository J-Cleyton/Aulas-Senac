# Listas de estoques e empresas
estoque  = [8000, 8000, 5000, 10000, 300]
empresas = ['Microsoft', 'Apple', 'Samsung', 'LG', 'Nokia']

# Estoque mínimo
estoque_minimo = 8000

# Percorre os estoques e verifica se cada um está abaixo ou acima do estoque mínimo
for i, qtd_estoque in enumerate(estoque):
    if qtd_estoque < estoque_minimo:
        # Se o estoque estiver abaixo do mínimo, imprime a empresa para o loop
        print(f'Empresa abaixo do mínimo: {empresas[i]}')
        break  # Interrompe o loop assim que encontrar o primeiro estoque abaixo do mínimo

else:
    #Se não encontrar nenhuma empresa abaixo do mínimo, exibe isso
    print('Todas as empresas têm estoque suficiente.')
