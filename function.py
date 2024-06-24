fields = ["Фамилия", "Имя", "Номер", "Город"]


def read_txt(filename: str):
    phone_book = []
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            record = [i.strip() for i in line.split(",")]
            phone_book.append(dict(zip(fields, record)))
    return phone_book


def show_all_file(filename):
    for line in filename:
        for k, v in line.items():
            print(f"{k}: {v}")
        print()


def append_num(filename):
    with open(filename, "a", encoding="utf-8") as phb:
        surname = input("Введите фамилию:")
        name = input("Введите имя:")
        phone = input("Введите номер телефона:")
        city = input("Введите город:")
        print(
            surname,
            name,
            phone,
            city,
            sep=",",
            file=phb,
        )


def find_person(filename, str):
    with open(filename, "r", encoding="utf-8") as phb:
        counter = 0
        list1 = phb.readlines()
        for line in list1:
            if str.lower() in line.lower():
                print(line)
            elif str.lower() not in line.lower():
                counter += 1
            if counter == len(list1):
                print("Абонент не найден.")


def with_ind(filename):
    with open(filename, "r", encoding="utf-8") as phb:
        ind = 1
        print("Список контактов:")
        for line in phb:
            surname, name, phone, city = line.split(",")
            print(f"{ind}", surname, name, phone, city, end="")
            ind += 1
        return ind - 1


def remove_contact(filename):
    print("\n")
    lenn = with_ind(filename)
    print("\n")
    i = int(input("Введите номер строки, которую необходимо удалить: "))
    with open(filename, "r", encoding="utf-8") as phb:
        data = []
        data = phb.readlines()
        with open(filename, "w", encoding="utf-8") as phb:
            phb.writelines(data[: int(i) - 1])
            phb.writelines(data[i:])
        with_ind(filename)


def copy_contact(filename, filename_2):
    print("\n")
    with_ind(filename)
    print("\n")
    with open(filename, "r", encoding="utf-8") as phb:
        i = int(
            input(
                "Введите номер контакта, который необходимо скопировать в другой файл: "
            )
        )
        file = phb.readlines()
        with open(filename_2, "a", encoding="utf-8") as copy:
            copy.write(file[i - 1])
            copy.seek(0)
            show_all_file(read_txt(filename_2))
