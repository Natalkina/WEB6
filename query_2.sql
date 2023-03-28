--Знайти студента із найвищим середнім балом з певного предмета
select r.student_id, s."name", r.value
from students as s
inner join rating as r  on s.id = r.student_id
where
	r.subject_id = 2 and
	r.value = (select max(r2.value) from rating r2 where r2.subject_id = 2)
order by r.student_id