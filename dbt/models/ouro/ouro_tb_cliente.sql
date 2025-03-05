{{ config(materialized='table') }}

select estado, count(1) as quantidade_cliente
from {{ ref('prata_tb_cliente') }}
group by estado
order by 1