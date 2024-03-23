from data import id_data, title_data, text_data
from datetime import datetime
import csv


def write_data():  # создаем новую заметку
    id = id_data()  
    title = title_data()
    text = text_data()
   
    with open('notes.csv', 'a', encoding = 'utf-8') as f:
        time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        f.write(f"{id}; {title}; {text}; {time}\n")

def change_data():  # Изменяем заметки
    n = int(input('Введите номер записи, которую хотите изменить '))
    write_data() # Вызываем функцию для записи новых данных в конец файла и дальнейшей записи в нужную строку
   
    with open('notes.csv','r', encoding = 'utf-8') as f:
        notes = f.readlines()
        change_el = notes.pop()
        notes_list = notes[:n-1] + [change_el] + notes[n:]
    with open('notes.csv','w', encoding = 'utf-8') as f:
            f.writelines(notes_list)

# change_data()      

def delete_data():  # Удаляем заметку файла
    n = int(input('Введите номер записи для удаления: '))

    with open('notes.csv','r', encoding = 'utf-8') as f:
        notes = f.readlines()
        notes_list = notes[:n-1] + notes[n:]
    with open('notes.csv','w', encoding = 'utf-8') as f:
        f.writelines(notes_list)
# delete_data()

def print_data(): # выводим данные из файла с заметками в терминал
    print('Вывожу данные из файла с заметками: \n')

    with open('notes.csv', 'r', encoding = 'utf-8') as f:
        notes = f.readlines()  # прочитали все наши строки
        print(*notes)      # выводим данные на печать, с распаковкой через *
# print_data()

def print_data_line(): # выводим данные из файла с заметками в терминал
    n = int(input('Введите номер заметки для вывода на печать: '))
    
    with open('notes.csv', 'r', encoding = 'utf-8') as f:
        if n not in range (len(f.readlines())):  # если введено не число в рамках количества заметок, просим пользователя повторить ввод
            print("Нет заметки под номером ", n)
            print_data_line()
        else:
            print('Вывожу заметку под номером: ', n)
            f.seek(0) # возвращаемся к началу файла
            notes = f.readlines()  # прочитали все наши строки
            print(notes[n-1])

# print_data_line()
            
def print_date_selection(): 
 with open('notes.csv', 'r', encoding = 'utf-8') as csv_file:
        search_value = input("Введите дату записи/изменения файла для поиска в формате DD.MM.YYYY: ")
        for row in csv_file:
            if (search_value in row): 
                print(row[:-1])
            else:
                print("Запись не найдена.")
                break
# print_date_selection()