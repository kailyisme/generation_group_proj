CREATE TABLE IF NOT EXISTS store (
    id VARCHAR(40) PRIMARY KEY,
    location VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS product_type (
    id VARCHAR(40) PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
-- CREATE TABLE IF NOT EXISTS product_size (
--     id VARCHAR(40) PRIMARY KEY,
--     name varchar(255) NOT NULL
-- );
CREATE TABLE IF NOT EXISTS product (
    id VARCHAR(40) PRIMARY KEY,
    type_id VARCHAR(40) REFERENCES product_type(id),
    name VARCHAR(255) NOT NULL,
    size VARCHAR(255),
    price NUMERIC(6, 2) NOT NULL
);
CREATE TABLE IF NOT EXISTS transaction (
    id VARCHAR(40) PRIMARY KEY,
    datetime NUMERIC(16,0) NOT NULL,
    store_id VARCHAR(40) REFERENCES store(id) NOT NULL,
    payment_type VARCHAR(4) NOT NULL,
    total_amount NUMERIC(6, 2) NOT NULL
);
CREATE TABLE IF NOT EXISTS basket (
    id VARCHAR(40) PRIMARY KEY,
    transaction_id VARCHAR(40) REFERENCES transaction(id) NOT NULL,
    product_id VARCHAR(40) REFERENCES product(id) NOT NULL
);