import dash
from dash import dcc, html
import plotly.graph_objs as go

# Tempos anotados (em horas)
tempos = [0.02, 0.06, 0.27, 1.16]
programas = ["PROGRAMA 2 (SB15_14)", "PROGRAMA 3 (SB15_13)", "PROGRAMA 4 (SB15_12)", "PROGRAMA 5 (SB15_11)"]

texto_analise = """
### ANÁLISE DE COMPLEXIDADE DE TEMPO

Para cada programa (2, 3, 4, 5), a complexidade é praticamente a mesma, mudando apenas o valor de t:

- **Carregamento dos subconjuntos:**  
  Carregar todas as combinações de tamanho t do arquivo para um set:  
  - Complexidade: O(Nₜ · t), onde Nₜ = C(25, t)

- **Loop principal (heurística gulosa):**  
  Enquanto houver subconjuntos a cobrir:
  - Para cada subconjunto semente, gera todas as combinações possíveis de tamanho k (15) que incluem a semente.
  - Para cada candidato, verifica quantos subconjuntos de tamanho t ele cobre.
  - Escolhe o candidato que cobre mais subconjuntos ainda não cobertos.

  - **Para cada iteração:**
    - Gera C(25-t, 15-t) candidatos.
    - Para cada candidato, gera C(15, t) subconjuntos.
    - Para cada subconjunto, verifica se está no set de subconjuntos a cobrir.

  - **Complexidade total aproximada:**  
    O(Nₜ · t + |SB| · C(25-t, 15-t) · C(15, t) · t)  
    Onde |SB| é o número de apostas no subconjunto final.

#### Resumindo para cada programa:
- **PROGRAMA 2:** t = 14  
- **PROGRAMA 3:** t = 13  
- **PROGRAMA 4:** t = 12  
- **PROGRAMA 5:** t = 11  

Quanto menor o t, maior o número de subconjuntos a cobrir e mais candidatos por iteração, então o tempo cresce rapidamente.

#### Tempos reais de execução:
- PROGRAMA 2: 0.02 horas
- PROGRAMA 3: 0.06 horas
- PROGRAMA 4: 0.27 horas
- PROGRAMA 5: 1.16 horas
"""

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Análise de Complexidade de Tempo - Lotofácil"),
    html.Div([
        dcc.Markdown(texto_analise, style={'whiteSpace': 'pre-line', 'fontSize': '16px'}),
    ], style={'width': '55%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingRight': '2%'}),
    html.Div([
        dcc.Graph(
            id='grafico-tempos',
            figure={
                'data': [
                    go.Bar(
                        x=programas,
                        y=tempos,
                        marker_color=['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728']
                    )
                ],
                'layout': go.Layout(
                    title='Tempo de Execução dos Programas (em horas)',
                    xaxis={'title': 'Programa'},
                    yaxis={'title': 'Tempo (horas)', 'rangemode': 'tozero'},
                    bargap=0.5
                )
            }
        )
    ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'}),
], style={'padding': '30px'})

if __name__ == '__main__':
    app.run(debug=True)