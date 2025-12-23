# Write your MySQL query statement below
select v.customer_id, count(customer_id) as count_no_trans #count function used to count num
from visits v
left join transactions t
on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id 
##Whenever we use aggregate function like here count, we have to use group by
