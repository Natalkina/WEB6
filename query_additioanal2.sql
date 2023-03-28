-- Оцінки студентів у певній групі з певного предмета на останньому занятті.
select g."name",  s."name",  s2."name", r.value, r.date_of
from  students s
inner join rating r on r.student_id  = s.id
inner join subjects s2 on s2.id = r.subject_id
inner join "groups" g on g.id = s.group_id
where g.id = 2 and r.subject_id = 2 and
r.date_of = (select max(r2.date_of) from rating r2 where g.id = 2 and r2.subject_id = 2)
