fields = ["Фамилия", "Имя", "Номер", "Город"]


def read_txt(filename: str):
    phone_book = []
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            record = [i.strip() for i in line.split(",")]
            phone_book.append(dict(zip(fields, record)))
    return phone_book


def show_all_file(filename):
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            name, surname, phone, city = line.split(",")
            print(
                name,
                surname,
                phone,
                city,
                sep="  ",
                end="\n",
            )


def append_num(filename):
    with open(filename, "a", encoding="utf-8") as phb:
        surname = input()
        name = input()
        phone = input()
        city = input()
        print(surname, name, phone, city, sep=",", end="\n", file=phb)
