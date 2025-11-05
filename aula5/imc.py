import streamlit as st

st.title("Calculador De IMC")

peso = st.number_input("Digite seu peso (kg):",step=1)
altura = st.number_input("Digite sua altura (m):",min_value=1)

imc = peso / altura**2

st.text(f"O seu IMC é: {imc:.2f}")

