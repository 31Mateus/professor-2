import streamlit as st

st.title("Conversor De Dólares!")

dolar = st.number_input("Digite um valor em dolar:")

reais = dolar * 5

st.text(f"O valor de {dolar:.2f} dolares é igual a {reais:.2f} Reais.")
