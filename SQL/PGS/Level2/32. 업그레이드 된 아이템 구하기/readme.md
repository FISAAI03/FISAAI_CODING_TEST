# [업그레이드 된 아이템 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/273711)


###### 문제 설명


어느 한 게임에서 사용되는 아이템들은 업그레이드가 가능합니다.  

'ITEM\_A'\-\>'ITEM\_B'와 같이 업그레이드가 가능할 때   

'ITEM\_A'를 'ITEM\_B' 의 PARENT 아이템,  

 PARENT 아이템이 없는 아이템을 ROOT 아이템이라고 합니다.


예를 들어 'ITEM\_A'\-\>'ITEM\_B'\-\>'ITEM\_C'와 같이 업그레이드가 가능한 아이템이 있다면  

'ITEM\_C'의 PARENT 아이템은 'ITEM\_B'  

'ITEM\_B'의 PARENT 아이템은 'ITEM\_A'  

ROOT 아이템은 'ITEM\_A'가 됩니다.


다음은 해당 게임에서 사용되는 아이템 정보를 담은 `ITEM_INFO` 테이블과 아이템 관계를 나타낸 `ITEM_TREE` 테이블입니다. `ITEM_INFO` 테이블은 다음과 같으며, `ITEM_ID`, `ITEM_NAME`, `RARITY`, `PRICE`는 각각 아이템 ID, 아이템 명, 아이템의 희귀도, 아이템의 가격을 나타냅니다.




| Column name | Type | Nullable |
| --- | --- | --- |
| ITEM\_ID | INTEGER | FALSE |
| ITEM\_NAME | VARCHAR(N) | FALSE |
| RARITY | INTEGER | FALSE |
| PRICE | INTEGER | FALSE |


`ITEM_TREE` 테이블은 다음과 같으며, `ITEM_ID`, `PARENT_ITEM_ID`는 각각 아이템 ID, PARENT 아이템의 ID를 나타냅니다.




| Column name | Type | Nullable |
| --- | --- | --- |
| ITEM\_ID | INTEGER | FALSE |
| PARENT\_ITEM\_ID | INTEGER | TRUE |


단, 각 아이템들은 오직 하나의 PARENT 아이템 ID를 가지며, ROOT 아이템의 PARENT 아이템 ID는 NULL 입니다.


ROOT 아이템이 없는 경우는 존재하지 않습니다.




---


##### 문제


아이템의 희귀도가 'RARE'인 아이템들의 모든 다음 업그레이드 아이템의 아이템 ID(ITEM\_ID), 아이템 명(ITEM\_NAME), 아이템의 희귀도(RARITY)를 출력하는 SQL 문을 작성해 주세요. 이때 결과는 아이템 ID를 기준으로 내림차순 정렬주세요.




---


##### 예시


예를 들어 `ITEM_INFO` 테이블이 다음과 같고




| ITEM\_ID | ITEM\_NAME | RARITY | PRICE |
| --- | --- | --- | --- |
| 0 | ITEM\_A | RARE | 10000 |
| 1 | ITEM\_B | RARE | 9000 |
| 2 | ITEM\_C | LEGEND | 11000 |
| 3 | ITEM\_D | RARE | 10000 |
| 4 | ITEM\_E | RARE | 12000 |


`ITEM_TREE` 테이블이 다음과 같다면




| ITEM\_ID | PARENT\_ITEM\_ID |
| --- | --- |
| 0 | NULL |
| 1 | 0 |
| 2 | 0 |
| 3 | 1 |
| 4 | 1 |


아이템의 희귀도가 'RARE'인 아이템은 'ITEM\_A', 'ITEM\_B', 'ITEM\_D', 'ITEM\_E' 입니다.   

이 중 'ITEM\_A' 는 'ITEM\_B', 'ITEM\_C' 로 업그레이드가 가능하며 'ITEM\_B' 는 'ITEM\_D' , 'ITEM\_E' 로 업그레이드가 가능합니다. 'ITEM\_D' 와 'ITEM\_E'는 더 이상 업그레이드가 가능하지 않습니다. 따라서 결과는 다음과 같이 나와야 합니다.




| ITEM\_ID | ITEM\_NAME | RARITY |
| --- | --- | --- |
| 4 | ITEM\_E | RARE |
| 3 | ITEM\_D | RARE |
| 2 | ITEM\_C | LEGEND |
| 1 | ITEM\_B | RARE |




---


※ 참고: 본 문제는 제출 내역 확인 기능을 지원하지 않습니다.



