--Знайти список курсів, які відвідує студент.
select distinct  s."name", s2."name"
from  students s
inner join rating r on r.student_id  = s.id
inner join subjects s2 on s2.id = r.subject_id
order by s."name"
