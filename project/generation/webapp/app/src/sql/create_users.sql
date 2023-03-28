CREATE TABLE users (
    UserID int NOT NULL,
    CompanyID int NOT NULL,
    FirstName varchar(50) NOT NULL,
    LastName varchar(50) NOT NULL,
    UserType smallint,
    Country varchar(50),
    State char(2),
    CreationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ModifiedTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DeletedTimestamp TIMESTAMP NULL,
    PRIMARY KEY (UserID)
);
