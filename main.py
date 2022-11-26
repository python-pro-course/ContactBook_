from Contact import Contact

# c = Contact(input('Введите имя: '),
#             input('Введите фамилию: '),
#             input('Введите телефон: '),
#             input('Введите email: '))

roman = Contact('Роман', 'Петров', '911', 'roman@mail.ru')
# c.print_info()
# roman.edit('Александр', 'Петров', '911', 'roman@mail.ru')
# roman.print_info()
Contact.search_by_id(1).print_info()


# line = 'Hello'
# if 'ell' in line:
#     print('да')
# else:
#     print('нет')
