from functional_record import create_registration, output, search_record, update_record


def menu():
    """Функция меню для удобного использования"""

    print("Рад приветствовать вас!")
    choice = input("Выберите, что вы хотите сделать:\n1 - Добавить новую запись,\n2 - Изменить запись,\n3 - Найти запись,\n4 - Показать записи\n")
    if choice == '1':
        create_registration.creating_record()
        answer = input('Вы хотите вернуться в главное меню? 1 - Да, 2 - Нет ')
        if answer == '1':
            menu()
        else:
            print("Всего доброго!")
            return

    elif choice == "2":
        update_record.update()
        answer = input('Вы хотите вернуться в главное меню? 1 - Да, 2 - Нет ')
        if answer == '1':
            menu()
        else:
            print("Всего доброго!")
            return

    elif choice == "3":
        search_record.search()
        answer = input('Вы хотите вернуться в главное меню? 1 - Да, 2 - Нет ')
        if answer == '1':
            menu()
        else:
            print("Всего доброго!")
            return

    elif choice == "4":
        output.information_output()
        answer = input('Вы хотите вернуться в главное меню? 1 - Да, 2 - Нет ')
        if answer == '1':
            menu()
        else:
            print("Всего доброго!")
            return


