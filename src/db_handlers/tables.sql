CREATE TABLE IF NOT EXISTS store (
    uuid UUID PRIMARY KEY,
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
    uuid UUID PRIMARY KEY,
    type_id UUID REFERENCES product_type(id),
    name VARCHAR(255) NOT NULL,
    size SIZE NOT NULL DEFAULT 'Regular',
    price NUMERIC(6, 2) NOT NULL
);
CREATE TABLE IF NOT EXISTS transaction (
    uuid UUID PRIMARY KEY,
    datetime TIMESTAMP NOT NULL,
    store_uuid UUID REFERENCES store(uuid) NOT NULL,
    payment_type VARCHAR(4) NOT NULL,
    total_amount NUMERIC(6, 2) NOT NULL
);
CREATE TABLE IF NOT EXISTS basket (
    id UUID PRIMARY KEY,
    transaction_uuid UUID REFERENCES transaction(uuid) NOT NULL,
    product_uuid UUID REFERENCES product(uuid) NOT NULL
);