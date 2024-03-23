from CW import write_data, print_data, change_data, delete_data, print_data_line, print_date_selection

def interface():
    print("Добрый день! Вы попали бот заметок от Anna \n 1 - запись данных \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных \n 5 - вывод конкретной заметки \n 6 - выборка по дате")
    command = int(input('Введите число '))  # принимаем данные из консоли сразу в виде числа

    while command not in range(1,7):  # если введено не число от 1 до 6 включительно, просим пользователя повторить ввод
        print("Неправильный ввод")
        command = int(input('Введите число '))

    if command == 1:
        write_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()
    elif command == 5:
        print_data_line()
    elif command == 6:
        print_date_selection()

interface() # вызываем функцию, чтобы ее запустить