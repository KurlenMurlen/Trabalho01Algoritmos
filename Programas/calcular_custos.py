import os
import pandas as pd
from tabulate import tabulate

RESULTADOS_DIR = "resultados"
CUSTO_POR_APOSTA = 3.00

ARQUIVOS = {
    "SB15_14": os.path.join(RESULTADOS_DIR, "SB15_14.txt"),
    "SB15_13": os.path.join(RESULTADOS_DIR, "SB15_13.txt"),
    "SB15_12": os.path.join(RESULTADOS_DIR, "SB15_12.txt"),
    "SB15_11": os.path.join(RESULTADOS_DIR, "SB15_11.txt"),
}

def calcular_custos():
    dados = []
    for nome, caminho in ARQUIVOS.items():
        try:
            with open(caminho, "r") as f:
                num_apostas = sum(1 for _ in f)
            custo = num_apostas * CUSTO_POR_APOSTA
            dados.append([nome, num_apostas, f"R$ {CUSTO_POR_APOSTA:.2f}", f"R$ {custo:,.2f}"])
        except FileNotFoundError:
            dados.append([nome, "Arquivo não encontrado", "-", "-"])
    df = pd.DataFrame(dados, columns=["Subconjunto", "Nº de Apostas", "Valor por Aposta", "Custo Total"])
    print("\nCUSTO FINANCEIRO DOS SUBCONJUNTOS:\n")
    print(tabulate(df, headers='keys', tablefmt='github', showindex=False))

if __name__ == "__main__":
    calcular_custos()