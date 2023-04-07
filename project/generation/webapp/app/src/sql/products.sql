DROP TABLE products;

CREATE TABLE products (
    ProductID int NOT NULL AUTO_INCREMENT,
    Name varchar(50) NOT NULL,
    Description text,
    CreationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ModifiedTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DeletedTimestamp TIMESTAMP NULL,
    PRIMARY KEY (ProductID)
);
