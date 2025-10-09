import streamlit as st
from views import View
import pandas as pd


class ManterProfissionalUI:


    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()


    @staticmethod
    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            list_dic = [obj.to_json() for obj in profissionais]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)


    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o email")
        telefone = st.text_input("Informe o telefone")
        especialidade = st.text_input("Informe a especialidade")
        if st.button("Inserir"):
            View.profissional_inserir(nome, email, telefone, especialidade)
            st.success("Profissional inserido com sucesso")
            st.rerun()


    @staticmethod
    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atuaização de Profissionais", profissionais)
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo email", op.get_email())
            telefone = st.text_input("Novo telefone", op.get_telefone())
            especialidade = st.text_input("Nova especialidade", op.get_especialidade())
            if st.button("Atualizar"):
                id = op.get_id()
                View.profissional_atualizar(id, nome, email, telefone, especialidade)
                st.success("Profissional atualizado com sucesso")
                st.rerun()


    @staticmethod
    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissonal cadastrado")
        else:
            op = st.selectbox("exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                View.profissional_excluir(id)
                st.success("profissional excluído com sucesso")
                st.rerun()
