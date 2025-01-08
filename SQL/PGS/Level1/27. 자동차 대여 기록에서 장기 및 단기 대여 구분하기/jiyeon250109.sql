-- 대여 시작일이 2022년 9월에 속하는 대여 기록에 대해서 대여 기간이 30일 이상이면 '장기 대여' 
-- 그렇지 않으면 '단기 대여' 로 표시하는 컬럼(컬럼명: RENT_TYPE)을 추가하여 대여기록을 출력
-- 결과는 대여 기록 ID를 기준으로 내림차순 정렬

SELECT HISTORY_ID, CAR_ID, 
    DATE_FORMAT(START_DATE,'%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE,'%Y-%m-%d') AS END_DATE,
    CASE WHEN DATEDIFF(END_DATE, START_DATE) >= 29 THEN '장기 대여'
    ELSE '단기 대여' END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09%'
ORDER BY HISTORY_ID DESC

/* 30이상이라고 했을 때, 
DATEDIFF 함수는 시작일과 종료일 사이의 **간격(일수)**만 계산한다.
실제 대여 기간은 시작일과 종료일을 포함해야 하므로, 차이 + 1일을 고려해야 한다.
이 때문에, 30일 이상을 판별하기 위해 SQL에서는 **DATEDIFF >= 29**로 조건을 설정한다. 
*/
