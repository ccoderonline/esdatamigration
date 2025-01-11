CREATE TABLE DAILY_RECORDS.expenses (
    date DATE PRIMARY KEY,                     -- Ensures one entry per date
    day VARCHAR(10) NOT NULL,                  -- Day of the week
    inventory JSON NOT NULL,                   -- JSON storing item names, quantities, and costs
    salaries JSON NOT NULL,                    -- JSON storing chef names and their salaries
);

CREATE TABLE DAILY_RECORDS.items (
    name VARCHAR(255) PRIMARY KEY             -- Unique item name
);

CREATE TABLE DAILY_RECORDS.chefs (
    name VARCHAR(255) PRIMARY KEY              -- Unique chef name
);

CREATE TABLE DAILY_RECORDS.collection (
    date DATE PRIMARY KEY,                     -- Ensures one entry per date
    day VARCHAR(10) NOT NULL,                  -- Day of the week
    upi DECIMAL(10, 2) DEFAULT 0.00 NOT NULL,  -- UPI payment collection
    cash DECIMAL(10, 2) DEFAULT 0.00 NOT NULL, -- Cash payment collection
    card DECIMAL(10, 2) DEFAULT 0.00 NOT NULL, -- Card payment collection
    others DECIMAL(10, 2) DEFAULT 0.00 NOT NULL -- Other payment modes
);
