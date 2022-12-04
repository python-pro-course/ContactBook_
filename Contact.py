from ContactController import ContactController


class Contact:
    all = []
    con = ContactController.connect()

    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.id = len(Contact.all) + 1
        Contact.all.append(self)
        ContactController.add_contact(Contact.con, self.name, self.surname, self.phone, self.email)

    @staticmethod
    def print_info(contact):
        for i in contact:
            print(i, end=' ')
        print()

    @staticmethod
    def edit(name, surname, phone, email, id):
        ContactController.update(Contact.con, name, surname, phone, email, id)

    # статический метод не привязан к конкретному объекту
    @staticmethod
    def print_all():
        all_contacts = ContactController.get_all_contacts(Contact.con)
        for contact in all_contacts:
            Contact.print_info(contact)

    @staticmethod
    def get_by_id(id):
        return ContactController.get_by_id(Contact.con, id)

    @staticmethod
    def delete(id):
        ContactController.delete(Contact.con, id)

    @staticmethod
    def search_contact(line):
        all_contacts = ContactController.get_all_contacts(Contact.con)
        for contact in all_contacts:
            for j in range(1, 5):
                if line in contact[j]:
                    print('Результаты поиска: ')
                    Contact.print_info(contact)

