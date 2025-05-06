import datetime
from modelo.cliente import Cliente
from modelo.itemVenda import ItemVenda


class Venda:
    def __init__(self):
        self.__idvenda = 0
        self.__data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__cliente = Cliente()
        self.__items = []
        self.__valortotal = 0

        self.__dadaosInserir = ''
        self.__dadosUpdate = ''
        self.__dadosDelete = ''
        self.__dadosPesquisa = ''

        self.__lista = 'data, idcliente, valortotal'
        self.__tabelaBanco = 'venda'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return "'{}', '{}', '{}'".format(self.data, self.cliente.idcliente, self.valortotal)

    @property
    def dadosUpdate(self):
        return "data='{}', idcliente='{}'".format(self.data, self.cliente.idcliente)

    @property
    def dadosDelete(self):
        return "where idvenda={}".format(self.idvenda)

    @property
    def dadosPesquisa(self):
        return "select * from venda where idvenda = {}".format(self.idvenda)

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idvenda(self):
        return self.__idvenda

    @idvenda.setter
    def idvenda(self, entrada):
        self.__idvenda = entrada

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, entrada):
        self.__data = entrada

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, entrada):
        if isinstance(entrada, Cliente):
            self.__cliente = entrada
        else:
            print("O cliente não é da classe cliente")

    @property
    def items(self):
        return self.__items

    @property
    def valortotal(self):
        return self.__valortotal

    @valortotal.setter
    def valortotal(self, entrada):
        self.__valortotal = entrada

    def calcular_total(self):
        self.__valortotal = 0
        for i in self.items:
            self.__valortotal += (i.valor * i.qtde)

    def adicionar_item(self, item):
        if isinstance(item, ItemVenda):
            if item in self.__items:
                for i in self.__items:
                    if i == item:
                        i.qtde = item.qtde + i.qtde
            else:
                self.__items.append(item)
        else:
            print("O item não é da classe item venda")

    def remover_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("O item não é da classe item venda")

    def pegar_item(self, item):
        if item in self.__items:
            for i in self.__items:
                if i == item:
                    return i
        return None

    def __repr__(self):
        items_str = "\n".join([f"      Produto: {item.idproduto:>7}  Qtde: {item.qtde:>7}  Valor: {item.valor:>10.2f}" for item in self.items])
        return f"Venda: {self.idvenda}\nData: {self.data}\nTotal: {self.valortotal:.2f}\nCliente: {self.cliente.nome}\nItens:\n{items_str}"
