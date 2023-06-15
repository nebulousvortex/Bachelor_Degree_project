import sys
from datetime import datetime
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
from dash import html, dcc, dash_table
from plotly.subplots import make_subplots as ms
from DataBaseConnection import cnxn
from DataEntity import DataEntity

from pages.ModalHelpLayout import modal_states

outside = ''
if len(sys.argv) < 2:
    sys.argv.append('')
checker = True
if sys.argv[1]:
    outside = sys.argv[1]
    checker = True

datas = DataEntity()

# подключение к БД для прогрузки стартовых значений
tables_query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"
second_query = "SELECT dbo.CHP_transformer_1.* FROM dbo.CHP_transformer_1"

all_objects_array = pd.read_sql(tables_query, cnxn)
object_data_array = pd.read_sql(second_query, cnxn)
date_time = str(datetime.now().date()).replace('-', '.')
graph_array = np.array([])
attributes_array = np.array([])

fig = ms(specs=[[{"secondary_y": True}]])
fig.update_layout()
fig.update_traces(hoverinfo="all", hovertemplate="Время: %{x}<br>Значение: %{y}")

# Загрузка модальных окон
modal = html.Div([
    dbc.Button("Помощь", id="open_modal"),
    modal_states['modal_1'],
    modal_states['modal_2'],
    modal_states['modal_3'],
    modal_states['modal_4'],
    modal_states['modal_5']
])

# Уведомление удаления графика
alert = html.Div([
    dbc.Alert(
        "Вы удалили последний добавленный график график!",
        id="alert-auto",
        is_open=True,
        duration=2000,
        color='success'
    ), ]
)

# Верстка виджета с вводом пользовательских данных
render_settings = html.Div([
    # Вводимые значения
    html.Div([
        html.H1(children='Ввод параметров', style={'color': 'white'}),
        dcc.Input(id="Param", value=outside, type="text", style={'display': 'none'}),  # Внутренний Параметр
        dcc.Input(id="Param2", value=outside, type="text", style={'display': 'none'}),  # Внутренний Параметр
        dcc.Input(id="non", value=outside, type="text", style={'display': 'none'}),  # Внутренний Параметр - пустышка
        html.Label("Дата: ", style={'color': 'white'}),
        dcc.DatePickerSingle(display_format='YY.MM.DD', date="2022.12.12", id='Date', style={'width': '300px'}),
        html.Br(),  # Выбор даты
        html.Label("С", style={'color': 'white'}), html.Br(),
        dcc.Input(id="startTime", value='00:00:00', type="text", style={'width': '100%'}),
        html.Br(),
        html.Label("До ", style={'color': 'white'}), html.Br(),
        dcc.Input(id="endTime", value='16:10:00', type="text", style={'width': '100%'})],
        style={"height": "auto", "width": "90%", "margin": "25px", "justify-content": "space-between"}),

    html.Div([
        dcc.Dropdown(all_objects_array['TABLE_NAME'], value='', placeholder='Выберите Объект', id='objects',
                     style={"margin": "14px"}),
        dcc.Dropdown(value='', placeholder='Выберите атрибут', id='attributes', style={"margin": "14px", })],
        style={"height": "auto"}),

    html.Div([
        html.Label("Обновление графика ", style={'color': 'white'}),
        # Радиокнопка для остановки обновления
        html.Br(),
        dbc.RadioItems(['Остановить', 'Продолжить'], 'Продолжить', id='check', inline=True,
                       style={"width": "50", 'color': 'white'}),
        html.Div([
            # Кнопка для удаления
            html.Br(), html.Button(id='delete_button', n_clicks=0, children='Удалить График', style={'width': '110%'}),
            # Кнопка для добавления
            html.Button(id='Confirm', n_clicks=0, children='Добавить График', style={'width': '110%'})],
            style={"height": "auto", "flex": "auto"})],
        style={"margin": "25px", "justify-content": "space-between", "height": "auto"}),
],
    style={"width": '20%', "flex": "auto", "height": "auto", "padding": 10, "align-items": "stretch"})

# Часть виджета с графиком
graph_layout = html.Div([
    html.H1(children="Графики данных атрибутов", style={'color': 'white'}),
    dcc.Graph(id="Chart", figure=fig),  # График на макете
    dcc.Interval(id="animateInterval", interval=1500, n_intervals=0)
])

# Часть виджета с таблицей
table_layout = html.Div([
    html.H1(children='Таблица Атрибутов Объекта', style={'color': 'white'}),
    dash_table.DataTable(data=object_data_array.to_dict('records'), id='Table', page_size=12,
                         style_header={
                             'backgroundColor': '#18191b',
                             'color': 'white'
                         },
                         style_data={
                             'backgroundColor': '#4e5259',
                             'color': 'white'
                         })
])

# Виджет с графиком и таблицей на TabPages
tab_layout = html.Div([
    html.Br(),
    html.H1('Выберите способ отображения данных: ', style={'color': 'white'}),
    dcc.Tabs(id="tabs-example-graph", value='tab-1', children=[
        dcc.Tab(label='График данных', children=graph_layout),
        dcc.Tab(label='Таблица данных', children=table_layout),
    ]),
    html.Div(id='tabs-content-example-graph')
], style={"width": '80%', "flex": "auto", "height": "auto", "padding": 20, "align-items": "stretch"})

# Все виджеты вместе
content = html.Div(children=[
    html.Div([
        modal
    ], style={"margin": "25px", "justify-content": "space-between", "height": "auto"}),
    alert,
    dbc.Row([
        render_settings,
        tab_layout],
        className="g-3",
        style={"align-items": "stretch", "height": "auto"}),
    dcc.Store(id='csrf-token', storage_type='session', data='redspace'),  # Базовый токен безопасности CSRF
], style={'backgroundColor': '#36393E', "min-height": "99vh", "height": "100%", 'zoom': '100%'})
