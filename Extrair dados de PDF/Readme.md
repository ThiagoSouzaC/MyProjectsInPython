# Extração de Dados de PDF

Este projeto em Python tem como objetivo extrair informações específicas de um arquivo PDF, procurando por um marcador ("CLIENTE:") e salvando o nome do cliente em uma planilha.

## Funcionalidades

- **Extração de Dados PDF:**
  - Utiliza a biblioteca PyPDF2 para extrair texto de arquivos PDF.
  - Procura por um marcador específico ("CLIENTE:") no texto extraído.
  - Salva o nome do cliente em uma planilha utilizando a biblioteca pandas.

## Como Usar

1. **Instalação:**
   - Certifique-se de ter as bibliotecas necessárias instaladas:
     ```bash
     pip install PyPDF2 pandas
     ```

2. **Execução:**
   - Clone o repositório:
     ```bash
     git clone https://github.com/seu-usuario/meus-projetos-python.git
     cd meus-projetos-python/projeto_exemplo_pdf
     ```
   - Execute o script principal:
     ```bash
     python main.py
     ```

3. **Configuração:**
   - Adapte o caminho do seu arquivo PDF no arquivo `main.py`:
     ```python
     caminho_do_pdf = 'caminho/do/seu/arquivo.pdf'
     ```

4. **Resultado:**
   - O nome do cliente, neste caso, será extraído do PDF e salvo em uma planilha.

