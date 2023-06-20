CREATE SCHEMA coffee;

CREATE TABLE IF NOT EXISTS coffee.Users (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Pwd VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS coffee.UserCoffee (
    Id SERIAL PRIMARY KEY,
    UserId INT,
    c1 VARCHAR(100),
    c2 VARCHAR(100),
    c3 VARCHAR(100),

    CONSTRAINT fk_user
        FOREIGN KEY (UserId)
        REFERENCES coffee.Users(Id)
);

INSERT INTO coffee.Users (Name, Pwd)
VALUES ('user', 'ea654541-426a-409c-a1b3-4597a0ecbfee');

INSERT INTO coffee.UserCoffee (UserId, c1, c2, c3)
   VALUES (1, 'espresso', 'capuccino', 'latte');


