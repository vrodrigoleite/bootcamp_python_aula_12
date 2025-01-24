import pandas as pd

class CsvProcessor:
    # Método construtor
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_por(self, coluna: str, atributo: str):
        return self.df[self.df[coluna]==atributo]
    
arquivo_csv = './vendas.csv'
coluna = 'estado'
atributo = 'PE'

obj_csv = CsvProcessor(arquivo_csv)
obj_csv.carregar_csv()
print(obj_csv.filtrar_por(coluna=coluna, atributo=atributo))