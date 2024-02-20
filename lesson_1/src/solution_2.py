import csv

with open('clients.csv', 'w', encoding='utf8', newline='') as file:
    writer: csv.writer = csv.writer(file)
    writer.writerow(['Name', ' Surname', ' Birthday', ' Bonuses'])

print('Добрый день! Вводите данные: ')

while True:
    name: str = input('Имя: ')

    if name == 'stop':
        break

    surname: str = input('Фамилия: ')
    birthday: str = input('День рождения: ')
    bonuses: str = input('Баланс бонусов: ')
        
    with open('clients.csv', 'a', encoding='utf8', newline='') as file:
        writer: csv.writer = csv.writer(file)
        writer.writerow([name, surname, birthday, bonuses])
    
    print(f'Спасибо! Клиент {name} добавлен!')