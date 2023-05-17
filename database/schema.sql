CREATE TABLE IF NOT EXISTS User (
           userID INTEGER PRIMARY KEY AUTOINCREMENT,
           username varchar(255) NOT NULL,
           password varchar(255) NOT NULL,
           firstname varchar(255),
           lastname varchar(255),
           hobby varchar(255),
           accStatus varchar(255)
);

CREATE TABLE IF NOT EXISTS Friendship (
    friendshipID INTEGER PRIMARY KEY AUTOINCREMENT,
    user1ID INTEGER,
    user2ID INTEGER,
    FOREIGN KEY (user1ID, user2ID) REFERENCES User(userID, userID)
);