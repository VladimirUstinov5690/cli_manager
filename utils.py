import os

from tabulate import tabulate


def change_file_name(filename, dest_path):
    """Изменяет имя файла и возвращает новый путь"""
    name, ext = os.path.splitext(filename)
    count = 1
    while True:
        new_file = f'{name}_copy{count}{ext}'
        new_path = os.path.join(dest_path, new_file)
        if not os.path.isfile(new_path):
            break
        count += 1
    return new_path


def pretty_print(data: list[tuple], columns: list):
    """Красиво отображает таблицу"""
    return tabulate(data, headers=columns, tablefmt='grid')