CREATE TABLE IF NOT EXISTS store (
    uuid UUID PRIMARY KEY,
    location VARCHAR(255) NOT NULL
    );


CREATE TABLE IF NOT EXISTS product_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    );


CREATE TYPE SIZE AS ENUM('Small', 'Regular', 'Large');


CREATE TABLE IF NOT EXISTS product (
    uuid UUID PRIMARY KEY,
    type_id INTEGER REFERENCES product_type(id),
    name VARCHAR(255) NOT NULL,
    size SIZE NOT NULL DEFAULT 'Regular',
    price NUMERIC(6,2) NOT NULL
    );


CREATE TABLE IF NOT EXISTS transaction (
    uuid UUID PRIMARY KEY,
    datetime TIMESTAMP NOT NULL,
    store_uuid UUID REFERENCES store(uuid) NOT NULL,
    payment_type VARCHAR(4) NOT NULL,
    total_amount NUMERIC(6,2) NOT NULL
    );


CREATE TABLE IF NOT EXISTS basket (
    id UUID PRIMARY KEY,
    transaction_uuid UUID REFERENCES transaction(uuid) NOT NULL,
    product_uuid UUID REFERENCES product(uuid) NOT NULL
    );