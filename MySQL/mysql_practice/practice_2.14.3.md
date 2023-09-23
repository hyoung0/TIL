```sql
DROP TABLE users;
SELECT * FROM users;
SHOW COLUMNS FROM users;


-- 1
CREATE TABLE users (
	userld INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,	
	birthday DATE NOT NULL,	
	city VARCHAR(100) NULL,
	country	VARCHAR(100) NULL,	
	email VARCHAR(100) NULL,	
	created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (userld)
);

-- 2
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES 
	('Beemo', 'Jeong', '1000-01-01',NULL, NULL,'beemo@hphk.kr'),
	('Jieun', 'Lee', '1993-05-16', 'Seoul',	'Korea', NULL),	
	('Dami', 'Kim',	'1995-04-09', 'Seoul', 'Korea',NULL),	
	('Kwangsoo', 'Lee',	'1985-07-14', 'Seoul', 'Korea',NULL);
    
-- INSERT INTO
-- 	users (first_name, last_name, birthday, city, country, email)
-- VALUES 
-- 	('Beemo', 'Jeong', '1000-01-01','', '','beemo@hphk.kr'),
-- 	('Jieun', 'Lee', '1993-05-16', 'Seoul',	'Korea', ''),	
-- 	('Dami', 'Kim',	'1995-04-09', 'Seoul', 'Korea',''),	
-- 	('Kwangsoo', 'Lee',	'1985-07-14', 'Seoul', 'Korea', '');

-- 3
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES 
	('HA', 'Jeong', '1000-01-01','','','beemo@hphk.kr'),
	('HAH', 'Lee', '1993-05-16', 'Seoul',	'Korea', ''),	
	('HAHA', 'Kim',	'1995-04-09', 'Seoul', 'Korea',''),	
	('HAHAH', 'Lee',	'1985-07-14', 'Seoul', 'Korea',''),
    ('HAHAHA', 'Lee',	'1985-07-14', 'Seoul', 'Korea','');

-- 4
UPDATE 
	users
SET 
	first_name = '현영',
    last_name = '조',
    birthday = '1999-09-28'
WHERE 
	userld = 2;

-- 5 ---------------------------------------------------------
UPDATE 
	users
SET
	country = 'korea'
WHERE
	country IS NULL;

-- 6
DELETE FROM users
WHERE 
	first_name = 'Beemo';

-- 7
DELETE FROM users
WHERE 
	first_name = 'Kwangsoo' OR last_name = 'Lee';

-- 8
DELETE FROM users
ORDER BY
	created_at DESC
LIMIT 1;
	
```