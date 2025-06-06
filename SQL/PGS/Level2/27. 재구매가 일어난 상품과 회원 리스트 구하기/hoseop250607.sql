select *
from online_sale A, online_sale B
where A.user_id = B.user_id and A.product_id = B.product_id