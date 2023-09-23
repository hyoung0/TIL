```sql
CREATE TABLE examples (
	examId INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    fistName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examId)
);

SHOW COLUMNS FROM examples;

ALTER TABLE
	examples
ADD
	country VARCHAR(100) NOT NULL;
    
ALTER TABLE 
	examples
ADD age INT NOT NULL,
ADD address VARCHAR(100) NOT NULL;
-- ADD는 쓸 때마다 ADD해야됨

ALTER TABLE
	examples
MODIFY
	address VARCHAR(50) NOT NULL; 
    -- NOT NULL이 사라져버리므로 다시 써줘야됨

ALTER TABLE
	examples
MODIFY lastName VARCHAR(10) NOT NULL,
MODIFY fistName VARCHAR(10) NOT NULL;

ALTER TABLE
	examples
CHANGE COLUMN
	country state VARCHAR(100) NOT NULL;
    -- CHANGE COLUMN은 MODIFY의 기능까지 함.

ALTER TABLE
	examples
DROP COLUMN
	address;
    
ALTER TABLE
	examples
DROP COLUMN state,
DROP COLUMN age;

```