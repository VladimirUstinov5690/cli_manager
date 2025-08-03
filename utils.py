import os


def change_file_name(filename, dest_path):
    name, ext = os.path.splitext(filename)
    count = 1
    while True:
        new_file = f'{name}_copy{count}{ext}'
        new_path = os.path.join(dest_path, new_file)
        if not os.path.isfile(new_path):
            break
        count += 1
    return new_path
