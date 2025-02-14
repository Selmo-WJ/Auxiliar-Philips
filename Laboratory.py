from tkinter import *
from tkinter import messagebox
import function, scriptsLaboratory

def abrirJanelaLaboratorio(callback_reabrir):
    """
    Abre a janela Não Laboratório com botões alinhados verticalmente no lado esquerdo.
    """
    janelaLab = Toplevel()
    janelaLab.title("Projeto Laboratório")
    function.centralizar_janela(janelaLab)
    janelaLab.geometry("800x600")  # Tamanho da janela para se ajustar ao design

    # Top Frame (Título)
    frame_top = Frame(janelaLab, bg="lightgray", height=50)
    frame_top.pack(side=TOP, fill=X)
    titulo_label = Label(frame_top, text="Bem-vindo ao Projeto Laboratório", font=("Arial", 14, "bold"), bg="lightgray")
    titulo_label.pack(pady=10)

    # Left Frame (Botões na área preta)
    frame_left = Frame(janelaLab, width=200)
    frame_left.pack(side=LEFT, fill=Y)

    label_opcoes = Label(frame_left, text="Escolha uma opção:", font=("Arial", 12), fg="Black")
    label_opcoes.pack(pady=10)

    botoes = [
        "obterListaExamesPendentes",
        "registraExamesIntegrados",
        "registraResultadoExame",
        "registraItemResultadoExame",
        "registraLaudoAnalitosExame",
        "registraLaudoAnalitosExameMicro",
        "registraDataColetaExame",
        "obterListaExamesSuspensos",
        "registraExamesSuspensos"
    ]

    acoes = {
        "obterListaExamesPendentes": lambda: scriptsLaboratory.obterListaExamesPendentes(janelaLab, texto_widget),
        "registraExamesIntegrados": lambda: scriptsLaboratory.registraExamesIntegrados(janelaLab, texto_widget),
        "registraResultadoExame": lambda: scriptsLaboratory.registraResultadoExame(janelaLab, texto_widget),
        "registraItemResultadoExame": lambda: scriptsLaboratory.registraItemResultadoExame(janelaLab, texto_widget),
        "registraLaudoAnalitosExame": lambda: scriptsLaboratory.registraLaudoAnalitosExame(janelaLab, texto_widget),
        "registraLaudoAnalitosExameMicro": lambda: scriptsLaboratory.registraLaudoAnalitosExameMicro(janelaLab, texto_widget),
        "registraDataColetaExame": lambda: scriptsLaboratory.registraDataColetaExame(janelaLab, texto_widget),
        "obterListaExamesSuspensos": lambda: scriptsLaboratory.obterListaExamesSuspensos(janelaLab, texto_widget),
        "registraExamesSuspensos": lambda: scriptsLaboratory.registraExamesSuspensos(janelaLab, texto_widget)
    }

    def criar_botao(nome_botao):
        return Button(
            frame_left,
            text=nome_botao,
            font=("Arial", 10),
            command=acoes[nome_botao]
        )

    for nome_botao in botoes:
        botao = criar_botao(nome_botao)
        botao.pack(pady=5)

    # Main Frame (Conteúdo principal)
    frame_main = Frame(janelaLab, bg="white", padx=20, pady=20)
    frame_main.pack(fill=BOTH, expand=True)

    # Área de texto
    label_texto = Label(frame_main, text="Exibição de Dados XML:", font=("Arial", 10), bg="white")
    label_texto.pack(anchor="w")
    texto_widget = Text(frame_main, height=15, width=60, font=("Courier", 10), wrap=NONE)
    texto_widget.pack(pady=10)

    # Botões de ações
    frame_botoes = Frame(frame_main, bg="white")
    frame_botoes.pack(pady=10)

    botao_copiar = Button(frame_botoes, text="Copiar", font=("Arial", 10),
                          command=lambda: function.copiar_para_area_de_transferencia(janelaLab, texto_widget))
    botao_copiar.grid(row=0, column=0, padx=10)

    botao_fechar = Button(frame_botoes, text="Fechar", font=("Arial", 10),
                          command=lambda: [janelaLab.destroy(), callback_reabrir()])
    botao_fechar.grid(row=0, column=1, padx=10)

    # Footer Frame (Rodapé)
    frame_footer = Frame(janelaLab, bg="lightgray", height=30)
    frame_footer.pack(side=BOTTOM, fill=X)
    rodape_label = Label(frame_footer, text="Criado por Selmo Werner Júnior", font=("Arial", 10), bg="lightgray")
    rodape_label.pack(pady=5)