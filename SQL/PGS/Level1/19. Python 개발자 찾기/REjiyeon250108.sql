--  Python 스킬을 가진 개발자의 ID, 이메일, 이름, 성을 조회
--  ID를 기준으로 오름차순
/* 
1번째 오답
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE 'Python' IN (SKILL_1 | SKILL_2 | SKILL_3)
ORDER BY 1 ;
*/

```
정답
```
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE 'Python' IN (SKILL_1, SKILL_2, SKILL_3)
ORDER BY ID;


/*
이 정답은, 
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'Python' OR SKILL_2 = 'Python' OR SKILL_3 = 'Python'
ORDER BY ID;

이것과 같음.



1. OR과 IN의 차이점
 - OR: 각각의 조건을 명시적으로 비교
  -- SKILL_1 = 'Python' OR SKILL_2 = 'Python' OR SKILL_3 = 'Python'
 - IN: 값이 리스트 중 하나라도 포함되면 참
  -- 'Python' IN (SKILL_1, SKILL_2, SKILL_3)
 -> 결론: 두 방식 모두 동일한 결과를 반환한다.
 
2. ,(콤마)는 논리 연산자가 아님
 - 콤마(,)는 IN 연산자 안에서 값을 나열할 때만 사용된다.
 - 예)
  -- 'Python' IN (SKILL_1, SKILL_2, SKILL_3) → 맞음
  -- 'Python' = SKILL_1, SKILL_2, SKILL_3 → 틀림 (문법 오류)
3. | 연산자는 SQL에서 지원되지 않음
 - `

*/