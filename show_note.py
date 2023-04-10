import control

def finde_to_data():
    with open('base.csv', encoding='UTF-8') as file:
        for line in file:
            print(line.rstrip())
    control.show_note_control()   



