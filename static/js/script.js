let itens = [];

function inserir_itemvenda() {
    const selectProduto = document.getElementById("produto");
    const idproduto = selectProduto.value;
    const nome = selectProduto.options[selectProduto.selectedIndex].getAttribute("data-estoque");
    const preco = parseFloat(selectProduto.options[selectProduto.selectedIndex].getAttribute("data-preco"));
    const qtde = parseInt(document.getElementById("qtde").value);
    const estoque = parseInt(selectProduto.options[selectProduto.selectedIndex].getAttribute("data-estoque"));

    if (!qtde || qtde <= 0) {
        alert("Informe uma quantidade válida.");
        return;
    }

    const indexExistente = itens.findIndex(item => item.idproduto === idproduto);
    const qtdeExistente = indexExistente !== -1 ? itens[indexExistente].qtde : 0;

    const qtdeTotal = qtdeExistente + qtde;

    if (qtdeTotal > estoque) {
        alert(`Estoque insuficiente! Disponível: ${estoque}`);
        return;
    }

    if (indexExistente !== -1) {
        itens[indexExistente].qtde += qtde;
    } else {
        const item = { idproduto, nome, qtde, valor: preco };
        itens.push(item);
    }

    atualizarTabela();
}

function remover_item(index) {
    itens.splice(index, 1);
    atualizarTabela();
}

function atualizarTabela() {
    const tabela = document.getElementById("tabela");
    tabela.innerHTML = `
        <thead>
            <tr>
                <th>Código</th>
                <th>Nome</th>
                <th>Quantidade</th>
                <th>Valor</th>
                <th>Subtotal</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            ${itens.map((item, index) => `
                <tr>
                    <td>${item.idproduto}</td>
                    <td>${item.nome}</td>
                    <td>${item.qtde}</td>
                    <td>${(item.valor).toFixed(2)}</td>
                    <td>${(item.qtde * item.valor).toFixed(2)}</td>
                    <td><button type="button" onclick="remover_item(${index})">Remover</button></td>
                </tr>
            `).join("")}
        </tbody>
    `;

    document.getElementById("itens_json").value = JSON.stringify(itens);
}
