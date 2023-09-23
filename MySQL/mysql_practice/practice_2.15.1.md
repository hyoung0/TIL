```sql
SELECT * FROM customers;

-- 1
SELECT employeeNumber, lastName, firstName, city
FROM  employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;

-- 2
SELECT customerNumber , officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 3
SELECT customerNumber , officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 4
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 5
-- 문제2,3 모두 custromeres에 있는 필드인 customerNumber가 먼저 나오므로 FROM 다음에 customers이다. 즉, customers가 왼쪽에 위치하고 JOIN되는 테이블은 오른쪽에 위치한다.(고정)
-- LEFT JOIN office를 할 경우 '왼쪽에 위치하는 customers는 모든 값이 나오고' JOIN된 office는 왼쪽테이블인 customers와 일치하는 레코드만 나온다.(따라서 왼쪽 테이블에는 NONE값이 없고 오른쪽 테이블은 있음)
-- RIGHT JOIN office를 할 경우 '오른쪽에 위치하는 office는 모든 값이 나오고' 왼쪽에 있는 custromers는 오른쪽테이블인 office와 일치하는 레코드만 나온다.( 따라서 오른쪽 테이블에는 NONE값이 없고 왼쪽 테이블은 있음)
-- 문제 4번은 INNER JOIN으로 city를 기준으로 같은 레코드에 대해서만 결과가 나온다. 

-- 6
SELECT customerNumber , officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices ON customers.city = offices.city
UNION
SELECT customerNumber , officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 7
SELECT * FROM orders;
SELECT * FROM orderdetails;

SELECT orders.orderNumber , orderDate
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
ORDER BY
	orderNumber;
    
-- 8
SELECT * FROM products;

SELECT orderNumber , orderdetails.productCode , productName
FROM orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;

-- 9
SELECT orderdetails.orderNumber , orderdetails.productCode , orderDate, productName
FROM orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber;

```