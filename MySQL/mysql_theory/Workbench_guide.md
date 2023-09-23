## Workbench 활용 MySQL 접속 방법  

1. sample database 다운로드
2. MySQL 접속
3. Local instance 클릭
4. Administration → Data Import/Restore
5. Import from Self-Contained File 체크 → . 클릭 → 다운로드 받은 sample_db.sql 파일 선택
→ Start Import
6. Import Completed 확인  

## 실습용 데이터 베이스 확인
1. Schemas 클릭 (Windows는 하단에 있음)
→ 새로고침 버튼 클릭
→ 데이터베이스 classicmodels 확인

## 쿼리(Query) 실행 테스트
1. `classicmodels` 데이터베이스 선택(더블 클릭)
2. Query 에디터 클릭
3. 쿼리문 입력 
    
    ```sql
    SELECT * FROM customers;
    ```
    
4. 쿼리 실행
5. Action Output 초록체크 확인, 출력 확인
