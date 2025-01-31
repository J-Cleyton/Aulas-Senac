# Tupla no python
contatos = (
    ('Godoy', '3457-4133'),
    ('Leticia', '3457-4123'),
    ('Sidnei', '3457-4163')
)

telefone_godoy = contatos[0][1]

print(telefone_godoy)

#--------------------------------------

# Acessando uma informação da tupla

for nome, telefone in contatos:
    if nome == 'Godoy':
        print(telefone)