class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo # Atributo
        self.cor = cor       # Atributo
        
    def ligar(self):
        print(f"O {self.modelo} de cor {self.cor} está ligado!")
        
    def desligar(self):
        print(f"O {self.modelo} de cor {self.cor} está desligado")
        
# Criando um objeto de classe Carro.
meu_carro = Carro("Fusca", "Azul")

# Acessando atributos.
print(meu_carro.modelo)  # Fusca
print(meu_carro.cor)     # Azul

# Chamando métodos
meu_carro.ligar()        # "O fusca de cor azul está ligado."
meu_carro.desligar()     # "O fusca de cor azul está delsigado."