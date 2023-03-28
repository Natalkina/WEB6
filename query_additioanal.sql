-- Середній бал, який певний викладач ставить певному студентові.
select  s."name", t."name", avg(r.value)
from  students s
inner join rating r on r.student_id  = s.id
inner join subjects s2 on s2.id = r.subject_id
inner join teachers t on t.id = s2.teacher_id
where t.id = 1 and s.id  = 2
group by  t."name", s."name"