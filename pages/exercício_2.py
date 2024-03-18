import streamlit as st
import pandas as pd 
import numpy as np
import os
st.set_page_config(page_title="Netflix Reviews", page_icon=":flag-kp:", layout="wide")
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


st.title('EXERCÍCIO FEITO NA PRÓPRIA PLANILHA EXCEL, "ex gerencial.xlsx"')