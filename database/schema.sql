DROP TABLE IF EXISTS User;

CREATE TABLE IF NOT EXISTS User
(
    userID    INTEGER PRIMARY KEY AUTOINCREMENT,
    username  varchar(255) NOT NULL,
    password  varchar(255) NOT NULL,
    firstname varchar(255),
    lastname  varchar(255),
    age       INTEGER,
    hobby     varchar(255),
    accStatus varchar(255)
);

-- Insert statement 1
INSERT INTO User (username, password, firstname, lastname, age, hobby, accStatus)
VALUES ('john_doe', 'password123', 'John', 'Doe', 30, 'Reading', 'Active');

-- Insert statement 2
INSERT INTO User (username, password, firstname, lastname, age, hobby, accStatus)
VALUES ('jane_smith', 'securepass', 'Jane', 'Smith', 25, 'Gardening', 'Active');

-- Insert statement 3
INSERT INTO User (username, password, firstname, lastname, age, hobby, accStatus)
VALUES ('mark_johnson', 'letmein', 'Mark', 'Johnson', 35, 'Hiking', 'Inactive');


DROP TABLE IF EXISTS Friendship;

CREATE TABLE IF NOT EXISTS Friendship
(
    friendshipID INTEGER PRIMARY KEY AUTOINCREMENT,
    user1ID      INTEGER,
    user2ID      INTEGER,
    FOREIGN KEY (user1ID, user2ID) REFERENCES User (userID, userID)
);