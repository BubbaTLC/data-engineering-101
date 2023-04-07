DROP TABLE companies;

CREATE TABLE companies (
    CompanyID int NOT NULL AUTO_INCREMENT,
    Name varchar(50) NOT NULL,
    Country varchar(50),
    State char(2),
    CreationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ModifiedTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DeletedTimestamp TIMESTAMP NULL,
    PRIMARY KEY (CompanyID)
);
