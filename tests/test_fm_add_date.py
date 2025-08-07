import os
import shutil
import pytest
from file_manager import FileManager
from utils import get_create_file_date


def create_file(path, content="test"):
    with open(path, "w") as f:
        f.write(content)


def test_add_date_non_recursive(tmp_path):
    # Создаем временные файлы
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    create_file(file1)
    create_file(file2)
    
    result = FileManager.add_date(str(tmp_path), recursive=False)
    
    assert isinstance(result, list)
    assert len(result) == 2
    new_filenames = [new for _, new in result]
    
    for new_name in new_filenames:
        assert tmp_path.joinpath(new_name).exists()
        assert get_create_file_date(tmp_path / new_name) in new_name


def test_add_date_recursive(tmp_path):
    # Создаём вложенную папку и файл
    nested_dir = tmp_path / "nested"
    nested_dir.mkdir()
    nested_file = nested_dir / "nested_file.txt"
    create_file(nested_file)
    
    result = FileManager.add_date(str(tmp_path), recursive=True)
    
    new_names = [new for _, new in result]
    assert any("nested_file" in new for new in new_names)
    for new_name in new_names:
        # Путь может быть с поддиректорией
        full_path = tmp_path / "nested" / new_name if "nested" in new_name else tmp_path / new_name
        assert full_path.exists()


def test_already_has_date(tmp_path):
    # Файл уже с датой
    date = get_create_file_date(tmp_path)
    file = tmp_path / f"file_{date}.txt"
    create_file(file)
    
    result = FileManager.add_date(str(tmp_path), recursive=False)
    assert result is None


def test_file_not_found(tmp_path):
    """Проверка вызова исключения FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        FileManager.delete(r'\inncorect_path')
