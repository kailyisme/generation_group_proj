CREATE TABLE IF NOT EXISTS store (
    id UUID PRIMARY KEY,
    location VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS product_type (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
DO $$ BEGIN
    CREATE TYPE SIZE AS enum('Small', 'Regular', 'Large');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;
CREATE TABLE IF NOT EXISTS product (
    id UUID PRIMARY KEY,
    type_id UUID REFERENCES product_type(id),
    name VARCHAR(255) NOT NULL,
    size SIZE NOT NULL DEFAULT 'Regular',
    price NUMERIC(6, 2) NOT NULL
);
CREATE TABLE IF NOT EXISTS transaction (
    id UUID PRIMARY KEY,
    datetime TIMESTAMP NOT NULL,
    store_id UUID REFERENCES store(id) NOT NULL,
    payment_type VARCHAR(4) NOT NULL,
    total_amount NUMERIC(6, 2) NOT NULL
);
CREATE TABLE IF NOT EXISTS basket (
    id UUID PRIMARY KEY,
    transaction_id UUID REFERENCES transaction(id) NOT NULL,
    product_id UUID REFERENCES product(id) NOT NULL
);