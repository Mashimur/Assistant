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
        phone = Phone(phone)
        if phone:
            lst = [phone.value for phone in self.phone_numbers]
            if phone.value not in lst:
                self.phone_numbers.append(phone)

    def change_phone_number(self, old_phone_number, new_phone_number):
        old_phone = Phone(old_phone_number)
        new_phone = Phone(new_phone_number)
        for phone in self.phone_numbers:
            if phone.value == old_phone.value:
                self.phone_numbers.remove(phone)
                self.phone_numbers.append(new_phone)

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
    rec = Record(Name('Bill'), Phone('123456'))
    rec.add_phone_number(Phone('098765'))
    print(len(rec.phone_numbers) == 2)  # True
    rec.change_phone_number(Phone('123456'), Phone('667890'))
    print(rec.phone_numbers)