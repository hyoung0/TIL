# SQL basic

## SQL

- Structure Query Language : 테이블 형태로 `구조화`된 관계형 데이터베이스에 정보 `질의(요청)`하는 언어

- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

### SQL Syntax
- 구글에 'how old is earth'라고 검색하는 것 처럼 SQL에서 다음과 같이 작성
  ```sql
  SELECT column_name FROM table_name;
  ```

- SQL 키워드는 대소문자를 구분하지 않으나 가독성을 위해 대문자로 작성

- 각 SQL statements의 끝에 세미콜론(;)으로 표시(각각의 statements 구분)

<br>

### SQL Statements
데이터베이스에서 수행 목적에 따라 대체로 4가지 범주로 나뉨

|             유형              |            역할             |       SQL 키워드     |
|-------------------------------|----------------------------|----------------------|
|DDL(Data Definition Language)  |데이터의 기본구조 및 형식 변경| CREATE, DROP, ALTER, RENAME  |
|DQL(Data Query Language)       |         데이터 검색         |       SELECT         |
|DML(Data Manipulation Language)|데이터 조작(추가, 수정, 삭제) |INSERT, UPDATE, DELETE|
|DCL(Data Control Language)     |데이터 및 작업에 대한 사용자권한 제어|COMMIT, ROLLBACK, GRANT, REVOKE|



