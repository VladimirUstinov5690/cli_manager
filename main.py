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
    
    args = parser.parse_args()
    
    print(f'{args.command} - {args.path_file} - {args.destination}')


if __name__ == '__main__':
    main()
