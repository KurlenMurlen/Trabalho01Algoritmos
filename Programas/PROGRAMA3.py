import itertools
import os
import time

UNIVERSO_NUMEROS = range(1, 26)
DADOS_DIR = "dados"
RESULTADOS_DIR = "resultados"
ARQUIVO_T = os.path.join(DADOS_DIR, "S13.txt")
ARQUIVO_SAIDA = os.path.join(RESULTADOS_DIR, "SB15_13.txt")

def encontrar_conjunto_de_cobertura():
    if not os.path.exists(DADOS_DIR):
        print(f"Diretório '{DADOS_DIR}' não encontrado.")
        return
    if not os.path.exists(RESULTADOS_DIR):
        os.makedirs(RESULTADOS_DIR)

    try:
        with open(ARQUIVO_T, 'r') as f:
            t_subsets_a_cobrir = {
                tuple(map(int, line.strip().replace(',', ' ').split()))
                for line in f
            }
        print(f"{len(t_subsets_a_cobrir):,} sequências de tamanho 13 carregadas.")
    except FileNotFoundError:
        print(f"Arquivo '{ARQUIVO_T}' não encontrado.")
        return

    conjunto_cobertura_final = set()
    total_t_subsets_inicial = len(t_subsets_a_cobrir)
    start_time = time.time()

    while t_subsets_a_cobrir:
        t_semente = t_subsets_a_cobrir.pop()
        t_subsets_a_cobrir.add(t_semente)

        melhor_k_candidato = None
        max_cobertos = -1
        subsets_cobertos_pelo_melhor = set()

        numeros_restantes = list(set(UNIVERSO_NUMEROS) - set(t_semente))
        for sub_combinacao in itertools.combinations(numeros_restantes, 2):
            k_candidato = tuple(sorted(t_semente + sub_combinacao))
            novos_cobertos = set(itertools.combinations(k_candidato, 13)).intersection(t_subsets_a_cobrir)
            if len(novos_cobertos) > max_cobertos:
                max_cobertos = len(novos_cobertos)
                melhor_k_candidato = k_candidato
                subsets_cobertos_pelo_melhor = novos_cobertos

        if melhor_k_candidato:
            conjunto_cobertura_final.add(melhor_k_candidato)
            t_subsets_a_cobrir.difference_update(subsets_cobertos_pelo_melhor)

        if len(conjunto_cobertura_final) % 100 == 0:
            percentual = (1 - len(t_subsets_a_cobrir) / total_t_subsets_inicial) * 100
            print(f"Progresso: {len(conjunto_cobertura_final)} apostas, {len(t_subsets_a_cobrir):,} restantes ({percentual:.4f}%)")

    end_time = time.time()
    with open(ARQUIVO_SAIDA, "w") as f:
        for aposta in sorted(conjunto_cobertura_final):
            f.write(" ".join(map(str, aposta)) + "\n")
    print(f"Arquivo '{ARQUIVO_SAIDA}' gerado com {len(conjunto_cobertura_final)} apostas em {(end_time - start_time)/3600:.2f} horas.")

if __name__ == "__main__":
    encontrar_conjunto_de_cobertura()