import streamlit as st
import pandas as pd


st.header('Calculadora em Streamlit 🐋')
st.write('ADICIONE OS NUMEROS PARA CALCULAR')

n1 = st.number_input('Digite um numero')
n2 = st.number_input('Digite outro numero', value =0.0)

soma_, div_, sub_, multi_ = st.columns(4)

if soma_.button('➕'):
    soma = n1 + n2
    st.info(soma)

elif sub_.button('➖'):
    sub = n1 - n2
    st.info(sub)

elif multi_.button('✖️'):
    multi = n1 * n2
    st.info(multi)

elif div_.button('➗'):
    div = n1 / n2
    st.info(div)
    