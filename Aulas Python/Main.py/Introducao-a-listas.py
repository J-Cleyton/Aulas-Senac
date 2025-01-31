#Até o momento estamos utilizando as variaveis para armazenar as informações:

nome = "Leticia"
idade = '22'
altura = '1,60'
cidade = 'Americana'
us = 'SP'
pais = 'Brasil'

#Podemos simplismente usar "Listas", para armazenar os dados como uma variável:

lista_informacoes = ['nome: Godoy',
                     'Idade: 26',
                     'Altura: 1.70',
                     'Cidade: Santa Barbara do Oeste',
                     'Estado: SP',
                     'Pais: Brasil']

print(lista_informacoes)


#Acessando informações da lista:

lista_perifericos = ['Memoria',
                     'HH',
                     'GPU',
                     'Processador',
                     'Mouse']

print(lista_perifericos[3])

#Utilizando o método index para verificação automática

#Msg, Info, Produtos
mensagem_indice     = 'O indice do produto é:'
mensagem_item       = 'e o item da lista é o:'
mensagem_quantidade = 'e quanditade do produto é:'

#listas de produtos e seus estoques
produtos = ['Caixa de som', 'celular', 'Monitor', 'Mouse', 'Teclado']
estoque  = [100, 200, 300, 400, 1000]

#Encontrando o índice do produto "Teclado"
indice_teclado = produtos.index('Teclado')

#Exibindo as informações do produto
print(f'\n{mensagem_indice} {indice_teclado}, {mensagem_item} {produtos[indice_teclado]}, {mensagem_quantidade} {estoque[indice_teclado]}')

#Lista com condições e verificações de índice

#Lista com produtos e seus estoques
produto = input('Insira o nome de um equipamento eletrônico')
produtos= ['Caixa de som', 'Celular', 'Monitor', 'Mouse', 'Teclado']
estoque = [100, 200, 300, 400, 1000]

#Verificação se o produto está na lista
if produto in produtos:
    indice = produtos.index(produto)  #Corrigido para usar 'produto' em vez de 'produtos'
    qtd_estoque = estoque[indice]
    print(f'A quantidade do produto "{produto}" em estoque é de: {qtd_estoque} unidades.')
else:
    print(f'O produto informado "{produto}"não existe no estoque')

    #Trocando um item da lista

    #Lista de celulares
    trocar_mobile = ['SAMSUNG S20', 'SAMSUNG A10', 'LG K10 PRO']
    print('Modelos atuais da lista:', trocar_mobile)

    #Troca o modelo 'LG K10 PRO' pelo 'IPHONE 12'
    trocar_mobile[2] = 'IPHONE 12'

    #Exibe a troca realizada
    print('O modelo foi trocado para:', trocar_mobile[2])

    #Mostra a lista atualizada
    print('Lista de produtos atualizada:', trocar_mobile)


    #Adicionando item na lista

    #Lista de celulares
    adiciona_mobile = ['SAMSUNG S20', 'SAMSUNG A10', 'LG K10 PRO']
    print('Modelos atuais da lista:', adiciona_mobile, '\n')

    #Adiciona um novo modelo á lista 
    adiciona_mobile.append('XIAOMI 13')

    #Exibe a configuração da adição
    print('O celular', adiciona_mobile[-1], 'foi adicionado ao estoque com sucesso.')

    '''Utilizado -1 para adicionar após o ultimo item da lista, porém poderia utilizar [3]'''

    #Mostra a loista atualizada
    print('A lista de produtos atualizada é', adiciona_mobile)


#Removendpo um item da lista usando metodo pop

#Lista de celulares
remove_mobile = [' SAMSUNG S20', 'SAMSUNG A10', 'LGF K10 PRO']
print('Modelos atuais da lista:', remove_mobile, '\n')

#Remove o modelo 'LG K10 PRO' da lista usando o indice
modelo_removido = remove_mobile.pop(2)   #'LG K10 PRO' esta na posição 2

#Exibe a confirmação da remoção
print('O celular', modelo_removido, 'foi removido com sucesso do estoque.')

#Mostra a lista atualizada
print('A lista de produtos atualizada é:', remove_mobile)

