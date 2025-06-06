SELECT book.author_id, author_name, category, sum(sales*price) as TOTAL_SALES
from book, author, book_sales
where book.book_id = book_sales.book_id and book.author_id = author.author_id
and date_format(sales_date, '%Y-%m') = '2022-01'
group by author_id, category
order by book.author_id, category desc