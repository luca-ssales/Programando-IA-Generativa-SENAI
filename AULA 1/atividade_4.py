import streamlit as st

st.text("ATV 4 - Crie um mini painel que exiba dados tabulares (você pode criar um dicionário ou DataFrame simples do Pandas no próprio código)")

st.divider()

st.title("Mini Painel de Dados")
st.dataframe({
    'Nome': ['Lucas', 'Thomas', 'Marcos', 'Ana'],
    'Idade': [19, 17, 22, 20]
})

st.table({
    'Nome': ['Lucas', 'Thomas', 'Marcos', 'Ana'],
    'Idade': [19, 17, 22, 20]
})
