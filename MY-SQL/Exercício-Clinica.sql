create database clinica;
use clinica;
create table paciente(
id int auto_increment primary key,
cpf varchar(11),
nome varchar(100),
fone varchar(12),
nascimento date);

create table medico(
id int auto_increment primary key,
crm varchar(6),
nome varchar (150),
especialidade varchar (50));

create table historico(
id int,
num_proc int auto_increment primary key,
data_proc date,
procedimento varchar(200),
id_med int,
preco float(5,2),
foreign key(id) references paciente(id),
foreign key(id_med) references medico(id));

create table anaminese(
id int auto_increment primary key,
alergia varchar(50),
cirurgias varchar(50),
foreign key(id) references paciente(id));

insert into paciente(cpf, nome, fone, nascimento)
values('123456789-10', 'Carabino Tiro Certo',
 '11-987654321', '1983-10-12'),
('123456789-10', 'Astolfo Sanches',
 '11-987654321', '1990-11-15');

insert into paciente(cpf, nome, fone, nascimento)
values('123456789-10', 'Pamela Silva',
 '11-987654321', '1999-10-18'),
('123456789-10', 'Debora Cristina',
 '11-987654321', '1995-01-25'); 
 
insert into medico(crm, nome, especialidade)
values('90264', 'Dr.Alisson Ford', 'Oncologista');

insert into historico(id, data_proc, procedimento, id_med, preco)
values(2, '2024-10-01', 'extração de mieloma', '1', '70,94');

 select * from paciente;
 select * from medico;
 select * from historico;
 #---------------------------------------------------------------------
 
 select * from paciente where id=2;
 
 select distinct m.id, m.nome from historico
 h join medico m on h.id_med = m.id
