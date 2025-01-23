from tkinter import *

def teste():
    print('teste com funcao') 


janela = Tk()
janela.title("Sistema XML")
texto_orientacao= Label(janela, text="teste")
texto_orientacao.grid(column=0,row=0)
texto_orientacao2= Label(janela, text="tefdfste")
texto_orientacao2.grid(column=0,row=1)

botao = Button(janela,text="teste aqui",command=teste)
botao.grid(column=0,row=3)

texto_botao = Label(janela, )
janela.mainloop()