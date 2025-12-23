# Write your MySQL query statement below
select distinct author_id as id #distinct for unique and as keyword for rename
from views 
where author_id = viewer_id 
order by id  #print in ascending order