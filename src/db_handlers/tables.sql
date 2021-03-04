CREATE TABLE IF NOT EXISTS store (
    uuid UUID PRIMARY KEY,
    location VARCHAR(255)
    );

CREATE TABLE IF NOT EXISTS product_size (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    );


CREATE TABLE IF NOT EXISTS product_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    );


CREATE TABLE IF NOT EXISTS product (
    uuid UUID PRIMARY KEY,
    type_id INTEGER REFERENCES product_type(id),
    name VARCHAR(255),
    size_id INTEGER REFERENCES product_size(id),
    price MONEY
    );


CREATE TABLE IF NOT EXISTS transaction (
    uuid UUID PRIMARY KEY,
    datetime TIMESTAMP,
    store_uuid UUID REFERENCES store(uuid),
    payment_type VARCHAR(4),
    total_amount MONEY
    );


CREATE TABLE IF NOT EXISTS basket (
    id UUID PRIMARY KEY,
    transaction_uuid UUID REFERENCES transaction(uuid),
    product_uuid UUID REFERENCES product(uuid)
    );