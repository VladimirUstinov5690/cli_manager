import os
import pytest

from filemanager.file_manager import FileManager


def test_delete_file(tmp_path):
    """Проверка удаления файла"""
    # Создание временного файла
    dir_test = tmp_path / 'folder'
    os.mkdir(dir_test)
    path_test = dir_test / 'test.txt'
    path_test.write_text('content')
    
    # Проверка существования временного файла
    assert os.path.exists(path_test)
    
    # Проверка удаления файла
    assert FileManager.delete(path_test)
    
    # Проверка, что файл удалён
    assert not os.path.exists(path_test)


def test_delete_dir(tmp_path):
    """Проверка удаления директории"""
    # Создание временной директории
    dir_test = tmp_path / 'folder2'
    dir_test.mkdir()
    path_test = dir_test / 'test2.txt'
    path_test.write_text('content2')
    
    # Проверка существования директории
    assert os.path.exists(dir_test)
    
    # Проверка удаления директории
    assert FileManager.delete(str(dir_test))
    
    # Проверка, что директория удалена
    assert not os.path.exists(dir_test)


def test_file_not_found():
    """Проверка вызова исключения FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        FileManager.delete(r'\inncorect_path')
