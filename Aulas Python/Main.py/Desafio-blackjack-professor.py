import random  # Importa a biblioteca 'random' para embaralhar o baralho


# Definindo os naipes e os valores das cartas
naipe = ['\u2660', '\u2665', '\u2666', '\u2663']  # Representação dos naipes: Espadas, Copas, Ouros, Paus
valor = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']

# Criação do baralho combinando os valores com os naipes
baralho = [f'{v} {n}' for in naipe for v in valor]  # Cria uma lista de cartas (ex: 'A♠', '2♠', etc.)
random.shuffle(baralho)  # Embaralha as cartas para garantir aleatoriedasde

# Função para calcular a pontuação da mão de um jogador
def calcular_pontuacao(mao):
    pontuacao = 0 # Inicializa a pontuação com 0
    num_as = 0 # Conta quantos As a mão possui
    for carta in mao: # Para cada carta na mão
        valor = carta.split()[0] # Pega o valor da carta (antes do naipe)
        
        # se a carta for uma figura ('J', 'Q', 'K'), vale 10 pontos
        if valor in ['J', 'Q', 'K']:
            pontuacao += 10
            # Se for um Ás (A), inicializamos com 11 pontos
        elif valor == 'A':
            pontuacao += 11
            num_as += 1 # Conta o número As
        else:
            pontuacao += int(valor) # Se for um número (2 a 10), adiciona seu valor númerico
            
# Se a pontuação ultrapassar 21 e houver As, converte-os de 11 para 1 (ajustando a pontuação)
def mostrar_mao(mao, revelar_dealer=False):
    mao_str = ', '.join(mao) # Concatena todas as cartas da mão em uma string
    if revelar_dealer: # Se for para revelar as cartas do dealer
        return f"Dealer: {mao_str} - Pontuação: {calcular_pontuacao(mao)}" # Mostra as cartas do dealer e sua pontuação
    return f"Dealer: {mao[0]}, ?" # Caso contrário, mostra a primeira carta do dealer e oculta a segunda

# Mão inicial: O jogador e o dealer recebem 2 cartas
jogador_map = [baralho.pop(), baralho.pop()] # O jogador recebe 2 cartas do baralho
dealer_mao = [baralho.pop(), baralho.pop()] # O dealer também recebe 2 cartas

# Exibe a mão inicial do jogador e do dealer
print("Mão inicial:")
print(f"Jogador: {', '.join(jogador_mao)} - pontuação: {calcular_pontuacao(jogador_mao)}") # Mostra as cartas e pontuação do jogador
print(mostrar_mao(dealer_mao)) # Mostra a mão do dealer (com a segunda carta oculta)

# Loop do jogo: O jogador pode pedir mais cartas até atingir ou ultrapassar 21 pontos
print("Mão Inicial:")
print(f"Jogador: {', '.join(jogador_mao)} -  Pontuação: {calcular_pontuacao(jogador_mao)}") # Mostra as cartas e pontuação do jogador
