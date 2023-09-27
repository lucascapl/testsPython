import tkinter as tk
from logs import criaArquivo, adicionaLog

janela = tk.Tk()
janela.title("Teste arquivo")
janela.geometry("500x500")

botao1 = tk.Button(janela, text="Gerar arquivo", command=criaArquivo)
botao2 = tk.Button(janela, text="Adicionar log no arquivo", command=adicionaLog)


botao1.pack()
botao2.pack()

janela.mainloop()
