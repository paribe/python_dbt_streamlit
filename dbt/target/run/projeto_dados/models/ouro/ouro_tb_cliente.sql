
  
    

  create  table "banco_dremio_sql"."public"."ouro_tb_cliente__dbt_tmp"
  
  
    as
  
  (
    

select estado, count(1) as quantidade_cliente
from "banco_dremio_sql"."public"."prata_tb_cliente"
group by estado
order by 1
  );
  