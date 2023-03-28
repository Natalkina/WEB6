-- Знайти середній бал у групах з певного предмета

select g."name", avg(r.value)
from students as s
inner join rating as r  on s.id = r.student_id
inner join "groups" as g on g.id = s.group_id
group by g.id
order by g.id