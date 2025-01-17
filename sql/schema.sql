-- Active: 1736442231636@@127.0.0.1@3306@dailyrecords
CREATE TABLE dailyrecords.expenses (
    date DATE,               -- Day of the week
    inventory JSON NOT NULL,                   -- JSON storing item names, quantities, and costs
    salaries JSON NOT NULL,                    -- JSON storing chef names and their salaries
    PRIMARY KEY (date),
    FOREIGN KEY (date) REFERENCES dailyrecords.date(date)
);

CREATE TABLE dailyrecords.chefs (
    name VARCHAR(255) PRIMARY KEY              -- Unique chef name
);

CREATE TABLE dailyrecords.items (
    name VARCHAR(255) PRIMARY KEY             -- Unique item name
);

CREATE TABLE dailyrecords.collection (
    date DATE,
    upi DECIMAL(10, 2) DEFAULT 0.00 NOT NULL,  -- UPI payment collection
    cash DECIMAL(10, 2) DEFAULT 0.00 NOT NULL, -- Cash payment collection
    card DECIMAL(10, 2) DEFAULT 0.00 NOT NULL, -- Card payment collection
    foodappsettlement DECIMAL(10, 2) DEFAULT 0.00 NOT NULL,
    others DECIMAL(10, 2) DEFAULT 0.00 NOT NULL, -- Other payment modes
    PRIMARY KEY (date),
    FOREIGN KEY (date) REFERENCES dailyrecords.date(date)
);

CREATE TABLE dailyrecords.date (
    date DATE PRIMARY KEY,                     -- Ensures one entry per date
    day VARCHAR(50) NOT NULL,                  -- Day of the week
    status VARCHAR(50) NOT NULL,               -- Status of the day
    importance VARCHAR(100) NOT NULL           -- Importance level of the day
);

CREATE TABLE dailyrecords.usage (
    date DATE,
    details JSON NOT NULL,
    PRIMARY KEY (date),
    FOREIGN KEY (date) REFERENCES dailyrecords.date(date)
);
