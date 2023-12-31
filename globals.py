import pandas as pd
import os

if("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)

else: 
    data_structure = {"Valor": [],
                      "Efetuado": [],
                      "Fixo":[],
                      "Data":[],
                      "Categoria":[],
                      "Descrição":[],}
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv")
    df_receitas.to_csv("df_receitas.csv")

if("df_cat_receitas.csv" in os.listdir()) and ("df_despesa.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_receita.csv", index_col=0)
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0)
    cat_receita = df_cat_receita.values.toList()
    cat_despesa = df_cat_despesa.values.toList()

else:
    cat_receita = {"Categoria": ["Salário", "Investimentos", "Comissão"]}
    cat_despesa = {"Categoria": ["Alimentação", "CardCrédito", "Saúde", "Lazer", "Faculdade", "Educação"]}

    df_cat_receita = pd.DataFrame(cat_receita)
    df_cat_despesa = pd.DataFrame(cat_despesa)
    df_cat_receita.to_csv("df_cat_receita.csv")
    df_cat_despesa.to_csv("df_cat_despesa.csv")