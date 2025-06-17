import dash
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import random

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

# Parâmetros da animação didática
N_SUBSETS = 15  # número de subconjuntos (exemplo pequeno)
STEP_SIZE = 4   # quantos subconjuntos são cobertos por passo

app = dash.Dash(__name__)

# Layout
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
                    bargap=0.5,
                    plot_bgcolor='#fafafc',
                    paper_bgcolor='#fafafc',
                    font=dict(family='-apple-system, BlinkMacSystemFont, Segoe UI, Arial, Helvetica, sans-serif', size=16)
                )
            },
            className="apple-graph"
        )
    ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    # ANIMAÇÃO ABAIXO DO GRÁFICO
    html.Div([
        html.H3("Demonstração Visual do Algoritmo Guloso de Cobertura"),
        html.P("Cada círculo representa um subconjunto. A cada passo, uma aposta cobre vários subconjuntos (círculos ficam verdes)."),
        dcc.Graph(id='animacao-cobertura'),
        html.Button("Próximo passo", id='btn-proximo', n_clicks=0),
        html.Div(id='animacao-status', style={'marginTop': '10px', 'fontWeight': 'bold'}),
        dcc.Store(id='store-animacao', data={'covered': [False]*N_SUBSETS, 'steps': []}),
    ], style={'marginTop': '60px', 'width': '100%', 'textAlign': 'center'})
], className="apple-container")

# Estado inicial da animação
initial_covered = [False] * N_SUBSETS
initial_steps = []

# Callback da animação
@app.callback(
    [Output('animacao-cobertura', 'figure'),
     Output('animacao-status', 'children'),
     Output('store-animacao', 'data')],
    [Input('btn-proximo', 'n_clicks')],
    [State('store-animacao', 'data')]
)
def animar_cobertura(n_clicks, store_data):
    if n_clicks == 0 or store_data is None:
        covered = [False] * N_SUBSETS
        steps = []
    else:
        covered = store_data['covered']
        steps = store_data['steps']

    if all(covered):
        status = "Todos os subconjuntos foram cobertos!"
        colors = ['green' if c else 'gray' for c in covered]
        fig = go.Figure(
            data=[go.Scatter(
                x=list(range(N_SUBSETS)),
                y=[0]*N_SUBSETS,
                mode='markers',
                marker=dict(size=40, color=colors, line=dict(width=2, color='black'))
            )],
            layout=go.Layout(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                margin=dict(l=20, r=20, t=20, b=20)
            )
        )
        return fig, status, store_data

    uncovered_indices = [i for i, c in enumerate(covered) if not c]
    random.shuffle(uncovered_indices)
    to_cover = uncovered_indices[:STEP_SIZE]
    for idx in to_cover:
        covered[idx] = True
    steps.append(to_cover)

    colors = []
    for i in range(N_SUBSETS):
        if i in to_cover:
            colors.append('orange')
        elif covered[i]:
            colors.append('green')
        else:
            colors.append('gray')

    fig = go.Figure(
        data=[go.Scatter(
            x=list(range(N_SUBSETS)),
            y=[0]*N_SUBSETS,
            mode='markers',
            marker=dict(size=40, color=colors, line=dict(width=2, color='black'))
        )],
        layout=go.Layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            margin=dict(l=20, r=20, t=20, b=20)
        )
    )
    status = f"Passo {len(steps)}: Cobriu {len(to_cover)} subconjuntos."
    return fig, status, {'covered': covered, 'steps': steps}

if __name__ == '__main__':
    app.run(debug=True)
