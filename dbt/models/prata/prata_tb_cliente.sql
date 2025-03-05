{{ config(materialized='table') }}

SELECT
    *
FROM {{ ref('bronze_tb_cliente') }}