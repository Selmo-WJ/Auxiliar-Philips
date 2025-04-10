from tkinter import messagebox
import Laboratory.JanelaLaboratory
import NoLaboratory.NoLaboratory as NoLaboratory
import Trigger.JanelaTrigger as Trigger
import Utils.function as function
from tkinter import *

def criarJanelaPrincipal():
    """
    Cria e exibe a janela principal.
    """
    if hasattr(criarJanelaPrincipal, "janela") and criarJanelaPrincipal.janela.winfo_exists():
        criarJanelaPrincipal.janela.destroy()

    criarJanelaPrincipal.janela = Tk()
    janela = criarJanelaPrincipal.janela
    function.centralizar_janela(janela)
    janela.title("Sistema XML para integração Padrão Tasy")
    janela.geometry("500x400")
    janela.resizable(False, False)

    top_frame = Frame(janela, bg="#f0f0f0", height=60, relief="ridge", bd=2)
    top_frame.pack(fill=X)

    label_title = Label(top_frame, text="Sistema XML para integração Padrão Tasy", font=("Arial", 14, "bold"), bg="#f0f0f0")
    label_title.pack(pady=15)

    main_frame = Frame(janela, bg="#ffffff")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    texto_orientacao = Label(main_frame, text="Selecione a Aplicação:", font=("Arial", 12), bg="#ffffff")
    texto_orientacao.pack(pady=20)

    botaoLaboratorio = Button(main_frame, text="Laboratório", font=("Arial", 10), width=20, command=lambda: abrirJanelaLaboratorio(janela))
    botaoLaboratorio.pack(pady=10)

    botaoNaoLaboratorio = Button(main_frame, text="Não Laboratório", font=("Arial", 10), width=20, command=lambda: abrirJanelaNaoLaboratorio(janela))
    botaoNaoLaboratorio.pack(pady=10)
    
    botaoGerarTrigger = Button(main_frame, text="Gerador de Trigger", font=("Arial", 10), width=20, command=lambda: abrirJanelaTrigger(janela))
    botaoGerarTrigger.pack(pady=10)


    footer_frame = Frame(janela, bg="#f0f0f0", height=40, relief="ridge", bd=2)
    footer_frame.pack(fill=X, side=BOTTOM)

    texto_rodape = Label(footer_frame, text="Criado por Selmo Werner Júnior", font=("Arial", 10), bg="#f0f0f0")
    texto_rodape.pack(pady=10)

    janela.protocol("WM_DELETE_WINDOW", janela.quit)
    janela.mainloop()

def abrirJanelaLaboratorio(janelaAnterior):
    """
    Fecha a janela anterior e abre a janela Laboratório.
    """
    janelaAnterior.withdraw()  
    Laboratory.JanelaLaboratory.abrirJanelaLaboratorio(lambda: janelaAnterior.deiconify())  
def abrirJanelaNaoLaboratorio(janelaAnterior):
    """
    Fecha a janela anterior e abre a janela Não Laboratório.
    """
    janelaAnterior.withdraw()  
    NoLaboratory.abrirJanelaNaoLaboratorio(lambda: janelaAnterior.deiconify())  
def abrirJanelaTrigger(janelaAnterior):
    """
    Fecha a janela anterior e abre a janela Trigger.
    """
    janelaAnterior.withdraw()  
    Trigger.abrirJanelaTrigger()

if __name__ == "__main__":
    criarJanelaPrincipal()