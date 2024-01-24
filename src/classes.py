from datetime import datetime
from collections import UserDict
import re
import pickle


class Field:

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self._validate(new_value)
        self.__value = new_value

    def _validate(self, value):
        pass

    def __str__(self):
        return str(self.__value)


class Name(Field):
    """class for validate name field"""

    def _validate(self, value):
        name_pattern = re.compile(r'^[a-zA-Z0-9а-яА-Я\s]+$')

        if len(value) < 1 or not name_pattern.match(value):
            raise ValueError("Invalid name format")

        return f'{value} is a valid name'


class Phone(Field):
    """class for validate phone field"""

    def _validate(self, value):
        pattern = re.compile(r"^((\+?3)?8)?0\d{9}$")
        if not pattern.match(value):
            raise ValueError("Phone number is not valid.\n"
                             "Example of correct number entry: "
                             "0991234567 or +380991234567")
        return f'{value} is valid phone number'


class Birthday(Field):
    """class for validating birthday field"""

    def _validate(self, value):
        separators = ["-", "/", " ", "."]
        day, month, year = None, None, None
        for sep in separators:
            if sep in value:
                try:
                    day, month, year = map(int, value.split(sep))
                    break
                except ValueError:
                    pass
        if day is None or month is None or year is None:
            raise ValueError(
                'Incorrect date format. Must be in dd-mm-yyyy,dd/mm/yyyy, '
                'dd mm yyyy, or dd.mm.yyyy')
        if 1 <= day <= 31 and 1 <= month <= 12 and len(str(year)) == 4:
            return f'{value} is valid birthday'
        else:
            raise ValueError('Invalid date: {value}. The date is not correct.')


class Email(Field):
    def _validate(self, value):
        pattern = (
            r'^((([0-9A-Za-z]{1}[-0-9A-z\.]{1,}[0-9A-Za-z]{1})|'
            r'([0-9А-Яа-я]{1}[-0-9А-я\.]{1,}[0-9А-Яа-я]{1}))@'
            r'([-A-Za-z]{1,}\.){1,2}[-A-Za-z]{2,})$'
        )
        if not re.match(pattern, value):
            raise ValueError("Invalid email address.\n"
                             "Example of correct number entry: "
                             "example@test.com")


class Address(Field):
    def _validate(self, value):
        # No special validation for address
        pass


class Title(Field):
    """class for validating the title of the note"""

    def _validate(self, value):
        # Title starts with a letter, can contain numbers
        pattern = re.compile(r'^[a-zA-Zа-яА-Я][a-zA-Z0-9а-яА-Я\s]*$')
        if not value or not pattern.match(value):
            raise ValueError(
                "Invalid title format. Title must start with a letter, "
                "can contain numbers and cannot be empty.")
        return f"'{value}' is a valid title for the note"


class Note:
    """class represents a single note with text"""

    def __init__(self, author, title, body, tags):
        self.author = Name(author)
        self.title = Title(title)
        self.body = body
        self.tags = tags if tags else []
        self.created_at = datetime.now()  # Time of note creation

    def edit_note(self, new_body):
        self.body = new_body

    def edit_note_title(self, new_title):
        self.title.value = new_title

    def to_dict(self):
        # Convert the Note instance into a dictionary
        return {
            'author': self.author.value,
            'title': self.title.value,
            'body': self.body,
            'tags': self.tags
        }

    @classmethod
    def from_dict(cls, notes):
        # Create a new Note instance from a dictionary
        record = cls(notes['author'], notes['title'],
                     notes['body'], notes['tags'])
        return record

    def __str__(self):
        return f"\nAuthor: {self.author}\n\
        Title: {self.title}\n\
        Created at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n\
        Note: {self.body}\nTags: {self.tags}\n"


class Notebook(UserDict):
    """class for managing a collection of notes"""

    def add_note(self, note):
        self.data[note.title.value] = note

    def find_notes(self, query):
        query_lower = query.lower()
        return [
            note for note in self.data.values()
            if query_lower in note.title.value.lower()
            or query_lower in note.body.lower()
            or query_lower in note.author.value.lower()]

    def delete_note(self, title):
        if title in self.data:
            del self.data[title]
            return True
        return False

    def get_note(self, title):
        return self.data.get(title, None)

    @staticmethod
    def tag_conversion(tags):
        if not tags:
            return ''
        tags = re.findall(r'#?\w+', tags)
        unique_tags = list(set(tags))
        sorted_tags = sorted(unique_tags, key=lambda x: x.lower())
        if sorted_tags[0].startswith("#"):
            str_tag = ', '.join([f'{tag}' for tag in sorted_tags])
        else:
            str_tag = ', '.join([f'#{tag}' for tag in sorted_tags])
        return str_tag

    def add_tags(self, title, new_tags):
        note = self.data[title]
        current_tags = note.tags
        updated_tags = self.tag_conversion(current_tags + ', ' + new_tags)
        note.tags = updated_tags

    def sort_notes_by_tags(self):
        sorted_notes = sorted(
            self.data.values(),
            key=lambda note: (len(note.tags),
                              sorted(note.tags, key=lambda tag: tag[1:])))
        return sorted_notes

    def find_notes_by_tags(self, query):
        return [note for note in self.data.values() if query in note.tags]

    def remove_tags(self, title, tags_to_remove):
        if title in self.data:
            current_tags = self.data[title].tags.split(', ')
            updated_tags = [
                tag for tag in current_tags if tag not in tags_to_remove]
            self.data[title].tags = ', '.join(updated_tags)
            return True
        return False


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.addresses = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return f'Number phone {phone} has been add'

    def add_email(self, email):
        self.emails.append(Email(email))
        return f'Email {email} has been add'

    def add_address(self, address):
        self.addresses.append(Address(address))
        return f'Address {address} has been add'

    def update_birthday(self, new_birthday):
        if self.birthday is not None:
            self.birthday.value = new_birthday
        else:
            self.birthday = Birthday(new_birthday)

    def remove_phone(self, phone):
        tel = Phone(phone)
        if tel.value in [item.value for item in self.phones]:
            self.phones = [
                item for item in self.phones if tel.value != item.value]
            return (f'Number phone {phone} has been removed '
                    f'from contact {self.name.value}.')
        else:
            return (f'Phone number {phone} not found '
                    f'in contact {self.name.value}.')

    def edit_name(self, name_new):
        self.name.value = name_new
        return f'Name has been changed to {name_new}'

    def edit_phone(self, phone_old, phone_new):
        tel_new = Phone(phone_new)
        for item in self.phones:
            if phone_old == item.value:
                idx = self.phones.index(item)
                self.phones.remove(item)
                self.phones.insert(idx, tel_new)
                return (f'Number phone {phone_old} has been changed '
                        f'to {tel_new.value}')
        raise ValueError("Phone number not found for changing")

    def remove_email(self, email):
        tel = Email(email)
        if tel.value in [item.value for item in self.emails]:
            self.emails = [
                item for item in self.emails if tel.value != item.value]
            return (f'Number email {email} has been removed '
                    f'from contact {self.name.value}.')
        else:
            return (f'email number {email} not found '
                    f'in contact {self.name.value}.')

    def edit_email(self, email_old, email_new):
        tel_new = Email(email_new)
        for item in self.emails:
            if email_old == item.value:
                idx = self.emails.index(item)
                self.emails.remove(item)
                self.emails.insert(idx, tel_new)
                return (f'Number email {email_old} has been changed '
                        f'to {tel_new.value}')
        raise ValueError("Email number not found for changing")

    def remove_address(self, address):
        tel = Address(address)
        if tel.value in [item.value for item in self.addresses]:
            self.addresses = [
                item for item in self.addresses if tel.value != item.value]
            return (f'Number address {address} has been removed '
                    f'from contact {self.name.value}.')
        else:
            return (f'address number {address} not found '
                    f'in contact {self.name.value}.')

    def edit_address(self, address_old, address_new):
        tel_new = Address(address_new)
        for item in self.addresses:
            if address_old == item.value:
                idx = self.addresses.index(item)
                self.addresses.remove(item)
                self.addresses.insert(idx, tel_new)
                return (f'Number address {address_old} has been changed '
                        f'to {tel_new.value}')
        raise ValueError("Address number not found for changing")

    def find_phone(self, phone):
        tel = Phone(phone)
        return next(
            (item for item in self.phones if tel.value == item.value), None)

    def days_to_birthday(self):
        today = datetime.now()
        if self.birthday is not None and self.birthday.value is not None:
            birth_day = self.birthday.value
            birth_day = [
                birth_day.replace(i, '-') for i in './- ' if i in birth_day][0]
            birth_day = datetime.strptime(birth_day, "%d-%m-%Y")
            next_birthday = datetime(
                today.year, birth_day.month, birth_day.day)
            if today > next_birthday:
                next_birthday = datetime(
                    today.year + 1, birth_day.month, birth_day.day)
            days_until_birthday = (next_birthday - today).days
            return days_until_birthday
        else:
            raise ValueError('Birthday is not set')

    def to_dict(self):
        return {
            'name': self.name.value,
            'phones': [phone.value for phone in self.phones],
            'emails': [email.value for email in self.emails],
            'addresses': [address.value for address in self.addresses],
            'birthday': self.birthday.value if (self.birthday and hasattr(
                self.birthday, 'value')) else None
        }

    @classmethod
    def from_dict(cls, data):
        record = cls(name=data['name'], birthday=data['birthday'])
        for phone in data['phones']:
            record.add_phone(phone)
        for email in data['emails']:
            record.add_email(email)
        for address in data['addresses']:
            record.add_address(address)
        return record

    def __str__(self):
        return f"Contact name: {self.name.value},\
             phones: {'; '.join(p.value for p in self.phones)},\
             emails: {'; '.join(e.value for e in self.emails)},\
             addresses: {'; '.join(a.value for a in self.addresses)}"


class AddressBook(UserDict):

    def add_record(self, obj):
        key = str(obj.name)
        if key in self.data:
            existing_record = self.data[key]
            for phone in obj.phones:
                if phone not in existing_record.phones:
                    existing_record.phones.append(phone)
            if obj.birthday:
                existing_record.birthday = obj.birthday
            print(f"Information added to existing contact: {key}")
        else:
            self.data[key] = obj

    def find(self, name):
        for record in self.data.values():
            if name.lower() == record.name.value.lower():
                return record
        return None

    def clear_all_contacts(self):
        yes_no = input('Are you sure you want to delete all users? '
                       '(y/n) ').lower().strip()
        if yes_no == 'y':
            self.data.clear()
            return "All contacts cleared."
        else:
            return 'Removal canceled'

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f'{name} not found')

    def iterator(self, n=4):
        for i in range(0, len(self.data), n):
            yield list(self.data.values())[i:i + n]

    def save_to_disk(self, filename, notebook):
        data = {
            'contacts': [record.to_dict() for record in self.data.values()],
            'notes': notebook.data
        }
        try:
            with open(filename, 'wb+') as file:
                pickle.dump(data, file)
        except FileNotFoundError:
            print(f"Error: The specified directory or file '{filename}' "
                  "does not exist.")
        except Exception as e:
            print(f"Error saving data to '{filename}': {str(e)}")

    def load_from_disk(self, filename, notebook):
        try:
            with open(filename, 'rb+') as file:
                print(f"\nReading data from {filename}")
                data = pickle.load(file)
                self.data.clear()  # Clear existing data
                notebook.data.clear()
                for record_data in data.get('contacts', []):  # Load contact
                    record = Record.from_dict(record_data)
                    self.data[str(record.name)] = record
                notebook.data.update(data.get('notes', {}))  # Load notes data
        except FileNotFoundError:
            print("File not found. Creating a new file.")
        except Exception as e:
            print(f"Error loading data: {str(e)}")

    def search_contacts(self, query):
        results = []
        query = query.lower()
        for record in self.data.values():
            if (
                query in record.name.value.lower() or
                any(query in phone.value for phone in record.phones)
            ):
                results.append(record)
        return results

    def search_by_birthday(self, number_of_days):
        self._contact = []
        for i in self.data.values():
            self._birth_date = i.days_to_birthday()
            if int(number_of_days) > self._birth_date:
                self._contact.append(i)
        return self._contact
