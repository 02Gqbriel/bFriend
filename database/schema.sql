DROP TABLE IF EXISTS User;

CREATE TABLE IF NOT EXISTS User
(
    userID    INTEGER PRIMARY KEY AUTOINCREMENT,
    username  varchar(255) NOT NULL UNIQUE,
    password  varchar(255) NOT NULL,
    email     varchar(255) NOT NULL UNIQUE,
    firstname varchar(255),
    lastname  varchar(255),
    age       INTEGER,
    hobby     varchar(255),
    accStatus varchar(255)
);

INSERT INTO User (username, password, email, firstname, lastname, age, hobby, accStatus)
VALUES ('johnsmith', 'pass123', 'johnsmith@example.com', 'John', 'Smith', 30, 'Reading', 'Active');

INSERT INTO User (username, password, email, firstname, lastname, age, hobby, accStatus)
VALUES ('janedoe', 'password456', 'jane.doe@example.com', 'Jane', 'Doe', 25, 'Painting', 'Active');

INSERT INTO User (username, password, email, firstname, lastname, age, hobby, accStatus)
VALUES ('mikebrown', 'securepass789', 'mike.brown@example.com', 'Mike', 'Brown', 35, 'Cooking', 'Inactive');




DROP TABLE IF EXISTS Friendship;

CREATE TABLE IF NOT EXISTS Friendship
(
    friendshipID INTEGER PRIMARY KEY AUTOINCREMENT,
    user1ID      INTEGER,
    user2ID      INTEGER,
    FOREIGN KEY (user1ID, user2ID) REFERENCES User (userID, userID)
);

-- Insert statement 1
INSERT INTO Friendship (user1ID, user2ID)
VALUES (1, 2);

-- Insert statement 2
INSERT INTO Friendship (user1ID, user2ID)
VALUES (1, 3);

-- Insert statement 3
INSERT INTO Friendship (user1ID, user2ID)
VALUES (2, 3);
