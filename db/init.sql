CREATE DATABASE IF NOT EXISTS interview;
USE interview;
CREATE TABLE IF NOT EXISTS product  (
    id int(10),
    name varchar(255),
    image varchar(255),
    price float(10)
    );

CREATE TABLE IF NOT EXISTS orders  (
    id int(10),
    productID int(10),
    quantity int	(3),
    price float(3)
    );

    SHOW TABLES;


CREATE TABLE IF NOT EXISTS inventory  (
    record int(10) auto_increment,
    productID int(10),
    availableQuantity int(10),
    primary key (record)
    );

INSERT INTO orders (id, productID, quantity, price)
VALUES ('12345', '1222', '3', '3001');
INSERT INTO product (id, name, image, price)
VALUES ('12345', 'nick', 'https://image.url', '3000');
INSERT INTO product (id, name, image, price)
VALUES ('1234', 'nick2', 'https://image.url', '53000');
INSERT INTO inventory (productID, availableQuantity)
VALUES ('1234','53000');
