-- Список курсів, які певному студенту читає певний викладач
select distinct  s."name", s2."name", t."name"
from  students s
inner join rating r on r.student_id  = s.id
inner join subjects s2 on s2.id = r.subject_id
inner join teachers t on t.id = s2.teacher_id
where t.id = 1 and s.id  = 2
order by s."name"