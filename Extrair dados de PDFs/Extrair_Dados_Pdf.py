import PyPDF2
import pandas as pd

def extrair_nome_do_pdf(caminho_do_pdf):
    with open(caminho_do_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        texto_pdf = ""
        for pagina in range(len(pdf_reader.pages)):
            texto_pdf += pdf_reader.pages[pagina].extract_text()
    #print(texto_pdf)
    return texto_pdf

def encontrar_nome_no_texto(texto):
    indice_cliente = texto.find("CLIENTE:")
    if indice_cliente != -1:
        inicio_nome = indice_cliente + len("CLIENTE:")
        fim_nome = texto.find("\n", inicio_nome)
        nome_cliente = texto[inicio_nome:fim_nome].strip()
        print(nome_cliente)
        return nome_cliente
    else:
        return None
    
def adicionar_nome_a_planilha(nome_cliente):
    try:
        df = pd.read_excel('exemploPlanilha.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Nome do Cliente'])

    df = pd.concat([df, pd.DataFrame({'Nome do Cliente': [nome_cliente]})], ignore_index=True)

    df.to_excel('exemploPlanilha.xlsx', index=False)

def main():
    caminho_do_pdf = r'C:\Users\Thiago\OneDrive - cefet-rj.br\Documentos\Python Scripts\exemploPdf.pdf'
    texto_pdf = extrair_nome_do_pdf(caminho_do_pdf)
    nome_cliente = encontrar_nome_no_texto(texto_pdf)

    if nome_cliente:
        adicionar_nome_a_planilha(nome_cliente)
        dados = {'Nome do Cliente': [nome_cliente]}
        df = pd.DataFrame(dados)
        
        df.to_excel('exemploPlanilha.xlsx', index=False)
        print(f"Nome do cliente '{nome_cliente}' salvo na planilha.")
    else:
        print("Nome do cliente não encontrado no PDF.")

if __name__ == "__main__":
    main()
