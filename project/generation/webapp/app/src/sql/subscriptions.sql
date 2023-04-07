DROP TABLE subscriptions;

CREATE TABLE subscriptions (
    SubscriptionID int NOT NULL AUTO_INCREMENT,
    LocationID int NOT NULL,
    Products JSON,
    CreationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ModifiedTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DeletedTimestamp TIMESTAMP NULL,
    PRIMARY KEY (SubscriptionID)
);
