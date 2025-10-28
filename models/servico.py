import json


class Servico:
    def __init__(self, id, descricao, valor):
        if not descricao:
            raise ValueError("Descrição não pode ser vazia.")
        
        if valor <= 0:
            raise ValueError("Valor do serviço deve ser maior que zero.")
        
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
    
    def get_id(self):
        return self.__id
    
    def get_descricao(self):
        return self.__descricao
    
    def get_valor(self):
        return self.__valor
    
    def get_duracao(self):
        return self.__duracao

    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao):
        if descricao == "": 
            raise ValueError("Descrição inválida")
        self.__descricao = descricao

    def set_valor(self, valor):
        if valor <= 0: 
            raise ValueError("Valor inválido")
        self.__valor = valor

    def to_json(self):
        dic = {
            "id": self.__id,
            "descricao": self.__descricao,
            "valor": self.__valor
        }
        return dic

    @staticmethod
    def from_json(dic):
        try:
            id = int(dic["id"])  
            descricao = str(dic["descricao"]) 
            valor = float(dic["valor"]) 
            return Servico(id, descricao, valor)
        except (KeyError, ValueError) as e:
            raise ValueError(f"Erro ao criar objeto Servico: {e}")



class ServicoDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: 
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Servico.to_json)