import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*"))
    )
    
    if arquivo:
        exibir_tabela(arquivo)

def exibir_tabela(nome_arquivo):
    try:
        dados = pd.read_csv(nome_arquivo)
        
        janela_tabela = tk.Toplevel()
        janela_tabela.title("Conteúdo do Arquivo CSV")
        
        colunas = dados.columns.tolist()
        
        tabela = ttk.Treeview(janela_tabela, columns=colunas, show="headings")
        
        for coluna in colunas:
            tabela.heading(coluna, text=coluna)

        for _, linha in dados.iterrows():
            tabela.insert("", "end", values=linha.tolist())
        
        tabela.pack(padx=10, pady=10)
        
        barra_rolagem = ttk.Scrollbar(janela_tabela, orient="vertical", command=tabela.yview)
        barra_rolagem.pack(side="right", fill="y")
        tabela.configure(yscrollcommand=barra_rolagem.set)

    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível ler o arquivo CSV.\nErro: {e}")

def criar_interface():
    janela = tk.Tk()
    janela.title("Leitor de Arquivo CSV")
    janela.geometry("300x150")

    btn_importar = tk.Button(janela, text="Importar Arquivo CSV", command=selecionar_arquivo)
    btn_importar.pack(pady=20)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
