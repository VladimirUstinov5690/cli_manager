import os
import pytest

from file_manager import FileManager


def test_copy_file_create(tmp_path):
    """Проверка копирования файла"""
    # Создание временного файла
    content = 'Test text!!!'
    file_test = tmp_path / 'test.txt'
    file_test.write_text(content)
    
    # Создание копии временного файла
    copy_file = FileManager.copy_file(str(file_test))
    
    # Проерка существованию скопированного файла
    assert os.path.isfile(copy_file)
    
    # Проверка содержимого файла
    with open(copy_file, 'r', encoding='utf-8') as file:
        file.read() == content
    
    # Проверка имени файла
    assert '_copy1' in copy_file


def test_copy_to_new_directory(tmp_path):
    """Проверка копирования в указанную директорию"""
    # Создание временного файла
    content = 'New text'
    file_test = tmp_path / 'test.txt'
    file_test.write_text(content)
    
    # Создание временной директории
    new_dir = tmp_path / 'target_dir'
    new_dir.mkdir()
    
    path_copy = FileManager.copy_file(str(file_test), str(new_dir))
    
    assert os.path.isfile(path_copy)
    
    with open(path_copy, 'r', encoding='utf-8') as f:
        assert f.read() == content


def test_file_not_found():
    """Проверка исключения FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        FileManager.copy_file('non_existing_file.txt')


def test_not_found_destination(tmp_path):
    """Проверка исключения, если путь копирования не существует"""
    file_test = tmp_path / 'file.txt'
    file_test.write_text('text')
    
    incorrect_dest = tmp_path / 'not_directory'
    with pytest.raises(FileNotFoundError):
        FileManager.copy_file(str(file_test), str(incorrect_dest))
