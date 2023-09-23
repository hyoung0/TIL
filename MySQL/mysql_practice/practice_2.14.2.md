```sql
SELECT * FROM posts;
SHOW COLUMNS FROM posts;

-- 1
CREATE TABLE posts (
	postld INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    PRIMARY KEY (postld)
);

-- 2
ALTER TABLE
	posts
ADD writer VARCHAR(100) NULL DEFAULT 'Anonymous',
ADD created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP;
-- 파란색으로 뜨면 함수나 명령어이고 검정색으로 뜨면 ''고민해봐야됨'

-- 3
ALTER TABLE
	posts
MODIFY
	content TEXT NULL;
    
-- 4
ALTER TABLE
	posts
DROP COLUMN 
	writer;
    
-- 5
DROP TABLE posts;

-- 6
CREATE TABLE IF NOT EXISTS posts (
	postld INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    writer VARCHAR(20) NOT NULL,
    created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (postld)
);

-- 7
DROP TABLE IF EXISTS posts;

```