from tkinter import *
from tkinter import ttk # importando o tkinter

# cores 
cor_branca = "#FFFFFF"
cor_rosa_escuro = "#851b63"
cor_rosa = "#fa75d2"
cor_rosa_claro = "#ed87cf"
cor_rosa_muito_claro = "#fac8eb"
cor_preta = "#0a080a"

janela = Tk()
janela.title("Calculadora")
janela.geometry("265x358") # primeiro valor para largura da tela e o segundo para o comprimento
janela.config(bg= cor_rosa)

# dividindo a tela em área de display e área de botões
frame_display = Frame(janela, width=265, height=50, bg= cor_rosa_escuro)
frame_display.grid(row=0, column=0) 

frame_corpo = Frame(janela, width=265, height=308, bg=cor_rosa_escuro)
frame_corpo.grid(row=1, column=0)

# criando label

app_label = Label(frame_display, text='123456789', width=16, height=2, padx=7, relief=FLAT, 
                  anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor_rosa_escuro,
                  fg= cor_branca)
app_label.place(x=0,y=0)

# Criando Botoes:
#  font=('Ivy 13 bold') -> responsavel pelo estilo da fonte 
#  relief=RAISED -> sem negrito quando pressionadas
#  overrelief=RIDGE -> por colocar bordas em negrito quando nao estao pressionadas 

# PRIMEIRA LINHA
btn_clear = Button(frame_corpo, text= "C", width=9, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_clear.place(x=0, y=0)

btn_percent = Button(frame_corpo, text= "%", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_percent.place(x=115, y=0)

btn_barra = Button(frame_corpo, text= "/", width=5, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_barra.place(x=190, y=0)

# SEGUNDA LINHA

btn_seven = Button(frame_corpo, text= "7", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_seven.place(x=0, y=62)

btn_eight = Button(frame_corpo, text= "8", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_eight.place(x=64, y=62)

btn_nine = Button(frame_corpo, text= "9", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_nine.place(x=129, y=62)

btn_asterisk = Button(frame_corpo, text= "*", width=5, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_asterisk.place(x=190, y=62)

# TERCEIRA LINHA

btn_four = Button(frame_corpo, text= "4", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_four.place(x=0, y=124)

btn_five = Button(frame_corpo, text= "5", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_five.place(x=64, y=124)

btn_six = Button(frame_corpo, text= "6", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_six.place(x=129, y=124)

btn_subtraction = Button(frame_corpo, text= "-", width=5, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_subtraction.place(x=190, y=124)

# QUARTA LINHA

btn_one = Button(frame_corpo, text= "1", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_one.place(x=0, y=186)

btn_two = Button(frame_corpo, text= "2", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_two.place(x=64, y=186)

btn_three = Button(frame_corpo, text= "3", width=4, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_three.place(x=129, y=186)

btn_addition = Button(frame_corpo, text= "+", width=5, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_addition.place(x=190, y=186)

# QUINTA LINHA
btn_zero = Button(frame_corpo, text= "0", width=9, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_zero.place(x=0, y=248)

btn_point = Button(frame_corpo, text= ".", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_point.place(x=115, y=248)

btn_equal = Button(frame_corpo, text= "=", width=5, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_equal.place(x=190, y=248)

janela.mainloop()