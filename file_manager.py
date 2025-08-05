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
    def delete(path):
        """Удаляет указанную директорию или файл"""
        pass
