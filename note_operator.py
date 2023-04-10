from colorama import Fore, init
init(autoreset=True)
import control

def delete_note(file_data, res_notes_for_dates):
    for idx, i in enumerate(file_data):
        if i[0] == res_notes_for_dates[0][0]:
            index_to_delete = idx
            break
    file_data.pop(index_to_delete)
    open('base.csv', 'w').close()
    final_str = ''
    for i in file_data:
        final_str += '\n'.join([str(i[0]), str(i[1]), str(i[2]), str(i[3])]) + '\n\n'
    final_str = final_str.rstrip().rstrip()
    with open('base.csv', 'w', encoding='UTF-8') as file:
        file.write(final_str)
    print(Fore.LIGHTGREEN_EX + 'Запись удалена')
    control.show_note_control()

def func_to_edit(file_data, res_notes_for_dates):
    new_note_text = input('Введите новый текст заметки: ')
    for idx, i in enumerate(file_data):
        if i[0] == res_notes_for_dates[0][0]:
            file_data[idx][3] = new_note_text
    open('base.csv', 'w').close()
    final_str = ''
    for i in file_data:
        final_str += '\n'.join([str(i[0]),str(i[1]),str(i[2]),'Заметка: ' + str(i[3])]) + '\n\n'
    final_str = final_str.rstrip().rstrip()
    with open('base.csv', 'w', encoding='UTF-8') as file:
        file.write(final_str)
    print(Fore.LIGHTGREEN_EX + 'Запись успешно изменина')
    control.show_note_control()

def func_to_edit_theme(file_data, res_notes_for_dates):
    new_note_text = input('Введите новую тему заметки: ')
    for idx, i in enumerate(file_data):
        if i[0] == res_notes_for_dates[0][0]:
            file_data[idx][2] = new_note_text
    open('base.csv', 'w').close()
    final_str = ''
    for i in file_data:
        final_str += '\n'.join([str(i[0]),str(i[1]),'Тема: ' + str(i[2]),str(i[3])]) + '\n\n'
    final_str = final_str.rstrip().rstrip()
    with open('base.csv', 'w', encoding='UTF-8') as file:
        file.write(final_str)
    print(Fore.LIGHTGREEN_EX + 'Запись успешно изменина')
    control.show_note_control()

def print_data(lst_to_print):
    for note in lst_to_print:
        for i in note:
            print(i)
        print()

def read_file_to_list():
    filename = 'base.csv'
    f = open(filename, 'r', encoding='UTF-8')
    a = f.read()
    s = a.split('\n\n')
    res = []
    for i in s:
        tmp = i.split('\n')
        res.append(tmp)
    return res

