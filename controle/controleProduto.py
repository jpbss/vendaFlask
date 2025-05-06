from controle.controleGenerico import ControleGenerico
from modelo.produto import Produto


class ControleProduto(ControleGenerico):
    def incluir_produto(self, produto):
        self.incluir(produto)

    def alterar_produto(self,produto):
        self.alterar(produto)

    def deletar_produto(self, produto):
        self.delete(produto)

    def pesquisar_codigo(self, entrada:Produto):
        produto = self.procuraRegistro(entrada)
        retorno = Produto()
        if len(produto) >= 1:
            retorno = self.converte_produto(produto)
        return retorno

    def converte_produto(self, produto):
        retorno = Produto()
        retorno.idproduto = produto[0][0]
        retorno.nome = produto[0][1]
        retorno.qtde = produto[0][2]
        retorno.preco = produto[0][3]

        return retorno

    def listar_todos_registros(self, objeto):
        lista = self.listarTodos(objeto)
        formatada = []
        for i in lista:
            formatada.append(self.converte_objeto(i))

        return formatada

    def converte_objeto(self, entrada):
        produto = Produto()
        produto.idproduto = entrada[0]
        produto.nome = entrada[1]
        produto.qtde = entrada[2]
        produto.preco = entrada[3]
        return produto

    def atualizar_quantidade(self, entrada:Produto):
        produto = self.pesquisar_codigo(entrada)
        produto.qtde = produto.qtde - entrada.qtde
        self.alterar(produto)

