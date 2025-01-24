import tkinter as tk
import xml.etree.ElementTree as ET

# Generico

def centralizar_janela(janela, largura=400, altura=400):
    """
    Centraliza a janela no centro da tela.
    Pode receber largura e altura como argumentos opcionais.
    """
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

#Laboratorial

def abrirJanelaLaboratorio():
    
    janelaLab = tk.Toplevel()
    janelaLab.title("Projeto Laboratório")
    
    centralizar_janela(janelaLab, largura=400, altura=400)

    label_lab = tk.Label(janelaLab, text="Bem-vindo ao Laboratório", padx=20, pady=20)
    label_lab.pack()

    botao_fechar = tk.Button(janelaLab, text="Fechar", command=janelaLab.destroy)
    botao_fechar.pack()
    
    
#Não Laboratorial

def abrirJanelaNaoLaboratorio():
    janelaNaoLab = tk.Toplevel()
    janelaNaoLab.title("Projeto Não Laboratório")
    
    centralizar_janela(janelaNaoLab, largura=400, altura=400)

    label_lab = tk.Label(janelaNaoLab, text="Bem-vindo ao Não Laboratório", padx=20, pady=20)
    label_lab.pack(pady=10)

    # Gerar o XML
    texto_xml = geraXML()
    texto_label = tk.Label(janelaNaoLab, text=texto_xml, padx=10, pady=10, wraplength=300)
    texto_label.pack(pady=10)

       # Botão para copiar o texto para a área de transferência
    botao_copiar = tk.Button(janelaNaoLab, text="Copiar XML", command=lambda: copiar_para_area_de_transferencia(abrirJanelaNaoLaboratorio, texto_xml))
    botao_copiar.pack(pady=10)

    botao_fechar = tk.Button(janelaNaoLab, text="Fechar", command=janelaNaoLab.destroy)
    botao_fechar.pack(side="bottom", pady=20)
    
def geraXML():
    # Criando os elementos principais do XML
    root = ET.Element("LABORATORIO")
    exames = ET.SubElement(root, "EXAMES")

    # Criando os exames
    exame1 = ET.SubElement(exames, "EXAME")
    nr_prescricao1 = ET.SubElement(exame1, "NR_PRESCRICAO")
    nr_prescricao1.text = "230973"
    nr_sequencia1 = ET.SubElement(exame1, "NR_SEQUENCIA")
    nr_sequencia1.text = "1"

    exame2 = ET.SubElement(exames, "EXAME")
    nr_prescricao2 = ET.SubElement(exame2, "NR_PRESCRICAO")
    nr_prescricao2.text = "230987"
    nr_sequencia2 = ET.SubElement(exame2, "NR_SEQUENCIA")
    nr_sequencia2.text = "1"

    # Criando a árvore e salvando o XML em um arquivo
    tree = ET.ElementTree(root)
    xml_str = ET.tostring(root, encoding="unicode", method="xml")
    
    return xml_str
    
def copiar_para_area_de_transferencia(janelaNaoLab, texto):
    """
    Copia o texto para a área de transferência usando tkinter.
    """
    janelaNaoLab.clipboard_clear()  # Limpa o conteúdo da área de transferência
    janelaNaoLab.clipboard_append(texto.get("1.0", tk.END))  # Adiciona o novo texto
    janelaNaoLab.update()  # Atualiza a área de transferência
    print("Texto copiado para a área de transferência!")