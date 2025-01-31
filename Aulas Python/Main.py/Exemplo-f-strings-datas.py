#Primeiro impor, utilizando para trabalhar com datas e horas
from datetime import datetime
#Data atual
data_atual = datetime.now()
#A função now(), passada irá obter a data e hora atual da máquina
#Devido a isso, precisamos chamar um import, para poder utilizar desta função.

#Formatando a data com F-Strings
data_formatada = f'A data de hoje é: {data_atual:%d/%m/%y}'
print(data_formatada)