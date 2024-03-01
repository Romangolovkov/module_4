import csv
import json
from datetime import date

with open('clients.csv', 'w', encoding='utf8', newline='') as file:
    writer: csv.writer = csv.writer(file)
    writer.writerow(['Name', 'Surname', 'Birthday', 'Bonuses'])
    writer.writerow(['Роман', 'Горбачёв', '28.01.1989', '9999999'])
    writer.writerow(['Игорь', 'Распутин', '01.02.2003', '1000'])
    writer.writerow(['Анна', 'Силина', '10.10.2000', '500000'])
    writer.writerow(['Юлия', 'Пугачева', '15.03.1991', '-1'])

with open('clients.csv', 'r', encoding='utf8') as file:
    content: list[list[str]] = list(csv.reader(file))
    headers: list[str] = content[0]


def check_cyrillic(text: str) -> bool:
    for elem in text.lower:
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
        if 0 <= self.bonuses <= 10000000:
            return True
        return False




with open('clients.json', 'w', encoding='utf8') as file:
    json.dump(content, file, ensure_ascii=False)

print()