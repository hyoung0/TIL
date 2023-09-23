```sql
CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL,
    PRIMARY KEY (id)
);

SHOW COLUMNS FROM articles;

SELECT * FROM articles;

INSERT INTO
	articles (title, content, createdAt)
VALUES 
	('hello', 'world', '2000-01-01');
-- pk값은 자동으로 지정될것이므로 안 써도 됨

INSERT INTO
	articles (title, content, createdAt)
VALUES 
	('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');

INSERT INTO
	articles (title, content, createdAt)
VALUES 
	('mytitle', 'mycontent', CURDATE());

UPDATE 
	articles
SET 
	title = 'newTitle'
WHERE
	id = 1;
-- WHERE절을 사용하지 않으면, title필드의 모든 값이 newTitle이 됨

UPDATE
	articles
SET
	title = 'hahah',
    content = 'hoho'
WHERE
	id = 2;

UPDATE
	articles
SET
	content = REPLACE(content, 'content', 'TEST');
-- safe 모드라서 안된다고 뜬다

SET SQL_SAFE_UPDATES = 0;
-- safe 모드 풀기

DELETE FROM
	articles
WHERE 
	id = 1;

DELETE FROM
	articles
ORDER BY
	createdAt DESC
LIMIT 2;

```