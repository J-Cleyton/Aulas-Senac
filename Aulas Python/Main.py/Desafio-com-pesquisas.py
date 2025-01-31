numeros = [5, 2, 9, 1, 5, 6]                                      #Imprimindo números em ordem
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)

numeros = [7, 8, 9, 7, 6, 8]                                      #Contagem de vezes que um número aparece
contagem = numeros.count(7)
print(f'O número 7 aparece {contagem} vezes na lista.')

materiais = ['Papel', 'Caneta', 'Caderno', 'Borracha']            #Verifica se há um ítem na lista
if 'lapiseira' not in materiais:
    print('A lapiseira não está na lista')
else:
    print('A lapiseira está na lista')