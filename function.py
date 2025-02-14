from tkinter import *
from tkinter import messagebox


def centralizar_janela(janela, largura=800, altura=600):
    """
    Centraliza a janela no centro da tela.
    """
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')


def copiar_para_area_de_transferencia(janela, texto_widget):
    texto_copiado = texto_widget.get("1.0", END).strip()
    janela.clipboard_clear()
    janela.clipboard_append(texto_copiado)
    janela.update()
    messagebox.showinfo("Sucesso!", "XML copiado com sucesso!")