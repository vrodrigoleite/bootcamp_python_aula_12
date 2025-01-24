from csv_class import CsvProcessor

arquivo_csv = './vendas.csv'
colunas = ['estado','preço']
atributos = ['SP',450]

obj_csv = CsvProcessor(arquivo_csv)
obj_csv.carregar_csv()
print(obj_csv.filtrar_por(colunas=colunas, atributos=atributos))