# Trabalho 01 - Algoritmos de Cobertura para Lotofácil

Este projeto contém programas em Python para geração de combinações, algoritmos de cobertura (heurística gulosa), análise de complexidade e cálculo de custo financeiro para apostas da Lotofácil.

## Estrutura do Projeto

```
Trabalho01Algoritmos/
├── dados/                # Arquivos de entrada (combinações S11.txt, S12.txt, S13.txt, S14.txt, etc)
├── resultados/           # Arquivos de saída gerados pelos programas (SB15_11.txt, SB15_12.txt, ...)
├── Programas/            # Programas Python principais
│   ├── programa2.py      # Cobertura para t=14
│   ├── programa3.py      # Cobertura para t=13
│   ├── programa4.py      # Cobertura para t=12
│   ├── programa5.py      # Cobertura para t=11
│   ├── analise_complexidade.py   # Análise visual e textual de complexidade (com gráfico interativo)
│   └── custo_financeiro.py       # Cálculo do custo financeiro dos subconjuntos
├── venv/                 # Ambiente virtual Python (opcional)
└── README.md             # Este arquivo
```

## Como executar

### 1. Crie e ative o ambiente virtual (opcional, recomendado)

```sh
python -m venv venv
venv\Scripts\activate
```

### 2. Instale as dependências

```sh
pip install dash plotly pandas tabulate
```

### 3. Execute os programas de cobertura

Cada programa cobre um valor de `t` e gera um arquivo na pasta `resultados`:

```sh
python Programas/programa2.py   # Gera SB15_14.txt
python Programas/programa3.py   # Gera SB15_13.txt
python Programas/programa4.py   # Gera SB15_12.txt
python Programas/programa5.py   # Gera SB15_11.txt
```

### 4. Análise de complexidade (com gráfico interativo)

```sh
python Programas/analise_complexidade.py
```
Abra o navegador no endereço indicado (geralmente http://127.0.0.1:8050).

### 5. Cálculo do custo financeiro

```sh
python Programas/custo_financeiro.py
```
Será exibida uma tabela com o custo total de cada subconjunto de apostas.

## Observações

- Os arquivos de entrada devem estar na pasta `dados` e os resultados serão salvos em `resultados`.
- Os programas podem consumir muita memória e tempo, dependendo do tamanho dos arquivos de entrada.
- O código está organizado para facilitar a leitura, análise e manutenção.

---

Desenvolvido para
   
