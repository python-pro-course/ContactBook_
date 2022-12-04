import sqlite3 as sq


class ContactController:
    CREATE_TABLE = """CREATE TABLE IF NOT EXISTS contacts
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    phone TEXT,
    email TEXT)"""
    ADD_CONTACT = """INSERT INTO contacts (name, surname, phone, email) VALUES (?, ?, ?, ?)"""
    ALL_CONTACTS = "SELECT * FROM contacts"
    UPDATE = "UPDATE contacts SET name = ?, surname = ?, phone = ?, email = ? WHERE id == ?;"
    DELETE_CONTACT = "DELETE FROM contacts WHERE id == ?;"
    GET_BY_ID = "SELECT * FROM contacts WHERE id == ?;"

    @staticmethod
    def connect():
        return sq.connect('data.db')

    @staticmethod
    def create_table(connection):
        with connection:
            connection.execute(ContactController.CREATE_TABLE)

    @staticmethod
    def add_contact(connection, name, surname, phone, email):
        with connection:
            connection.execute(ContactController.ADD_CONTACT, (name, surname, phone, email))
            connection.commit()

    @staticmethod
    def get_all_contacts(connection):
        with connection:
            return connection.execute(ContactController.ALL_CONTACTS).fetchall()

    @staticmethod
    def update(connection, name, surname, phone, email, id):
        with connection:
            connection.execute(ContactController.UPDATE, (name, surname, phone, email, id))
            connection.commit()

    @staticmethod
    def get_by_id(connection, id):
        with connection:
            return connection.execute(ContactController.GET_BY_ID, (id,)).fetchone()

    @staticmethod
    def delete(connection, id):
        with connection:
            connection.execute(ContactController.DELETE_CONTACT, (id,))
            connection.commit()





