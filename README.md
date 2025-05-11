# 📁 Folders-Extractor (English)

Python script to extract images from subfolders, rename them with the containing folder's name, and move them to the root directory. Ideal for organizing manga chapters, scans, or images distributed across multiple folders.

⚙️ What does this script do?
📂 Goes through all subfolders within a directory.

🧹 Cleans the name of each folder (keeps only numbers, dots, and commas).

🖼️ Renames the images inside each folder as: FolderName 1.jpg, FolderName 2.jpg, etc.

🚚 Moves all images to the main directory.

🧹 Deletes the empty folders after moving the files.

📦 Finally, moves the processed directory to another destination folder.

🖥️ Requirements
Python 3.x

Uses only Python's standard library modules:
os, re, shutil
(No need to install external libraries)

📝 Usage
Place your folders inside a root directory, for example:

Chapters/01. Introduction/image1.png, image2.jpg; 02. Action/image1.jpg

⚠️ IMPORTANT (Windows): Use double backslashes (\):

source_directory = "C:\Users\Username\Mangas\Chapters\1.Preparing\F

Run the script from terminal or your editor:

python extractor.py

🧼 Expected result
After running the script:

All image files will be in the root directory, renamed.

Example:

01 1.jpg
01 2.jpg
02 1.jpg




# 📁 Folders-Extractor (Español)


Script en Python para **extraer imágenes de subcarpetas**, renombrarlas con el nombre de la carpeta contenedora y moverlas al directorio raíz. Ideal para organizar capítulos de manga, escaneos o imágenes distribuidas por carpetas.

---

## ⚙️ ¿Qué hace este script?

- 📂 Recorre todas las subcarpetas dentro de un directorio.
- 🧹 Limpia el nombre de cada carpeta (manteniendo solo números, puntos y comas).
- 🖼️ Renombra las imágenes dentro de cada carpeta como: `NombreCarpeta 1.jpg`, `NombreCarpeta 2.jpg`, etc.
- 🚚 Mueve todas las imágenes al directorio principal.
- 🧹 Elimina las carpetas vacías después de mover los archivos.
- 📦 Finalmente, mueve el directorio procesado a otra carpeta destino.

---

## 🖥️ Requisitos

- Python 3.x  
- Usa solo módulos de la **biblioteca estándar** de Python:  
  `os`, `re`, `shutil`  
  *(No necesitas instalar librerías externas)*

---

## 📝 Uso

1. Coloca tus carpetas dentro de un directorio raíz, por ejemplo:

  Capitulos/01. Introducción/imagen1.png, imagen2.jpg; 02. Acción/imagen1.jpg


⚠️ IMPORTANTE (Windows): Usa doble barra invertida (\\):

source_directory = "C:\Users\Usuario\Mangas\Capitulos\1.Por Preparar\F

Ejecuta el script desde terminal o tu editor:

python extractor.py

🧼 Resultado esperado
Después de ejecutar el script:

Todos los archivos de imagen estarán en el directorio raíz renombrados.

Ejemplo:

01 1.jpg
01 2.jpg
02 1.jpg
