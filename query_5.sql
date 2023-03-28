--Знайти які курси читає певний викладач.
select s."name" , t."name"
from subjects s
inner join teachers t on s.teacher_id =t.id