def main():
    while True:
        nome = input("Digite o nome do estudante (ou pressione Enter para sair): ")
        if nome == "":
            break
        try:
            nota = float(input(f"Digite a nota de {nome}: "))
        except ValueError:
            print("Por favor, insira um valor numérico válido para a nota.")
            continue

        if nota >= 6:
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"

        print(f"{nome} está {resultado} com média {nota:.2f}.\n")

if __name__ == "__main__":
    main()