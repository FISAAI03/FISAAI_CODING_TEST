-- 2022년도 한해 평가 점수가 가장 높은 사원 정보 조회
-- 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회

SELECT SUM(SCORE) AS SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
    FROM HR_EMPLOYEES E
    JOIN HR_GRADE G
      ON E.EMP_NO = G.EMP_NO
    GROUP BY E.EMP_NO
    ORDER BY 1 DESC
    LIMIT 1


-- HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블에서 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회
-- [SELECT]2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회
-- 2022년도의 평가 점수는 상,하반기 점수의 합, 평가 점수를 나타내는 컬럼의 이름은 SCORE
SELECT G.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E
LEFT JOIN 
    (SELECT EMP_NO, SUM(SCORE) AS SCORE
    FROM HR_GRADE
    WHERE YEAR = '2022'
    GROUP BY EMP_NO) G
     -- 사번 별 평가 점수 환산 테이블
    ON E.EMP_NO = G.EMP_NO
ORDER BY G.SCORE DESC
LIMIT 1