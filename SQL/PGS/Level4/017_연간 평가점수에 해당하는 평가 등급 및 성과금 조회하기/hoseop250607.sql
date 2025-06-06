SELECT E.EMP_NO, EMP_NAME, (CASE WHEN AVG(SCORE) >= 96 THEN 'S'
                                WHEN AVG(SCORE) >= 90 THEN 'A'
                                WHEN AVG(SCORE) >= 80 THEN 'B'
                                ELSE 'C'
                                END) GRADE,
                            (CASE WHEN AVG(SCORE) >= 96 THEN SAL*0.2
                                WHEN AVG(SCORE) >= 90 THEN SAL*0.15
                                WHEN AVG(SCORE) >= 80 THEN SAL*0.1
                                ELSE 0 
                                END) BONUS
FROM HR_GRADE G, HR_EMPLOYEES E
WHERE G.EMP_NO=E.EMP_NO
GROUP BY E.EMP_NO
ORDER BY E.EMP_NO