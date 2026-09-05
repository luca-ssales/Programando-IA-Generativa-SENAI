import streamlit as st

st.text("ATV 2 - Desenvolver um formulário de cadastro utilizando Streamlit")

st.divider()

st.title("Formulário de Cadastro")
nome = st.text_input("Digite seu nome")
idade = st.number_input("Digite sua idade", value=0)
termos = st.checkbox("Aceito os termos de uso")
if st.button("Enviar"):
    st.write(f"Nome: {nome}")
    st.write(f"Idade: {idade}")
    st.write(f"Termos aceitos: {termos}")