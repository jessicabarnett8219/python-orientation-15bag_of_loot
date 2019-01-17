PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Children;
DROP TABLE IF EXISTS Gifts;

CREATE TABLE `Children` (
    `ChildId`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `FirstName`    TEXT NOT NULL,
    `LastName`    TEXT NOT NULL,
    `IsBest` BIT NOT NULL
);

CREATE TABLE `Gifts` (
    `GiftId`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `GiftName`    TEXT NOT NULL,
    `Delivered`    BIT NOT NULL,
    `ChildId` INTEGER NOT NULL,
    FOREIGN KEY(`ChildId`)
    REFERENCES `Children`(`ChildId`)
    ON DELETE cascade
);
