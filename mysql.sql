create database vegetablecart;

use vegetablecart;
drop database vegetablecart;

create table owners(vegetables varchar(20),cost decimal(3,1),quantity decimal(3,1),price decimal(3,1));

insert into owners values('onions',30.0,70.0,40.0),
('tomatos',20.0,18.0,30.0),
('brinjals',17.0,8.0,25.0),
('potatoes',12.0,15.0,20.0),
('carrots',30.0,28.0,50.0);

drop table owners;
select * from owners;
select price from owners;
select *  from owners where vegetables='onions';
select quantity,price,cost from owners where vegetables='onions';
rollback;
commit;

create table users(vegs varchar(20),quants decimal(3,1),pris decimal(3,1),profit decimal(3,1));

select * from users;
alter table users modify profit decimal(10,2);
alter table users modify pris decimal(10,2);


delete from users;
drop table userdetails;
create table userdetails(customername varchar(30),customermobileno bigint);
drop table userdetails;
alter table userdetails modify customermobileno bigint;
select * from userdetails;


show processlist;
select * from owners