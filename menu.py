from colorama import Fore, init
init(autoreset=True)
import check


def main_choise():
    what_to_do = Fore.LIGHTBLUE_EX + 'Выберите соответствующую цифру в меню:'
    new_note = Fore.WHITE +'1. Добавить новую заметку'
    show_all_note = '2. Показать все заметки'
    find_note = '3. Найти замету'
    to_exit = '4. Выход'

    print(f'{what_to_do}\n{new_note}\n{show_all_note}\n{find_note} \n{to_exit}')
    return check.main_check()

def show_note_choise():
    what_to_do = Fore.LIGHTCYAN_EX + 'Выберите соответствующую цифру в меню:'
    date_sort = Fore.WHITE + '1. Найти заметку по дате'
    theme_sort = '2. Найти заметку по теме'
    chose_note = '3. Выбрать заметку по id'
    to_main_menu = '4. Назад'

    print(f'{what_to_do}\n{date_sort}\n{theme_sort}\n{chose_note}\n{to_main_menu}')
    return check.show_note_check()

def edit_note_choise():
    what_to_do = Fore.LIGHTYELLOW_EX + 'Выберите соответствующую цифру в меню:'
    date_sort = Fore.WHITE + '1. Редактировать заметнку'
    theme_sort = '2. Редактировать тему'
    chose_note = '3. Удалить заметку'
    to_main_menu = '4. Назад'

    print(f'{what_to_do}\n{date_sort}\n{theme_sort}\n{chose_note}\n{to_main_menu}')
    return check.edit_check()