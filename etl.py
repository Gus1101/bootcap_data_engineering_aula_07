import pandas as pd
import os
import glob
from util_log import log_decorator

### Função para leitura e concatenação de arquivos Json

@log_decorator
def ler_arquivos_json(pasta:str) -> pd.DataFrame:
    """
    Função para leitura e concatenação de arquivos json
    """
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_vendas_concatenado = pd.concat(df_list, ignore_index=True)
    return df_vendas_concatenado

### Função para criar KPI

@log_decorator
def criar_kpi(df:pd.DataFrame) -> pd.DataFrame:
    """
    Função para crair o KPI de total de vendas
    """
    df = df
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

### Procedure para exportar arquivos em Parquet ou csv

@log_decorator
def exportar_arquivos_parquet_csv(df:pd.DataFrame, lista:list):
    """
    Procedure para carregar dados
    """
    for formato in lista:
        if formato == 'csv':
            df.to_csv('dados.csv',index=False) 
        if formato == 'parquet':
            df.to_parquet('dados.parquet',index=False)

### Procedure para consolidar o processo

@log_decorator
def pipeline_geracao_kpi(pasta_argumento:str, formato_saida:list ):
    """
    Procedure para pipeline de dados de vendas
    """
    df = ler_arquivos_json(pasta_argumento)
    df_kpi = criar_kpi(df)
    exportar_arquivos_parquet_csv(df_kpi,formato_saida)