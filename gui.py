# Autor:    diX - Diego Silva
# GitHub:   https://github.com/diwalker
# Email:    dwalkerserver@gmail.com
# Apoie meu trabalho: pix telefone 87988370228
import tkinter
from tkinter import *
from tkinter import Tk
from playsound import playsound
import main, acerto2, fora, fora2
from threading import Thread

def play():
    playsound("media/jam.mp3")

root: Tk = Tk()
root.iconbitmap('media/ball.ico')
root.geometry("800x500")
root.minsize(800, 500)
root.maxsize(800, 500)

logo = tkinter.PhotoImage(file='media\logo.png')  # Logo
mainTitle = tkinter.Label(root, image=logo, bg='#000')
mainTitle.pack()
mainTitle.imagem = logo

root.frame_cima = Frame(root, background='#000') # Cria dois frames e os empacota
root.frame_baixo = Frame(root, background='#000')
root.frame_cima.pack()
root.frame_baixo.pack()

root.radio_valor = IntVar() # Cria os radio buttons e o label e os empacota
root.label = Label(root.frame_cima,text='Bem-vindo ao BASKETBOT, o Preditor de arremessos no Basquete! Selecione uma opção:', bg='#000',fg='#fff', font=80, padx=10, pady=10)
root.cesta1 = Radiobutton(root.frame_cima, text='1: Cesta', bg='#000', fg='#fff', pady=7, padx=5, font=40,variable=root.radio_valor, value=1, command=lambda: main.main1())
root.cesta2 = Radiobutton(root.frame_cima, text='2: Cesta', bg='#000', fg='#fff', pady=7, padx=5, font=40,variable=root.radio_valor, value=2, command=lambda: acerto2.main2())
root.erro1 = Radiobutton(root.frame_cima, text='3: Pra Fora', bg='#000', fg='#fff', pady=7, padx=5, font=40,variable=root.radio_valor, value=3, command=lambda: fora.main3())
root.erro2 = Radiobutton(root.frame_cima, text='4: Pra Fora', bg='#000', fg='#fff', pady=7, padx=5, font=40,variable=root.radio_valor, value=4, command=lambda: fora2.main4())
root.label.pack(anchor='center')
root.cesta1.pack(anchor='center')
root.cesta2.pack(anchor='center')
root.erro1.pack(anchor='center')
root.erro2.pack(anchor='center')

root.quit = Button(root.frame_baixo, text='Sair', bg='#28282b', font=('Helvetica', 11, 'bold'), pady=10, fg='#ffffff', cursor='hand2',command=root.quit)
root.sound = Button(root.frame_baixo, text='Som', bg='#28282b', font=('Helvetica', 11, 'bold'), pady=10,fg='#ffffff', cursor='hand2',command=lambda: [Thread(target=play, daemon=True).start()])
root.quit.pack(side='left', ipadx=30, ipady=3)
root.sound.pack(side='right', ipadx=30, ipady=3)

root.title('BASKETBOT    by @diwalker')
root.config(background='#000', padx=20, pady=20)
root.mainloop()

if __name__ == "__main__":
    gui()
