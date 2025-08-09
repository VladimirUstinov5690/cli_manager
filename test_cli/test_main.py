from unittest import mock

from main import FileManager


def main():
    import sys
    cmd = sys.argv[1]
    if cmd == 'copy':
        print('Выполняем команду copy')
        FileManager.copy_file(sys.argv[2],
                              sys.argv[3] if len(sys.argv) > 3 else None)
    elif cmd == 'delete':
        print('Выполняем команду delete')
        FileManager.delete(sys.argv[2])
    elif cmd == 'num_files':
        print('Выполняем команду num_files')
        FileManager.num_files(sys.argv[2])
    elif cmd == 'find_file':
        print('Выполняем команду find_file')
        FileManager.find_file(sys.argv[2], sys.argv[3])
    elif cmd == 'add_date':
        print('Выполняем команду add_date')
        recursive = '--recursive' in sys.argv
        FileManager.add_date(sys.argv[2], recursive)
    elif cmd == 'analyze':
        print('Выполняем команду analyze')
        path = sys.argv[2] if len(sys.argv) > 2 else None
        FileManager.analyze(path)


@mock.patch('filemanager.file_manager.FileManager.copy_file')
def test_copy_called(mock_copy, capsys):
    args = ['prog', 'copy', 'file.txt', 'dest_dir']
    mock_copy.return_value = 'dest_dir/file.txt'
    with mock.patch('sys.argv', args):
        main()
    mock_copy.assert_called_once_with('file.txt', 'dest_dir')
    captured = capsys.readouterr()
    assert 'Выполняем команду copy' in captured.out


@mock.patch('filemanager.file_manager.FileManager.delete')
def test_delete_called(mock_delete, capsys):
    args = ['prog', 'delete', 'some_path']
    mock_delete.return_value = True
    with mock.patch('sys.argv', args):
        main()
    mock_delete.assert_called_once_with('some_path')
    captured = capsys.readouterr()
    assert 'Выполняем команду delete' in captured.out


@mock.patch('filemanager.file_manager.FileManager.num_files')
def test_num_files_called(mock_num_files, capsys):
    args = ['prog', 'num_files', 'dir_path']
    mock_num_files.return_value = 5
    with mock.patch('sys.argv', args):
        main()
    mock_num_files.assert_called_once_with('dir_path')
    captured = capsys.readouterr()
    assert 'Выполняем команду num_files' in captured.out


@mock.patch('filemanager.file_manager.FileManager.find_file')
def test_find_file_called(mock_find_file, capsys):
    args = ['prog', 'find_file', 'dir_path', '*.txt']
    mock_find_file.return_value = [('1', 'dir_path', 'file.txt')]
    with mock.patch('sys.argv', args):
        main()
    mock_find_file.assert_called_once_with('dir_path', '*.txt')
    captured = capsys.readouterr()
    assert 'Выполняем команду find_file' in captured.out


@mock.patch('filemanager.file_manager.FileManager.add_date')
def test_add_date_called_without_recursive(mock_add_date, capsys):
    args = ['prog', 'add_date', 'some_path']
    mock_add_date.return_value = None
    with mock.patch('sys.argv', args):
        main()
    mock_add_date.assert_called_once_with('some_path', False)
    captured = capsys.readouterr()
    assert 'Выполняем команду add_date' in captured.out


@mock.patch('filemanager.file_manager.FileManager.add_date')
def test_add_date_called_with_recursive(mock_add_date, capsys):
    args = ['prog', 'add_date', 'some_path', '--recursive']
    mock_add_date.return_value = None
    with mock.patch('sys.argv', args):
        main()
    mock_add_date.assert_called_once_with('some_path', True)
    captured = capsys.readouterr()
    assert 'Выполняем команду add_date' in captured.out


@mock.patch('filemanager.file_manager.FileManager.analyze')
def test_analyze_called_with_path(mock_analyze, capsys):
    args = ['prog', 'analyze', 'some_path']
    mock_analyze.return_value = None
    with mock.patch('sys.argv', args):
        main()
    mock_analyze.assert_called_once_with('some_path')
    captured = capsys.readouterr()
    assert 'Выполняем команду analyze' in captured.out


@mock.patch('filemanager.file_manager.FileManager.analyze')
def test_analyze_called_without_path(mock_analyze, capsys):
    args = ['prog', 'analyze']
    mock_analyze.return_value = None
    with mock.patch('sys.argv', args):
        main()
    mock_analyze.assert_called_once_with(None)
    captured = capsys.readouterr()
    assert 'Выполняем команду analyze' in captured.out
