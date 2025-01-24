import function
from tkinter import *

janela = Tk()

function.centralizar_janela(janela)

janela.title("Sistema XML para integração Padrão Tasy")

# Label de orientação
texto_orientacao = Label(janela, text="Selecione a Aplicação:")
texto_orientacao.pack(side=TOP, fill=X, padx=0, pady=50)

# Label vazio (para algum propósito específico, se necessário)
texto_botao = Label(janela, text="")
texto_botao.pack()

# Botão Laboratório
botaoLaboratorio = Button(janela, text="Laboratório", command=lambda: function.abrirJanelaLaboratorio())
botaoLaboratorio.pack(pady=5)  # Separação entre os botões

# Botão Não Laboratório
botaoNaoLaboratorio = Button(janela, text="Não Laboratório", command=lambda: function.abrirJanelaNaoLaboratorio())
botaoNaoLaboratorio.pack(pady=5)  # Separação leve entre os botões

# Texto de rodapé com centralização
texto_rodape = Label(janela, text="Criado por Selmo Werner Júnior", padx=20, pady=20)
texto_rodape.place(relx=0.5, rely=1.0, anchor='s')

janela.mainloop()
