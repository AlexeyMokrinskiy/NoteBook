from colorama import Fore, init
init(autoreset=True)

def main_check():
    try:
        input_number = int(input(Fore.LIGHTYELLOW_EX + 'Введите число от 1 до 4: '))
        if 0 < input_number < 5:
            return input_number
        else:
            return main_check()
    except ValueError:
        print(Fore.RED +'Это должно быть число: ')
        return main_check()
        

def show_note_check():
    try:
        input_number = int(input(Fore.LIGHTYELLOW_EX + 'Введите число от 1 до 4: '))
        if 0 < input_number < 5:
            return input_number
        else:
            return show_note_check()
    except ValueError:
        print(Fore.RED +'Это должно быть число: ')
        return show_note_check()
    

def find_check():
    try:
        input_number = int(input(Fore.LIGHTYELLOW_EX + 'Введите число от 1 до 4: '))
        if 0 < input_number < 5:
            return input_number
        else:
            return find_check()
    except ValueError:
        print(Fore.RED +'Это должно быть число: ')
        return find_check()
    

def edit_check():
    try:
        input_number = int(input(Fore.LIGHTYELLOW_EX + 'Введите число от 1 до 4: '))
        if 0 < input_number < 5:
            return input_number
        else:
            return edit_check()
    except ValueError:
        print(Fore.RED +'Это должно быть число: ')
        return edit_check()