class ItemVenda:
    def __init__(self):
        self.idproduto = 0
        self.idvenda = 0
        self.qtde = 0
        self.valor = 0

        self.__lista = 'idproduto, idvenda, qtde, valor'

        self.__dadosInserir = ''
        self.__dadosUpdate = ''
        self.__dadosDelete = ''
        self.__dadosPesquisa = ''
        self.__tabelaBanco = 'itemvenda'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return "'{}', '{}', '{}', '{}'".format(self.idproduto, self.idvenda, self.qtde, self.valor)

    @property
    def dadosUpdate(self):
        return "idproduto='{}', idvenda='{}', qtde='{}', valor='{}'".format(self.idproduto, self.idvenda, self.qtde, self.valor)

    @property
    def dadosDelete(self):
        return "where idvenda={}".format(self.idproduto, self.idvenda)

    @property
    def dadosPesquisa(self):
        return "select * from itemvenda where idvenda={}".format(self.idvenda)

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idproduto(self):
        return self.__idproduto

    @idproduto.setter
    def idproduto(self, entrada):
        self.__idproduto = entrada

    @property
    def idvenda(self):
        return self.__idvenda

    @idvenda.setter
    def idvenda(self, entrada):
        self.__idvenda = entrada

    @property
    def qtde(self):
        return self.__qtde

    @qtde.setter
    def qtde(self, entrada):
            self.__qtde = entrada

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, entrada):
        self.__valor = entrada

    def __eq__(self, other):
        if isinstance(other, ItemVenda):
            return self.idproduto == other.idproduto
        return False