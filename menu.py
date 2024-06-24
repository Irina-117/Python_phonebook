from function_menu import read_txt, show_all_file, append_num


def show_menu():
    print(
        "\nВыберите необходимое действие:\n"
        "1. Отобразить весь сравочник\n"
        "2. Добавить абонента в справочник\n"
        "3. Найти абонента\n"
        "4. Скопировать контакт в другой файл\n"
        "5. Переместить контакт в другой файл\n"
        "6. Удалить контакт\n"
        "7. Закончить работу"
    )
    choice = int(input())
    return choice


def work_with_phonebook():
    filename = "phone_book.txt"
    choice = show_menu()
    while choice != 7:
        if choice == 1:
            show_all_file(filename)
        elif choice == 2:
            pass
        elif choice == 3:
            append_num(filename)
    # elif choice==4:

    # elif choice==5:

    # elif choice==6:

    # elif choice==7:

    # elif choice==8:
    choice = show_menu()


work_with_phonebook()
