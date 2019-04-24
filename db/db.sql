CREATE DATABASE if not EXISTS mydb;
use mydb;

create table if not exists news(
	time varchar(30) not null,
    title text not null,
    href varchar(100) not null,
    detail text not null,
    primary key(time, href)
);