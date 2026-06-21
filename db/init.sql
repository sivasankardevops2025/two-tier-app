CREATE DATABASE IF NOT EXISTS employeedb;
USE employeedb;

CREATE TABLE IF NOT EXISTS employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  department VARCHAR(100)
);

INSERT INTO employees (name, department) VALUES
  ('Anita Rao', 'DevOps'), 
  ('Karthik Reddy', 'Cloud');
