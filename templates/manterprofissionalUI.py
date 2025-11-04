import streamlit as st
import pandas as pd
from views import View
import time

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            lista = [obj.to_json() for obj in profissionais]
            df = pd.DataFrame(lista)
            st.dataframe(df, hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            try:
                View.profissional_inserir(nome, especialidade, conselho, email, senha)
                st.success("Profissional inserido com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")

    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Selecione o profissional para atualizar", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")

            if st.button("Atualizar"):
                try:
                    View.profissional_atualizar(op.get_id(), nome, especialidade, conselho, email, senha)
                    st.success("Profissional atualizado com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(f"Erro: {e}")

    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Selecione o profissional para excluir", profissionais)
            if st.button("Excluir"):
                try:
                    View.profissional_excluir(op.get_id())
                    st.success("Profissional excluído com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(f"Erro: {e}")
