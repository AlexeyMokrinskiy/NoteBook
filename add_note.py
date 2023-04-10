import control
import os
from colorama import Fore
os.chdir(os.path.dirname(__file__))

def new_note(data):   
    id, data_time, theme, body = data
    with open('base.csv', 'a', encoding='UTF-8') as file:
        file.write('\nid: {}\nДата: {}\nТема: {}\nЗаметка: {}\n'.format(id, data_time, theme, body))
    print(Fore.LIGHTGREEN_EX + 'Новая запсь успешно добавлена с id ' + id + '\n')
    control.main_choise_control()