import tkinter as tk
from logs import criaArquivo

janela = tk.Tk()
janela.title("Teste arquivo")
janela.geometry("500x500")

botao1 = tk.Button(janela, text="Gerar arquivo", command=criaArquivo)




janela.mainloop()
