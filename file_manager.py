import os
import shutil

from fnmatch import fnmatch

from utils import change_file_name, pretty_print, create_new_file, \
    size_calculation


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
    
    @staticmethod
    def find_file(path_dir: str, pattern: str) -> list[tuple] | None:
        """Ищет все файлы согласно шаблону (pattern)"""
        if not os.path.exists(path_dir):
            raise FileNotFoundError(f'Директория {path_dir} не найдена!')
        
        if not os.path.isdir(path_dir):
            raise IsADirectoryError(
                'Необходимо передать директорию для поиска файлов!')
        
        files_list = []
        for path_dir, _, lst_files in os.walk(path_dir):
            files_list += [(path_dir, file) for file in lst_files if
                           fnmatch(file, pattern)]
        
        res_lst = []
        
        if files_list:
            print(f'Найдено совпадений: {len(files_list)}')
            for i, file in enumerate(files_list):
                res_lst.append((i + 1, file[0], file[1]))
            
            columns = ['№', 'Путь', 'Имя файла']
            print(pretty_print(res_lst, columns))
            return res_lst
        else:
            print('Совпадений не найдено!')
            return None
    
    @staticmethod
    def add_date(path: str, recursive=False) -> list[tuple] | None:
        """Добавляет к файлу дату создания, если выбрана директория
         ко всем файлам в директории, если есть ключ --recursive - во
          все файлы на всех уровнях вложения
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f'Не удается найти указанный файл {path}!')
        
        if os.path.isfile(path):
            new_path = create_new_file(path)
            os.rename(path, new_path)
            print(
                f'Файл {os.path.basename(path)} переименован -> {os.path.basename(new_path)}')
            return None
        
        res_files = []
        if recursive:
            for current_dir, _, filenames in os.walk(path):
                for file in filenames:
                    path_file = os.path.join(current_dir, file)
                    new_path_file = create_new_file(path_file)
                    if not os.path.isfile(new_path_file):
                        os.rename(path_file, new_path_file)
                    else:
                        continue
                    res_files.append((file, os.path.basename(new_path_file)))
        else:
            for obj in os.listdir(path):
                path_file = os.path.join(path, obj)
                if os.path.isfile(path_file):
                    new_path_file = create_new_file(path_file)
                    if not os.path.isfile(new_path_file):
                        os.rename(path_file, new_path_file)
                    else:
                        continue
                    res_files.append((obj, os.path.basename(new_path_file)))
        
        res_list = []
        if res_files:
            for i, file in enumerate(res_files):
                res_list.append((i + 1, file[0], file[1]))
        else:
            print('Все файлы уже с датой создания!!!')
            return None
        
        columns = ['№', 'Старое имя', 'Новое имя']
        print(pretty_print(res_list, columns))
        return res_files
    
    @staticmethod
    def analyse(path: str = None):
        """Анализирует папку и выводит размеры содержимого уровня"""
        if path is None:
            path = os.getcwd()
        
        if not os.path.exists(path):
            raise FileNotFoundError(f'Путь {path} не существует!')
        
        # Общий размер всех вложенных файлов
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                fp = os.path.join(dirpath, filename)
                if os.path.isfile(fp):
                    total_size += os.path.getsize(fp)
        
        print(f"Общий размер: {size_calculation(total_size)}")
        
        # Размер объектов первого уровня
        data_lst = []
        for obj in os.listdir(path):
            obj_path = os.path.join(path, obj)
            size = 0
            if os.path.isfile(obj_path):
                size = os.path.getsize(obj_path)
            elif os.path.isdir(obj_path):
                for dirpath, _, filenames in os.walk(obj_path):
                    for filename in filenames:
                        fp = os.path.join(dirpath, filename)
                        if os.path.isfile(fp):
                            size += os.path.getsize(fp)
            data_lst.append((obj, size_calculation(size)))
        
        res_files_data = []
        if data_lst:
            for i, file in enumerate(data_lst):
                res_files_data.append((i + 1, file[0], file[1]))
        
        columns = ['№', 'Имя', 'Размер']
        print(pretty_print(res_files_data, columns))
        
        return data_lst

