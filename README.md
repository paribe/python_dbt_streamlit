# **Passo 1: Criando o ambiente com Poetry**

### 📌 **Instalar o Poetry**
```sh
pip install poetry
```

### 📌 **Criar o projeto**
```sh
poetry new projeto_dados
cd projeto_dados
```

### 📌 **Adicionar dependências**
```sh
poetry add pandas duckdb dbt-core dbt-postgres streamlit python-dotenv
```

---

# **Passo 2: Criar os arquivos do projeto**

## 📂 **1. Criar os dados de entrada (data/cliente.csv)**
### `data/cliente.csv`
```csv
id,nome,limite,compra_do_mes,valor,cidade
1,Ana Silva,5000,3,1200.50,São Paulo
2,Carlos Souza,3000,2,800.00,Rio de Janeiro
3,Mariana Lima,7000,5,1500.75,Belo Horizonte
4,Roberto Alves,2500,1,600.00,Salvador
5,Juliana Mendes,4500,4,900.30,Curitiba
```

---

## 📂 **2. Criar a modelagem dbt**

### 📂 `dbt/models/bronze/bronze_tb_cliente.sql`
```sql
{{ config(materialized='table') }}

SELECT *
FROM read_csv_auto('data/cliente.csv', HEADER=True)
```

---

### 📂 `dbt/models/prata/prata_tb_cliente.sql`
```sql
{{ config(materialized='table') }}

SELECT
    id,
    nome,
    limite,
    compra_do_mes,
    valor,
    cidade,
    CURRENT_TIMESTAMP AS data_processamento
FROM {{ ref('bronze_tb_cliente') }}
```

---

### 📂 `dbt/models/ouro/ouro_tb_cliente.sql`
```sql
{{ config(materialized='table') }}

SELECT
    nome,
    cidade,
    SUM(valor) AS total_gasto
FROM {{ ref('prata_tb_cliente') }}
GROUP BY nome, cidade
```

---

### 📂 `dbt/profiles.yml`
```yaml
default:
  outputs:
    dev:
      type: postgres
      host: {{ env_var('DB_HOST') }}
      user: {{ env_var('DB_USER') }}
      password: {{ env_var('DB_PASSWORD') }}
      port: {{ env_var('DB_PORT') | int }}
      dbname: {{ env_var('DB_NAME') }}
      schema: {{ env_var('DB_SCHEMA') }}
  target: dev
```

---

### 📂 `.env`
```ini
DB_HOST=dpg-cv2rncij1k6c739ofhag-a.oregon-postgres.render.com
DB_USER=banco_dremio_sql_user
DB_PASSWORD=L9py97LBW21AmTKu9C2LwbwIS2ajrPkZ
DB_PORT=5432
DB_NAME=banco_dremio_sql
DB_SCHEMA=public
```

---

## 📂 **3. Criar o Streamlit para visualização dos dados**
### `web/app.py`
```python
import streamlit as st
import duckdb
import pandas as pd

db_path = 'clientes.duckdb'

def get_data():
    con = duckdb.connect(db_path)
    query = "SELECT * FROM ouro_tb_cliente"
    df = con.execute(query).fetch_df()
    con.close()
    return df

st.title("Dashboard de Clientes")

st.write("### 📊 Dados da camada OURO")
df = get_data()
st.dataframe(df)
```

---

# **Passo 3: Rodar o projeto**

### 📌 **Rodar o dbt para processar os dados**
```sh
dbt run
```

### 📌 **Rodar a aplicação Streamlit**
```sh
streamlit run web/app.py
```

Agora, seu projeto está pronto! 🚀
