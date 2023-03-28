-- Знайти оцінки студентів у окремій групі з певного предмета
select g."name",  s."name", s2."name", r.value
from students s
inner join "groups" g  on g.id = s.group_id
inner join rating r on r.student_id = s.id
inner join subjects s2 on s2.id = r.subject_id
where g."name" = 'А-01' and r.subject_id = 1
order by r.value desc
