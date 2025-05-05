function inserir_itemvenda() {
   var table = document.getElementById("tabela");
   var produto = document.getElementById("produto");
   var idproduto = produto.value;
   var produtoAtributos = produto.options[produto.selectedIndex];

   var qtde = parseInt(document.getElementById("qtde").value)
   if (isNaN(qtde) || qtde <= 0) {
        alert("Informe uma quantidade válida.");
        return;
   }

   var valor = parseFloat(produtoAtributos.getAttribute("data-preco"))
   var estoque = parseInt(produtoAtributos.getAttribute("data-estoque"))

   var linhas = table.getElementsByTagName("tr");
   for (let i = 1; i < linhas.length; i++) {
        let colunas = linhas[i].getElementsByTagName("td");
        if (colunas[0].innerText === idproduto) {
            let qtdeAtual = parseInt(colunas[2].innerText);
            let novaQtde = qtdeAtual + qtde;

            if (novaQtde > estoque) {
                alert("Estoque insuficiente! Estoque disponível: " + estoque);
                return;
            }

            colunas[2].innerText = novaQtde;
            colunas[4].innerText = (novaQtde * valor).toFixed(2);
            return;
        }

   }

   if (qtde > estoque) {
        alert("Estoque insuficiente! Estoque disponível: " + estoque);
        return;
    }

   var row = table.insertRow(-1);
   row.insertCell(0).innerHTML = idproduto

   row.insertCell(1).innerHTML = produtoAtributos.getAttribute("data-nome");

   row.insertCell(2).innerHTML = qtde;

   row.insertCell(3).innerHTML = valor.toFixed(2)

   row.insertCell(4).innerHTML = (valor * qtde).toFixed(2)

}

clientesFiltrados[{idcliente: 1, nome:"João", endereco:"Avenida"}]

document.querySelector("form").addEventListener("submit", function () {
    const tabela = document.getElementById("tabela");
    const linhas = tabela.getElementsByTagName("tr");
    let itens = [];

    for (let i = 1; i < linhas.length; i++) {
        const colunas = linhas[i].getElementsByTagName("td");

        const item = {
            idproduto: parseInt(colunas[0].innerText),
            nome: colunas[1].innerText,
            qtde: parseInt(colunas[2].innerText),
            valor: parseFloat(colunas[3].innerText)
        };
        itens.push(item);

    }

    document.getElementById("itens_json").value = JSON.stringify(itens);
});
