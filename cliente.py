
# ------------------------------- CLASSE DA ENTIDADE CLIENTE --------------------------------------
# -------------------------------------- CUSTOMER CLASS -------------------------------------------


class Cliente:

    def __init__(self, nome, cpf, endereco, telefone):
        self.__id_cliente = None
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone
