import os
import re
import shutil

def rename_files_and_move_up(directory, destination_directory):
    # Iterar sobre cada carpeta dentro del directorio dado
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        # Verificar si es una carpeta
        if os.path.isdir(folder_path):
            new_folder_name = folder_name.translate(str.maketrans('', '', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Eliminar letras del nombre de la carpeta
            new_folder_name = re.sub(r'(?<=\d)\.(?=\d)', ',', new_folder_name)  # Reemplazar "." entre números por ","
            new_folder_name = re.sub(r'[^0-9.,]', '', new_folder_name)  # Mantener solo números y comas
            
            # Cambiar el nombre de los archivos dentro de la carpeta
            file_names = os.listdir(folder_path)
            for i, file_name in enumerate(file_names, 1):
                file_path = os.path.join(folder_path, file_name)
                # Cambiar el nombre del archivo y agregar la extensión .jpg
                new_file_name = f"{new_folder_name} {i}.jpg"
                # Verificar si el nombre ya existe y agregar un número secuencial si es necesario
                while os.path.exists(os.path.join(folder_path, new_file_name)):
                    i += 1
                    new_file_name = f"{new_folder_name} {i}.png"
                os.rename(file_path, os.path.join(folder_path, new_file_name))
            
            # Mover archivos a la carpeta superior
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    shutil.move(file_path, os.path.join(directory, file_name))
            
            # Eliminar la carpeta y su contenido
            shutil.rmtree(folder_path)
    
    # Mover la carpeta a otro directorio después de procesar todos los archivos
    shutil.move(directory, destination_directory)

# Directorio donde se encuentran las carpetas
directory = ""

# Directorio de destino para mover la carpeta
destination_directory = ""

# Llamar a la función para renombrar archivos, moverlos y mover la carpeta
rename_files_and_move_up(directory, destination_directory)
