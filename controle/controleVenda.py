from controle.controleCliente import ControleCliente
from controle.controleGenerico import ControleGenerico
from controle.controleProduto import ControleProduto
from modelo.cliente import Cliente
from modelo.itemVenda import ItemVenda
from modelo.produto import Produto
from modelo.venda import Venda


class ControleVenda(ControleGenerico):

    def incluir_venda(self, venda):
        clienteDao = ControleCliente()
        produtoDAO = ControleProduto()
        self.incluir(venda)
        clienteDao.alterar_cliente(venda.cliente)
        self.ob.abrirConexao()
        id_venda = self.ob.selectQuery("Select max(idvenda) from venda")[0][0]
        for item in venda.items:
            item.idvenda = id_venda
            self.incluir(item)
            produto = Produto()
            produto.idproduto = item.idproduto
            produto.qtde = item.qtde
            produtoDAO.atualizar_quantidade(produto)

    def deletar_venda(self, venda):
        self.delete(venda)

    def pesquisa_codigo(self, entrada):
        venda = self.procuraRegistro(entrada)
        if venda and len(venda) > 0:
            return self.converte_venda(venda[0])
        return Venda()

    def converte_venda(self, entrada):
        clienteDao = ControleCliente()
        retorno = Venda()
        retorno.idvenda = entrada[0]
        retorno.data = entrada[1]
        cliente = Cliente()
        cliente.idcliente = entrada[2]
        retorno.valortotal = entrada[3]
        retorno.cliente = clienteDao.pesquisa_codigo(cliente)
        item = ItemVenda()
        item.idvenda = retorno.idvenda
        itens_venda = self.procuraRegistro(item)

        for item in itens_venda:
            novo_item = ItemVenda()
            novo_item.idproduto = item[0]
            novo_item.idvenda = item[1]
            novo_item.qtde = item[2]
            novo_item.valor = item[3]
            retorno.items.append(novo_item)

        return retorno

    def listar_todas_vendas(self, objeto: Venda):
        vendas = self.listarTodos(objeto)
        formatadas = []
        for venda in vendas:
            formatadas.append(self.converte_venda(venda))
        return formatadas

    def listar_vendas_cliente(self, entrada: Venda):
        sql = "select * from venda where idcliente = {}".format(entrada.cliente.idcliente)
        self.ob.abrirConexao()
        lista = self.ob.selectQuery(sql)
        return lista
