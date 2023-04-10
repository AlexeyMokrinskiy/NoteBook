import datetime
import uuid
from colorama import init
init(autoreset=True)

def get_value():
    return input('->:')


def input_data():

    print('\nвведите тему заметки')
    theme = get_value()
    print('\nвведите тело заметки')
    body = get_value()
    data_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    id = str(uuid.uuid1())[0:3]
    return (id, data_time, theme, body)

