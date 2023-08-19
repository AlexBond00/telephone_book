import json


def collecting_info():
    """Функция, которая получает от пользовтаеля информацию по записи, чтобы дальше ее использовать"""

    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    organization_name = input("Введите название организации: ")
    work_phone = input("Введите рабочий номер телефона: ")
    personal_phone = input("Введите личный номера телефона: ")
    human_info = {
        "name": name,
        "surname": surname,
        "patronymic": patronymic,
        "organization_name": organization_name,
        "work_phone": work_phone,
        "personal_phone": personal_phone
    }
    return human_info



def creating_record():
    """Функция, которая создает новую запись, заменяя пустые поля на "Данных нет" """

    info = collecting_info()
    for key, value in info.items():
        if value == "":
            info[key] = "Данных нет"

    with open("functional_record/telephone_directory.json", mode='r', encoding='utf-8') as file:
        feeds = json.load(file)

    with open("functional_record/telephone_directory.json", mode='w', encoding='utf-8') as feedsjson:
        feeds.append(info)
        json.dump(feeds, feedsjson)

    print("Добавление контактной информации в справочник прошло успешно!")

