class Calculadora:
    # Função que soma dois números.
    def somar(self, a, b):
        return a + b

    # Função que subtrai dois números.
    def subtrair(self, a, b):
        return a - b

    # Função que multiplica dois números.
    def multiplicar(self, a, b):
        return a * b

    # Função que divide dois números.
    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Não é possível dividir por zero"

    # Função principal que chama as operações matemáticas.
    def calcular(self):
        print("Escolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        
        escolha = input("Digite o número da operação: ")
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            resultado = self.somar(num1, num2)
        elif escolha == '2':
            resultado = self.subtrair(num1, num2)
        elif escolha == '3':
            resultado = self.multiplicar(num1, num2)
        elif escolha == '4':
            resultado = self.dividir(num1, num2)
        else:
            resultado = "Operação inválida."
        
        print(f"Resultado: {resultado}")

# Criando uma instância da classe Calculadora
calc = Calculadora()

# Chamando o método calcular para iniciar a interação com o usuário
calc.calcular()