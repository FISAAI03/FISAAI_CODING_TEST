SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%el%" AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME;

-- mysql에서는 대소문자 구분을 별도로 하지 않는다.
-- 하지만 만약 대소문자를 구분해야 할 경우에는 BINARY를 사용한다. ex) WHERE NAME LIKE BINARY "%el%" AND ANIMAL_TYPE = 'Dog'