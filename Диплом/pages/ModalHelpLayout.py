import dash_bootstrap_components as dbc
from dash import html

# Описание модального окна 1
startModal = dbc.Modal([
    dbc.ModalHeader("Помощь в использовании!"),
    dbc.ModalBody([
        html.Label("Это небольшая справка, которая расскажет, как работать с данной программой.",
                   style={'text-align': 'justify'}),
        html.Br(),
        html.Label("Далее будет пошагово рассказано о возможностях данного приложения",
                   style={'text-align': 'justify'})]),
    dbc.ModalFooter([
        html.Label("1 / 5"),
        dbc.Button("Далее", id="next_modal1", className="ml-auto")
    ]),
],
    id="modal1",
    centered=True,
    keyboard=False,
    backdrop="static")

# Описание модального окна 2
modalStepOne = dbc.Modal([
    dbc.ModalHeader("Помощь в использовании! Шаг 1"),
    dbc.ModalBody([
        html.Label("Первым делом настройте необходимые дату и время. По умолчанию выбран весь рабочий день.",
                   style={'text-align': 'justify'}),
        html.Br(), html.Br(),
        html.Img(src='/assets/timeSetting.png',
                 style={'display': 'block', 'margin': '0 auto'})]),
    dbc.ModalFooter([
        html.Label("2 / 5"),
        dbc.Button("Далее", id="next_modal2", className="ml-auto")
    ]),
],
    id="modal2",
    centered=True,
    keyboard=False,
    backdrop="static")

# Описание модального окна 3
modalStepTwo = dbc.Modal([
    dbc.ModalHeader("Помощь в использовании! Шаг 2"),
    dbc.ModalBody([
        html.Label("Затем выберите объект и атрибут, который необходимо отслеживать. Подсказка: Вы можете начать "
                   "вводить название, чтобы быстрее найти его. После того, как вы выберете объект - нажмите кнопку, "
                   "чтобы построить или же удалить график",
                   style={'text-align': 'justify'}),
        html.Br(), html.Br(),
        html.Img(src='/assets/objectSetting.png',
                 style={'display': 'block', 'margin': '0 auto'})]),
    dbc.ModalFooter([
        html.Label("3 / 5"),
        dbc.Button("Далее", id="next_modal3", className="ml-auto")
    ]),
],
    id="modal3",
    centered=True,
    keyboard=False,
    backdrop="static")

# Описание модального окна 4
modalStepThree = dbc.Modal([
    dbc.ModalHeader("Помощь в использовании! Шаг 3"),
    dbc.ModalBody([
        html.Label("Вы можете строить до 5 графиков одновременно. Наведитесь курсором на определенную точку на "
                   "графике и вы увидите точные данные, которые вас интересуют. График интерактивный: вы можете "
                   "двигать оси, можете увеличить фрагменты полотна и т.д.",
                   style={'text-align': 'justify'}),
        html.Br(), html.Br(),
        html.Img(src='/assets/graphRender.png',
                 style={'display': 'block', 'margin': '0 auto'})]),
    dbc.ModalFooter([
        html.Label("4 / 5"),
        dbc.Button("Далее", id="next_modal4", className="ml-auto")
    ]),
],
    id="modal4",
    centered=True,
    keyboard=False,
    backdrop="static")

# Описание модального окна 5
modalStepFour = dbc.Modal([
    dbc.ModalHeader("Помощь в использовании! Шаг 4"),
    dbc.ModalBody([
        html.Label("В правом верхнем угру графиков есть небольшая панель. Здесь вы можете сохранить результат в виде "
                   "скриншота, приблизить или отдалить результат, а так же сбросить все изменения",
                   style={'text-align': 'justify'}),
        html.Br(), html.Br(),
        html.Img(src='/assets/funcPanel.png',
                 style={'display': 'block', 'margin': '0 auto'})]),
    dbc.ModalFooter([
        html.Label("5 / 5"),
        dbc.Button("Далее", id="next_modal5", className="ml-auto")
    ]),
],
    id="modal5",
    centered=True,
    keyboard=False,
    backdrop="static")

modal_states = {
    'modal_1': startModal,
    'modal_2': modalStepOne,
    'modal_3': modalStepTwo,
    'modal_4': modalStepThree,
    'modal_5': modalStepFour
}
