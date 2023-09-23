```sql

-- join
DROP TABLE IF EXISTS users;
 
CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

DROP TABLE articles;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userid INT NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO
	users (name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');

INSERT INTO
	articles (title, content, userId)
VALUES
	('제목1', '내용1', '1'),
    ('제목2', '내용2', '2'),
    ('제목3', '내용3', '4');
    
SELECT articles.id, title, content, name
FROM articles
INNER JOIN users
	ON articles.userId = users.id;
-- SELECT 다음에 id만 사용하면 어떤 테이블의 id인지 모른다.(둘 다 id가 있기 떄문)명시해줘야됨

SELECT productCode, productName, textdescription
FROM products
INNER JOIN productlines
	ON products.productline = productlines.productline;

SELECT orders.orderNumber, status, priceEach
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;

SELECT orders.orderNumber, status, SUM(quantityOrdered * priceEach) AS totalSales
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
GROUP BY
	orderNumber;

SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber;

SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber IS NULL;

-- left, right 모두 from다음에 오는 것이 왼쪽에 위치함
```