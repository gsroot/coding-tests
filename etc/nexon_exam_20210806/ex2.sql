select b.name name, count(a.id) cnt
from EMPLOYEE a right join DEPARTMENT b on a.DEPT_ID = b.ID
group by b.name
order by cnt desc, name asc