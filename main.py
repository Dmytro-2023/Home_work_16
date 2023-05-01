CREATE DATABASE employees;
USE employees;
CREATE TABLE employee (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  salary DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id)
);
INSERT INTO employee (first_name, last_name, salary)
VALUES
  ('John', 'Doe', 50000.00),
  ('Jane', 'Doe', 60000.00),
  ('Bob', 'Smith', 45000.00),
  ('Alice', 'Johnson', 70000.00),
  ('Joe', 'Brown', 55000.00);
SELECT * FROM employee ORDER BY first_name ASC;

SELECT CONCAT(first_name, ' ', last_name) AS full_name, salary, salary * 0.15 AS tax FROM employee;

SELECT SUM(salary) AS total_salary FROM employee;

SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM employee;

SELECT AVG(salary) AS avg_salary, COUNT(*) AS num_employees FROM employee;
