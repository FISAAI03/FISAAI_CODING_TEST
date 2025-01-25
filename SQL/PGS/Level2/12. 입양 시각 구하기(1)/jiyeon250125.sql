-- 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회
-- 결과는 시간대 순으로 정렬
SELECT DATE_FORMAT(DATETIME, '%H') as hour, count(*) as count
FROM ANIMAL_OUTS
WHERE  DATE_FORMAT(DATETIME, '%H') BETWEEN 09 AND 19
GROUP BY DATE_FORMAT(DATETIME, '%H')
ORDER BY DATE_FORMAT(DATETIME, '%H')

/* 
SELECT - FROM - WHERE - GROUP BY - HAVING - ORDER BY 
GROUP BY는 집계 빼고는 모두 사용 가능
*/