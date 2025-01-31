class Produto:
    # Classe que representa um produto com informações de nome, preço, estoque e vendas.
    
    def __init__(self, nome, preco, estoque, vendas):
        # Inicializa um objeto Produto com nome, preço, estoque e vendas
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.vendas = vendas

    def atualizar_estoque(self, quantidade):
        # Atualiza o estoque do produto
        self.estoque += quantidade
    
    def atualizar_vendas(self, quantidade):
        # Atualiza as vendas do produto
        self.vendas += quantidade

    def valor_total_vendas(self):
        # Calcula o valor total de vendas do produto
        return self.vendas * self.preco


class SistemaControleEstoque:
    # Classe que representa o sistema de controle de estoque e vendas:

    def __init__(self):
        # Inicializa o sistema com um dicionário vazio para armazenar os produtos e valores de vendas
        self.produtos = {}  # Dicionário para armazenar produtos, chave: nome do produto, valor: objeto Produto
        self.valor_total_vendas = 0  # Inicializa o valor total das vendas como 0
        self.produto_mais_vendido = None  # Inicializa a variável para armazenar o produto mais vendido
        self.maior_quantidade_vendida = 0  # Inicializa a quantidade vendida máxima como 0

    def adicionar_produto(self, nome, preco, estoque, vendas):
        # Adiciona ou atualiza um produto no sistema.
        if nome in self.produtos:
            # Se o produto existe, atualiza o estoque e vendas do produto existente
            produto = self.produtos[nome]
            produto.atualizar_estoque(estoque)  # Atualiza o estoque do produto
            produto.atualizar_vendas(vendas)  # Atualiza as vendas do produto
        else: 
            # Se o produto não existe, cria um novo objeto Produto e adiciona ao dicionário
            produto = Produto(nome, preco, estoque, vendas)
            self.produtos[nome] = produto  # Adiciona o novo produto ao dicionário (corrigido: era Produto, agora é produto)

    def calcular_vendas_totais(self):
        # Calcula o valor total das vendas e determina o produto mais vendido.
        for produto in self.produtos.values():
            # Soma o valor total das vendas de cada produto
            self.valor_total_vendas += produto.valor_total_vendas()

            # Verifica se a quantidade vendida desse produto é maior que a anterior
            if produto.vendas > self.maior_quantidade_vendida:
                self.maior_quantidade_vendida = produto.vendas  # Atualiza a maior quantidade vendida
                self.produto_mais_vendido = produto  # Atualiza o produto mais vendido

    def exibir_relatorio(self):
        # Exibe o relatório com as informações de todos os produtos.
        for produto in self.produtos.values():
            print(f"\nProduto: {produto.nome}")
            print(f"Estoque: {produto.estoque}")
            print(f"Quantidade vendida: {produto.vendas}")
            print(f"Valor total das vendas: R$ {produto.valor_total_vendas():.2f}")

        # Exibe o valor total das vendas e o produto mais vendido
        print(f"\nValor total de vendas de todos os produtos: R$ {self.valor_total_vendas:.2f}, com {self.maior_quantidade_vendida} unidades vendidas.")


def boas_vindas():
    # Exibe as boas-vindas e informações iniciais do sistema.
    print("Bem-vindo ao sistema de controle de estoque de vendas.")
    print("Você pode adicionar produtos, inserir preços, quantidades em estoque e quantidades vendidas.")
    print("Para sair, basta deixar o nome em branco e pressionar Enter.")

def obter_entrada_produto():
    # Solicita e valida as entradas do usuário para um produto.
    nome_produto = input("\nDigite o nome do produto/item (ou pressione Enter para sair do programa): ")
    if nome_produto == "":
        return None  # Retorna None para indicar que o usuário quer sair

    # Solicita o preço do produto
    try:
        preco_produto = float(input(f"Qual o preço unitário do {nome_produto}?: R$ "))  # Alterado para float para permitir preços com centavos
    except ValueError:
        print("Entrada inválida! O preço deve ser um número.")
        return obter_entrada_produto()  # Chama recursivamente para tentar novamente

    # Solicita a quantidade em estoque
    try:
        estoque_produto = int(input(f"Digite a quantidade em estoque do {nome_produto}: "))
    except ValueError:
        print("Entrada inválida! A quantidade deve ser um número inteiro.")
        return obter_entrada_produto()  # Chama recursivamente para tentar novamente

    # Solicita a quantidade vendida
    try:
        quantidade_vendida = int(input(f"Digite a quantidade vendida do {nome_produto}: "))
    except ValueError:
        print("Entrada inválida! A quantidade vendida deve ser um número inteiro.")
        return obter_entrada_produto()  # Chama recursivamente para tentar novamente

    return nome_produto, preco_produto, estoque_produto, quantidade_vendida


def main():
    # Função principal que executa o fluxo do programa.
    sistema = SistemaControleEstoque()  # Instancia o sistema de controle de estoque

    boas_vindas()

    while True:
        # Coleta os dados do produto
        dados_produto = obter_entrada_produto()
        if dados_produto is None:
            break  # Sai do loop se o nome do produto for deixado em branco

        nome_produto, preco_produto, estoque_produto, quantidade_vendida = dados_produto
        sistema.adicionar_produto(nome_produto, preco_produto, estoque_produto, quantidade_vendida)

    # Calcula as vendas totais e o produto mais vendido
    sistema.calcular_vendas_totais()

    # Exibe o relatório final
    sistema.exibir_relatorio()
    
    # Finalização
    print("\nObrigado por utilizar nosso programa! Em breve iremos ter interface.")


# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    main()