def pub_732(relatorio, campanha_732:str): 
    import numpy as np
    import pandas as pd
    
    '''
     Use o relatorio como argumento da função, parsseadno o caminho
     Ex: x = pub_732(relatorio-000, 'campanha de credito')

     o retorno será apenas os MCIs  

     para a campanha, use uma string com uma das campanhas do relatório, caso não saiba,
     rode com qualquer string, e irá retornar no terminal a lista de campanhas.

     irá retornar uma lista com os MCIs de clientes com ANC vigente, não rotacionados e
     que constem na campanha escolhida

     '''
   
    
    df = pd.read_excel(relatorio)   
    de = df.copy()
    de.rename(columns = {'Unnamed: 56':'Rotacionado'}, inplace=True)
    colunas_ler = ['MCI','Situação do Limite', 'Campanha','Rotacionado'] 
    # limpeza de dados 
    de = de[colunas_ler]
    de['MCI'].fillna('0', inplace=True)
    de['MCI'] = de['MCI'].astype(int)
    de.dropna()
    
    # Separando lista unica de campanhas
    camp = de['Campanha'].unique()
    camp = np.sort(camp[~pd.isnull(camp)]) # Ordenando o array unique pelo numpy sem NAN
    
    for i,item in enumerate(camp):
        print(i, item)
        # print(f'{i} - {item}')
    

    
    
    filtro_campanha = de['Campanha'] == campanha_732
    filtro_rotacionado = de['Rotacionado'] == False
    #filtro_limite = de['Situação do Limite'] == 'Vigente'
    #filtro_limite = de['Situação do Limite'] == 'cancelado'
    
    credito = de.loc[filtro_campanha & filtro_rotacionado, colunas_ler]
    
    #credito.count()
    x = credito['MCI'].unique()
    
    
    publico= []
    for i in x:
        try:
            
            publico.append(i)   
        except:
            publico.append(i)

    
    return publico

def pub_aco_caracteristicas_especiais(relatorio = 'relatorio-2795.xlsx'):
    ''''Por padrão está o relatório 2795, e a função vai retornar uma lisca de mcis, 
    únicos que conste com característica especial de parente de funcionário, funci, ativa e aposntado
    '''
    import pandas as pd


    df = pd.read_excel(relatorio)   
    de = df.copy()
    de.rename(columns= {'Unnamed: 28':'Endividamento_Finan'}, inplace=True)
    colunas_ler = ['MCI', 'Característica Especial','Endividamento_Finan'] # Inclui a ultima coluna
    
    de = de[colunas_ler]
    de
    #de['Campanha'].unique()

    
    de['MCI'].fillna('0', inplace=True)
    de['MCI'] = de['MCI'].astype(int)
    
    filtro_funci = de['Característica Especial'] == 'Funci BB Ativa'
    filtro_aposentado = de['Característica Especial'] == 'Funci BB Aposentado'
    filtro_parente = de['Característica Especial'] == 'Parente Funci BB'
    filtro_nenhuma = de['Característica Especial'] == 'Nenhuma'

    
    credito = de.loc[filtro_funci | filtro_aposentado | filtro_parente, colunas_ler]
    
    #credito.count()
    x = credito['MCI'].unique()
    
    publico= []
    for i in x:
        try:
            
            publico.append(i)   
        except:
            publico.append(i)

    
    return publico

def tratarcontatos(df):
    '''Utilize a função com o excel que contém a agenda com os campos
    MCI nome Telefone, nessa ordem, para que seja feita a verificação se os telefones 
    tem 5596 na frente'''
    
    prefix = '5596'
    tell = []
    df['Telefone'] = df['Telefone'].astype(str)
    for i in df.index:
        if len(df.loc[i,'Telefone'])<10:
            tel=df.loc[i,'Telefone']
            tel1 = prefix+tel
            df.loc[i,'Telefone'] = tel1
            tell.append(tel1)
        else: 
            tel2=df.loc[i,'Telefone'] 
            tell.append(tel2)
    df['MCI'].fillna('0', inplace =True)
    return df

def pub_1018(mes_indicado, r1018 = 'rels/relatorio-1018.xlsx' ):
    '''
   Utilize como argumento o relatorio 1018, e o mês solicitado, com o formato: 2023-10
   em string

   será retornada uma lista de MCI com todos os teds com liberação de crédito de outros bancos
   ex: x = pub
   '''
   

    import pandas as pd

    df = pd.read_excel(r1018)   
    de = df.copy()
    #de.rename(columns= {'Unnamed: 55':'Rotacionado'}, inplace=True)
    colunas_ler = ['MCI','Valor', 'Finalidade','Mês de Referência' ] # Inclui a ultima coluna

    de = de[colunas_ler]


    
    de['MCI'].fillna('0', inplace=True)
    de['MCI'] = de['MCI'].astype(int)
    
    filtro_finalidade = de['Finalidade'] == 'Liberação de Operacoes de Crédito'
    filtro_mes = de['Mês de Referência'] == mes_indicado
    
    credito = de.loc[filtro_finalidade & filtro_mes, colunas_ler]
    
    de.info()

    credito.count()

    #credito.count()
    x = credito['MCI'].unique()
    x
    publico_1018= []
    for i in x:
        try:
            
            publico_1018.append(i)   
        except:
            publico_1018.append(i)

    
    return publico_1018

def sd_conta_25k(df = 'rels/relatorio-2104.xlsx'):
    import pandas as pd
    df = 'rels/relatorio-2104.xlsx'
    df = pd.read_excel(df)
    df.drop([0,1,2], inplace = True)
    df['Unnamed: 36'] = df['Unnamed: 36'].astype(float)
    df['MCI'] = df['MCI'].astype(int).astype(str)
    df
    df.rename(columns = {'Unnamed: 36':'sd_conta'}, inplace=True)

    colunas = ['MCI', 'sd_conta']

    df = df[colunas]
    df = df[df['sd_conta']>25000.00]
    pub = list(df['MCI'])
    
    return list(set(pub))



