SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, round(avg(REVIEW_SCORE),2) as SCORE
from rest_info A, rest_review B
where A.rest_id = B.rest_id and A.address like '서울%'
group by A.rest_id
order by SCORE desc, A.favorites desc