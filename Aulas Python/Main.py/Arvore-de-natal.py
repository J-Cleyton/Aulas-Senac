# Altura da árvore
altura = 10

# Parte da copa da árvore
for i in range(altura):
    # Imprime espaçoes para centralizar a árvore
    print(" " * (altura - i - 1) + "*" * (2 * i + 1))

# Parte do tronco da árvore
for i in range(2):
    print(" " * (altura - 1) + "|") 