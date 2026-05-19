# Proyecto 6: Computer Vision

## Descripción

Este proyecto de visión por computadora consiste en un sistema de reconocimiento facial para hogares inteligentes que hace uso de las librerías DeepFace y OpenCV para hacer la verificación y análisis del rostro de una persona y permitir o denegar el acceso a un hogar. Al permitir el acceso, el sistema debería activar una configuración del entorno de dispositivos que forman parte del hogar inteligente, pero para este proyecto el programa se limita a ejecutar las acciones relacionadas al reconocimiento facial y simula las acciones posteriores al acceso con una línea de texto.

## Requisitos

- Python 3.13
- Cámara web (opcional, se puede usar cargando una imagen)

NOTA IMPORTANTE:
Para aprovechar las funciones de reconocimiento a través de la cámara web del equipo, es necesario ejecutar este programa desde la terminal de Windows, no desde WSL. Si se ejecuta desde WSL es muy probable que algunas características no funcionen correctamente. Para evitar problemas, se recomienda crear una carpeta en Windows, ahí dentro crear el entorno virtual e instalar las librerías del proyecto. En WSL solo se puede ejecutar la función de Cargar imagen, y se debe ingresar la ruta manualmente, sin comillas; el resto de funciones no funcionan en WSL por los permisos de uso de la cámara web.

## Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/FernandoFelixA/Computer-Vision
cd Computer-Vision
```

2. Crear entorno virtual
   En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

En terminal de Ubuntu:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias (archivo requirements.txt)

```bash
pip install -r requirements.txt
```

## Cómo ejecutar

El proyecto por defecto incluye 5 archivos Python: `main.py`, `camara.py`, `hogar.py`, `reconocimiento.py` y `registro.py`.
Además, incluye una carpeta llamada 'face-db' que sirve como base de datos local para almacenar los rostros y las configuraciones de cada perfil (en un archivo JSON).
Cada archivo incluye funciones relacionadas a un aspecto del programa, pero el archivo principal y que deberá ejecutarse es `main.py`

## Uso

Al ejecutar el archivo `main.py` el programa comenzará mostrando un menú con 5 opciones:

### 1. Activar cámara

Al seleccionar esta opción se activa la cámara web del equipo para iniciar el reconocimiento facial. Con la cámara abierta se pueden ejecutar dos acciones: tomar una fotografía con la tecla 'f' y cerrar la cámara con la tecla 'q'. Cuando se presiona la tecla 'f' el programa toma una fotografía y ejecuta el reconocimiento. Si el rostro coincide con el de alguna persona almacenada en la carpeta `face-db`, se imprime un mensaje dándole la bienvenida a la persona y avisando de la configuración que está por activarse. Si el programa no encuentra el rostro, simplemente muestra un mensaje que denega el acceso.

### 2. Cargar imagen

Se incluye la opción de cargar una imagen para hacer pruebas con el programa en caso de no tener una cámara web. Al seleccionar esta opción se deberá ingresar la ruta de la imagen para que el programa pueda hacer el reconocimiento facial y permitir o denegar el acceso a la persona. El resultado es igual al que se obtiene cuando se hace el reconocimiento por medio de una cámara.

### 3. Registrar nuevo miembro

Se implementa esta opción para que los usuarios puedan registrarse y hacer pruebas con sus rostros. Simula una comprobación de permisos donde primero se debe ingresar la contraseña del administrador para evitar que cualquier externo pueda registrarse (contraseña: 1234567890). Después de comprobar permisos se pide el nombre de la persona a registrar y se le crea una carpeta en `face-db`. Posteriormente se activa la cámara y se pueden ejecutar dos acciones: tomar una fotografía con la tecla 'f' y cerrar la cámara con la tecla 'q'. El sistema guarda la(s) foto(s) en la base de datos y le pregunta al usuario si quiere configurar su perfil. Si el usuario accede, se le harán unas preguntas, cuyas respuestas serán almacenadas en el archivo perfiles.json; si no quiere configurar su perfil, se termina el registro y puede hacer el reconocimiento. Para esta opción de registrar nuevos miembros, se utiliza la librería DeepFace para analizar los rostros registrados y obtener el género y edad de los individuos. Si el sistema reconoce que se está registrando a un niño, se saltará la parte de preguntar una configuración y le asignará el modo infantil automáticamente.

### 4. Eliminar un miembro existente

Esta opción sirve para eliminar miembros de la base de datos. Al ejecutarse primero se simula una comprobación de permisos, solicitando la contraseña del administrador y cuando es validada pregunta el nombre del miembro que se desea eliminar. Si el nombre del miembro se encuentra en la base de datos, procede a eliminar tanto su carpeta de fotos como su información del archivo perfiles.json.

### 5. Salir

El programa se ejecutará hasta que el usuario indique que lo quiere finalizar. Esta opción finaliza el programa.

## Estructura del proyecto

### main.py

Es la columna vertebral del programa, desde donde se llaman todas las funciones distribuidas en los demás archivos y se define el flujo del menú desde donde el usuario interactua con todas las opciones.

### camara.py

Incluye todas las funciones relacionadas a la ejecución y uso de la cámara, así como a las tareas de guardar y cargar imágenes.

### hogar.py

Incluye todas las funciones relacionadas a la administración de los perfiles de cada miembro del hogar. Desde aquí se obtiene la configuración de cada miembro almacenada en el archivo perfiles.json.

### reconocimiento.py

Este archivo incluye las funciones que sirven para localizar el rostro del usuario en la base de datos del programa.

### registro.py

Incluye las funciones que se encargan de comprobar permisos y registrar a una nueva persona en la base de datos del programa.

## Personas registradas por defecto

La base de datos del programa incluye tres personas registradas por defecto: un hombre adulto, una mujer adulta y un niño. Con estos tres casos se hicieron pruebas para comprobar que el programa es capaz de hacer el reconocimiento facial correctamente.
