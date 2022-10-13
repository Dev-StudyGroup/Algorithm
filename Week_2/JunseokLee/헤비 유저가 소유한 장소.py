select p.id, p.name, p.host_id
from places p
where p.host_id in (select p.host_id
from places p
group by p.host_id
having count(p.host_id)>=2)
order by p.id