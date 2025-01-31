create database correcao;
use correcao;
CREATE TABLE clientes (
cliente_id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE,
telefone VARCHAR(15),
data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Produtos (
produto_id INT AUTO_INCREMENT PRIMARY KEY,
nome_produto VARCHAR(255) NOT NULL,
descricao TEXT,
preco DECIMAL(10, 2) NOT NULL,
quantidade_em_estoque INT DEFAULT 0
);
CREATE TABLE Pedidos (
pedido_id INT AUTO_INCREMENT PRIMARY KEY,
cliente_id INT,
data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
status VARCHAR(50) DEFAULT 'Pendente',
FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
);
CREATE TABLE Itens_Pedido (
item_id INT AUTO_INCREMENT PRIMARY KEY,
pedido_id INT,
produto_id INT,
quantidade INT NOT NULL,
preco_unitario DECIMAL(10, 2) NOT NULL,
FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id),
FOREIGN KEY (produto_id) REFERENCES Produtos(produto_id)
);
CREATE TABLE Vendas (
venda_id INT AUTO_INCREMENT PRIMARY KEY,
pedido_id INT,
data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
total_venda DECIMAL(10, 2) NOT NULL,
FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id)
);
CREATE TABLE Historico_Compras (
historico_id INT AUTO_INCREMENT PRIMARY KEY,
cliente_id INT,
pedido_id INT,
data_compra DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id),
FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id)
);

#--------------------------------------------------------------------------

INSERT INTO Clientes (nome, email, telefone) VALUES
('João Silva', 'joao.silva@example.com', '11987654321'),
('Maria Oliveira', 'maria.oliveira@example.com', '11976543210'),
('Carlos Souza', 'carlos.souza@example.com', '11876543219'),
('Ana Costa', 'ana.costa@example.com', '11765432100'),
('Luiz Santos', 'luiz.santos@example.com', '11654321009'),
('Fernanda Lima', 'fernanda.lima@example.com', '11543210987'),
('Roberto Pereira', 'roberto.pereira@example.com', '11432109876'),
('Patrícia Almeida', 'patricia.almeida@example.com', '11321098765');
INSERT INTO Produtos (nome_produto, descricao, preco,
quantidade_em_estoque) VALUES
('Camiseta Polo', 'Camiseta polo masculina, tamanho M, diversas cores', 49.99,
100),
('Calça Jeans', 'Calça jeans feminina, tamanho 38, cor azul', 89.90, 50),
('Tênis Esportivo', 'Tênis esportivo, modelo unissex', 159.99, 80),
('Relógio de Pulso', 'Relógio de pulso digital, modelo esportivo', 120.50, 30),
('Bermuda Casual', 'Bermuda casual masculina, tamanho G', 59.99, 60),
('Boné', 'Boné esportivo, ajustável, diversas cores', 25.00, 100),
('Camisa de Manga Longa', 'Camisa social de manga longa', 75.00, 40),
('Blusa de Frio', 'Blusa de frio masculina, tamanho P', 99.90, 70),
('Saia de Verão', 'Saia de verão feminina, tamanho M', 49.50, 30),
('Shorts Esportivo', 'Shorts feminino, tecido leve e confortável', 35.00, 90),
('Jaqueta de Couro', 'Jaqueta de couro masculina, tamanho GG', 199.90, 20),
('Suéter', 'Suéter de lã feminina, tamanho P', 85.00, 40),
('Chapéu', 'Chapéu estiloso unissex', 50.00, 50),
('Bolsa de Couro', 'Bolsa de couro feminina, estilo casual', 149.90, 60),
('Cinto de Couro', 'Cinto de couro masculino, preto', 35.00, 120),
('Meias Esportivas', 'Meias esportivas, pacote com 3 pares', 19.90, 200),
('Tênis Casual', 'Tênis casual feminino, modelo confortável', 129.99, 75),
('Relógio Analógico', 'Relógio analógico de luxo, modelo prata', 350.00, 25),
('Óculos de Sol', 'Óculos de sol unissex, proteção UV', 59.99, 150);
INSERT INTO Pedidos (cliente_id, status) VALUES
(1, 'Pendente'),
(1, 'Pendente');
INSERT INTO Pedidos (cliente_id, status) VALUES
(2, 'Pendente'),
(2, 'Concluído'),
(2, 'Pendente');
INSERT INTO Pedidos (cliente_id, status) VALUES
(3, 'Pendente'),
(3, 'Concluído');
INSERT INTO Pedidos (cliente_id, status) VALUES
(4, 'Concluído'),
(4, 'Pendente'),
(4, 'Concluído');
INSERT INTO Pedidos (cliente_id, status) VALUES
(5, 'Concluído');
INSERT INTO Pedidos (cliente_id, status) VALUES
(6, 'Pendente'),
(6, 'Concluído'),
(6, 'Concluído');
INSERT INTO Pedidos (cliente_id, status) VALUES
(7, 'Pendente'),
(7, 'Concluído');
INSERT INTO Pedidos (cliente_id, status) VALUES
(8, 'Pendente'),
(8, 'Concluído');
INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(1, 1, 2, 49.99),
(1, 5, 1, 59.99),
(2, 3, 1, 159.99),
(2, 12, 1, 85.00);
INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(3, 6, 2, 25.00),
(3, 4, 1, 120.50),
(2, 9, 1, 49.50),
(2, 8, 1, 99.90);
INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(4, 7, 1, 75.00),
(4, 18, 1, 129.99),
(5, 2, 2, 89.90);
INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(6, 19, 1, 59.99),
(6, 10, 1, 35.00),
(7, 11, 1, 199.90),
(7, 1, 3, 49.99);
INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(8, 2, 1, 89.90);
INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(9, 3, 1, 159.99),
(9, 15, 1, 149.90),
(10, 5, 2, 59.99),
(10, 4, 1, 120.50);
INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(11, 14, 1, 50.00),
(11, 6, 1, 25.00),
(12, 3, 2, 159.99);
INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(13, 17, 1, 19.90),
(13, 9, 1, 49.50),
(14, 12, 1, 85.00);
INSERT INTO Vendas (pedido_id, total_venda) VALUES
(1, 199.97),
(2, 389.89);
INSERT INTO Vendas (pedido_id, total_venda) VALUES
(3, 470.00),
(2, 349.40),
(4, 330.00);
INSERT INTO Vendas (pedido_id, total_venda) VALUES
(4, 264.99),
(5, 179.80);
INSERT INTO Vendas (pedido_id, total_venda) VALUES
(6, 184.99),
(7, 335.89),
(8, 149.97);
INSERT INTO Vendas (pedido_id, total_venda) VALUES
(8, 89.90);
INSERT INTO Vendas (pedido_id, total_venda) VALUES
(9, 409.89),
(10, 340.00),
(11, 220.50);
INSERT INTO Vendas (pedido_id, total_venda) VALUES
(11, 125.00),
(12, 319.98);
INSERT INTO Vendas (pedido_id, total_venda) VALUES
(13, 69.40),
(14, 85.00);
INSERT INTO Historico_Compras (cliente_id, pedido_id) VALUES
(1, 1), (1, 2),
(2, 3), (2, 2), (2, 4),
(3, 4), (3, 5),
(4, 6), (4, 7), (4, 8),
(5, 8),
(6, 9), (6, 10), (6, 11),
(7, 11), (7, 12),
(8, 13), (8, 14);

select count(*) as totcli from clientes;
select count(*) as totped from pedidos;
select count(*) as totalped from pedidos group by status;
select pedido_id, count(*) as tot from itens_pedido group by pedido_id;

select sum(pedido_id) as totvend from historico_compras;

select avg(total_venda) as medvend from vendas;

select avg(item_id) as tot from itens_pedido;
select * from pedidos;

select p.pedido_id, i.produto_id, i.quantidade, i.preco_unitario from pedidos p join itens_pedido i on i.pedido_id = p.pedido_id;
select c.cliente_id, c.nome, p.pedido_id from clientes c join pedidos p on c.cliente_id = p.cliente_id;

#---------------------------------------------------------------------------------------------------------------------------------------

select c.cliente_id AS cliente_id, c.nome AS cliente_nome, SUM(ip.quantidade) AS historico_compras FROM clientes c 
JOIN pedidos p ON c.cliente_id = p.cliente_id JOIN itens_pedido ip ON p.pedido_id = ip.pedido_id GROUP BY c.cliente_id, c.nome;

#---------------------------------------------------------------------------------------------------------------------------------------

select c.cliente_id, c.nome, pedido_id, p.status from
clientes c join pedidos p on c.cliente_id = p.cliente_id;


select count(*) from pedidos;

#query de produtos cujo estoque esta abaixo de 10 unid
