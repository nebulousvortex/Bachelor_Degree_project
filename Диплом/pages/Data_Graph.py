import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash import dash
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

def get_figure_sin():
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    return {
        'data': [
            {'x': x, 'y': y, 'type': 'line', 'name': 'sin(x)'},
        ],
        'layout': {
            'title': 'График функции sin(x)',
        }
    }

def get_figure_cos():
    x = np.linspace(0, 2*np.pi, 100)
    y = np.cos(x)
    return {
        'data': [
            {'x': x, 'y': y, 'type': 'line', 'name': 'cos(x)'},
        ],
        'layout': {
            'title': 'График функции cos(x)',
        }
    }

@app.callback(
    Output('output', 'children'),
    [Input('sinus', 'clickData')])
def display_click_data(clickData):
    if clickData:
        x = clickData['points'][0]['x']
        y = clickData['points'][0]['y']
        return f'Вы нажали на точку с координатами на графике sin(x): ({x}, {y})'

app.layout = html.Div([
    dcc.Graph(
        id='sinus',
        figure=get_figure_sin()
    ),
    dcc.Graph(
        id='cosinus',
        figure=get_figure_cos()
    ),
    html.Div(id='output')
])

if __name__ == '__main__':
    app.run_server(debug=True)