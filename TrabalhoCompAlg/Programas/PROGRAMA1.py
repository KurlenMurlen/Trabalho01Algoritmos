import itertools

def gerar_combinacoes(n, p):
    """
    Gera todas as combinações possíveis de p números distintos entre 1 e n.
    
    Args:
        n (int): Número total de elementos (25 para Lotofácil)
        p (int): Tamanho da combinação (15, 14, 13, 12 ou 11)
    
    Returns:
        list: Lista de tuplas contendo todas as combinações
    """
    numeros = range(1, n+1)
    return list(itertools.combinations(numeros, p))

def salvar_combinacoes(combinacoes, nome_arquivo):
    """
    Salva as combinações em um arquivo de texto.
    
    Args:
        combinacoes (list): Lista de combinações a serem salvas
        nome_arquivo (str): Nome do arquivo de saída
    """
    with open(nome_arquivo, 'w') as f:
        for comb in combinacoes:
            linha = ','.join(map(str, comb)) + '\n'
            f.write(linha)

def main():
    # Configurações para Lotofácil
    n = 25
    tamanhos = {
        'S15': 15,
        'S14': 14,
        'S13': 13,
        'S12': 12,
        'S11': 11
    }
    
    print("Iniciando geração de combinações para Lotofácil...")
    
    for nome, p in tamanhos.items():
        print(f"\nGerando {nome}...")
        
        # Calcula o número esperado de combinações para verificação
        total_esperado = len(list(itertools.combinations(range(n), p)))
        print(f"Total esperado de combinações: {total_esperado:,}")
        
        # Gera as combinações
        combinacoes = gerar_combinacoes(n, p)
        
        # Verifica se o número gerado corresponde ao esperado
        total_gerado = len(combinacoes)
        print(f"Total gerado de combinações: {total_gerado:,}")
        
        if total_gerado == total_esperado:
            print("Verificação: OK")
        else:
            print("Verificação: FALHA - Número de combinações incorreto")
        
        # Salva em arquivo (comente esta linha para testes rápidos)
        nome_arquivo = f"{nome}.txt"
        salvar_combinacoes(combinacoes, nome_arquivo)
        print(f"Combinações salvas em {nome_arquivo}")
    
    print("\nConcluído!")

if __name__ == "__main__":
    main()