-- 평균 대여 기간이 7일 이상인 자동차들의 자동차 ID와 평균 대여 기간(컬럼명: AVERAGE_DURATION) 리스트를 출력
-- 평균 대여 기간은 소수점 두번째 자리에서 반올림
SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY 2 DESC, CAR_ID DESC
--  평균 대여 기간을 기준으로 내림차순, 평균 대여 기간이 같으면 자동차 ID를 기준으로 내림차순


/* TIMESTAMPDIFF('결과값 형식','날짜1','날짜2')
- 내부의 계산은 위의 함수들과 반대로, 날짜 2 - 날짜 1로 진행
- 결괏값 형식: (SECOND: 초, WEEK: 주, MINUTE: 분, MONTH: 월, HOUR: 시, QUARTER: 분기, DAY: 일, YEAR: 년도)
*/