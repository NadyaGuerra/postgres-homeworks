-- SQL-команды для создания таблиц


CREATE TABLE customers_data
(
    customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) not null,
	contact_name varchar(100) not null
);

SELECT * FROM customers_data

CREATE TABLE employees_data
(
    employee_id int PRIMARY KEY,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	title  varchar(100),
	birth_date date,
	notes text
);

SELECT * FROM employees_data



CREATE TABLE orders_data
(
    orders_id int PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers_data(customer_id) not null,
	employee_id int REFERENCES employees_data(employee_id) not null,
	order_date date,
	ship_city varchar(100) not null
);