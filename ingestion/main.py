import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Carregar variáveis do ambiente
load_dotenv()

# Configuração do banco de dados
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_SCHEMA = os.getenv("DB_SCHEMA", "public")

# Caminho do arquivo CSV
csv_path = "ingestion/data/cliente.csv"
print("Teste")
try:
    # Conectar ao PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        dbname=DB_NAME
    )
    print("✅ Conexão com o banco de dados estabelecida!")

    # Ler o CSV
    df = pd.read_csv(csv_path)

    # Inserir os dados na tabela tb_cliente
    with conn.cursor() as cursor:
        for _, row in df.iterrows():
            cursor.execute(
                f"""
                INSERT INTO {DB_SCHEMA}.tb_cliente (id_cliente, nm_cliente, vl_limite, estado)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id_cliente) DO NOTHING
                """,
                (row["id_cliente"], row["nm_cliente"], row["vl_limite"], row["estado"])
            )

    # Confirmar a transação e fechar conexão
    conn.commit()
    print("✅ Dados inseridos com sucesso no banco!")

except psycopg2.Error as e:
    print(f"❌ Erro no banco de dados: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("🔌 Conexão com o banco fechada.")
