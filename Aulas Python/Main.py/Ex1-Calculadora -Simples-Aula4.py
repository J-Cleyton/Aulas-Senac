#Solicitar ao usuario para informar os números
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

#Solicitar ao usuario a operação desejada com explicação
operacao = input(
    "digite a operação que deseja realizar (+, -, /, %):\n"
    "Mais: +\n"
    "Menos: -\n"
    "Vezes: *\n"
    "Dividir: /\n"
    "Resto da divisão : %\n"
)

#Realizar a operação conforme solicitado
if operacao == '+':
    resultado = primeiro_numero + segundo_numero
    operacao_nome = "Soma"
elif operacao == '-':
    resultado = primeiro_numero - segundo_numero
    operacao_nome = "Subtração"
elif operacao == '*':
    resultado = primeiro_numero * segundo_numero
    operacao_nome = "Multiplicação"
elif operacao == '/':
    resultado = primeiro_numero / segundo_numero if segundo_numero != 0 else "Erro: Divisão por zero"
    operacao_nome = "Divisão"
elif operacao == '%':
    resultado = primeiro_numero % segundo_numero
    operacao_nome = "Resto da divisão"
else:
    resultado = "Operação Inválida"
    operacao_nome = ""

    #Exibir o resultado com concatenação e f-string
if resultado != "Operação inválida": #Caso não escolha uma opção
    print(f'O resultado da {operacao_nome} entre {primeiro_numero} e {segundo_numero} é: {resultado}')
else:
    print("Operação Inválida. Tente Novamente.")