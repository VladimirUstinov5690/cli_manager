import argparse
from file_manager import FileManager


def main():
    parser = argparse.ArgumentParser(
        description="Manager for working with the file system")
    sub_parser = parser.add_subparsers(dest='command')
    
    # Парсеры для команды COPY и аргументов
    copy_parser = sub_parser.add_parser('copy', help='Copy file')
    copy_parser.add_argument('path_file', help='Path to file')
    copy_parser.add_argument('destination', help='Path to directory',
                             nargs='?',
                             default=None)
    
    # Парсеры для команды DELETE и аргументов
    delete_parser = sub_parser.add_parser('delete', help='Delete file or dir')
    delete_parser.add_argument('path', help='Path to file or dir')
    
    # Парсеры для команды NUM_FILES и аргументов
    delete_parser = sub_parser.add_parser('num_files',
                                          help='Delete file or dir')
    delete_parser.add_argument('path', help='Path to dir')
    
    # Парсеры для команды NUM_FILES и аргументов
    delete_parser = sub_parser.add_parser('find', help='Search files')
    delete_parser.add_argument('path', help='Path to dir')
    delete_parser.add_argument('pattern', help='Search pattern')
    
    args = parser.parse_args()
    
    commands = {
        'copy': lambda: FileManager.copy_file(args.path_file,
                                              args.destination),
        'delete': lambda: FileManager.delete(args.path),
        'num_files': lambda: FileManager.num_files(args.path),
        'find': lambda: FileManager.find_file(args.path, args.pattern)
    }
    
    print(f'Выполняем команду {args.command} >>>')
    try:
        commands[args.command]()
    except FileNotFoundError as m:
        print(f'Ошибка: {m}')
    except NotADirectoryError as m:
        print(f'Ошибка: {m}')


if __name__ == '__main__':
    main()
