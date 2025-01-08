-- 가장 큰 물고기 10마리의 ID와 길이를 출력
-- 길이를 기준으로 내림차순 정렬하고, 길이가 같다면 물고기의 ID에 대해 오름차순 정렬
-- 가장 큰 물고기 10마리 중 길이가 10cm 이하인 경우는 없습니다.
-- 컬럼명 조건: ID 컬럼명은 ID, 길이 컬럼명은 LENGTH

SELECT ID, LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID
LIMIT 10
