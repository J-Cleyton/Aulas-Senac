soma = 0

while True:  # O loop vai continuar até que o usuário decida parar
    numero = input("Digite um número (Ou 'sair' para encerrar): ")

    if numero.lower () == 'sair':
        break  # Encerra o loop se o usuário digitar 'Sair'

    try:
        numero = float(numero)  # Tenta converter a entrada para número
        soma += numero # Adiciona o número a soma
    except ValueError:
        print("Por Favor, digite um número válido.")

print(f"A soma dos números digitados é: {soma}")