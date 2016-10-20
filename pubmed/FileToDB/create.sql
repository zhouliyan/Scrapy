drop database papaer_information;


create database Paper_Information;

use Paper_Information;

create table paper(
PMID int not null primary key,
title varchar(400) not null,
pubdate date,
journal char(40),
abstract varchar(4000) not null
)default charset=utf8;

create table author(
PMID int not null,
name char(50) not null,
PRIMARY KEY (PMID,name),
CONSTRAINT FK_ID FOREIGN KEY (PMID) REFERENCES paper(PMID)
)default charset=utf8;

