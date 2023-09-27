from datetime import datetime
import os
dirAtual = os.getcwd()
caminhoArquivo = os.path.join(dirAtual, "teste.txt")

def criaArquivo():


    if not os.path.isfile(caminhoArquivo):
        with open(caminhoArquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write("Este é o conteúdo do arquivo 'teste.txt'\n")

        print("O arquivo 'teste.txt' foi criado.")
    else:
        print("O arquivo 'teste.txt' já existe no diretório.")

def adicionaLog():
    horario = datetime.now()
    localErro = "routes.py"
    with open(caminhoArquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"Ocorreu um erro em {localErro} às {horario}\n")