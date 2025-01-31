import random

def criar_baralho():
    baralho = []
    naipes = ['♥', '♦', '♠', '♣']
    valores = ['2', '3', '4', '5','6', '7', '8', '9', '10',
'Valete', 'Dama', 'Rei', 'Às']
    for naipe in naipes:
        for valor in valores:
            baralho.append((valor, naipe))
    random.shuffle(baralho)
    return baralho

def calcular_valor_mao(mao):
    valor = 0
    ases = 0
    for carta in mao:
        if carta[0] in ['Valete', 'Dama', 'Rei']:
            valor += 10
        elif carta[0] == 'Ás':
            valor += 11
            ases += 1
        else:
            valor += int(carta[0])
    while valor > 21 and ases:
        valor -= 10
        ases-= 1
    return valor
    
def jogar_blackjack():
    baralho = criar_baralho()
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_dealer = [baralho.pop(), baralho.pop()]
    
    print(" Sua mão:", mao_jogador)
    print("Mão de dealer: [", mao_dealer[0], ", ? ]")
    
    while True:
        acao = input("Deseja 'hit' ou 'stand'? ").lower()
        if acao == 'hit':
            mao_jogador.append(baralho.pop())
            print("Sua mão:", mao_jogador)
            if calcular_valor_mao(mao_jogador) > 21:
                print("Você estourou! Dealer vence.")
                return
        
        elif acao == 'stand':
            break
            
    while calcular_valor_mao(mao_dealer) < 17:
        mao_dealer.append(baralho.pop())
        
    print("Mão do deader:", mao_dealer)
    
    valor_jogador = calcular_valor_mao(mao_jogador)
    valor_dealer = calcular_valor_mao(mao_dealer)
    
    if valor_dealer > 21 or valor_jogador > valor_dealer:
        print("Você venceu!")
    elif valor_jogador < valor_dealer:
        print("Dealer vence.")
    else:
        print("Empate.")
        
jogar_blackjack()