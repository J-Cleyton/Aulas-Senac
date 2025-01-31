#Informaçoes da empresa
qtd_coca_cola = 100  #Quantidade de Coca-Cola vendida
qtd_pepsi = 50        #Quantidade de Pesi vendida
preco_coca_cola = 4.50  #Preço unitário da Coca-Cola
preco_pepsi = 3.90      #Preço unitário da Pepsi
investimento_total = 6000.00  #Investimento total
linha = '-' * 63

print('\n' + linha)
print(f'O total de vendas de latas de Coca-Cola foi de: R$ {qtd_coca_cola * preco_coca_cola:,.2f}' + '\n')
print(f'O total de vendas de latas de Pepsi foi de: R$ {qtd_pepsi * preco_pepsi:,.2f}')

faturamento = (qtd_coca_cola * preco_coca_cola) + (qtd_pepsi * preco_pepsi)

print(linha + '\n')
print(f'O faturamento das vendas de latas de refri foi de: R$ {investimento_total - faturamento:,.2f}' + '\n')

if investimento_total > faturamento:
    print(linha + '\n')
    print('         A empresa levou prejuiso nas vendas de refri')
    print('\n' + linha)
else:
    print(linha + '\n')
    print('         A empresa teve lucro nas vendas de refri')
    print('\n' + linha)
