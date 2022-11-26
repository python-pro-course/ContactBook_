class Contact:
    all = []

    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.id = len(Contact.all) + 1
        Contact.all.append(self)

    def print_info(self):
        print(self.id, self.name,
              self.surname, self.phone,
              self.email, sep=', ')

    def edit(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    # статический метод не привязан к конкретному объекту
    @staticmethod
    def print_all():
        for contact in Contact.all:
            contact.print_info()

    @staticmethod
    def search_by_id(id):
        for contact in Contact.all:
            if id == contact.id:
                return contact

    @staticmethod
    def search_contact(line):
        for contact in Contact.all:
            if line in contact.name or \
                    line in contact.surname or \
                    line in contact.phone or \
                    line in contact.email:
                contact.print_info()

    def delete(self):
        Contact.all.remove(self)3
