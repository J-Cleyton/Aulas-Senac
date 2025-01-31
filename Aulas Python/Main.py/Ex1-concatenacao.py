#Informações da pessoa
nome = "Leticia"
sobrenome = "Souza"
idade = 22
cidade = "São Paulo"

#Contatenando as informaçoes em uma variavel e utilizando conversão
mensagem = "Meu nome é " + nome + " " + sobrenome + ", tenho " + str(idade) + " anos e moro em " + cidade + "." 

print(mensagem)

#Exemplo de concatenação, caso queima colocar aspas em uma das infomações, dentro da string

#informaçoes da pessoa
nome = "Leticia"
cidade = "São Paulo"

#irá conter aspas no nome
mensagem = "Meu nome é \"" + nome + "\", Meu sobrenome é, " + sobrenome + ", Tenho " + str(idade) + " anos e moro em " + cidade + "."
print(mensagem)