from tkinter import *
from tkinter import messagebox
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import function

def abrirJanelaNaoLaboratorio(callback_reabrir):
    """
    Abre a janela Laboratório.
    """
    janelaNaoLab = Toplevel()
    janelaNaoLab.title("Projeto Não Laboratório")
    function.centralizar_janela(janelaNaoLab)

    label_lab = Label(janelaNaoLab, text="Bem-vindo ao Não Laboratório", padx=20, pady=20)
    label_lab.pack(pady=10)

    botao_fechar = Button(janelaNaoLab, text="Fechar", command=lambda: [janelaNaoLab.destroy(), callback_reabrir()])
    botao_fechar.pack(side="bottom", pady=20)