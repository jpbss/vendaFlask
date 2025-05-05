from sqlite3 import converters

from controle.controleGenerico import ControleGenerico
from modelo.cliente import Cliente


class ControleCliente(ControleGenerico):

    def incluir_cliente(self, cliente):
        self.incluir(cliente)

    def alterar_cliente(self,cliente):
        self.alterar(cliente)

    def deletar_cliente(self, cliente):
        self.delete(cliente)

    def pesquisa_codigo(self, entrada:Cliente):
        cliente = self.procuraRegistro(entrada)
        retorno = Cliente()
        if len(cliente) >= 1:
            retorno = self.converte_cliente(cliente)
        return retorno

    # idcliente, nome, endereco, cidade, uf, cep, credito, saldo
    def converte_cliente(self, cliente):
        retorno = Cliente()
        retorno.idcliente = cliente[0][0]
        retorno.nome = cliente[0][1]
        retorno.endereco = cliente[0][2]
        return retorno

    def listar_todos_registros(self, objeto):
        lista = self.listarTodos(objeto)
        formatada = []
        for i in lista:
            formatada.append(self.converte_objeto(i))

        return formatada

    def converte_objeto(self,entrada):
        cliente = Cliente()
        cliente.idcliente=entrada[0]
        cliente.nome = entrada[1]
        cliente.endereco = entrada[2]

        return cliente

