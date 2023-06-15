import dash
import pandas as pd
import pyodbc
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

_date = ''
object_array = ''
server = 'REDSPACESHIP'
database = 'HEC'
username = ''
password = ''
name = ''

cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
# Выше подключение к БД, ниже выполнение запросов.
first_query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"
second_query = "SELECT dbo.Boiler_room.* FROM dbo.Boiler_room"

df1 = pd.read_sql(first_query, cnxn)
object_data_array = pd.read_sql(second_query, cnxn)

dash.register_page(__name__, path='/home')

table_layout = html.Div([
    html.H1(children='Таблица Атрибутов Объекта', style={'color': 'white'}),
    dash_table.DataTable(data=object_data_array.to_dict('records'), id='Table', page_size=25,
                         style_header={
                             'backgroundColor': '#18191b',
                             'color': 'white'
                         },
                         style_data={
                             'backgroundColor': '#4e5259',
                             'color': 'white'
                         })
])