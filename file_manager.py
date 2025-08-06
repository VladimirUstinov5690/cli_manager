import os
import shutil

from utils import change_file_name


class FileManager:
    @staticmethod
    def copy_file(path_file: str, dest_path: str = None):
        """Создаёт копию файла в указанную директорию или создают копию файла
        в папке исходного файла при dest_path=None"""
        if not os.path.isfile(path_file):
            raise FileNotFoundError(
                f'Файл {os.path.basename(path_file)} не найден!')
        if dest_path is not None and not os.path.isdir(dest_path):
            raise FileNotFoundError(
                f'Указанной директории {dest_path} не существует!')
        
        if not os.path.abspath(path_file):
            path_file = os.path.join(os.getcwd(), path_file)
        
        if os.path.dirname(path_file) == dest_path or dest_path is None:
            dest_path = os.path.dirname(path_file)
        
        path_file = os.path.abspath(path_file)
        
        if dest_path is None or os.path.dirname(path_file) == dest_path:
            dest_path = os.path.dirname(path_file)
        
        filename = os.path.basename(path_file)
        create_path = os.path.join(dest_path, filename)
        
        if os.path.isfile(create_path):
            create_path = change_file_name(filename, dest_path)
        
        shutil.copy(path_file, create_path)
        print(f'Файл {filename} успешно скопирован в {create_path}')
        return create_path
    
    @staticmethod
    def delete(path_to_obj: str):
        """Удаляет указанную директорию или файл"""
        if os.path.exists(path_to_obj):
            if os.path.isdir(path_to_obj):
                shutil.rmtree(path_to_obj)
                print(f'Директория {os.path.basename(path_to_obj)} удалёна!')
            else:
                os.remove(path_to_obj)
                print(f'Файл {os.path.basename(path_to_obj)} удалён!')
            return True
        else:
            raise FileNotFoundError(f'Путь {path_to_obj} не существует!')
    
    @staticmethod
    def num_files(path_dir: str):
        """Считает количество файлов в директории"""
        if not os.path.exists(path_dir):
            raise FileNotFoundError(f'Директория {path_dir} не найдена!')
        
        if not os.path.isdir(path_dir):
            raise NotADirectoryError(
                'Необходимо передать директорию для подсчёта количества файлов!')
        
        amount_files = 0
        for _, _, lst_files in os.walk(path_dir):
            amount_files += len(lst_files)
        print(f'Количество файлов в директории: {amount_files}')
        return amount_files
