import streamlit as st

st.set_page_config(page_title="Atividade 8 - Suporte vs Financeiro", page_icon="🏷️")

st.title("🏷️ Atividade 8: Classificação entre Suporte e Financeiro")
st.write("Categoriza solicitações com base nas palavras-chave detectadas.")

solicitacao = st.text_input("Solicitação do cliente:", value="Preciso do boleto atualizado para realizar o pagamento")

if st.button("Categorizar", type="primary"):
    termos_fin = ["pagamento", "boleto", "fatura", "cobrança", "reembolso"]
    termos_sup = ["erro", "bug", "senha", "login", "lentidão", "acesso"]
    
    msg = solicitacao.lower()
    eh_financeiro = any(t in msg for t in termos_fin)
    eh_suporte = any(t in msg for t in termos_sup)
    
    if eh_financeiro:
        st.info("Categoria Identificada: **Financeiro**")
    elif eh_suporte:
        st.error("Categoria Identificada: **Suporte Técnico**")
    else:
        st.write("Categoria Identificada: **Não Identificado / Outros**")