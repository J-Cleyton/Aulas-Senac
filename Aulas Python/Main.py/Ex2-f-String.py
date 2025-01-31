#Exemplo de formatação com F-String, para saída, onde irá conter virgulas e pontos realizando a separação.

#O faturamento mensal será exibido: R$ 30000.00 e R$ 30,000.00
faturamento_mensal = 30000
print(f'O faturamento mensal é de: R$ {faturamento_mensal:.2f}')
print(f'O faturamento mensal é de: R$ {faturamento_mensal:,.2f}')
#A formatação ":,.2f" faz com que o número apareça com virgula como separador decimal.
#E ponto como separador de milhares, além de mostrar duas casas decimais.


#Alterando para o padrão brasileiro no F-String
#Faturamento mensal será exibido : R$ 30.000,00
print(f'O faturamento mensal é de: R$ {faturamento_mensal:,.2f}'
       .replace(',', 'x').replace(',',',').replace('x' , '.'))
                                                   
#replace(',', 'X'): Troca a virgula por um marcador temporario (x).
#replace(',', ','): Troca o ponto pela virgula. 
#replace('X', '.'): Troca o marcador temporário de volta para o ponto
