import pandas as pd

class CsvProcessor:
    # Método construtor
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    # Aplicando recursividade
    def filtrar_por(self, colunas: list, atributos: list):

        if len(colunas) != len(atributos):
            raise ValueError('O número de colunas e atributos é diferente')
        
        if len(colunas) == 0: 
            return  self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(colunas[1:], atributos[1:])
        

 