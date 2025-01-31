#Com as variaveis abaixo, crie uma nova variavel e faça a concatenação das informações.
#O titulo do filme, deve ser exibido entre aspas.
#O ano de lançamento deve ser convertido para string
#Após exiba em um print:

#Informações do filme
titulo_filme = "Batman: O Cavaleiro das Trevas"
diretor = "Christopher Nolan"
ano_lancamento = 2010
genero_filme = "Ação"

#Concatenando as informações em uma variavel:
mensagem = "O filme é \"" + titulo_filme + "\", dirigido por \"" + diretor + "\", lançado em " + str(ano_lancamento) + " Do genero " + genero_filme +"."

print(mensagem)