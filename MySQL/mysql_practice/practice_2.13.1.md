```sql
-- 1
SELECT DISTINCT
	country
FROM
	customers
ORDER BY
	country;
    
-- 2
SELECT DISTINCT
	state
FROM
	customers
ORDER BY
	state DESC;
    
-- 3
SELECT 
	customerNumber , customerName , country
FROM
	customers
WHERE
	country != 'USA'
ORDER BY
	customerNumber DESC;

-- 4
SELECT 
	*
FROM
	offices
WHERE
	city = 'Paris';

-- 5
SELECT 
	customerNumber , customerName , country , state
FROM
	customers
WHERE
	country = 'USA' AND state = 'CA'
ORDER BY
	customerName DESC;

-- 6
SELECT 
	customerNumber , customerName , country , state
FROM
	customers
-- WHERE
-- 	country = 'USA' AND (state = 'CA' OR state = 'NY')
WHERE
	country = 'USA' AND (state IN ('CA', 'NY'))
ORDER BY
	customerNumber DESC;
    
-- 7 
SELECT 
	 customerNumber , customerName , state
FROM
	customers
WHERE
	state IN ('CA', 'NY', 'CT', 'PA')
ORDER BY
	customerNumber DESC;

-- 8
SELECT 
	productCode , productName , quantityInStock
FROM
	products
WHERE
	quantityInStock < 1000
ORDER BY
	quantityInStock;
    
-- 9
SELECT 
	productCode , productName , quantityInStock
FROM
	products
WHERE
	quantityInStock BETWEEN 2000 AND 3000
ORDER BY
	quantityInStock DESC; 
    
-- 10
SELECT 
	customerNumber , customerName , phone
FROM
	customers
WHERE
	phone LIKE '%555'
ORDER BY
	customerName DESC;

-- 11
SELECT
	productCode , quantityInStock
FROM
	products 
ORDER BY
	quantityInStock DESC
LIMIT 5;

-- 12
SELECT
	jobTitle, COUNT(jobTitle) AS count_job
FROM
	employees 
GROUP BY
	jobTitle
ORDER BY
	count_job DESC,
    jobTitle DESC;

-- 13
SELECT
	country, COUNT(country) AS count_country
FROM
	customers 
GROUP BY
	country
ORDER BY
	count_country DESC,
    country DESC;
    
-- 14
SELECT
	orderNumber, SUM(quantityOrdered * priceEach) AS total
FROM
	orderdetails
GROUP BY
	orderNumber
ORDER BY
	total DESC;

-- 15
SELECT
	year(orderDate) AS 'year', COUNT(orderNumber)
FROM
	orders
GROUP BY
	year;

-- 16
SELECT
	productLine, MAX(quantityInStock)
FROM
	products
GROUP BY
	productLine
HAVING
	MAX(quantityInStock) < 9000;

-- 17
SELECT 
	ordernumber, 
    SUM(quantityOrdered) AS itemsCount, 
    SUM(priceeach * quantityOrdered) AS total
FROM
	orderdetails
GROUP BY
	orderNumber
HAVING
	itemsCount >= 500 and total >= 50000

    
```