import os
import tempfile
import pytest
from filemanager.file_manager import FileManager


def create_test_files(base_dir):
    """Создаем тестовую структуру: 1 файл и 1 папка с файлом внутри"""
    file1 = os.path.join(base_dir, "file1.txt")
    with open(file1, "w") as f:
        f.write("Hello World")
    
    sub_dir = os.path.join(base_dir, "folder")
    os.makedirs(sub_dir)
    file2 = os.path.join(sub_dir, "file2.txt")
    with open(file2, "w") as f:
        f.write("Python Test")


def test_analyse_returns_correct_structure():
    with tempfile.TemporaryDirectory() as tmpdir:
        create_test_files(tmpdir)
        
        result = FileManager.analyze(tmpdir)
        
        # В папке два объекта: файл и папка
        assert len(result) == 2
        
        # Проверяем, что первый элемент - имя файла или папки, второй - размер (строка)
        for obj_name, size_str in result:
            assert isinstance(obj_name, str)
            assert isinstance(size_str, str)
            assert len(obj_name) > 0
            assert len(size_str) > 0
        
        # Проверяем, что суммарный размер >= 0
        for _, size_str in result:
            assert size_str


def test_analyse_raises_incorrect_path():
    with pytest.raises(FileNotFoundError):
        FileManager.analyze("/incorrect_path/")

