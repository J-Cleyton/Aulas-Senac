for nome in range (10):
    print('Johnney')

inicio = 0
final = 5
while inicio < final:
    print(inicio)
    inicio += 1


    #Lista range de rede
    
    #Rede Base
rede_base = '192.168.0.1'

    #Imprimir a rede base

print('A rede é:', rede_base)
print('\nA lista de IPs é:')

    #Gerar a lista de IPs

for sequencia in range(1, 11):     #Gera IPs de 192.168.0.1 até 182.168.0.10
    ip = f'192.168.0.{sequencia}'  #Cria o IP com a sequência
    print(ip)

    #Mostrar indices de uma lista durante 5 vezes em um print

    #Listas de marcas e quantidades
    marcas = ['Ford', 'Toyota', 'Ferrari', 'McLaren']
    qtd_disponivel = [500, 2000, 6, 2]

    #Verificando o comprimento das listas (quantidade de elementos)
    qtd = len(marcas)

    #Loop para mostrar a marca e quantidade
    for indice in range(qtd):
        print(f'A marca: {marcas[indice]}), teve {qtd_disponivel[indice]} fabricados')