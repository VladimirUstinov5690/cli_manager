import pytest
import os

from filemanager.file_manager import FileManager


def test_num_files(tmp_path):
    """Проверка подсчёта количества файлов"""
    # Создаём временные директории
    test_dir1 = tmp_path / 'folder_test1'
    test_dir1.mkdir()
    
    test_dir2 = tmp_path / 'folder_test2'
    test_dir2.mkdir()
    
    # Добавляем временные файлы
    test_file1 = tmp_path / 'test1.txt'
    test_file1.write_text('Test1')
    
    test_file2 = test_dir1 / 'test1.txt'
    test_file2.write_text('Test2')
    
    test_file3 = test_dir2 / 'test3.txt'
    test_file3.write_text('Test3')
    
    # Проверка создания директорий
    assert os.path.exists(test_dir1)
    assert os.path.exists(test_dir2)
    
    # Проверка создания файлов
    assert os.path.exists(test_file1)
    assert os.path.exists(test_file2)
    assert os.path.exists(test_file3)
    
    assert FileManager.num_files(tmp_path) == 3


def test_not_directory(tmp_path):
    """Проверка поднятия исключения NotADirectoryError"""
    test_dir = tmp_path / 'folder_test1'
    test_dir.mkdir()
    
    test_file = test_dir / 'test.txt'
    test_file.write_text(" content")
    
    with pytest.raises(NotADirectoryError):
        FileManager.num_files(test_file)


def test_file_not_found(tmp_path):
    """Проверка поднятия исключения FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        FileManager.num_files(tmp_path / 'incorrect_path')
