from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Phone(Field):
    @staticmethod
    def sanitize_phone_number(phone):
        new_phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        try:
            new_phone = [str(int(i)) for i in new_phone]
        except ValueError:
            print("Phone number was entered incorrectly!")
        else:
            new_phone = "".join(new_phone)
            if len(new_phone) == 12:
                return f"+{new_phone}"
            elif len(new_phone) == 10:
                return f"+38{new_phone}"
            else:
                print("Phone number was entered incorrectly! Please check phone`s number length")

    def __init__(self, value):
        self._value = Phone.sanitize_phone_number(value)

    @Field.value.setter
    def value(self, value):
        self._value = Phone.sanitize_phone_number(value)


class Name(Field):
    def __str__(self):
        return self._value.title()


class Birthday(Field):
    @staticmethod
    def validate_date(birthday):
        try:
            birthday = datetime.strptime(
                birthday, "%d.%m.%Y"
            )
        except ValueError:
            print("Birthday was entered incorrectly!")
            return None
        else:
            return str(birthday.date())

    def __init__(self, value):
        self._value = Birthday.validate_date(value)

    def __repr__(self):
        return str(self._value)

    @property
    def birthday(self):
        return self._value

    @birthday.setter
    def birthday(self, value):
        self._value = Birthday.validate_date(value)


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phone_numbers = []
        self.birthday = birthday
        if isinstance(phone, Phone):
            self.phone_numbers.append(phone)
        if isinstance(birthday, Birthday):
            self.birthday = birthday
        else:
            self.birthday = None

    def add_phone_number(self, phone):
        if phone:
            lst = [phone.value for phone in self.phone_numbers]
            if phone.value not in lst:
                self.phone_numbers.append(phone)

    def change_phone_number(self, old_phone, new_phone):
        for phone in self.phone_numbers:
            if phone.value == old_phone.value:
                self.phone_numbers.remove(phone)
                self.phone_numbers.append(new_phone)

    def remove_phone_number(self, old_phone):
        for phone in self.phone_numbers:
            if phone.value == old_phone.value:
                self.phone_numbers.remove(phone)

    def days_to_birthday(self):
        current_date = datetime.now().date()
        current_birth = datetime(year=int(datetime.now().year), month=int(self.birthday.value[5:7]), day=int(self.birthday.value[8:10])).date()
        delta = current_birth - current_date
        if int(delta.days) >= 0:
            return f"User {self.name}'s birthday will be in {delta.days} days"
        else:
            next_year_birth = datetime(year=int(datetime.now().year) + 1, month=int(self.birthday.value[5:7]), day=int(self.birthday.value[8:10])).date()
            delta = next_year_birth - current_date
            return f"User {self.name}'s birthday will be in {delta.days} days"

    def add_birthday(self, birthday):
        if isinstance(birthday, Birthday):
            self.birthday = birthday
        else:
            self.birthday = Birthday(birthday)

    def show_contact(self):
        return {"name": self.name, "phone": self.phone_numbers}

    def get_contact(self):
        phones = ", ".join([str(p) for p in self.phone_numbers])
        return {
            "name": str(self.name.value),
            "phone": phones,
            "birthday": self.birthday.value,
        }


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def remove_record(self, record):
        self.data.pop(record.name.value, None)

    def show_records(self):
        return {key: value.get_contact() for key, value in self.data.items()}

    def iterator(self):
        for record in self.data.values():
            yield record.get_contact()


if __name__ == '__main__':
    # Перевірка
    rec = Record(Name("Bill"), Phone("0958481169"), Birthday("17.03.2003"))
    rec.add_phone_number(Phone("0505688424"))
    rec.remove_phone_number(Phone("0958481169"))
    rec.change_phone_number(Phone("0505688424"), Phone("0958001170"))
    rec1 = Record(Name("Den"), Phone("0979001260"), Birthday("26.12.2004"))
    rec1.add_birthday("19.10.1996")
    rec1.add_phone_number(Phone("0505008323"))
    rec1.remove_phone_number(Phone("0979001260"))
    rec1.change_phone_number(Phone("0505008323"), Phone("0636121320"))
    print(rec.get_contact())
    print(rec1.get_contact())
    test_ABook = AddressBook()
    test_ABook.add_record(rec)
    test_ABook.add_record(rec1)
    print(test_ABook.show_records())
    test_ABook.remove_record(rec1)
    print(test_ABook.show_records())
    rec.add_birthday(Birthday("17.01.2002"))
    print(rec.get_contact())
    print(rec.days_to_birthday())
    p = Phone("12345")
