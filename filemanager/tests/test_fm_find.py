import os
import pytest
from filemanager.file_manager import FileManager


def test_find_files(tmp_path):
    """Проверка поиска файла по маске"""
    # Создаём временную директорию
    test_dir = tmp_path / 'folder'
    test_dir.mkdir()
    
    # Добавляем временные файлы
    test_file1 = test_dir / 'test1.txt'
    test_file1.write_text('Test1')
    
    test_file2 = test_dir / 'test2.txt'
    test_file2.write_text('Test2')
    
    assert os.path.exists(test_dir)
    assert os.path.exists(test_file1)
    assert os.path.exists(test_file2)
    
    pattern = '*.txt'
    result = FileManager.find_file(str(test_dir), pattern)
    expected = [
        (1, str(test_dir), 'test1.txt'),
        (2, str(test_dir), 'test2.txt')
    ]
    
    assert result == expected


def test_no_matches_found(tmp_path):
    """Проверка отсутсия совпадений"""
    # Создаём временую директорию
    test_dir = tmp_path / 'folder'
    test_dir.mkdir()
    
    # Добавляем временный файл
    test_file = test_dir / 'test.txt'
    test_file.write_text('Test1')
    
    assert os.path.exists(test_dir)
    assert os.path.exists(test_file)
    
    pattern = '*.tx'
    result = FileManager.find_file(str(test_dir), pattern)
    expected = None
    
    assert result == expected


def test_file_not_found(tmp_path):
    """Проверка поднятия исключения FileNotFoundError"""
    # Создаём временую директорию
    test_dir = tmp_path / 'incorrect_path'
    pattern = '*.txt'
    
    with pytest.raises(FileNotFoundError):
        FileManager.find_file(test_dir, pattern)


def test_not_directory(tmp_path):
    """Проверка поднятия исключения IsADirectoryError"""
    # Создаём временую директорию
    test_dir = tmp_path / 'folder'
    test_dir.mkdir()
    
    # Добавляем временный файл
    test_file = test_dir / 'test.txt'
    test_file.write_text('Test1')
    pattern = '*.txt'
    
    with pytest.raises(IsADirectoryError):
        FileManager.find_file(test_file, pattern)
