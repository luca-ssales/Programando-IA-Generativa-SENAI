import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

st.set_page_config(page_title="Atividade 2 - Frequência de Palavras", page_icon="📊")

@st.cache_resource
def carregar_nltk():
    nltk.download('punkt_tab')

carregar_nltk()

st.title("📊 Atividade 2: Frequência de Palavras")
st.write("Calcula quantas vezes cada palavra aparece no texto.")

texto = st.text_area("Texto para análise:", value="o produto é bom o produto é excelente o serviço é bom")

if st.button("Calcular Frequência", type="primary"):
    if texto.strip():
        tokens = word_tokenize(texto.lower())
        frequencia = nltk.FreqDist(tokens)
        
        dados = [{"Palavra": palavra, "Quantidade": qtd} for palavra, qtd in frequencia.items()]
        st.dataframe(dados, use_container_width=True)
    else:
        st.warning("Por favor, digite um texto antes de analisar.")