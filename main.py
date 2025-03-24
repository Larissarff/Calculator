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
janela.geometry("265x310") # primeiro valor para largura da tela e o segundo para o comprimento
janela.config(bg= cor_rosa)


# dividindo a tela em área de display e área de botões
frame_display = Frame(janela, width=265, height=50, bg= cor_rosa_escuro)
frame_display.grid(row=0, column=0) 

frame_corpo = Frame(janela, width=265, height=260, bg=cor_rosa_escuro)
frame_corpo.grid(row=1, column=0)


# variável de todos os valores
todos_valores = ''


# criando funções:
def entrar_valores(event):

    global todos_valores 

    todos_valores = todos_valores + str(event)

    # passando valor para tela
    valor_texto.set(todos_valores)


# função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)# eval efetua equações passadas como string
    valor_texto.set(resultado)


# função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# criando label
valor_texto = StringVar() # parte responsável por imprimir no display da calculadora os valores 

app_label = Label(frame_display, textvariable=valor_texto, width=17, height=2, padx=7, relief=FLAT, 
                  anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor_rosa_escuro,
                  fg= cor_branca)
app_label.place(x=0,y=0)


# Criando Botoes:
#  font=('Ivy 13 bold') -> responsavel pelo estilo da fonte 
#  relief=RAISED -> sem negrito quando pressionadas
#  overrelief=RIDGE -> por colocar bordas em negrito quando nao estao pressionadas 


# PRIMEIRA LINHA
btn_clear = Button(frame_corpo, command= limpar_tela, text= "C", width=10, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_clear.place(x=0, y=0)

btn_percent = Button(frame_corpo, command= lambda: entrar_valores('%'), text= "%", width=6, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_percent.place(x=110, y=0)

btn_barra = Button(frame_corpo, command= lambda: entrar_valores('/'), text= "/", width=8, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_barra.place(x=180, y=0)


# SEGUNDA LINHA
btn_seven = Button(frame_corpo, command= lambda: entrar_valores('7'), text= "7", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_seven.place(x=0, y=52)

btn_eight = Button(frame_corpo, command= lambda: entrar_valores('8'), text= "8", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_eight.place(x=61, y=52)

btn_nine = Button(frame_corpo, command= lambda: entrar_valores('9'), text= "9", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_nine.place(x=122, y=52)

btn_asterisk = Button(frame_corpo, command= lambda: entrar_valores('*'), text= "*", width=8, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_asterisk.place(x=183, y=52)


# TERCEIRA LINHA
btn_four = Button(frame_corpo, command= lambda: entrar_valores('4'), text= "4", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_four.place(x=0, y=104)

btn_five = Button(frame_corpo, command= lambda: entrar_valores('5'), text= "5", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_five.place(x=61, y=104)

btn_six = Button(frame_corpo, command= lambda: entrar_valores('6'), text= "6", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_six.place(x=122, y=104)

btn_subtraction = Button(frame_corpo, command= lambda: entrar_valores('-'), text= "-", width=8, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_subtraction.place(x=183, y=104)


# QUARTA LINHA
btn_one = Button(frame_corpo, command= lambda: entrar_valores('1'), text= "1", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_one.place(x=0, y=156)

btn_two = Button(frame_corpo, command= lambda: entrar_valores('2'), text= "2", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_two.place(x=61, y=156)

btn_three = Button(frame_corpo, command= lambda: entrar_valores('3'), text= "3", width=5, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_three.place(x=122, y=156)

btn_addition = Button(frame_corpo, command= lambda: entrar_valores('+'), text= "+", width=8, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_addition.place(x=183, y=156)


# QUINTA LINHA
btn_zero = Button(frame_corpo, command= lambda: entrar_valores('0'), text= "0", width=10, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_zero.place(x=0, y=208)

btn_point = Button(frame_corpo, command= lambda: entrar_valores('.'), text= ".", width=6, height=2, bg = cor_rosa_muito_claro, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_point.place(x=110, y=208)

btn_equal = Button(frame_corpo, command= calcular, text= "=", width=8, height=2, bg = cor_rosa, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_equal.place(x=180, y=208)

janela.mainloop()