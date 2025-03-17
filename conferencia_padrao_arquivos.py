import pandas as pd

def compare_excel_structure(model_file, new_file):
    df_model = pd.read_excel(model_file)
    df_new = pd.read_excel(new_file)

    if set(df_model.columns) == set(df_new.columns):
        print('A estrutura dos arquivos é a mesma')
    else:
        missing_columns = set(df_model.columns) - set(df_new.columns)
        additional_columns = set(df_new.columns) - set(df_model.columns)

        if missing_columns:
            print(f'As colunas {missing_columns} estão faltando no novo arquivo.')
        if additional_columns:
            print(f'As colunas {additional_columns} foram adicionadasao novo arquivo.')
        
# Usando a função
compare_excel_structure('model_file.xlsx', 'new_file.xlsx')