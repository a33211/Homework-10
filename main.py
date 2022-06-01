from collections import UserDict

class Field:
    pass
class Name(Field):
    def __init__(self, param):
        self.param = param

class Phone(Field):
    def __init__(self, param):
        self.param = param
    def __repr__(self):
        return f'{self.param}'
class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
    def __repr__(self):
        return f'{self.phones}'
    def addPhone(self, phone:Phone):
        self.phones.append(phone)


class AddressBook(UserDict):
    def add_record(self, rec):
        self.data[rec.name.param] = rec


phone_book = AddressBook()


def add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, phone)
    phone_book.add_record(rec)
    print(phone_book)
    return f'Contact {name.param} add successful'
def adds_phone(*args):
    key = args[0]
    phone = Phone(args[1])
    value = phone_book.get(key)
    if value:
        value.addPhone(phone)
        print(phone_book)
    return phone_book
def erase_phone(*args):
    key = args[0]
    phone = Phone(args[1])
    value = phone_book.get(key)
    if value:
        value = value.remove(phone)
    print(phone_book)
    return phone_book
def change_phone(*args):
    pass

COMMANDS = {#show_all:["show all"],
    #hello:["hello"],
    add:["add"],
    adds_phone:['append phone'],
    erase_phone:["erase"],# in command enter command, user, phone number to erase
    #show_all:["show all"],
    # exit:["good bye", "close", "exit"]
}

def parse_command(user_input:str):
    for k,v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")


def main():
    while True:
        user_input = input('Please enter your command')
        result, data = parse_command(user_input)
        print(result(*data))
        if result is exit:
            break
'''Записи Record в AddressBook хранятся как значения в словаре. В качестве ключей используется значение Record.name.value.
Record хранит объект Name в отдельном атрибуте.
Record хранит список объектов Phone в отдельном атрибуте.
Record реализует методы для добавления/удаления/редактирования объектов Phone.
AddressBook реализует метод add_record, который добавляет Record в self.data.'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
