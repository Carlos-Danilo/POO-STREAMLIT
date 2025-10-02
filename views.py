from models.cliente import Cliente, ClienteDAO
from models.Servico import Servico, ServicoDAO
from models.Horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO

class View:

    
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None



    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)
    
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico) 
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)     
    def servico_listar(): 
        return ServicoDAO.listar()
    def servico_atualizar(id, descricao, valor): 
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id): 
        servico = Servico(id, "", 0)
        ServicoDAO.excluir(servico)

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.inserir(c)
    def horario_listar():
        return HorarioDAO.listar()
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.atualizar(c)
    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)
    

    def profissional_inserir(nome, email, telefone, especialidade):
        p = Profissional(0, nome, email, telefone, especialidade)
        ProfissionalDAO.inserir(p)
    def profissional_listar():
        return ProfissionalDAO.listar()
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    def profissional_atualizar(id, nome, email, telefone, especialidade):
        p = Profissional(id, nome, email, telefone, especialidade)
        ProfissionalDAO.atualizar(p)
    def profissional_excluir(id):
        p = Profissional(id, "", "", "", "")
        ProfissionalDAO.excluir(p)

    