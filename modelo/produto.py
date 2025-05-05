class Produto:
    def __init__(self):
        self.__idproduto=0
        self.__nome=''
        self.__qtde = 0
        self.__preco = 0

        self.__lista = 'nome, qtde, preco'

        self.__dadosInserir = ''
        self.__dadosUpdate = ''
        self.__dadosDelete = ''
        self.__dadosPesquisa = ''
        self.__tabelaBanco = 'produto'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}'".format(self.nome, self.qtde, self.preco)
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = "nome='{}', qtde='{}', preco='{}' where idproduto='{}'".format(self.nome, self.qtde, self.preco, self.idproduto)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idproduto={}".format(self.idproduto)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from produto where idproduto = {}".format(self.idproduto)
        return self.__dadosPesquisa

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
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, entrada):
        self.__nome = entrada

    @property
    def qtde(self):
        return self.__qtde

    @qtde.setter
    def qtde(self, entrada):
        self.__qtde = entrada

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, entrada):
        self.__preco = entrada

    def __repr__(self):
        return f"Produto: {self.nome:>30}  Quantidade: {self.qtde:>8}  Preço: R$ {self.preco:>8.2f}"
