import json


def information_output():
    """Функция, которая выводит записи из файла"""

    with open('functional_record/telephone_directory.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        for item in text:
            print(
                f"Имя: {item['name']}\n"
                f"Фамилия: {item['surname']}\n"
                f"Отчество: {item['patronymic']}\n"
                f"Название организации: {item['organization_name']}\n"
                f"Рабочий номер телефона: {item['work_phone']}\n"
                f"Личный номера телефона: {item['personal_phone']}"
            )
            print("************************************************")
