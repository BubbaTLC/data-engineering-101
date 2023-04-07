DROP TABLE locations;

CREATE TABLE locations (
    LocationID int NOT NULL AUTO_INCREMENT,
    CompanyID int NOT NULL,
    Name varchar(50) NOT NULL,
    Street varchar(50),
    Country varchar(50),
    State char(2),
    PostalCode VARCHAR(6),
    CreationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ModifiedTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DeletedTimestamp TIMESTAMP NULL,
    PRIMARY KEY (LocationID)
);
