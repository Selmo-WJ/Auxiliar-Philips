from tkinter import *
from tkinter import messagebox
import pyperclip

def abrirJanelaTrigger():
    def centralizar_janela(janela):
        janela.update_idletasks()
        largura = janela.winfo_width()
        altura = janela.winfo_height()
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        janela.geometry(f'{largura}x{altura}+{x}+{y}')

    def copiar_para_area_de_transferencia(janela, widget_texto):
        texto = widget_texto.get("1.0", END).strip()
        if texto:
            pyperclip.copy(texto)
            messagebox.showinfo("Copiado", "Trigger copiada para a área de transferência!")
        else:
            messagebox.showwarning("Aviso", "Nada para copiar!")

    def gerar_trigger():
        nome_trigger = entry_nome_trigger.get().strip()
        nome_tabela = entry_nome_tabela.get().strip()
        usuario = entry_usuario.get().strip()
        atributos = entry_atributos.get().strip()

        if not nome_trigger or not nome_tabela or not atributos:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        lista_atributos = [attr.strip().upper() for attr in atributos.split(",")]

        # Gera dinamicamente os campos para INSERT e UPDATE
        insert_linhas = "\n".join(
            [f"            ' {attr}: ' || :NEW.{attr} || CHR(13) ||" for attr in lista_atributos]
        )
        update_linhas = "\n".join(
            [f"            ' {attr} (NEW): ' || :NEW.{attr} || CHR(13) ||\n            ' {attr} (OLD): ' || :OLD.{attr} || CHR(13) ||" for attr in lista_atributos]
        )

        trigger = f"""CREATE OR REPLACE TRIGGER {nome_trigger} INSERT OR UPDATE ON {nome_tabela} FOR EACH ROW
DECLARE
BEGIN
    IF(INSERTING) THEN
        GRAVAR_LOG_TASY(1310, 'INSERT' || CHR(13) ||
{insert_linhas} d
            ' STACK: ' || SUBSTR(DBMS_UTILITY.FORMAT_CALL_STACK,1,4000),
            '{usuario}');
    ELSE
        GRAVAR_LOG_TASY(1310, 'UPDATE' || CHR(13) ||
{update_linhas} 
            ' STACK: ' || SUBSTR(DBMS_UTILITY.FORMAT_CALL_STACK,1,4000),
            '{usuario}');
    END IF;
END;
/
"""
        texto_widget.delete("1.0", END)
        texto_widget.insert(END, trigger)

    janela = Tk()
    janela.title("Gerador de Trigger")
    janela.geometry("800x850")
    centralizar_janela(janela)

    frame_top = Frame(janela, bg="lightgray", height=50)
    frame_top.pack(side=TOP, fill=X)
    titulo_label = Label(frame_top, text="Gerador de Trigger", font=("Arial", 14, "bold"), bg="lightgray")
    titulo_label.pack(pady=10)

    frame_input = Frame(janela, pady=20)
    frame_input.pack()

    Label(frame_input, text="Nome da Trigger:", font=("Arial", 10)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_nome_trigger = Entry(frame_input, width=40)
    entry_nome_trigger.grid(row=0, column=1, padx=5, pady=5)

    Label(frame_input, text="Nome da Tabela:", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_nome_tabela = Entry(frame_input, width=40)
    entry_nome_tabela.grid(row=2, column=1, padx=5, pady=5)

    Label(frame_input, text="Usuário:", font=("Arial", 10)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_usuario = Entry(frame_input, width=40)
    entry_usuario.insert(0, "TASY")
    entry_usuario.grid(row=3, column=1, padx=5, pady=5)

    Label(frame_input, text="Atributos (separados por vírgula):", font=("Arial", 10)).grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_atributos = Entry(frame_input, width=40)
    entry_atributos.insert(0, "")
    entry_atributos.grid(row=4, column=1, padx=5, pady=5)

    botao_gerar = Button(janela, text="Gerar Trigger", font=("Arial", 10), command=gerar_trigger)
    botao_gerar.pack(pady=10)

    label_texto = Label(janela, text="Trigger Gerada:", font=("Arial", 10))
    label_texto.pack(anchor="w", padx=20)
    texto_widget = Text(janela, height=20, width=100, font=("Courier", 10), wrap=NONE)
    texto_widget.pack(padx=20, pady=10)

    botao_copiar = Button(janela, text="Copiar para área de transferência", font=("Arial", 10),
                        command=lambda: copiar_para_area_de_transferencia(janela, texto_widget))
    botao_copiar.pack(pady=5)

    frame_footer = Frame(janela, bg="lightgray", height=30)
    frame_footer.pack(side=BOTTOM, fill=X)
    rodape_label = Label(frame_footer, text="Criado por Selmo Werner Júnior", font=("Arial", 10), bg="lightgray")
    rodape_label.pack(pady=5)

    janela.mainloop()
