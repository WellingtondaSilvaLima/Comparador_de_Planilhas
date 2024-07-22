from tkinter import Label, Button, filedialog, messagebox, Entry, END, Tk, mainloop, Frame, LEFT, RIGHT, PhotoImage
import pandas as pd


# -------------Configurações da Tela-----------------
janela = Tk()
largura = 550
altura = 230

icon = PhotoImage(file='imagem/logo.png')

janela.title('Comparador')
janela.iconphoto(False, icon)
janela.geometry(f'{largura}x{altura}')
janela.resizable(False, False)
janela.configure(bg='purple')
# ---------------------------------------------------


janela.mainloop()
