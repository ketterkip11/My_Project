import dash
# import dash_core_components as dcc
from dash import dcc,html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('/home/ketter/PycharmProjects/My_Project/nse_data.csv')
# print(df)
# fig = px.scatter(
#     df,
#     x = 'date',
#     y = 'price',
#     color= 'company',
#     hover_name='ticker',
#     log_x=True
# )


# app.layout = html.Div(id = 'company', children=[
#
# ])
company = df['company'].unique()



app.layout = html.Div(id= 'parent', children=[
    html.H1(id = 'H1', children='NSE stock Exchange',
            style={'textAlign': 'centre',\
            'marginTop':40, 'marginBottom':40}),

    html.Div([
        html.Label('company '),
        dcc.Dropdown(
            id = 'company',
            options = [{'label': i, 'value': i} for i in df.company.unique()],
            value = 'company',
            placeholder='select...',
            multi=True
        )
    ],
    style={'width': '20%', 'display': 'inline-block', 'margin-bottom': '20px'}),
    dcc.Graph(id='bar_plot')

   ]
)

@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])

def nse_stock(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x = df['date'], y = df['company'],\
                     line=dict(color = 'firebrick', width = 4), name='NSE_STOCKS')
                     ])
    fig.update_layout(title = 'stock exchange',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig

if __name__=='__main__':
    app.run_server()

