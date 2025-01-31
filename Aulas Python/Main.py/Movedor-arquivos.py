# Importa o módulo os, que fornece uma maneira de interagir com o sistema operacional.
# Como manipular arquivos e diretórios.
import os

# Importa o módulo shutil, que fornece funções para operações de arquivos e diretórios.
# Incluindo mover arquivos de um lugar para outro.
import shutil

def organizar_por_extensao(diretorio):
    # Dicionário para mapear extensões de arquivos aos diretórios de destino
    extensoes = {
        'txt': 'Arquivos TXT',
        'png': 'Arquivos PNG',
        'docx': 'Arquivos DOCX',
        'pdf': 'Arquivos PDF',
        'jpg': 'Arquivos JPG',
        # Adicione mais extensões e diretórios conforme necessário.
    }

    # Verifica se os diretórios para cada tipo de arquivo já existem. Se não, cria-os.
    for destino in extensoes.values():
        caminho_destino = os.path.join(diretorio, destino)
        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)

    # Percorre todos os arquivos no diretório.
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

        # Verifica se o item é um arquivo (não uma pasta).
        if os.path.isfile(caminho_arquivo):
            # Pega a extensão do arquivo (sem o ponto inicial)
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao[1:].lower()  # Converte a extensão para minúsculas.

            # Se a extensão do arquivo está no dicionário, move o arquivo para o diretório correspondente.
            if extensao in extensoes:
                destino = extensoes[extensao]
                caminho_destino = os.path.join(diretorio, destino, arquivo)
                shutil.move(caminho_arquivo, caminho_destino)
                print(f'Movido: {arquivo} para {destino}')

# Organiza os arquivos no diretório especificado
dir_destino = "C:\Organizado"
organizar_por_extensao(dir_destino)