from tkinter import *
from tkinter import messagebox
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

def centralizar_janela(janela, largura=400, altura=400):
    """
    Centraliza a janela no centro da tela.
    """
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

def abrirJanelaNaoLaboratorio(callback_reabrir):
    """
    Abre a janela Não Laboratório.
    """
    janelaNaoLab = Toplevel()
    janelaNaoLab.title("Projeto Não Laboratório")
    centralizar_janela(janelaNaoLab)

    label_lab = Label(janelaNaoLab, text="Bem-vindo ao Não Laboratório", padx=20, pady=20)
    label_lab.pack(pady=10)

    texto = Text(janelaNaoLab, height=20, width=50)
    texto.pack(pady=1)
    selecionarMetodo(janelaNaoLab, texto)
    
    botao_copiar = Button(janelaNaoLab, text="Copiar", command=lambda: copiar_para_area_de_transferencia(janelaNaoLab, texto))
    botao_copiar.pack()

    botao_fechar = Button(janelaNaoLab, text="Fechar", command=lambda: [janelaNaoLab.destroy(), callback_reabrir()])
    botao_fechar.pack(side="bottom", pady=20)
    
    
def abrirJanelaLaboratorio(callback_reabrir):
    """
    Abre a janela Laboratório.
    """
    janelaNaoLab = Toplevel()
    janelaNaoLab.title("Projeto Laboratório")
    centralizar_janela(janelaNaoLab)

    label_lab = Label(janelaNaoLab, text="Bem-vindo ao Laboratório", padx=20, pady=20)
    label_lab.pack(pady=10)

    botao_fechar = Button(janelaNaoLab, text="Fechar", command=lambda: [janelaNaoLab.destroy(), callback_reabrir()])
    botao_fechar.pack(side="bottom", pady=20)

def selecionarMetodo(janelaNaoLab, texto_widget):
    registraExamesIntegrados = Button(
        janelaNaoLab,
        text="registraExamesIntegrados",
        command=lambda: abrirFormularioXML(janelaNaoLab, texto_widget)
    )
    registraExamesIntegrados.pack(pady=10)
    
def abrirFormularioXML(janelaNaoLab, texto_widget):
    """
    Abre um formulário para entrada de NR_PRESCRICAO e NR_SEQUENCIA.
    """
    janelaFormulario = Toplevel(janelaNaoLab)
    janelaFormulario.title("Preencher Dados para XML")
    centralizar_janela(janelaFormulario, largura=300, altura=300)

    Label(janelaFormulario, text="Preencha os dados para o XML", font=("Arial", 14)).pack(pady=10)

    # Lista para armazenar prescrições e sequências
    lista_prescricoes = []

    def adicionar_prescricao():
        """
        Adiciona os valores informados à lista de prescrições.
        """
        nr_prescricao = entrada_prescricao.get()
        nr_sequencia = entrada_sequencia.get()
        
        if not nr_prescricao or not nr_sequencia:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para NR_PRESCRICAO e NR_SEQUENCIA.")
            return

        lista_prescricoes.append((nr_prescricao, nr_sequencia))
        entrada_prescricao.delete(0, END)
        entrada_sequencia.delete(0, END)
        messagebox.showinfo("Sucesso", f"Prescrição {nr_prescricao} e Sequência {nr_sequencia} adicionada.")

    # Campo para NR_PRESCRICAO
    label_prescricao = Label(janelaFormulario, text="Digite o NR_PRESCRICAO:")
    label_prescricao.pack(pady=5)
    entrada_prescricao = Entry(janelaFormulario, width=30)
    entrada_prescricao.pack(pady=5)

    # Campo para NR_SEQUENCIA
    label_sequencia = Label(janelaFormulario, text="Digite o NR_SEQUENCIA:")
    label_sequencia.pack(pady=5)
    entrada_sequencia = Entry(janelaFormulario, width=30)
    entrada_sequencia.pack(pady=5)

    # Botão para adicionar prescrição à lista
    botao_adicionar = Button(
        janelaFormulario,
        text="Adicionar Prescrição",
        command=adicionar_prescricao
    )
    botao_adicionar.pack(pady=5)

    # Botão para gerar XML
    botao_gerar = Button(
        janelaFormulario,
        text="Gerar XML",
        command=lambda: [
            inserirXMLNoTexto(texto_widget, lista_prescricoes),
            janelaFormulario.destroy()
        ]
    )
    botao_gerar.pack(pady=20)

def inserirXMLNoTexto(texto_widget, lista_prescricoes):
    """
    Insere o XML gerado no widget de texto.
    """
    if not lista_prescricoes:
        messagebox.showerror("Erro", "Nenhuma prescrição foi adicionada.")
        return

    texto_xml = geraXML(lista_prescricoes)
    texto_widget.delete("1.0", END)
    texto_widget.insert("1.0", texto_xml)

def geraXML(lista_prescricoes):
    """
    Gera um XML com os valores dinâmicos fornecidos.
    """
    root = ET.Element("LABORATORIO")
    exames = ET.SubElement(root, "EXAMES")

    # Adiciona cada prescrição à lista de exames no XML
    for nr_prescricao, nr_sequencia in lista_prescricoes:
        exame = ET.SubElement(exames, "EXAME")
        nr_prescricao_elem = ET.SubElement(exame, "NR_PRESCRICAO")
        nr_prescricao_elem.text = nr_prescricao
        nr_sequencia_elem = ET.SubElement(exame, "NR_SEQUENCIA")
        nr_sequencia_elem.text = nr_sequencia

    xml_str = ET.tostring(root, encoding="unicode", method="xml")
    pretty_xml = parseString(xml_str).toprettyxml(indent="  ")
    return pretty_xml

def copiar_para_area_de_transferencia(janelaNaoLab, texto):
    """
    Copia o conteúdo do widget de texto para a área de transferência.
    """
    janelaNaoLab.clipboard_clear()
    texto_copiado = texto.get("1.0", END).strip()
    janelaNaoLab.clipboard_append(texto_copiado)
    janelaNaoLab.update()
    messagebox.showinfo("Sucesso!", "XML copiado com sucesso!")