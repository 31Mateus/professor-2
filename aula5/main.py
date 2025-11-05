import streamlit as st

st.title("Olá Mundo!")

numero = st.number_input("Digite um número:")

st.text(f"Você digitou o número: {numero}")
