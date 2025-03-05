import streamlit as st
import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_data():
    try:
        # Conecta ao banco de dados PostgreSQL
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME")
        )
        cursor = conn.cursor()

        # Executa a query SQL
        cursor.execute("SELECT * FROM public.ouro_tb_cliente")
        rows = cursor.fetchall()

        # Converte os resultados em um DataFrame pandas
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

        # Fecha a conexão
        cursor.close()
        conn.close()

        return df

    except psycopg2.Error as e:
        st.error(f"Erro ao acessar o banco de dados: {e}")
        return None

st.title("Dashboard de Clientes")

st.write("### Dados da camada OURO")
df = get_data()
if df is not None:
    st.dataframe(df)
else:
    st.write("Tabela não encontrada ou erro ao acessar os dados.")