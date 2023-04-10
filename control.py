import menu 
import add_note
import data_collector
import show_note
import note_operator

def main_choise_control():
    user_main_choise = menu.main_choise()
    if user_main_choise == 1:
        data = data_collector.input_data()
        add_note.new_note(data)
    if user_main_choise == 2:
        show_note.finde_to_data()
    if user_main_choise == 3:
       show_note_control()
    if user_main_choise == 4:
        print('До новых встречь!')

def show_note_control():
    user_show_note_choise = menu.show_note_choise()
    if user_show_note_choise == 1:
        find_note_by_detail(1, 'Введите дату в формате дд.мм.гггг: ')
    if user_show_note_choise == 2:
        find_note_by_detail(3, 'Введите тему: ')
    if user_show_note_choise == 3:
       find_note_by_detail(0, 'Введите id: ')
    if user_show_note_choise == 4:
        main_choise_control()


def find_note_by_detail(detail, text):
    date = input(text)
    check_flag = False
    res_notes_for_dates = []
    for i in note_operator.read_file_to_list():
        if date == i[detail].split()[1]:
            res_notes_for_dates.append(i)
            check_flag = True
    if check_flag:
        note_operator.print_data(res_notes_for_dates)
    else:
        print('нет заметок')
        show_note_control()
    choise_theme_or_text = menu.edit_note_choise()
    if choise_theme_or_text == 1:
        note_operator.func_to_edit(note_operator.read_file_to_list(), res_notes_for_dates)
    elif choise_theme_or_text == 2:
        note_operator.func_to_edit_theme(note_operator.read_file_to_list(), res_notes_for_dates)
    elif choise_theme_or_text == 3:
        note_operator.delete_note(note_operator.read_file_to_list(), res_notes_for_dates)
    elif choise_theme_or_text == 4:
        main_choise_control()