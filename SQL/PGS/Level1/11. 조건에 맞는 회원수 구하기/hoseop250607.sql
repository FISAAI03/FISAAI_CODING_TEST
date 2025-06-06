SELECT count(user_id) as USERS
from user_info
where 20 <= age and age <= 29 and year(joined)=2021