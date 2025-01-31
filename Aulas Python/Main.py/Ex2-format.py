#Exemplo de formatação, para saída, onde irá conter virgulas e pontos realizando a separação.

faturamento_mensal = 30000

#O faturamento mensal será exibido: R$ 30000.00 e R$ R$ 30,000.00
print("O faturamento mensal é de: R$ {:.2f}".format(faturamento_mensal))
print("O faturamento mensal é de: R$ {:,.2f}".format(faturamento_mensal))

#Alterando para o padrão brasileiro no format
#O faturamento mensal será exibido : R$ 30.000,00
print("O faturamento mensal é de: R$ {:,.2f}".format(faturamento_mensal)
      .replace (',', 'X').replace('.', ',').replace('X', '.'))
# Saída: O faturamento mensal é de 30.000,00

#replace(',', 'X'): Troca a virgula por um marcador temporário (X).
#replace('.', ','): Troca o ponto pela virgula.
#replace('X', '.'):Troca o marcador temporário de volta para o ponto