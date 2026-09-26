import streamlit as st

st.set_page_config(page_title="Atividade 6 - Roteamento de Chatbot", page_icon="🤖")

st.title("🤖 Atividade 6: Roteamento de Chatbot")
st.write("Analisa a mensagem do usuário e encaminha para o departamento correto.")

mensagem = st.text_input("Mensagem do usuário:", value="Gostaria de solicitar o cancelamento da minha assinatura")

if st.button("Encaminhar", type="primary"):
    msg = mensagem.lower()
    if "cancelar" in msg or "cancelamento" in msg:
        st.warning("Direcionando para: **Setor de Retenção e Cancelamentos**")
    elif "erro" in msg or "problema" in msg:
        st.error("Direcionando para: **Suporte Técnico**")
    elif "pagamento" in msg or "fatura" in msg:
        st.info("Direcionando para: **Setor Financeiro**")
    else:
        st.write("Direcionando para: **Atendimento Geral**")