# Teoria Poetry 

## Introducción

En el desarrollo de software con Python, la gestión de dependencias, entornos virtuales y empaquetado de proyectos puede resultar compleja si se realiza manualmente o con múltiples herramientas.  
**Poetry** surge como una solución moderna que unifica estos procesos en una sola herramienta, facilitando la vida de los desarrolladores y mejora la organización de los proyectos.

---

## ¿Qué es Poetry?

**Poetry** es una herramienta de administración de dependencias y empaquetado para proyectos de Python.  
Permite gestionar las librerías necesarias, crear entornos virtuales automáticamente y preparar proyectos para su distribución o publicación.

A diferencia del uso tradicional de `pip` y `virtualenv`, **Poetry combina ambas funciones** y añade control preciso de versiones mediante archivos estructurados y reproducibles.

### Archivos principales que usa:
- **`pyproject.toml`** → Contiene la configuración del proyecto (nombre, versión, dependencias, etc.).
- **`poetry.lock`** → Registra las versiones exactas de las dependencias instaladas para garantizar la reproducibilidad.

---

## ¿Por qué usar Poetry?

###  1. Gestión simplificada de dependencias
Con Poetry, agregar o eliminar paquetes se realiza mediante comandos sencillos, sin editar manualmente archivos.

```bash
poetry add requests
poetry remove requests

---

```
### 2. Entornos virtuales automáticos
Poetry crea un entorno virtual para cada proyecto de manera automática, sin necesidad de usar venv o virtualenv.Usa un comando que activa el entorno del proyecto, aislando las dependencias de otros proyectos o del sistema.
```bash
poetry shell

```
### 3. Instalaciones reproducibles
Gracias al archivo poetry.lock, cualquier persona puede clonar un repositorio y ejecutar.  
Para instalar coorectamente las librerias usa:
``` bash
poetry install

```
### 4. Empaquetado y publicación sencilla 
Poetry facilita la creación y distribución de paquetes de Python, ideal para publicar librerías o proyectos internos. Para subir su paquete de forma segura y automatizada debe usar:

``` bash
poetry build
poetry publish --build

```
### Mejor colaboración y mantenimiento
Poetry estandariza la configuración del entorno, por lo que todos los miembros de un equipo trabajan en condiciones idénticas.
Esto evita conflictos entre versiones y simplifica el mantenimiento del proyecto a largo plazo

---

## ¿Cómo usar Poetry?
### 1. Instalación
En Windows mediante -> **PowerShell**
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

```
Verifica la instalación con el siguiente comando:
```bash
poetry --version

```
### 2. Crear un  nuevo proyecto
Para ello usa:
```bash
poetry new mi_proyecto

```
La estructura automatizada es la siguiente:

```md
mi_proyecto/
├── pyproject.toml
├── README.md
├── mi_proyecto/
│   └── __init__.py
└── tests/

```
## 3. Agregar dependencias
A través de:
```bash
cd mi_proyecto
poetry add requests

```
Dependencia de desarrollo:
```bash
poetry add --dev pytest

``` 
### 4. Activar el entorno virtual
Con:
```bash
poetry shell

```
Para salir del entorno:
```bash
exit

```
### 5. Ejecutar un script
Usa:
```bash
poetry run pytest
bash
poetry run python main.py
# o también:
poetry run pytest

---

```

## Importancia de Python para crear gráficos

Python es uno de los lenguajes más poderosos y versátiles para la visualización de datos y la creación de gráficos.  
Bibliotecas como **Matplotlib, Seaborn, Plotly y Pandas** permiten representar información de forma clara, visual y dinámica, lo que lo convierte en una herramienta fundamental para la ciencia de datos, la estadística, la inteligencia artificial y la presentación de resultados en proyectos técnicos o académicos.

La relación entre Python y Git es fundamental para el trabajo colaborativo. Git permite controlar las versiones del código, incluyendo los scripts de Python que generan gráficos, modelos o análisis. De esta forma, varios desarrolladores o investigadores pueden trabajar en el mismo proyecto, registrar los cambios realizados, revertir errores y mantener un historial completo del desarrollo.

Cuando se usa junto con Poetry, Git ayuda a asegurar que todos los colaboradores trabajen con las mismas dependencias y versiones, evitando incompatibilidades al ejecutar los mismos scripts o notebooks.

Poetry es una herramienta moderna que simplifica y mejora el flujo de trabajo en proyectos Python.
Permite gestionar dependencias, entornos y empaquetado de forma integrada, eficiente y reproducible.

---

### Importante:
En conjunto, Python, Poetry y Git forman una tríada poderosa:

- **Python** aporta la lógica y las herramientas de análisis.

- **Poetry** garantiza la coherencia del entorno.

- **Git** permite la colaboración y la trazabilidad de los cambios.

---

## Conclusión
Poetry es una herramienta moderna que simplifica y mejora el flujo de trabajo en proyectos Python.
Permite gestionar dependencias, entornos y empaquetado de forma integrada, eficiente y reproducible

---

### Recuerda:
--- 

- Usa Poetry para proyectos profesionales, colaborativos o que requieran empaquetado.

- Evítalo solo en scripts simples o experimentales donde la configuración rápida con pip sea suficiente.

---

##### Poetry representa el futuro de la gestión de proyectos en Python, combinando simplicidad con potencia profesional.

---

## Referencias

- Documentación oficial de Poetry

- PEP 518 – pyproject.toml specification

- Tutorial de publicación con Poetry en PyPI