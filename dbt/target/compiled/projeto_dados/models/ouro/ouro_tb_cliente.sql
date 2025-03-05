

select estado, count(1) as quantidade_cliente
from "banco_dremio_sql"."public"."prata_tb_cliente"
group by estado
order by 1