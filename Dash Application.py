import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd

data = pd.read_csv('/home/ketter/PycharmProjects/pythonProject1/avocado.csv')
# print(data)
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"
# server = app.server
#
app.layout = html.Div(
    children=[
        html.P(children="🥑",className="header-emoji"),
        html.H1(children="Avocado Analytics",
                className="header-title",
        ),
        html.P(
            children="Analyze the behaviour of avocado prices"
                    "and the number of avocado sold in thr US"
                    "between 2015 and 2018",
            className="header-description",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price=chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "lines",
                                    "hovertemplate": "$%{y:.2f}"
                                                        "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Average Price of Avocados",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },

                        },
                    ),
                    className="card",
                ),
            ],
        ),
        html.Div(
            children=dcc.Graph(
                id="volume-chart",
                config={"displayModeBar": False},
                figure={
                    "data": [
                        {
                            "x": data["Date"],
                            "y": data["Total Volume"],
                            "type": "lines",
                        },
                    ],
                    "layout": {
                        "title": "Avocado Sold",
                        "x": 0.05,
                        "xanchor": "left",
                    },
                },

            ),
            className="card",
        ),
    ],

)

if __name__=="__main__":
    app.run_server(debug=True)