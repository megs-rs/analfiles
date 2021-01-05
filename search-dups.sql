select *
from (
select data, tamanho, md5sum, count(*) as total 
from arquivos 
group by data, tamanho, md5sum 
) a
where a.total > 1
order by total desc, tamanho desc