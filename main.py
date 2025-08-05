import argparse
from file_manager import FileManager


def main():
    parser = argparse.ArgumentParser(
        description="Manager for working with the file system")
    sub_parser = parser.add_subparsers(dest='command')
    
    copy_parser = sub_parser.add_parser('copy', help='Copy file')
    copy_parser.add_argument('path_file', help='Path to file')
    copy_parser.add_argument('destination', help='Path to directory',
                             nargs='?',
                             default=None)
    
    delete_parser = sub_parser.add_parser('delete', help='Delete file or dir')
    delete_parser.add_argument('path', help='Path to file or dir')
    
    args = parser.parse_args()
    
    commands = {
        'copy': lambda: FileManager.copy_file(args.path_file, args.destination),
        'delete': lambda: FileManager.delete(args.path)
        
    }
    
    print(f'Выполняем команду {args.command} >>>')
    try:
        commands[args.command]()
    except FileNotFoundError as a:
        print(f'Ошибка: {a}')


if __name__ == '__main__':
    main()
