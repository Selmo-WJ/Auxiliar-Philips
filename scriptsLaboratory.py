from tkinter import *
from tkinter import messagebox
import function
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

def obterListaExamesPendentes(janelaLab, texto_widget):
    janelaFormulario = Toplevel(janelaLab)
    janelaFormulario.title("Preencher Dados para XML")
    function.centralizar_janela(janelaFormulario, largura=400, altura=400)
    
    Label(janelaFormulario, text="Preencha os dados para o XML", font=("Arial", 14)).pack(pady=10)
    
    def adicionarDados():
        nmUsuario = entrada_nmUsuario.get()
        dsSenha = entrada_dsSenha.get()
        nmUsuarioBanco = entrada_nmUsuarioBanco.get()
        
        if not nmUsuario or not dsSenha or not nmUsuarioBanco:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para nmUsuario, dsSenha e nmUsuarioBanco.")
            return
        
        texto_xml = obterListaExamesPendentesXML(nmUsuario, dsSenha, nmUsuarioBanco)
        texto_widget.delete("1.0", END)
        texto_widget.insert("1.0", texto_xml)
        messagebox.showinfo("Sucesso", f"Usuário: {nmUsuario}, senha: {dsSenha} e usuário do banco: {nmUsuarioBanco} adicionados.")
        janelaFormulario.destroy()
        
    Label(janelaFormulario, text="Digite o nmUsuario:").pack(pady=5)
    entrada_nmUsuario = Entry(janelaFormulario, width=30)
    entrada_nmUsuario.pack(pady=5)

    Label(janelaFormulario, text="Digite o dsSenha:").pack(pady=5)
    entrada_dsSenha = Entry(janelaFormulario, width=30, show="*")
    entrada_dsSenha.pack(pady=5)

    Label(janelaFormulario, text="Digite o nmUsuarioBanco:").pack(pady=5)
    entrada_nmUsuarioBanco = Entry(janelaFormulario, width=30)
    entrada_nmUsuarioBanco.pack(pady=5)

    Button(janelaFormulario, text="Adicionar Dados", command=adicionarDados).pack(pady=20)
    
def obterListaExamesPendentesXML(nmUsuario, dsSenha, nmUsuarioBanco):
    root = ET.Element("LABORATORIO")
    usuario = ET.SubElement(root, "USUARIO")
    ET.SubElement(usuario, "nmUsuario").text = nmUsuario
    ET.SubElement(usuario, "dsSenha").text = dsSenha
    ET.SubElement(usuario, "nmUsuarioBanco").text = nmUsuarioBanco

    xml_str = ET.tostring(root, encoding="unicode", method="xml")
    return parseString(xml_str).toprettyxml(indent="  ")

def obterListaExamesPendentesTexto(texto_widget, lista_prescricoes):
    if not lista_prescricoes:
        messagebox.showerror("Erro", "Nenhuma prescrição foi adicionada.")
        return

    texto_xml = obterListaExamesPendentesXML(lista_prescricoes)  
    texto_widget.delete("1.0", END)  
    texto_widget.insert("1.0", texto_xml)





def registraExamesIntegrados(janelaLab, texto_widget):
    """
    Abre um formulário para entrada de NR_PRESCRICAO e NR_SEQUENCIA.
    """
    janelaFormulario = Toplevel(janelaLab)
    janelaFormulario.title("Preencher Dados para XML")
    function.centralizar_janela(janelaFormulario, largura=400, altura=400)

    Label(janelaFormulario, text="Preencha os dados para o XML", font=("Arial", 14)).pack(pady=10)

    lista_prescricoes = []

    def adicionar_prescricao():
        nr_prescricao = entrada_prescricao.get()
        nr_sequencia = entrada_sequencia.get()

        if not nr_prescricao or not nr_sequencia:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para NR_PRESCRICAO e NR_SEQUENCIA.")
            return

        lista_prescricoes.append((nr_prescricao, nr_sequencia))
        entrada_prescricao.delete(0, END)
        entrada_sequencia.delete(0, END)
        messagebox.showinfo("Sucesso", f"Prescrição {nr_prescricao} e Sequência {nr_sequencia} adicionada.")

    Label(janelaFormulario, text="Digite o NR_PRESCRICAO:").pack(pady=5)
    entrada_prescricao = Entry(janelaFormulario, width=30)
    entrada_prescricao.pack(pady=5)

    Label(janelaFormulario, text="Digite o NR_SEQUENCIA:").pack(pady=5)
    entrada_sequencia = Entry(janelaFormulario, width=30)
    entrada_sequencia.pack(pady=5)

    Button(janelaFormulario, text="Adicionar Prescrição", command=adicionar_prescricao).pack(pady=5)

    Button(janelaFormulario, text="Gerar XML", command=lambda: [
        registraExamesIntegradosTexto(texto_widget, lista_prescricoes),
        janelaFormulario.destroy()
    ]).pack(pady=20)
    
def registraExamesIntegradosTexto(texto_widget, lista_prescricoes):
    if not lista_prescricoes:
        messagebox.showerror("Erro", "Nenhuma prescrição foi adicionada.")
        return

    texto_xml = registraExamesIntegradosXML(lista_prescricoes)  
    texto_widget.delete("1.0", END)  
    texto_widget.insert("1.0", texto_xml)


def registraExamesIntegradosXML(lista_prescricoes):
    root = ET.Element("LABORATORIO")
    exames = ET.SubElement(root, "EXAMES")

    for nr_prescricao, nr_sequencia in lista_prescricoes:
        exame = ET.SubElement(exames, "EXAME")
        ET.SubElement(exame, "NR_PRESCRICAO").text = nr_prescricao
        ET.SubElement(exame, "NR_SEQUENCIA").text = nr_sequencia

    xml_str = ET.tostring(root, encoding="unicode", method="xml")
    return parseString(xml_str).toprettyxml(indent="  ")