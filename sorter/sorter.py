import os
import shutil

def sort_files_by_type(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError(f"The provided path {folder_path} is not a valid directory.")
    
    file_types = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1][1:]  # Get the file extension without the dot
            if file_extension not in file_types:
                file_types[file_extension] = []
            file_types[file_extension].append(file_path)
    
    for file_type, files in file_types.items():
        type_folder = os.path.join(folder_path, file_type)
        os.makedirs(type_folder, exist_ok=True)
        for file in files:
            shutil.move(file, type_folder)
