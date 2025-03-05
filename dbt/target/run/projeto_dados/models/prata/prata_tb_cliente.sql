
  
    

  create  table "banco_dremio_sql"."public"."prata_tb_cliente__dbt_tmp"
  
  
    as
  
  (
    

SELECT
    *
FROM "banco_dremio_sql"."public"."bronze_tb_cliente"
  );
  