CREATE TABLE IF NOT EXISTS sales_data (
    id SERIAL PRIMARY KEY,
    region VARCHAR(100),
    product_category VARCHAR(100),
    sales_amount NUMERIC,
    sales_date TIMESTAMPTZ
);

-- Sample data insertion
INSERT INTO sales_data (region, product_category, sales_amount, sales_date)
VALUES
    ('North America', 'Electronics', 100000, '2023-05-01'),
    ('Europe', 'Clothing', 50000, '2023-06-01'),
    ('Asia', 'Electronics', 200000, '2023-07-01'),
    ('South America', 'Toys', 30000, '2023-05-01'),
    ('Europe', 'Electronics', 150000, '2023-08-01');
