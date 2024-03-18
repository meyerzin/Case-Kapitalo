import streamlit as st
import pandas as pd 
import numpy as np
import os
st.set_page_config(page_title="Kapitalo Investimentos", page_icon=":flag-kp:", layout="wide")
background_image_url = 'https://media.licdn.com/dms/image/D4D3DAQEknFfNUDcqyA/image-scale_191_1128/0/1706636797019/kapitaloinvestimentos_cover?e=1711033200&v=beta&t=6OVjJp3Kmy8qc9eziF8z1w37-nUm-ZBiRjM8fijKWes'

# Injetando CSS com st.markdown para adicionar a imagem de fundo ao elemento desejado
css = (f"""
    <style>
    .block-container.st-emotion-cache-z5fcl4.ea3mdgi5 {{
        background-image: url({background_image_url});
        background-size: cover;  # Cobrir o elemento inteiro
        background-position: center;  # Centralizar imagem de fundo
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    </style>
    """)

st.markdown(css, unsafe_allow_html=True )

col1,col2 = st.columns([0.2,0.8])
with col2:
    st.title('RESOLUÇÃO DO CASE - KAPITALO INVESTIMENTOS')
with col1:
    st.image('https://media.licdn.com/dms/image/C4D0BAQFyfB_I5MQ3-Q/company-logo_200_200/0/1668447886595/kapitaloinvestimentos_logo?e=1718236800&v=beta&t=dOOn7tNcd_QVtbMGPdKc2znRe9PN6MsdS4n5fEYggCo')

if st.checkbox('ver o codigo completo'):
    st.code('''
df_dados_novos = pd.DataFrame()
criar_planilha = st.button('puxar os dados e exportar para "Base.csv"')
if criar_planilha:
    df_dados_novos = pd.read_csv('Dados.csv')

    if os.path.exists('Base.csv'):
        dados_base = pd.read_csv('Base.csv')
        df_junto = pd.concat([dados_base,df_dados_novos], ignore_index=True)
        df_junto.to_csv('Base.csv')
        st.success('base importada e mesclada/exportada com sucesso!')
    else:
        df_dados_novos.to_csv('Base.csv',index=False)
        st.success('base importada e criada/exportada com sucesso!')
if st.checkbox('vizualizar o DATABASE completo'):
    try:
        st.dataframe(pd.read_csv('Base.csv'))
    except:
        st.warning('Falha ao tentar visualizar o DATABASE. Certifique-se que a mesma existe ou que esteja no diretório atual com nome "Base.csv"')

if st.button('apagar a base de dados'):
    try:
        os.remove('Base.csv')
        st.success('base de dados apagada com sucesso!')
    except:
        st.warning('Falha ao tentar apagar O DATABSE. Certifique-se que a mesma existe ou que esteja no diretório atual com nome "Base.csv"')

ler_e_fazer_relatorio = st.button('ler a base e gerar relatório')
if ler_e_fazer_relatorio:
    try:
        database_completa = pd.read_csv('Base.csv')
    except:
        st.warning('Falha ao tentar ler O DATABASE. Certifique-se que a mesma existe ou que esteja no diretório atual com nome "Base.csv"')
    database_completa['Total_price'] = database_completa['Qty'] * database_completa['Price']
    agg_df = database_completa.groupby(['Broker','Produto','Compra/Venda'])[['Total_price','Qty']].sum()
    agg_df['preco_medio_ponderado'] = agg_df['Total_price'] / agg_df['Qty']

    relatorio_final = agg_df[['preco_medio_ponderado','Total_price','Qty']]
    st.dataframe(relatorio_final)
    # st.dataframe(agg_df)

if st.checkbox('ver mais detalhes'):
    database_completa = pd.read_csv('Base.csv')
    database_completa['Total_price'] = database_completa['Qty'] * database_completa['Price']
    agg_df = database_completa.groupby(['Broker','Produto','Compra/Venda'])[['Total_price','Qty']].sum()
    agg_df['preco_medio_ponderado'] = agg_df['Total_price'] / agg_df['Qty']

    filtro1 = st.selectbox('selecione a informação para filtrar',list(agg_df.index.names) )
    valores_coluna = list(agg_df.index.get_level_values(filtro1).unique())
    filtro2 = st.selectbox('selecione o item específico a visualizar ',valores_coluna )
    st.dataframe(agg_df.loc[agg_df.index.get_level_values(filtro1) == filtro2])
''')
df_dados_novos = pd.DataFrame()
criar_planilha = st.button('puxar os dados e exportar para "Base.csv"')
if criar_planilha:
    df_dados_novos = pd.read_csv('Dados.csv')

    if os.path.exists('Base.csv'):
        dados_base = pd.read_csv('Base.csv')
        df_junto = pd.concat([dados_base,df_dados_novos], ignore_index=True)
        df_junto.to_csv('Base.csv')
        st.success('base importada e mesclada/exportada com sucesso!')
    else:
        df_dados_novos.to_csv('Base.csv',index=False)
        st.success('base importada e criada/exportada com sucesso!')
if st.checkbox('vizualizar o DATABASE completo'):
    try:
        st.dataframe(pd.read_csv('Base.csv'))
    except:
        st.warning('Falha ao tentar visualizar o DATABASE. Certifique-se que a mesma existe ou que esteja no diretório atual com nome "Base.csv"')

if st.button('apagar a base de dados'):
    try:
        os.remove('Base.csv')
        st.success('base de dados apagada com sucesso!')
    except:
        st.warning('Falha ao tentar apagar O DATABSE. Certifique-se que a mesma existe ou que esteja no diretório atual com nome "Base.csv"')

ler_e_fazer_relatorio = st.button('ler a base e gerar relatório')
if ler_e_fazer_relatorio:
    try:
        st.subheader('relatório de preços médio ponderado por ativos e lado da operação (compra ou venda) executados em cada “Broker”.',divider='rainbow')
        database_completa = pd.read_csv('Base.csv')
    except:
        st.warning('Falha ao tentar ler O DATABASE. Certifique-se que a mesma existe ou que esteja no diretório atual com nome "Base.csv"')
    database_completa['Total_price'] = database_completa['Qty'] * database_completa['Price']
    agg_df = database_completa.groupby(['Broker','Produto','Compra/Venda'])[['Total_price','Qty']].sum()
    agg_df['preco_medio_ponderado'] = agg_df['Total_price'] / agg_df['Qty']

    relatorio_final = agg_df[['preco_medio_ponderado','Total_price','Qty']]
    st.dataframe(relatorio_final)
    # st.dataframe(agg_df)

if st.checkbox('ver mais detalhes'):
    database_completa = pd.read_csv('Base.csv')
    database_completa['Total_price'] = database_completa['Qty'] * database_completa['Price']
    agg_df = database_completa.groupby(['Broker','Produto','Compra/Venda'])[['Total_price','Qty']].sum()
    agg_df['preco_medio_ponderado'] = agg_df['Total_price'] / agg_df['Qty']

    filtro1 = st.selectbox('selecione a informação para filtrar',list(agg_df.index.names) )
    valores_coluna = list(agg_df.index.get_level_values(filtro1).unique())
    filtro2 = st.selectbox('selecione o item específico a visualizar ',valores_coluna )
    st.dataframe(agg_df.loc[agg_df.index.get_level_values(filtro1) == filtro2])

    # st.dataframe(agg_df[filtro1])