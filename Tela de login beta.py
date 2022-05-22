from concurrent.futures.process import _python_exit
import sqlite3
from sqlite3 import Error
from turtle import left
banco = sqlite3.connect('banco1.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")

#Tkinter criar tela de login

from tkinter import*
from tkinter import Tk, ttk
from tkinter import messagebox

# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

#criando janela-------------
janela = Tk()
janela.title('Tela login beta')
janela.geometry('350x320')
janela.configure(background=co1)
janela.resizable(width= FALSE, height=FALSE)

#dividindo a janela
frame_janela = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_janela.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_janelabaixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_janelabaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#criando labels de cima--------
l_nome = Label(frame_janela, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_janela, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

#funçao para verificar senha
credenciais = ['Davi','dadatata13']
def verifica_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo admin')

    elif credenciais[0] == nome and credenciais[1] == senha: 
         messagebox.showinfo('Login', 'Seja bem vindo de volta' + credenciais [0])

    else: 
         messagebox.showwarning('Erro', 'Verifique Login ou Senha')

#funçao após verificaçao

def nova_janela():
  l_nome = Label(frame_janela, text='Usuário:' +credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
  l_nome.place(x=5, y=5)

  l_linha = Label(frame_janela, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
  l_linha.place(x=10, y=45)

  l_nome = Label(frame_janelabaixo, text='Seja bem vindo!:' +credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
  l_nome.place(x=5, y=105)



#criando labels de baixo--------
l_nome = Label(frame_janelabaixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_janelabaixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=12, y=50)

l_pass = Label(frame_janelabaixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_janelabaixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=12, y=125)

b_confirmar =  Button(frame_janelabaixo, command=verifica_senha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief= RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=175)

b_registrar =  Button(frame_janelabaixo, text='Registre-se',  width= 12,  font=('Ivy 8 '), bg=co1, fg=co2, relief= RAISED)
b_registrar.place(x=5, y=226)

janela.mainloop()
