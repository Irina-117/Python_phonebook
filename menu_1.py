from function import (
    read_txt,
    show_all_file,
    append_num,
    find_person,
    remove_contact,
    with_ind,
    copy_contact,
)


def show_menu():
    print(
        "\nВыберите необходимое действие:\n"
        "1. Отобразить весь сравочник\n"
        "2. Найти абонента\n"
        "3. Добавить абонента в справочник\n"
        "4. Скопировать контакт в другой файл\n"
        "5.Удалить контакт\n"
        "6. Закончить работу"
    )
    choice = int(input())
    return choice


def work_with_phonebook():
    choice = show_menu()
    filename = "phone_book.txt"
    filename_2 = "phone_book_2.txt"
    while choice != 6:
        phb_list = read_txt(filename)
        if choice == 1:
            show_all_file(phb_list)
        elif choice == 2:
            str = input("Введите информацию о человеке, которого хотите найти:")
            find_person(filename, str)
        elif choice == 3:
            append_num(filename)
        elif choice == 4:
            copy_contact(filename, filename_2)

        elif choice == 5:
            remove_contact(filename)
        choice = show_menu()


work_with_phonebook()
