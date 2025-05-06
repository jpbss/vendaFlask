import decimal


class Cliente:
    def __init__(self):
        self.__idcliente = 0
        self.__nome = ''
        self.__endereco = ''

        self.__lista = 'nome, endereco'

        self.__dadaosInserir=''
        self.__dadosUpdate=''
        self.__dadosDelete=''
        self.__dadosPesquisa=''
        self.__tabelaBanco='cliente'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.nome}','{self.endereco}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("nome='{}', endereco='{}'where idcliente={}").format(self.nome,
                                                                                         self.endereco,
                                                                                         self.idcliente)
        return self.__dadosUpdate

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = 'select * from cliente where idcliente={}'.format(self.__idcliente)
        return self.__dadosPesquisa

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idcliente={}".format(self.idcliente)
        return self.__dadosDelete

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idcliente(self):
        return self.__idcliente

    @idcliente.setter
    def idcliente(self, entrada):
        self.__idcliente = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, entrada):
        self.__nome = entrada

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, entrada):
        self.__endereco = entrada

    def __repr__(self):
        return (
            f"Nome: {self.__nome}\n"
            f"Endereço: {self.__endereco}\n"
        )