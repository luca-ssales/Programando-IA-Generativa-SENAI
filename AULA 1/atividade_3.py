import streamlit as st

st.text("ATV 3 - Desenvolver um painel onde o usuário possa filtrar ou escolher preferências de aprendizado.")

st.divider()

st.title("Painel de Preferências")
st.selectbox("Selecione uma opção", ["Python", "Web"])
st.multiselect("Selecione múltiplas opções", ["HTML", "CSS", "SQL", "GIT"])
st.button("Enviar")