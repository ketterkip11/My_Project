import dash
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from dash import dcc, html


app = dash.Dash()

#create layout
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        placeholder='Select City'
        ),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    # style={'color':'white'}
    ),
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),
    html.Label('Text Box'),
    dcc.Input(value='MTL', type='text'),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

colors = {
    'background': '#44D908',
    'text': '#7FDBFF'
}


if __name__== '__main__':
    app.run_server()



from dash.dependencies import Input, Output

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='num-1',
        options=[
            {'label': '10', 'value': 10},
            {'label': '15', 'value': 15},
            {'label': '22', 'value': 22}
        ],
        placeholder='First Number'
    ),
    dcc.Dropdown(
        id='num-2',
        options=[
            {'label': '20', 'value': 20},
            {'label': '12', 'value': 12},
            {'label': '32', 'value': 32}
        ],
        placeholder='Second Number'
    ),
    html.Div(id='divide'),
    html.Div(id='multiply')
])


@app.callback(
    [Output(component_id='divide', component_property='children'),
     Output(component_id='multiply', component_property='children')],
    [Input(component_id='num-1', component_property='value'),
     Input(component_id='num-2', component_property='value')])
def update_output(num1, num2):
    divide = num1 / num2
    multiply = num1 * num2
    return divide, multiply


if __name__ == '__main__':
    app.run_server()