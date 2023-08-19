import json

from functional_record.search_record import search
from functional_record.create_registration import collecting_info


def update():
    """В этой функции сначала идет вызов функции поиска, после фуункции ввода,
    дальше идет замена найденнй функции на введенную пользователем"""

    count = search()
    print("Введите данные для замены")
    info = collecting_info()


    with open('functional_record/telephone_directory.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        text[count] = info
        print("Данные изменены!")
        print(
            f"Имя: {text[count]['name']}\n"
            f"Фамилия: {text[count]['surname']}\n"
            f"Отчество: {text[count]['patronymic']}\n"
            f"Название организации: {text[count]['organization_name']}\n"
            f"Рабочий номер телефона: {text[count]['work_phone']}\n"
            f"Личный номера телефона: {text[count]['personal_phone']}"
        )
