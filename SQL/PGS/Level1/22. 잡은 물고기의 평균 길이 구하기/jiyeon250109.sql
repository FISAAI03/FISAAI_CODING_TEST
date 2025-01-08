-- 잡은 물고기의 평균 길이를 출력, 컬럼 명은 AVERAGE_LENGTH
-- 평균 길이는 소수점 3째자리에서 반올림하며, 10cm 이하의 물고기들은 10cm 로 취급하여 평균 길이
-- -- 평균길이는 그냥 구하고, 10CM 이하만, NULL을 10으로 취급하라.
SELECT ROUND(AVG(B.LENGTH), 2) AS AVERAGE_LENGTH
FROM (SELECT I.ID, I.FISH_TYPE, IFNULL(I.LENGTH, 10) AS LENGTH FROM FISH_INFO I) B

/* 서브쿼리 뒤에 alias 붙이는것 명심 */
