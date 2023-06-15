import time as tm
import webbrowser
from datetime import datetime

import dash
import dash_auth
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash import ctx
from dash.dependencies import Output, Input, State
# from flask_wtf import CSRFProtect
from plotly.subplots import make_subplots as ms
from flask import Flask
from DataBaseConnection import cnxn
from DataEntity import DataEntity
from pages.MainLayout import content as cont

# Универсальный ключ быстрой аутентификации
VALID_USERNAME_PASSWORD_PAIRS = {
    'username': 'aa'
}

datas = DataEntity()
modalNum = 1

# Базовые SQL запросы
tables_query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"
second_query = "SELECT dbo.Boiler_room_1.* FROM dbo.Boiler_room_1"
# Выполнение SQL запросов
all_objects_array = pd.read_sql(tables_query, cnxn)
object_data_array = pd.read_sql(second_query, cnxn)
date_time = str(datetime.now().date()).replace('-', '.')
graph_array = np.array([])
attributes_array = np.array([])

#  Приложение без использования CSS
# app = dash.Dash()
# Приложение с использованием CSS
server = Flask(__name__)
server.secret_key = 'redspace'
# Модуль CSRF защиты
# csrf = CSRFProtect(server)
# Правила запуска локального сервера
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

dash.register_page(__name__, path='/')

app.title = 'Визуализация данных'
# Создание правил оформления макета

app.layout = cont

# Callback методы

""" convert_date
В данном методе происходит преобразование даты и времени в один строковый параметр для SQL.
"""


@app.callback(
    Output("Param", "value"),
    Input("Date", "date"),
    Input("startTime", "value"),
    Input("endTime", "value"),
)
def convert_date(date, start, end):
    return date + '  ' + start + '  ' + end


""" get_attributes
В данном методе происходит получение атрибута для выпадающего списка по SQL запросу.
"""


@app.callback(
    Output("Param2", "value"),
    Output("attributes", "options"),
    Input("objects", "value"),
)
def get_attributes(value):
    global object_data_array

    object_query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + str(value) + "'"
    object_array = pd.read_sql(object_query, cnxn)
    if value == '':
        return dash.no_update
    attribute_query = "SELECT dbo.[" + value + "].* FROM dbo.[" + value + "]"
    object_data_array = pd.read_sql(attribute_query, cnxn)
    return value, object_array['COLUMN_NAME']


""" update_fig
В данном методе описаны все обновления полотна и графиков на нем по заданному интервалу.
"""


@app.callback(Output("Chart", "figure"),
              Output("alert-auto", "is_open"),
              Input("animateInterval", "n_intervals"),
              Input('check', 'value'),
              Input("delete_button", "n_clicks"),
              prevent_initial_call=True)
def update_fig(n_intervals, check, n_clicks):
    global fig
    global graph_array
    global object_data_array
    global attributes_array
    triggered_id = ctx.triggered_id
    # Триггер на кнопку удаления
    if triggered_id == 'delete_button':

        datas.delete_graph()
        datas.delete_attribute()

        return fig, True
    # Триггер на все остальное
    else:
        if check == 'Остановить':
            tm.sleep(1)
            return dash.no_update, dash.no_update  # если отмечено "стоп", то обновления не учитываются
        else:
            # настройки оформления графика с жестким ограничением осей.
            fig = ms(specs=[[{"secondary_y": True}]])
            fig.update_layout(
                legend_orientation="h",
                paper_bgcolor='#4e5259',
                plot_bgcolor='rgba(250,250,250,250)',
                xaxis_showgrid=False, yaxis_showgrid=False,
                legend=dict(x=0, xanchor="left"),
                hovermode="x",
                margin=dict(l=0, r=0, t=0, b=0),
                xaxis=dict(domain=[0.2, 1]),

                yaxis=dict(
                    title="",
                    titlefont=dict(color="#0000ff"),
                    tickfont=dict(color="#0000ff")),

                yaxis2=dict(
                    title="",
                    titlefont=dict(color="#FF0000"),
                    tickfont=dict(color="#FF0000"),
                    anchor="free",
                    overlaying="y",
                    side="left",
                    position=0.15),

                yaxis3=dict(
                    title="",
                    titlefont=dict(color="#00ff00"),
                    tickfont=dict(color="#00ff00"),
                    anchor="free",
                    overlaying="y",
                    side="left",
                    position=0.1),

                yaxis4=dict(
                    title="",
                    titlefont=dict(color="#ffd600"),
                    tickfont=dict(color="#ffd600"),
                    anchor="free",
                    overlaying="y",
                    side="left",
                    position=0.05),

                yaxis5=dict(
                    title="",
                    titlefont=dict(color="#ff69b4"),
                    tickfont=dict(color="#ff69b4"),
                    anchor="free",
                    overlaying="y",
                    side="left",
                    position=0.0))

            if datas.get_attribute_count() > 0:
                for i in range(datas.get_graph_count()):
                    fig.add_trace(datas.get_graph(i))
            fig.update_traces(hoverinfo="all", hovertemplate="Время: %{x}<br>Значение: %{y}")
            return fig, dash.no_update


""" update_atr
В данном методе происходит получение данных атрибута и их обновление в заданном интервале
"""


@app.callback(Output("non", "value"),
              Input("Confirm", "n_clicks"),
              Input("Param2", "value"),
              Input("attributes", "value"),
              Input("Date", "date"),
              Input("startTime", "value"),
              Input("endTime", "value"),
              prevent_initial_call=True)
def update_atr(n_clicks, objects, attribute, date, start, end):
    global object_data_array
    global graph_array
    global attributes_array
    startTime = date + " " + start
    endTime = date + " " + end
    triggered_id = ctx.triggered_id
    # Получение данных для графика по внутреннему параметру
    if objects:
        if triggered_id == 'Confirm':
            attributes_query = "SELECT dbo.[" + objects + "].[" + attribute + "] FROM dbo.[" + objects + \
                               "] Where Time >= '" + startTime + "' and Time <= '" + endTime + "'"
            current_attribute = pd.read_sql(attributes_query, cnxn)
            x = object_data_array['Time']
            y = current_attribute[attribute]
            fig.update_traces(hoverinfo="all", hovertemplate="Время: %{x}<br>Значение: %{y}")
            axis_number = datas.get_graph_count()
            datas.add_graph(go.Scatter(x=x, y=y, yaxis='y' + str(axis_number + 1), name=attribute))
            datas.add_attribute(attributes_query)
        return dash.no_update
    else:
        return dash.no_update


""" toggle_modal_1
В данном методе описаны действия в модальном окне 1
"""


@app.callback(
    Output("modal1", "is_open"),
    [
        Input("open_modal", "n_clicks"),
        Input("next_modal2", "n_clicks"),
    ],
    [State("modal1", "is_open")],
)
def toggle_modal_1(n0, n1, is_open):
    if n0 or n1:
        return not is_open
    return is_open


""" toggle_modal_2
В данном методе описаны действия в модальном окне 2
"""


@app.callback(
    Output("modal2", "is_open"),
    [
        Input("next_modal1", "n_clicks"),
        Input("next_modal2", "n_clicks"),
    ],
    [State("modal2", "is_open")],
)
def toggle_modal_2(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


""" toggle_modal_3
В данном методе описаны действия в модальном окне 3
"""


@app.callback(
    Output("modal3", "is_open"),
    [
        Input("next_modal2", "n_clicks"),
        Input("next_modal3", "n_clicks"),
    ],
    [State("modal3", "is_open")],
)
def toggle_modal_3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


""" toggle_modal_4
В данном методе описаны действия в модальном окне 4
"""


@app.callback(
    Output("modal4", "is_open"),
    [
        Input("next_modal3", "n_clicks"),
        Input("next_modal4", "n_clicks"),
    ],
    [State("modal4", "is_open")],
)
def toggle_modal_4(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


""" toggle_modal_5
В данном методе описаны действия в модальном окне 5
"""


@app.callback(
    Output("modal5", "is_open"),
    [
        Input("next_modal4", "n_clicks"),
        Input("next_modal5", "n_clicks"),
    ],
    [State("modal5", "is_open")],
)
def toggle_modal_5(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


""" open_browser
В данном методе вызывается автоматическое открытие страницы браузера с веб-приложением
"""


def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')


# Запуск
if __name__ == "__main__":
    # open_browser()
    app.run_server(debug=True)
