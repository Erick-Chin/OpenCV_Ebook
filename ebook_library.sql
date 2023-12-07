CREATE DATABASE IF NOT EXISTS ebook_libary;
USE ebook_libary;

CREATE TABLE ebook (
	Book_id INT NOT NULL,
	Title CHAR(32) NOT NULL,
	Publisher_name VARCHAR(28) NOT NULL,
	PRIMARY KEY(Book_id), --primary keys are used because the table cannot be null this is the unique record 
	FOREIGN KEY(Publisher_name) REFERENCES PUBLISHER(Name) -- references a primary key from another table to create a relation 
);

CREATE TABLE ebook_author (
	Book_id INT NOT NULL,
	Author_name VARCHAR(32) NOT NULL,
	PRIMARY KEY(Book_id, Author_name),
	FOREIGN KEY(Book_id) REFERENCES BOOK(Book_id)
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    --This is non-standard MySQL syntax. After the brackets that enclose the list of columns and indexes, MySQL allows table options. Lets it store the tables in a specific place 
);

CREATE TABLE publisher (
	Name VARCHAR(28) NOT NULL,
	Address VARCHAR(32) NOT NULL,
	Phone CHAR(10) NOT NULL,
	PRIMARY KEY(Name)
);

CREATE TABLE user (
	Card_no INT NOT NULL,
	Name VARCHAR(32) NOT NULL,
	Address VARCHAR(32) NOT NULL,
	Phone CHAR(10) NOT NULL,
	PRIMARY KEY(Card_no)
);

