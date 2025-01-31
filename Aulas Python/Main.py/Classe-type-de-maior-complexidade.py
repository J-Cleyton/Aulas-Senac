#Exemplos com maior complexidade
#Convertendo a string '1' para Inteiro
valor_inteiro = int('1')  #Converte '1' (String) para 1 (int)
print("O tipo de dado informado é:", '1', type(valor_inteiro))

#Convertendo a letra 'A' para string (Mantém o mesmo tipo, mas apenas para exemplo)
letra = str('A')  #A letra 'A' já é uma string
print("O tipo de dado informado é:", letra, type(letra))

#Convertendo o numero 1.0 para float
valor_decimal = 1.0  #Float
valor_inteiro_2 = int(valor_decimal)  #Converte 1.0 (Float) para 1 (int)
print("O tipo do dado informado é:", valor_decimal, type(valor_inteiro_2))

#Convertendo o resultado da comparação para inteiro
resultado_comparacao = 10 == 9  #Isso retorna false (bool)
resultado_inteiro = int(resultado_comparacao)  #Converte False (bool) oara 0 (int)
print("O tipo do dado informado é:", resultado_inteiro, type(resultado_inteiro))
  