# Trabalho01Algoritmos
# Projeto de Complexidade de Algoritmos - Lotofácil

## Descrição do Projeto
Este projeto visa analisar e implementar algoritmos para geração e manipulação de combinações numéricas relacionadas à Lotofácil, conforme os requisitos especificados no trabalho acadêmico. O objetivo principal é desenvolver soluções eficientes para gerar combinações e encontrar subconjuntos ótimos que cubram todas as sequências de tamanhos menores.

## Integrantes do Grupo
- Tarso Bertolini
- Gabriel Simini
- Eduardo Contin
- Mariana de Castro
- Alex Secco

## Estrutura do Projeto
/projeto_lotofacil
│
├── README.md # Este arquivo
├── programa1.py # Gerador de combinações (S11 a S15)
├── programa2.py # Subconjunto SB15_14 (Cenário C1)
├── programa3.py # Subconjunto SB15_13 (Cenário C2)
├── programa4.py # Subconjunto SB15_12 (Cenário C3)
├── programa5.py # Subconjunto SB15_11 (Cenário C4)
├── analise_complexidade.md # Relatório de análise de complexidade
├── custos_financeiros.md # Cálculo dos custos para cada subconjunto
├── dados/ # Pasta para armazenar combinações geradas
│ ├── S11.txt
│ ├── S12.txt
│ ├── S13.txt
│ ├── S14.txt
│ └── S15.txt
└── resultados/ # Pasta para armazenar subconjuntos resultantes
├── SB15_11.txt
├── SB15_12.txt
├── SB15_13.txt
└── SB15_14.txt

---

## Requisitos
- Python 3.8+
- Bibliotecas Python (instaláveis via `pip install -r requirements.txt`):
  - itertools (já incluído na biblioteca padrão)
  - math (já incluído na biblioteca padrão)
  - time (já incluído na biblioteca padrão)

## Como Executar
1. Clone o repositório ou baixe os arquivos do projeto
2. Execute os programas em ordem:
   ```bash
   python programa1.py        # Gera todas as combinações base
   python programa2.py        # Gera SB15_14
   python programa3.py        # Gera SB15_13
   python programa4.py        # Gera SB15_12
   python programa5.py        # Gera SB15_11

Observações Importantes
O programa1.py pode consumir recursos significativos de memória e tempo para gerar todas as combinações

Para testes iniciais, recomenda-se reduzir o valor de n no código-fonte

### Os programas 2-5 podem implementar abordagens alternativas (heurísticas) caso a solução por força bruta seja inviável

Prazos
Turma A: Entrega até 16/06/2025

Turma B: Entrega até 17/06/2025

### Metodologia
O projeto será desenvolvido utilizando PBL (Problem-Based Learning), com distribuição equitativa de tarefas entre os membros do grupo. Cada integrante será responsável por parte da implementação e deverá estar preparado para defender qualquer aspecto do projeto.
   
