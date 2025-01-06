-- 경기도에 위치한 창고의 ID, 이름, 주소, 냉동시설 여부를 조회
-- 냉동시설 여부가 NULL인 경우, 'N'으로 출력시켜 주시고 결과는 창고 ID를 기준으로 오름차순
`SOL 1`

SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
CASE WHEN FREEZER_YN IS NULL THEN 'N'
    WHEN FREEZER_YN = 'N' THEN 'N'
    ELSE 'Y'
    END AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID


`SOL2`
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N')
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC;
