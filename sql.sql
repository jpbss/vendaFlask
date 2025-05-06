use tpc10

create table cliente(
	idcliente int auto_increment primary key,
	nome varchar(120),
    endereco varchar(100)
);

create table produto(
	idproduto int auto_increment primary key,
    nome varchar(120),
    qtde int,
    preco decimal(10, 2)
);

create table venda(
	
    idvenda int auto_increment primary key,
    data datetime,
    idcliente int,
    valortotal decimal(10,2),
	foreign key  (idcliente) references cliente(idcliente)
);

create table itemvenda(
	idproduto int,
    idvenda int,
    qtde int,
    valor decimal(10,2),
    primary key(idproduto, idvenda),
    foreign key(idproduto) references produto(idproduto),
    foreign key(idvenda) references venda(idvenda)
);