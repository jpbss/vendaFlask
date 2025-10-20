# Sistema de Vendas Simples (vendaflask)

Este é um projeto acadêmico desenvolvido em Python para a matéria eletiva de Tópicos em Programação durante a minha graduação em Ciência da Computação. A aplicação é um sistema web simples de Ponto de Venda (PDV), focado no gerenciamento de produtos, clientes e no registo de vendas com controlo de stock.

## 1\. Visão Geral

O projeto implementa uma aplicação web monolítica usando Flask, seguindo uma arquitetura que separa a lógica de apresentação, a lógica de negócio e o acesso aos dados. O sistema permite realizar operações CRUD (Create, Read, Update, Delete) para clientes e produtos, e possui um módulo central para a realização de vendas.

### Funcionalidades Principais

  * **CRUD de Clientes:** Cadastro, listagem e edição de clientes.
  * **CRUD de Produtos:** Cadastro, listagem e edição de produtos, incluindo nome, quantidade (stock) e preço.
  * **Sistema de Vendas:**
      * Uma interface dinâmica (front-end) para selecionar um cliente e adicionar múltiplos produtos a uma "cesta".
      * Uso de JavaScript para gerir os itens da venda no lado do cliente antes de submeter ao servidor.
      * Ao salvar a venda, o sistema regista a transação, associa os itens da venda e **atualiza o stock** dos produtos vendidos.
      * Listagem de vendas realizadas e visualização de detalhes (itens, cliente, valor total).

## 2\. Pilha Tecnológica (Tech Stack)

  * **Backend:** Python 3
  * **Framework Web:** Flask
  * **Banco de Dados:** MySQL
  * **Frontend:** HTML, CSS, JavaScript (puro) e Jinja2 (Templates).

## 3\. Estrutura do Projeto

A aplicação está organizada da seguinte forma:

  * **`princ.py`**: Ponto de entrada da aplicação. Define todas as rotas (endpoints) do Flask e trata as requisições HTTP.
  * **`modelo/`**: Contém as classes de modelo (POPOs - Plain Old Python Objects) que representam as entidades da base de dados (`Cliente`, `Produto`, `Venda`, `ItemVenda`). Estas classes também geram os fragmentos SQL necessários para as operações de CRUD.
  * **`controle/`**: Contém a lógica de negócio e as classes de acesso a dados (DAO).
      * `controleGenerico.py`: Classe base que fornece métodos genéricos de CRUD (incluir, alterar, delete) e configura a conexão com o banco de dados.
      * Controladores específicos (ex: `controleCliente.py`, `controleProduto.py`, `controleVenda.py`): Herdam do `controleGenerico` e implementam a lógica de negócio de cada módulo.
  * **`templates/`**: Ficheiros HTML (renderizados com Jinja2) que compõem a interface do usuário.
  * **`static/`**: Contém os ficheiros estáticos (CSS e JavaScript).
  * **`sql.sql`**: Script DDL para criação do banco de dados `tpc10` e suas tabelas (`cliente`, `produto`, `venda`, `itemvenda`).

## 4\. Como Executar

1.  **Configurar o Banco de Dados:**

      * Garanta que um servidor MySQL esteja acessível.
      * Execute o script `sql.sql` para criar o banco `tpc10` e as tabelas.
      * **Importante:** As credenciais de conexão com o banco de dados estão fixas no ficheiro `controle/controleGenerico.py`. Atualize os valores de `ho` (host), `db` (database), `us` (usuário), `se` (senha) e `po` (porta) conforme a sua configuração local.

2.  **Instalar Dependências:**
    (Recomenda-se usar um ambiente virtual `venv`)

    ```bash
    # Instalar as dependências listadas
    pip install -r requirements.txt
    # Ou, no mínimo:
    # pip install Flask mysql-connector-python
    ```

3.  **Iniciar a Aplicação:**

    ```bash
    python princ.py
    ```

4.  **Aceder ao Sistema:**
    Abra o seu navegador e aceda ao endereço `http://127.0.0.1:5000` (ou o host configurado no `app.run`).
