import tkinter as tk

def verificaClick():
    print("Botão foi clicado!")

janela = tk.Tk()
janela.title("Teste arquivo")
janela.geometry("500x500")

botao1 = tk.Button(janela, text="Clique aqui", command=verificaClick)


botao1.pack()

janela.mainloop()
