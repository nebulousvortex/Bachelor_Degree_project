import pyodbc

server = 'REDSPACESHIP'
database = 'HEC'
username = ''
password = ''
name = ''

try:
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    print("Подключение к базе данных было успешным")

except pyodbc.Error as e:
    print("Ошибка при подключении к базе данных:", e)
