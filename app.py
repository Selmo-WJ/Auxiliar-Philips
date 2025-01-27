from tkinter import messagebox
import function
from tkinter import *
import re
import requests  # Importando a biblioteca para requisições HTTP (se necessário)

def criarJanelaPrincipal():
    """
    Cria e exibe a janela principal.
    """
    # Criando a janela principal como Toplevel se já existir outra instância
    if hasattr(criarJanelaPrincipal, "janela") and criarJanelaPrincipal.janela.winfo_exists():
        criarJanelaPrincipal.janela.destroy()

    criarJanelaPrincipal.janela = Tk()
    janela = criarJanelaPrincipal.janela
    function.centralizar_janela(janela)
    janela.title("Sistema XML para integração Padrão Tasy")

    # Label de orientação
    texto_orientacao = Label(janela, text="Selecione a Aplicação:")
    texto_orientacao.pack(side=TOP, fill=X, padx=0, pady=50)

# Campo para inserir o endpoint
    texto_endpoint = Label(janela, text="Digite o Endpoint para Simulação:")
    texto_endpoint.pack(pady=5)

    entrada_endpoint = Entry(janela, width=40)
    entrada_endpoint.pack(pady=5)

    # Função de validação do endpoint
    def validar_endpoint():
        endpoint = entrada_endpoint.get()
        
        # Regex para verificar se o endpoint é uma URL válida
        regex = r'^(http|https)://[a-zA-Z0-9-_.]+(\.[a-zA-Z]{2,})+(:[0-9]{1,5})?(/.*)?$'
        if re.match(regex, endpoint):
            # Se for válido, exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Endpoint válido!")
        else:
            # Se não for válido, exibe uma mensagem de erro
            messagebox.showerror("Erro", "Endpoint inválido! Certifique-se de que a URL está correta.")

    # Botão para validar o endpoint
    botao_validar_endpoint = Button(janela, text="Validar Endpoint", command=validar_endpoint)
    botao_validar_endpoint.pack(pady=5)

    # Botão Laboratório
    botaoLaboratorio = Button(janela, text="Laboratório", command=lambda: abrirJanelaLaboratorio(janela))
    botaoLaboratorio.pack(pady=5)

    # Botão Não Laboratório
    botaoNaoLaboratorio = Button(janela, text="Não Laboratório", command=lambda: abrirJanelaNaoLaboratorio(janela))
    botaoNaoLaboratorio.pack(pady=5)

    # Texto de rodapé
    texto_rodape = Label(janela, text="Criado por Selmo Werner Júnior", padx=20, pady=20)
    texto_rodape.place(relx=0.5, rely=1.0, anchor='s')

    janela.protocol("WM_DELETE_WINDOW", janela.quit)
    janela.mainloop()

def abrirJanelaLaboratorio(janelaAnterior):
    """
    Fecha a janela anterior e abre a janela Laboratório.
    """
    janelaAnterior.withdraw()  # Oculta a janela principal
    function.abrirJanelaLaboratorio(lambda: janelaAnterior.deiconify())  # Mostra a janela principal ao fechar

def abrirJanelaNaoLaboratorio(janelaAnterior):
    """
    Fecha a janela anterior e abre a janela Não Laboratório.
    """
    janelaAnterior.withdraw()  # Oculta a janela principal
    function.abrirJanelaNaoLaboratorio(lambda: janelaAnterior.deiconify())  # Mostra a janela principal ao fechar

if __name__ == "__main__":
    criarJanelaPrincipal()