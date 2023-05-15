import os
import shutil

class DeleteFile:
    def __init__(self) -> None:
        self.directory_path = r"C:\Users\Eva\Desktop\java"


    def delete_files_in_folder(self,folder_path):
        # Получаем список файлов в папке
        files = os.listdir(folder_path)
        
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            
            if os.path.isfile(file_path):
                # Удаляем файл
                os.remove(file_path)
                print(f"Удален файл: {file_path}")

    def delete_files_in_directory(self):
        for root, dirs, files in os.walk(self.directory_path):
            for dir_name in dirs:
                folder_path = os.path.join(root, dir_name)
                self.delete_files_in_folder(folder_path)
                shutil.rmtree(self.directory_path + "\\" + dir_name)

# Пример использования:

dele = DeleteFile()

dele.delete_files_in_directory()