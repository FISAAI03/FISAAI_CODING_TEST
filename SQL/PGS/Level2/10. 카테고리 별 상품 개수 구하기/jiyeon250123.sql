-- 상품 카테고리 코드(PRODUCT_CODE 앞 2자리) 별 상품 개수를 출력
--  상품 카테고리 코드를 기준으로 오름차순 정렬
SELECT LEFT(PRODUCT_CODE,2) AS CATEGORY, COUNT(LEFT(PRODUCT_CODE,2)) AS PRODUCTS
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE, 2)

/* SQL 슬라이싱 
SQL에서 문자열 슬라이싱(문자열 자르기) 요약 및 예시:

1. **`SUBSTRING` 또는 `SUBSTR`**
   - 문자열의 특정 위치에서 원하는 길이만큼 자름.
   - 문법: `SUBSTRING(문자열, 시작위치, 길이)`

   예시:
   ```sql
   SELECT SUBSTRING('Hello, World!', 1, 5);
   -- 결과: 'Hello'

   SELECT SUBSTRING('Hello, World!', 8, 5);
   -- 결과: 'World'
   ```

2. **`LEFT`**
   - 문자열의 왼쪽에서 n글자를 잘라냄.
   - 문법: `LEFT(문자열, 길이)`

   예시:
   ```sql
   SELECT LEFT('Hello, World!', 5);
   -- 결과: 'Hello'
   ```

3. **`RIGHT`**
   - 문자열의 오른쪽에서 n글자를 잘라냄.
   - 문법: `RIGHT(문자열, 길이)`

   예시:
   ```sql
   SELECT RIGHT('Hello, World!', 6);
   -- 결과: 'World!'
   ```

4. **`CHARINDEX` 또는 `POSITION`**
   - 특정 문자열의 위치를 찾음. `SUBSTRING`과 조합 가능.
   - SQL Server: `CHARINDEX(찾을문자열, 원본문자열)`
   - MySQL/PostgreSQL: `POSITION(찾을문자열 IN 원본문자열)`

   예시:
   ```sql
   SELECT CHARINDEX(',', 'Hello, World!');
   -- 결과: 6

   -- CHARINDEX와 SUBSTRING을 조합
   SELECT SUBSTRING('Hello, World!', CHARINDEX(',', 'Hello, World!') + 2, 5);
   -- 결과: 'World'
   ```

5. **`TRIM`**
   - 문자열의 앞뒤 공백 또는 특정 문자를 제거.
   - 문법: `TRIM(문자열)` 또는 `TRIM(특정문자 FROM 문자열)`

   예시:
   ```sql
   SELECT TRIM('   Hello, World!   ');
   -- 결과: 'Hello, World!'

   SELECT TRIM('!' FROM '!Hello, World!!!');
   -- 결과: 'Hello, World'
 
*/