create database url_shortener;
create table url 
(
	id int NOT NULL PRIMARY KEY,
  longurl varchar (255) NOT NULL,
	hash varchar (255) NOT NULL
);
create user test_user with password '1234';
grant all privileges on database url to test_user;
grant all privileges on table url_shortener.url to test_user;