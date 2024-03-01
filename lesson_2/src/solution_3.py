import csv
import json
from json import JSONEncoder
from datetime import date

with open('clients.csv', 'w', encoding='utf8', newline='') as file:
    writer: csv.writer = csv.writer(file)
    writer.writerow(['Name', 'Surname', 'Birthday', 'Bonuses'])
    writer.writerow(['Роман', 'Горбачёв', '28.01.1989', '9999999'])
    writer.writerow(['Игорь', 'Распутин', '01.02.1003', '1000'])
    writer.writerow(['Анна', 'СилFина', '10.10.2000', '500000'])
    writer.writerow(['Юлия', 'Пугачева', '15.03.1991', '-1'])
    writer.writerow(['Роман', 'Головков', '01.03.1991', '0'])


def check_cyrillic(text: str) -> bool:
    for elem in text.lower():
        if ord(elem) < 1072 or ord(elem) > 1103 and ord(elem) != 1105:
            return False
    return True
    

class Client:
    def __init__(self, name: str, surname: str, birthday: str, bonuses: int) -> None:
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses
        
    def check_name(self) -> bool:
        if check_cyrillic(self.name) and check_cyrillic(self.surname):
            return True
        return False
    
    def check_birthday(self) -> bool:
        year: int = int(self.birthday.split('.')[2])
        month: int = int(self.birthday.split('.')[1])
        day: int = int(self.birthday.split('.')[0])
        birthday: date = date(year, month, day)

        if 1950 <= year and birthday < date.today():
            return True
        return False
    
    def check_bonuses(self) -> bool:
        if 0 <= int(self.bonuses) <= 10000000:
            return True
        return False
    
    def correct_attributes(self) -> bool:
        return (self.check_name() and self.check_birthday() and self.check_bonuses())


clients: dict[str: list] = {"clients": []}
uncorrect_clients: int = 0

with open('clients.csv', 'r', encoding='utf8') as file:
    clients_list: list[list[str]] = list(csv.reader(file))
    headers: list[str] = clients_list[0]
    for i in clients_list[1:]:
        client = Client(i[0], i[1], i[2], i[3])
        if client.correct_attributes():
            clients['clients'].append(client)
        else:
            uncorrect_clients += 1
    correct_clients: int = len(clients['clients'])
    

class CustomEncoder(JSONEncoder):
    def default(self, o: any) -> dict[str: list[dict[str: str]]|str]:
        if isinstance(o, Client):
            return {headers[0]: o.name, headers[1]: o.surname, headers[2]: o.birthday, headers[3]: o.bonuses}
        return super().default(o)


with open('clients.json', 'w', encoding='utf8') as file:
    json.dump(clients, file, ensure_ascii=False, cls=CustomEncoder)
    print(f'Было обработано(клиентов): {correct_clients}')
    print(f'Было пропущено(клиентов): {uncorrect_clients}')