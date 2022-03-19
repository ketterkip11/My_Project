import datetime

import dash
from dash import dcc,html
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]

    )


df = pd.read_csv('/home/ketter/Downloads/NseData.csv')
label = df['company'].values
labels = set(label)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("STOCKS FOR COMPANIES IN NSE",
                        className='text-center text-primary, mb-4'),
                width=12)
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Dropdown(id='my_dropdown', options=[

                {'label': i, 'value': i} for i in labels],

                         )
        ),
        dcc.Graph(id='line-fig', figure={})

    ],
    ),
    ])

@app.callback(
    Output('line-fig', 'figure'),
    Input('my_dropdown', 'value')
)
def update_graph(stock_selected):
    df1 = df
    dff = df1[df1['company']==stock_selected]
    dates = pd.to_datetime(dff.loc[:, 'date']).dt.date

    fig_1= go.Scatter(
        x=dates,
        y=dff['price'],
        mode='lines+markers',
        line=dict(color='#483D8B', width=0.5),
        marker=dict(color='#A10197', size=4),
        text=dff.company
    )

    fig = go.Figure(data=fig_1)
    fig.update_layout(title=dict(text=stock_selected, font_color='black', font_size=30, x=0.5),
                      xaxis=dict(title='Date', color='purple', showgrid=False, showspikes=True,
                                 spikethickness=1, spikedash='solid', spikemode='toaxis+across+marker',
                                 spikecolor='black', spikesnap='cursor'),
                      yaxis=dict(title='Price', color='green', showgrid=True, gridwidth=0.1,
                                 gridcolor='#7AE2E6'),
                      hovermode='x',
                      autosize=True,
                      paper_bgcolor='#C2DBDC',
                      plot_bgcolor='#C2DBDC',
                      template='plotly_dark',
                      )
    return fig

if __name__ == '__main__':
    app.run_server(port=8001)