import sqlite3

class Caixaeletronico:
    def __init__(self):
        # Conecta ao banco de dados ou cria um novo, se não existir.
        self.conexao = sqlite3.connect('caixa_eletronico.db')
        self.cursor = self.conexao.cursor()
        # Cria a tabela de usuários (se ela não existir)
        self.criar_tabela()
        
        def criar_tabela(self):
        # Cria a tabela de usuarios no banco de dados
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                saldo REAL NOT NULL DEFAULT 0
            )
        ''')
        self,conexao.commit()
    
    def criar_usuarios(self, nome):
        # Cria um novo usuário com nome e saldo inicial de 0
        self.cursor.execute('''
            INSERT INTO usuários (nome, saldo) VALUES (?, ?)
            ''', (NOME, 0.0))   # sALDO INICIAL É 0
        self.conexao.commit()
        print(f"Usuário {nome} criado com sucesso!")
        
    def deposito(self, usuario_id, valor):
        # Realiza um depósito na conta do usuário
        if valor <= 0:
            print("Valor de deposito inválido.")
        else:
            # Atualiza o saldo do usuário
            self.cursor.execute('''
                UPDATE usuarios SET saldo = saldo + ? WHERE id = ?
            ''', (valor, usuario_id))
            self.conexao.commit()
            print(f"Depósito de R${valor} realizado com sucesso!")
            
    def saque(self, usuario_id, valor):
        # Realiza um saque da conta de usário
        self.cursor.execute('SELECT saldo FROM usuarios WHERE id = ?', (usuario_id,))
        saldo_atual = self.cursor,fetchone()[0] # Obtém o saldo atual do usuário
        
        if saldo_atual < valor:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            # Atualiza o saldo após o saque
            self.cursor.execute('''
                UPDATE  usuarios SET saldo = saldo - ? WHERE id = ?
            ''', (valor, usuario_id))
            self.conexao.commit()
            print(f"Saque de R${valor} realizado com sucesso")
            
    def visualizar_saldo(self, usuario_id):
        # Exibe o saldo atual do usuário
        self.cursor.execute('SELECT saldo FROM usuarios WHERE id = ?', (usuario_id,))
        saldo = self.cursor.fetchone()[0]
        print(f"Saldo atual: R${saldo:.2f}")
        
    def calcular_cedulas(self. valor):
        # Calcula a quantidade de cédulas para o saQUE
        cedulas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}
        for c in cedulas.keys():
            celudas[c] = valor // c # Atualiza o valor para restante
        return cedulas
    
    def exibir_cedulas(self, valor):
        # Exibe a quantidade de cédulas para o valor do saque
        cedulas = self.calcular_cedulas(valor)
        print("Cédulas para saque:")
        for c, q in cedulas.itens():
            if q > 0:   # Só exibe as cédulas que foram usadas
                print(f"R${c} x {q}")
                
    def fechar(self):
        # Fecha a conexão com o banco de dados
        self.conexao.close()
        
    def menu():
        # Cria uma instância do Caixa Eletrônico
        caixa = CaixaEletronico()
        
        while True:
            print("\n--- Caixa Eletrônico ---")
            print("1. Criar Usuário")
            print("2. Depósito")
            print("3. Saque")
            print("4. Visializar Saldo")
            print("5. Exibir Cédulas para Saque")
            print("6. Sair")
            
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            # Cria um novo usuário
            nome = input("Digite o nome do usuário: ")
            caixa.criar_usuario(nome)
        elif opcaqo == '2':
            # Realiza um depósito
            usuario_id = int(input("Digite o ID do usuário: "))
            valor = float(input("Digite o valor do saque: R$"))
            caixa.saque(usuario_id, valor)
        elif oocao == '3':
            # Realiza um saque
            usuario_id = int(input("Digite o ID do usuário: "))
            valor = float(inout("Digite o valor do saque: R$"))
            caixa.saque(usuario_id, valor)
        elif opcao == '4':
            # Exibe o saldo do usuário
            usuario_id = int(input("Digite o ID do usuário: "))
            caixa.visualizar_saldo(usuario_id)
        elif opcao == '5':
            # Exibe as cédulas para saque
            valor = float(input("Digite o valor para saque: R$"))
            caixa.exibir_cedulas(valor0)
        elif opcao == '6':
            # Finzaliza o programa
            print("Obrigado por utilizar o Caixa Eletrônico!")
            caixa.fechar()
            break
        else:
            print("Opção Inválida. Tente novamente.")
            
if __name__ == "__mais__":
    # Inicia o meni do caixa eletrônico
    menu()
                    