from Contact import Contact


def print_menu():
    print("""Меню действий:
1 - Добавить контакт
2 - Посмотреть все контакты
3 - Найти контакт по id
4 - Поиск контакта
5 - Редактировать контакт
6 - Удалить
0 - Выход""")


def add_contact():
    Contact(input('Ведите имя: '),
            input('Ведите фамилию: '),
            input('Ведите телефон: '),
            input('Ведите email: '))
    print('Контакт успешно создан')


def search_by_id():
    id = int(input('Введите id контакта: '))
    print('Результаты поиска : ')
    Contact.search_by_id(id).print_info()
    print('Конец результатов поиска')


def search():
    line = input('Введите строку для поиска: ')
    print('Результаты поиска: ')
    Contact.search_contact(line)
    print('Конец результатов поиска')


def edit_contact():
    id = int(input('Введите id контакта для редактирования: '))
    Contact.search_by_id(id).edit(
        input('Ведите имя: '),
        input('Ведите фамилию: '),
        input('Ведите телефон: '),
        input('Ведите email: ')
    )
    print('Контакт успешно отредактирован')


def delete_contact():
    id = int(input('Введите id контакта, который вы хотите удалить: '))
    Contact.search_by_id(id).delete()
    print('Контакт успешно удален')


menu = 7
while menu != 0:
    match menu:
        case 7:
            print_menu()
        case 1:
            add_contact()
        case 2:
            Contact.print_all()
        case 3:
            search_by_id()
        case 4:
            search()
        case 5:
            edit_contact()
        case 6:
            delete_contact()
    if 1 <= menu <= 6:
        print('----------------------------------------')
        print('Для вызова меню нажмите Enter...')
        str = input('Enter...')
        print_menu()
    menu = int(input())
