import os
import pytest

from file_manager import FileManager


def test_copy_file_create(tmp_path):
    """Checking file copying"""
    # Creating a temporary file
    content = 'Test text!!!'
    file_test = tmp_path / 'test.txt'
    file_test.write_text(content)
    
    # Create a copy of the file
    copy_file = FileManager.copy_file(str(file_test))
    
    # Checking file existence
    assert os.path.isfile(copy_file)
    
    # Text match check
    with open(copy_file, 'r', encoding='utf-8') as file:
        file.read() == content
    
    # Checking copy's name
    assert '_copy1' in copy_file


def test_file_not_found():
    """Exception checking FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        FileManager.copy_file('path_not_exist.py')


def test_is_directory(tmp_path):
    """Exception checking IsADirectoryError"""
    with pytest.raises(IsADirectoryError):
        FileManager.copy_file(tmp_path)
