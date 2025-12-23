# Write your MySQL query statement below
select emu.unique_id as unique_id , e.name as name #select which i have to print
from employees e 
left join employeeuni emu #left join beacause need to print all left table value
on e.id = emu.id #left join condition