import streamlit as st
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha", type="password")
    if st.button("Abrir Conta"):
      if not nome or not email or not fone or not senha:
        st.error("Todos os campos devem ser preenchidos")
      else:
        try:
          View.cliente_inserir(nome, email, fone, senha)
          st.success("Conta criada com sucesso!")
        except ValueError as erro:
          st.error(f"Erro: {erro}")
      time.sleep(2)
      st.rerun()