import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

st.set_page_config(page_title="Atividade 7 - Top Palavras em Reclamações", page_icon="📈")

@st.cache_resource
def carregar_nltk():
    nltk.download('punkt_tab')
    nltk.download('stopwords')

carregar_nltk()

st.title("📈 Atividade 7: Palavras Frequentes em Reclamações")
st.write("Identifica os termos principais em um texto de reclamação.")

reclamacao = st.text_area("Reclamação completa:", value="O aplicativo dá erro toda hora. O erro impede de pagar a fatura e o aplicativo fecha sozinho.")

if st.button("Analisar Reclamação", type="primary"):
    tokens = word_tokenize(reclamacao.lower())
    stopwords_pt = set(stopwords.words('portuguese'))
    palavras_limpas = [w for w in tokens if w.isalpha() and w not in stopwords_pt]
    freq = nltk.FreqDist(palavras_limpas)
    
    st.subheader("Top 3 palavras mais frequentes:")
    for palavra, q in freq.most_common(3):
        st.write(f"- **{palavra}**: {q} vezes")