# 📁 Extractor-Fotos-de-Carpetas

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


⚠️ IMPORTANTE (Windows): Usa doble barra invertida (\\) o el prefijo r para evitar errores:

python
Copiar
Editar
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
