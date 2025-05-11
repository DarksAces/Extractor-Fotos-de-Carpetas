# 📁 Folders-Extractor

## English

Python script to extract images from subfolders, rename them using the parent folder’s name, and move them to the root directory. Perfect for organizing manga chapters, scans, or large batches of images across multiple folders.

### ⚙️ What does this script do?

- 📂 Goes through all subfolders inside a selected directory.
- 🧹 Cleans folder names (keeps only numbers, dots, and commas).
- 🖼️ Renames images as: `FolderName 1.jpg`, `FolderName 2.jpg`, etc.
- 🚚 Moves all images to the main directory.
- 🧼 Deletes the empty folders after moving the files.
- 📦 Moves the entire processed directory to a destination folder chosen by the user.

### 🖥️ Requirements

- Python 3.x
- Uses only Python’s standard libraries: `os`, `re`, `shutil`, `tkinter`
- ✅ No external libraries required

### 📝 Usage

1. Run the script:

```bash
python extractor.py
```

2. A dialog will appear asking you to:
   - Select the root folder containing the subfolders with images
   - Select the destination folder where the processed root folder will be moved

### ⚠️ NOTE (Windows)

You **no longer need to edit any paths manually**. Everything is done through a folder selection dialog.

### 🧼 Expected Result

After running the script, all image files will be in the root directory, renamed like:

```
01 1.jpg
01 2.jpg
02 1.jpg
```

---

## Español

Script en Python para extraer imágenes de subcarpetas, renombrarlas con el nombre de la carpeta contenedora y moverlas al directorio raíz. Ideal para organizar capítulos de manga, escaneos o imágenes distribuidas por carpetas.

### ⚙️ ¿Qué hace este script?

- 📂 Recorre todas las subcarpetas dentro de un directorio seleccionado.
- 🧹 Limpia el nombre de cada carpeta (manteniendo solo números, puntos y comas).
- 🖼️ Renombra las imágenes como: `NombreCarpeta 1.jpg`, `NombreCarpeta 2.jpg`, etc.
- 🚚 Mueve todas las imágenes al directorio principal.
- 🧼 Elimina las carpetas vacías después de mover los archivos.
- 📦 Mueve la carpeta raíz procesada a una carpeta destino que el usuario elige.

### 🖥️ Requisitos

- Python 3.x
- Usa solo módulos de la biblioteca estándar: `os`, `re`, `shutil`, `tkinter`
- ✅ No necesitas instalar librerías externas

### 📝 Uso

1. Ejecuta el script:

```bash
python extractor.py
```

2. Aparecerán dos ventanas para:
   - Seleccionar la carpeta raíz con subcarpetas
   - Seleccionar la carpeta destino donde se moverá la carpeta procesada

### ⚠️ IMPORTANTE (Windows)

Ya **no necesitas modificar rutas manualmente**. Todo se hace con ventanas emergentes de selección de carpetas.

### 🧼 Resultado esperado

Después de ejecutar el script, todas las imágenes estarán renombradas en el directorio raíz.

Ejemplo:

```
01 1.jpg
01 2.jpg
02 1.jpg
```
