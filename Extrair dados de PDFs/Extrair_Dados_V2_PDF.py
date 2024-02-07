import PyPDF2
import re
import openpyxl
import tkinter as tk
from tkinter import messagebox, filedialog

def extrair_valor_cbio(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        texto = ''
        for page_num in range(len(pdf_reader.pages)):
            texto += pdf_reader.pages[page_num].extract_text()

        padrao = r'Valor\s*CBIO\s*\(R\$\):\s*([\d,]+)'
        match = re.search(padrao, texto)
        if match:
            valor_cbio = match.group(1).replace(',', '.')
            return float(valor_cbio)
        else:
            return None

def escrever_no_excel(valor_cbio, excel_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Valor CBIO (R$)'
    sheet['B1'] = valor_cbio
    workbook.save(excel_path)

def exibir_mensagem_sucesso():
    messagebox.showinfo("Sucesso", "Dados copiados com sucesso.")

if __name__ == "__main__":
    root = tk.Tk()

    pdf_path = filedialog.askopenfilename(title="Selecione o arquivo PDF", filetypes=[("Arquivos PDF", "*.pdf")])
    excel_path = filedialog.asksaveasfilename(title="Salve o arquivo Excel", defaultextension=".xlsx",
                                              filetypes=[("Arquivos Excel", "*.xlsx")])

    valor_cbio = extrair_valor_cbio(pdf_path)

    if valor_cbio is not None:
        escrever_no_excel(valor_cbio, excel_path)
        print(f"Valor do CBIO (R$) encontrado e salvo no Excel: {valor_cbio}")

        exibir_mensagem_sucesso()
    else:
        print("Valor do CBIO (R$) não encontrado no PDF.")

    root.destroy()  # Feche a janela Tkinter após a execução do código
