while True:
    numero = int(inpout("Digite um número (0 para sair): "))

    if numero == 0:
        print("Programa encerrado.")
        break # Encerra o loop se número for 0

    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")
