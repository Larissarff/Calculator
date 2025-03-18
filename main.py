from tkinter import *
from tkinter import ttk # importando o tkinter

# cores 
cor_rosa_escuro = "#851b63"
cor_rosa = "#b837a0"
cor_rosa_claro = "#f77ee1"
cor_rosa_muito_claro = "#f2a5e4"
cor_preta = "#0a080a"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318") # primeiro valor para largura da tela e o segundo para o comprimento
janela.config(bg= cor_rosa)

# dividindo a tela em área de display e área de botões
frame_display = Frame(janela, width=235, height=50, bg= cor_rosa_claro)
frame_display.grid(row=0, column=0) 

frame_corpo = Frame(janela, width=235, height=258, bg=cor_rosa)
frame_corpo.grid(row=1, column=0)

# criando botoes
btn_1 = Button(frame_corpo, text= "C", width=11, height=2, bg = cor_rosa_muito_claro)
btn_1.place(x=0, y=0)

janela.mainloop()