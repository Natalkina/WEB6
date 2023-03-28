-- Знайти список студентів у певній групі.
select s."name" , g."name"
from students s
inner join "groups" g  on g.id = s.group_id
where g."name" = 'А-01'