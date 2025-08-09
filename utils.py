import os

from tabulate import tabulate
from datetime import datetime


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


def get_create_file_date(filename: str) -> str:
    """Возвращает дату создания файла в формате dd.mm.YY"""
    timestamp = os.path.getctime(filename)
    create_date_file = datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y')
    return create_date_file


def create_new_file(path_file: str) -> str:
    """Добавляет к имени файла, дату создания.
    Возвращает полный путь к файлу."""
    path_dir = os.path.dirname(path_file)
    filename = os.path.basename(path_file)
    create_date = get_create_file_date(path_file)
    
    if create_date in filename:
        return path_file
    
    file, ext = os.path.splitext(filename)
    new_filename = f'{file}_{create_date}{ext}'
    new_path = os.path.join(path_dir, new_filename)
    
    return new_path


def size_calculation(size):
    """Преобразует размер в байты, килобайты, мегабайты, гигабайты, терабайты"""
    for unit in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} ПБ"
