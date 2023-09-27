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
    horario = horario.strftime("%Y-%m-%d %H:%M:%S")
    localErro = "routes.py"
    try:
        with open(caminhoArquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"Ocorreu um erro em {localErro} às {horario}\n")
        print('Log registrado com sucesso.')
        
    except FileNotFoundError as e:
        print(f"Erro: {e} - O arquivo não foi encontrado.")
    except PermissionError as e:
        print(f"Erro: {e} - Permissão negada para acessar o arquivo.")
    except Exception as e:
        print(f"Erro desconhecido: {e}")