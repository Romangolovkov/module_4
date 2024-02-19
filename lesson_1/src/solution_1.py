def add_for_buh(first_file: str, last_file: str) -> None:

    first_file_int: int = int(first_file[:-4])
    last_file_int: int = int(last_file[:-4])
    number_files: int = last_file_int - first_file_int + 1
    
    for i in range(number_files):

        with open(str(first_file_int + i) + '.txt', 'r', encoding='utf8') as file:
            content: str = file.read()

            with open('for_buh.txt', 'a', encoding='utf8') as for_buh:
                for_buh.write(content)
                for_buh.write('\n')
    
    print(f'Файлы успешно обработаны! Всего {number_files} шт.')


add_for_buh('1.txt', '3.txt')