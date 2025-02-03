-- 만원 단위의 가격대 별로 상품 개수를 출력
-- 컬럼명은 각각 컬럼명은 PRODUCT, PRODUCTS로 지정
-- 가격대 정보는 각 구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시
-- 결과는 가격대를 기준으로 오름차순 정렬

# -- 1만원: FLOOR(A_PRICE % 10000) * 10000
# -- 2만원: FLOOR(B_PRICE % 10000) * 10000


SELECT FLOOR(PRICE / 10000) * 10000 AS PRICE_GROUP
        -- FLOOR으로 만원 이하의 단위를 절삭하여 그룹화 할 수 잇도록 함
    , COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP

/* GROUP BY에 SELECT 절에서 계산이 완료된 컬럼을 사용할 수 있음.
-- SQL의 실행 순서는 "FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY"이지만,
편의상, SELECT에서 정의된 "계산식"을 GROUP BY에서도 사용 가능하도록 최적화되어 있음. 따라서 그냥 사용하던지 OR 똑같이 "FLOOR(PRICE / 10000) * 10000" 처럼 계산식을 사용해도 됨.
*/
