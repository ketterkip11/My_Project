import dash
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from dash import dcc, html
from dash.dependencies import Input, Output

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash('auth')#, external_stylesheets=external_stylesheets)
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
# import bcrypt
#
# username = b""
# password = b"secretpas"
#
# user=b'postgres'
# password=b'postgres'
#
#
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
#
#
# # if bcrypt.checkpw(password, hashed):
# #     print("it matches")
# # else:
# #     print("didnt match")
# print(hashed)



# b'$2b$12$.GG7OZ1vh4ggDHZWNAYzf.5mc8FZT3PgPE/cxELtP0X8SO1aNN5J6'

# b'$2b$12$BfKPox00sQ8fBWrv./YYEeuvH3qjQudwqf.FxKJisOOUWci.wtjku'
