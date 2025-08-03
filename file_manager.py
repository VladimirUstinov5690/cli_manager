import os
import shutil


class FileManager:
    @staticmethod
    def copy_file(path_file: str):
        """The function creates a copy of the file in the same
        directory as the file"""
        if os.path.isdir(path_file):
            raise IsADirectoryError(
                "You must pass the path to the file or the file name."
            )

        if not os.path.isabs(path_file):
            path_file = os.path.join(os.getcwd(), path_file)

        if os.path.isfile(path_file):
            count = 1
            path_to_file = os.path.dirname(path_file)
            filename = os.path.basename(path_file)
            file, ext = os.path.splitext(filename)
            while True:
                new_file = f"{file}_copy{count}{ext}"
                new_path = os.path.join(path_to_file, new_file)
                if not os.path.isfile(new_path):
                    shutil.copy(path_file, new_path)
                    print(f"File was successfully copied: {new_path}")
                    return new_path
                count += 1
        else:
            raise FileNotFoundError(f"File not found: {path_file}")


FileManager.copy_file(r'C:\Users\Anva\Desktop\folder\file.log')