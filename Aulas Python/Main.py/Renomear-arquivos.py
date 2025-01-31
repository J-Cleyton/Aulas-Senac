import os

def renomear_arquivos_em_passa(diretorio):
    # Verificar todos os arquivos no diretorio
    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        # Verificar se é um arquivo (e nao uma pasta)
        if os.path.isfile(caminho_arquivo):
            # Substituir espaços por underscores
            novo_nome = nome_arquivo.replace(' ', '_')

            # Adicionar o prefixo "backuo_"
            novo_nome = 'backup_' + novo_nome

            # Caminho completo para o novo nome do arquivo
            novo_caminho = os.path.join(diretorio, novo_nome)

            # Renomear o arquivo
            os.rename(caminho_arquivo, novo_caminho)
            print(f'Organizado: {nome_arquivo} -> {novo_nome}')
            
def apagar_texto_nos_nomes(diretori0, texto_a_remover):
        # Verificar todos os arquivos no diretorio
        for nome_arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)

            # Verificar se é um arquivo (e não uma pasta)
            if os.path.isfile(caminho_arquivo):
                # Apagar o texto especificado do nome do arquivo
                if texto_a_remover in nome_arquivo:
                    novo_nome = nome_arquivo.replace(texto_a_remover, '')

                    # Caminho completo para novo nome do arquivo
                    novo_caminho = os.path.join(diretorio, novo_nome)

                    # Renomear o arquivo
                    os.rename(caminkho_arquivo, novo_caminho)
                    print(f'Organizado: {nome_arquivo} -> {novo_nome}')

def adicionar_texto_nos_nomes(diretorio, texto_a_adicionar):
     # Verificar todos os arquivos no diretorio
     for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        # Verificar se é um arquivo (e não uma pasta)
        if os.path.isfile(caminho_arquivo):
            # Adicionar o texto especificado ao nome do arquivo
            novo_nome = texto_a_adicionar + nome_arquivo

            # Caminho completo para o nome nome do arquivo
            novo_caminho = os.path.join(diretorio, novo_nome)

            # Renomear o arquivo
            os.rename(caminho_arquivo, novo_caminho)
            print(f'Organizado: {nome_arquivo} -> {novo_nome}')

def menu(diretorio):
    while True:
        print("\nEscolha uma opção:")
        print("1. Renomear arquivos (Adicionar prefixo 'backup_' e substituir espaçoes por undercores)")
        print("2. Apagar texto especifico nos nomes dos arquivos")
        print("3. Adicionar texto nos nomes dos arquivos")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            renomear_arquivos_em_massa(diretorio)
        elif escolha == '2':
            texto = input("Digite o texto que você deseja remover dos nomes dos arquivos: ")
            adicionar_texto_nos_nomes(diretorio, texto)
        elif escolha == '3':
            texto = input("Digite o texto que você deseja adicionar aos nomes do arquivo: ")
            adicionar_texto_nos_nomes(diretorio, texto)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente Nnovamente.")
            
# Defina o diretório onde estão os arquivos a serem renomeados
diretorio = 'C:\Organizado' # Substitua com o caminho correto

# Inicia o menu opções
menu(diretorio)