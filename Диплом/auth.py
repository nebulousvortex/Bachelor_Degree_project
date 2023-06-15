import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app
from Main import content

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Button('Go to Main', id='go-to-main', n_clicks=0)],
    id='page-content')

@app.callback(Output('url', 'pathname'),
              [Input('go-to-main', 'n_clicks')])
def display_main_page(n_clicks):
    if n_clicks == 1:
        return '/main'

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/main':
        return content
    else:
        return dash.no_update


if __name__ == '__main__':
    app.run_server()