import json

from flask import Flask, render_template, request, redirect

from controle.controleCliente import ControleCliente
from controle.controleProduto import ControleProduto
from controle.controleVenda import ControleVenda
from modelo.cliente import Cliente
from modelo.itemVenda import ItemVenda
from modelo.produto import Produto
from modelo.venda import Venda

app = Flask(__name__)

clienteDAO = ControleCliente()
produtoDAO = ControleProduto()
vendaDAO = ControleVenda()

clientes = []
produtos = []
vendas = []


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/clientes')
def clientes():
    global clientes
    clientes = clienteDAO.listar_todos_registros(Cliente())

    return render_template('listaCliente.html', lista=clientes, titulo='Lista de Clientes')


@app.route('/clientes/cadastrar')
def cadastrar_cliente():
    return render_template('cadastroCliente.html', titulo="Cadastro de Cliente")

@app.route('/clientes/salvar', methods=['POST'])
def salvar_cliente():
    c = Cliente()

    c.nome = request.form['nome']
    c.endereco = request.form['endereco']
    clienteDAO.incluir_cliente(c)

    return redirect('/clientes')

#produtos
@app.route('/produtos')
def produtos():
    global produtos
    produtos = produtoDAO.listar_todos_registros(Produto())

    return render_template('listaProdutos.html', lista=produtos, titulo='Lista de Produtos')

@app.route('/produtos/cadastrar')
def cadastrar_produto():
    return render_template('cadastroProduto.html', titulo="Cadastro de Produto")

@app.route('/produtos/salvar', methods=['POST'])
def salvar_produto():
    p = Produto()

    p.nome = request.form['nome']
    p.qtde = request.form['qtde']
    p.preco = request.form['preco']

    produtoDAO.incluir_produto(p)

    return redirect('/produtos')

#venda
@app.route('/vendas')
def vendas():
    global vendas
    vendas = vendaDAO.listar_todas_vendas(Venda())

    return render_template('listaVendas.html', lista=vendas, titulo='Lista de Vendas')

@app.route('/vendas/cadastrar')
def efetuar_venda():
    produtos = produtoDAO.listar_todos_registros(Produto())
    clientes = clienteDAO.listar_todos_registros(Cliente())
    return render_template('efetuarVenda.html', produtos=produtos, clientes=clientes, titulo="Venda de Produto")

@app.route('/vendas/salvar', methods=['POST'])
def salvar_venda():
    v = Venda()

    cliente = Cliente()
    cliente.idcliente = int(request.form['idcliente'])
    cliente = clienteDAO.pesquisa_codigo(cliente)

    v.cliente = cliente

    itens_json = request.form.get('itens_json')

    itens_data = json.loads(itens_json)
    for item in itens_data:
        item_venda = ItemVenda()
        item_venda.idproduto = item['idproduto']
        item_venda.qtde = item['qtde']
        item_venda.valor = item['valor']
        v.adicionar_item(item_venda)

    v.calcular_total()

    vendaDAO.incluir_venda(v)
    return redirect('/vendas')

@app.route('/vendas/detalhes/<int:idvenda>')
def detalhes_venda(idvenda):
    v = Venda()
    v.idvenda = idvenda

    v = vendaDAO.pesquisa_codigo(v)
    print(v.items[0])
    return render_template('detalhesVenda.html', venda=v, titulo="Detalhes da venda")

if __name__ == "__main__":
    app.run(debug=True)
