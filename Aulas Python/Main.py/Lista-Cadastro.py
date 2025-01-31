# Exemplo de lista para cadastro (Cada quarto tem nome e cpf do hospede)
quartos = [
    ['Gabriel', 'CPF: 456.563.002-00'],
    ['Leticia', 'CPF: 456.563.001-01'],
    ['Sidmei', 'CPF: 456.563.002-02'],
]

#Perguntar quantas pessoasvão se cadastrar
qtd_pessoas = int(input('Quantas pessoas você quercadastrar?'))

# Laço para fazer o cadastro das pessoas
for i in range(qtd_pessoas):
    # Perguntar o nome do hóspede
    nome = input('Nome do hóspede: ')

    # Perguntar o CPF do hóspede
    cpf = input('CPF do Hóspede: ')

    #Adicionar o nome e CPF na lista de quartos
    quartos.append([nome, f'CPF:{cpf}'])

# Mostrar os cadastros realizados
print('\nCadastro dos Hóspedes:')
for hospede in quartos:
    print(f'{hospede[0]} - {hospede[1]}')