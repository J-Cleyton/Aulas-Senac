create database techsstore;
use techsstore;
drop database techsstore;
create table clientes(
id int auto_increment primary key,
nome varchar(100),
email varchar(100),
telefone varchar(15),
endereco text );

create table produtos(
id int auto_increment primary key,
nome varchar(100),
descricao text,
preco decimal(10, 2),
estoque int );

create table pedidos(
id int auto_increment primary key,
id_cliente int,
data_pedido date,
total decimal (10, 2),
foreign key (id_cliente) references clientes(id));

create table itens_pedido(
id_pedido int,
id_produto int,
quantidade int,
preco_unitario decimal(10, 2),
primary key (id_pedido, id_produto),
foreign key (id_pedido) references pedidos(id),
foreign key (id_produto) references produtos(id));

#-----------------------------------------------------------------------------------

#Controle de estoque

SELECT
    id,
    nome,
    estoque
FROM
    produtos
WHERE
    estoque < 10; -- Necessário reabastecer estoque
