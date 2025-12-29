CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Commission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, Commission) VALUES
('S001', 'John Doe', 'New York', 0.10),
('S002', 'Jane Smith', 'Los Angeles', 0.12),
('S003', 'Jim Brown', 'Chicago', 0.11),
('S004', 'Jake White', 'Houston', 0.09),
('S005', 'Jill Black', 'Phoenix', 0.13),
('S006', 'Joe Green', 'Philadelphia', 0.10),
('S007', 'Jenny Blue', 'San Antonio', 0.14),
('S008', 'Jack Yellow', 'San Diego', 0.08),
('S009', 'Jessica Purple', 'Dallas', 0.15),
('S010', 'Jeremy Orange', 'San Jose', 0.07);

SELECT * FROM Salesman;


CREATE TABLE IF NOT EXISTS Orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
('O001', 1500.00, '2024-01-15', 'C001', 'S001'),
('O002', 2500.00, '2024-02-20', 'C002', 'S002'),
('O003', 1800.00, '2024-03-10', 'C003', 'S003'),
('O004', 3000.00, '2024-04-05', 'C004', 'S004'),
('O005', 2200.00, '2024-05-12', 'C005', 'S005'),
('O006', 2700.00, '2024-06-18', 'C006', 'S006'),
('O007', 3200.00, '2024-07-22', 'C007', 'S007'),
('O008', 2900.00, '2024-08-30', 'C008', 'S008'),
('O009', 3500.00, '2024-09-14', 'C009', 'S009'),
('O010', 4000.00, '2024-10-25', 'C010', 'S010');

SELECT * FROM Orders;

SELECT name, Commission
FROM Salesman;
