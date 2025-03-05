import pandas as pd
import random

# Definição da quantidade de registros (pode ser alterada facilmente)
NUM_REGISTROS = 30  # Altere este valor para 10, 20, 15, etc.

# Lista de estados brasileiros
estados = ["SP", "RJ", "MG", "RS", "SC", "PR", "BA", "PE", "CE", "GO"]

# Gerar dados aleatórios
data = {
    "id_cliente": list(range(1, NUM_REGISTROS + 1)),
    "nm_cliente": [f"Cliente {i}" for i in range(1, NUM_REGISTROS + 1)],
    "vl_limite": [round(random.uniform(500, 5000), 2) for _ in range(NUM_REGISTROS)],
    "estado": [random.choice(estados) for _ in range(NUM_REGISTROS)]
}

# Criar DataFrame e salvar como CSV
df = pd.DataFrame(data)
df.to_csv("ingestion/data/cliente.csv", index=False)

print(f"✅ Arquivo cliente.csv gerado com {NUM_REGISTROS} registros!")
