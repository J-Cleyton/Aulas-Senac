codigo_skol = '7891149105366'
codigo_brahma = '7891149102488'
linha = '-' * 63

print('\n' + linha)
bebida = input('Insira a descrição da bebida em letra Maíuscula!')

if bebida.isupper(): #Verifica se a enterada está em caixa alta
    if bebida == 'SKOL':
        print('\n' + linha)
        print('Esta descrição é referente ao código do produto:', codigo_skol)
        print(linha)
    elif bebida == 'BRAHMA':
        print('\n' + linha)
        print('Esta descrição é referente ao código do produto:', codigo_brahma)
        print(linha)
    else:
        print('\n' + linha)
        print('Erro: Bebida não reconhecida. Por Favor, insira "SKOL" ou "BRAHMA".')
        print(linha)
else:
    print('\n' + linha)
    print('ERRO: por favor, digite a descrição em letra MAÍUSCULA!')
    print(linha)

