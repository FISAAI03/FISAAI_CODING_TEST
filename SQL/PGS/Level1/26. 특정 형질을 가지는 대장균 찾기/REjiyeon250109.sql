SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0 
AND ((GENOTYPE & 1) > 0 OR (GENOTYPE & 4) > 0);

/* 비트연산자 연습 더 필요 대장균 관련 연습 예제 더 풀어보기. */
