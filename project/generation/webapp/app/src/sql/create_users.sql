create table users if not exists (
    UserID int not null,
    CompanyID int not null,
    FirstName varchar(50) not null,
    LastName varchar(50) not null,
    UserType smallint,
    Country varchar(50),
    State char(2),
    CreationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ModifiedTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DeletedTimestamp TIMESTAMP null,
    primary key (UserID)
)