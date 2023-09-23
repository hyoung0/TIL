```sql
DROP TABLE users;

SET autocommit = 0;  -- 자동 COMIT 비활성화

-- ussers 테이블 생성
CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);

START TRANSACTION;

INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;

-- ROLLBACK;
COMMIT;



-- TRIGER
DROP TABLE articles;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createAt DATETIME NOT NULL,
    updateAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO articles (title1, createAt, updateAt)
VALUES ('title', CURRENT_TIME(), CURRENT_TIME);

SELECT * FROM articles;

DELIMITER //  
 -- 여기서부터 종료조건은 이제 '//'이다. BEGIN-END사이에 여러 SQL문이 들어갈 수 있기 때문.
CREATE TRIGGER myTrigger
	-- 언제?? 전이다.commit이 되기 전에 수정이 되어 올라가야됨. commit된 후에 수정이되면 수정된 값이 안 올라감.
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
	-- 전의 필드인지 후의 필드인지 정해줘야됨.이 경우 새로운 updatedAt에 넣어줘야함
    SET NEW.updatedAt = CURRENT_TIME(); 
END//
DELIMITER; 
-- 여기서부터는 다시 ; 으로 변경

DELIMITER //
CREATE TRIGGER
	BEFORE DELETE
    ON arricles FOR EACH ROW
BEGIN
	INSERT INTO 
    VALUES (OLD.id, OLD.
END//
DELIMITER

```

<br>

```sql

-- 1
SELECT * FROM products; -- msrp짤림

SELECT productCode , productName , MSRP 
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products
)
ORDER BY
	MSRP;

-- 2
SELECT * FROM customers;
SELECT * FROM orders;

SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
	FROM orders
	WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-27'  -- 날짜는 하루 더 해줘야됨
)
ORDER BY
	customerNumber;

-- 3
SELECT * FROM productlines;
SELECT * FROM products;

SELECT productCode , productName , productLine , MSRP
FROM products
WHERE productLine = 'Classic Cars' AND
	MSRP = (
    SELECT MAX(MSRP)
    FROM products
    );
    
-- 4
SELECT customerNumber , customerName , country 
FROM customers
WHERE country = (
	SELECT MAX(country)
    FROM customers
)
ORDER BY
	customerNumber;

-- 5
-- customerNumber로 그룹하고 count 
SELECT customerNumber , customerName , COUNT(customerNumber) AS order_count
FROM (
	SELECT *
    FROM customers
    INNER JOIN orders USING (customerNumber)
) AS sub
GROUP BY
	customerNumber
HAVING
	order_count = 26;   -- 이거 26 직접 안 치고 어떻게 하나??
    
-- 6
SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM orderdetails;

SELECT productCode , productName
FROM orderdetails
INNER JOIN orders USING (orderNumber)
INNER JOIN products USING (productCode)
WHERE year(orderDate) = '2004'
ORDER BY productCode DESC;

SELECT DISTINCT productCode , productName
FROM (
	SELECT *
    FROM orderdetails
	INNER JOIN orders USING (orderNumber)
	INNER JOIN products USING (productCode)
) AS sub
WHERE year(orderDate) = '2004'
ORDER BY productCode DESC;
```