import streamlit as st
import pandas as pd
import time
from views import View

class ManterServicoUI:

    @staticmethod
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    @staticmethod
    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            dic = []
            for obj in servicos:
                dic.append({
                    "id": obj.get_id(),
                    "descricao": obj.get_descricao(),
                    "valor": obj.get_valor()
                })
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor (R$)")
        duracao = st.text_input("Informe a duração (minutos)")

        # Verifica se todos os campos estão preenchidos antes de tentar inserir
        if st.button("Inserir"):
            if not descricao or not valor or not duracao:
                st.error("Todos os campos devem ser preenchidos")
                return

            try:
                valor = float(valor)
                duracao = int(duracao)
                if valor <= 0:
                    st.error("O valor do serviço deve ser maior que zero.")
                    return
                if duracao <= 0:
                    st.error("A duração do serviço deve ser maior que zero.")
                    return
                View.servico_inserir(descricao, valor)
                st.success("Serviço inserido com sucesso!")
            except ValueError as erro:
                st.error(f"Erro: {erro}")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Escolha um serviço para atualizar", servicos)
            descricao = st.text_input("Nova descrição", op.get_descricao())
            valor = st.number_input("Novo valor", value=op.get_valor(), min_value=0.1)

            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.servico_atualizar(id, descricao, float(valor))
                    st.success("Serviço atualizado com sucesso")
                except ValueError as erro:
                    st.error(f"Erro: {erro}")

                time.sleep(2)
                st.experimental_rerun()

    @staticmethod
    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Escolha um serviço para excluir", servicos)

            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.servico_excluir(id)
                    st.success("Serviço excluído com sucesso")
                except ValueError as erro:
                    st.error(f"Erro: {erro}")

                time.sleep(2)
                st.rerun()
