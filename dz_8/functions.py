def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        return print(file.read())

def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone_num}')

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Поиск подстроки: ')
    return search(data, contact_to_find)


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    a = list(filter(lambda x: info.lower() in x.lower(), book))
    if len(a) == 0:
        print('\nНичего не найдено! Проверьте вводные данные и повторите поиск.\n')
        return find_data()
    while len(a) != 1:
        input_info = input('\nНайдено несколько строк. Дя сужения области поиска добавьте информацию: ')
        a = list(filter(lambda x: input_info.lower() in x.lower(), a))
    return a

def refactor_data():
    '''Позволяет изменять и удалять данные'''
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    result = search(data, input('Поиск строки для изменения: '))
    new_data = data.replace(*result, input(f'\nВведите новые данные для изменения строки: ') + '\n')
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(new_data)
        print('\nДанные изменены!\n')

def del_data():
    import re

    with open('book.txt', 'r', encoding='utf-8') as f:
        line = f.read()

    str_for_del = search(line, input('\nВведите строку для удаления: '))
    line = line.replace(*str_for_del, '').strip('\n')
    line = '\n'.join([i for i in line.split('\n') if len(i) != 0])

    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(line)
        print('\nДанные успешно удалены!\n')