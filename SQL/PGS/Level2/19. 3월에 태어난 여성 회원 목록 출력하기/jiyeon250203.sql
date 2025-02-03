-- MEMBER_PROFILE 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회
-- 전화번호가 NULL인 경우는 출력대상에서 제외
-- 결과는 회원ID를 기준으로 오름차순
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE 
WHERE MONTH(DATE_OF_BIRTH) = 03    -- 생일이 3월
    AND GENDER = 'W'   -- 여성 회원
    AND TLNO IS NOT NULL    -- 전화번호가 NULL인 경우 출력 X
ORDER BY MEMBER_ID

