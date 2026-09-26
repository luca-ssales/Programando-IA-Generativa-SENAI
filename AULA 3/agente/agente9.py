import streamlit as st
import nltk
import string
from nltk.tokenize import word_tokenize

st.set_page_config(page_title="Atividade 9 - Limpeza e Normalização", page_icon="🧼")

@st.cache_resource
def carregar_nltk():
    nltk.download('punkt_tab')

carregar_nltk()

st.title("🧼 Atividade 9: Limpeza e Normalização de Texto")
st.write("Normaliza o texto (minúsculas) e remove caracteres de pontuação.")

texto_bruto = st.text_area("Texto bruto:", value="Atenção! O pedido #12345 foi entregue? Sim, com sucesso...")

if st.button("Limpar Texto", type="primary"):
    tokens = word_tokenize(texto_bruto.lower())
    limpos = [w for w in tokens if w not in string.punctuation]
    texto_resultado = " ".join(limpos)
    
    st.subheader("Resultado do Texto Limpo:")
    st.code(texto_resultado)