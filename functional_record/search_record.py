import json
from functional_record.create_registration import collecting_info


def filter_dict():
    """Функция, котораая принимает ловарь введенных даанных пользователем для поискаа записи.
    Она удаляет пустые поля и возвращает словарь с только заполненными значениями."""

    print("Введите данные, по которым хотите искать запись.")
    info = collecting_info()
    del_list = []
    for key, value in info.items():
        if value == "":
            del_list.append(key)

    for item in del_list:
        del info[item]

    return info


def search():
    """Функция, которая проходится поо файлу и ищет соответствие
    нашего словаря для поискак с теми, которые уже в файле"""

    dict_info = filter_dict()
    count = 0

    with open('functional_record/telephone_directory.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        for i_dict in text:
            if set(dict_info).issubset(i_dict):
                print("Нашел!")
                print(i_dict)
            else:
                print("Не нашел")
            count += 1
        print(dict_info)
    return count-1






