-- Creación de tablas e inserción de datos iniciales
CREATE TABLE IF NOT EXISTS tables (
    id SERIAL PRIMARY KEY,
    number INT UNIQUE NOT NULL,
    status VARCHAR(20) DEFAULT 'FREE'
);
CREATE TABLE IF NOT EXISTS dishes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    table_id INT REFERENCES tables(id),
    status VARCHAR(20) DEFAULT 'PENDING',
    special_instructions TEXT,
    total NUMERIC(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    dish_id INT REFERENCES dishes(id),
    quantity INT NOT NULL DEFAULT 1
);
INSERT INTO tables (number, status) VALUES 
(1, 'FREE'), (2, 'FREE'), (3, 'FREE'), (4, 'FREE'), (5, 'FREE'), (6, 'FREE')
ON CONFLICT (number) DO NOTHING;
INSERT INTO dishes (name, price) VALUES 
('Hamburguesa Clásica', 45.00), ('Pizza Artesanal', 60.00),
('Ceviche Mixto', 55.00), ('Papas Supremas', 25.00),
('Cerveza de Barril', 20.00), ('Gaseosa', 12.00)
ON CONFLICT DO NOTHING;
