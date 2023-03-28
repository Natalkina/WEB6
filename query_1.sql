--Знайти 5 студентів із найбільшим середнім балом з усіх предметів

select r.student_id, s."name", sum(r.value)
from students as s
join rating as r
on s.id = r.student_id
group by r.student_id, s."name"
order by sum(r.value) desc
limit 5