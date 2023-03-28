-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
select t."name", avg(r.value)
from  teachers t
inner join subjects s on s.teacher_id = t.id
inner join rating r on r.subject_id  = s.id
group by t."name"
order by avg(r.value) desc
