import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

st.set_page_config(page_title="Atividade 10 - Análise de Avaliação", page_icon="⭐")

@st.cache_resource
def carregar_nltk():
    nltk.download('punkt_tab')

carregar_nltk()

st.title("⭐ Atividade 10: Análise Completa de Avaliações")
st.write("Combina tokenização com condicionais para verificar o sentimento final da avaliação.")

avaliacao = st.text_area("Avaliação de produto:", value="Excelente produto! Chegou antes do prazo e funciona muito bem.")

if st.button("Analisar Avaliação", type="primary"):
    tokens = word_tokenize(avaliacao.lower())
    
    palavras_pos = {"excelente", "bom", "ótimo", "otimo", "maravilhoso", "bem", "recomendo"}
    palavras_neg = {"ruim", "péssimo", "pessimo", "defeito", "lixo", "horrível"}
    
    s_pos = sum(1 for t in tokens if t in palavras_pos)
    s_neg = sum(1 for t in tokens if t in palavras_neg)
    
    col1, col2 = st.columns(2)
    col1.metric("Termos Positivos", s_pos)
    col2.metric("Termos Negativos", s_neg)
    
    st.subheader("Veredito:")
    if s_pos > s_neg:
        st.success("Cliente Satisfeito (Sentimento Positivo) 😊")
    elif s_neg > s_pos:
        st.error("Cliente Insatisfeito (Sentimento Negativo) 😞")
    else:
        st.info("Sentimento Neutro 😐")