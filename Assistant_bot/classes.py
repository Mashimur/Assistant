from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

class Phone(Field):
    pass

class Name(Field):
    pass

class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phone_numbers = []
        if isinstance(phone, Phone):
            self.phone_numbers.append(phone)

    def add_phone_number(self, phone):
        self.phone.append(phone)

    def change_phone_number(self, phone):
        self.phone_numbers = phone

    def remove_phone_number(self):
        self.phone_numbers = []

    def show_contact(self):
        return {"name": self.name, "phone": self.phone_numbers}


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def remove_record(self, record):
        self.data.pop(record.name.value, None)

    def show_records(self):
        return self.data


if __name__ == '__main__':
    # Перевірка
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phone_numbers, list)
    assert isinstance(ab['Bill'].phone_numbers[0], Phone)
    assert ab['Bill'].phone_numbers[0].value == '1234567890'

    print('All Ok)')