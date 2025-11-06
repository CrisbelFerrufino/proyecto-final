#  Teoria Git

## ¿Qué es Git?

**Git** es un **sistema de control de versiones distribuido**, creado por **Linus Torvalds** (el mismo creador de Linux) en 2005.  
Sirve para **registrar los cambios que se hacen en los archivos de un proyecto** a lo largo del tiempo, permitiendo volver atrás, comparar versiones y trabajar en equipo de forma segura.

Nota: **Git es una herramienta que te ayuda a guardar el historial de tu proyecto y colaborar con otros sin perder trabajo.**

---

## 💡 ¿Por qué usar Git?

Usar Git trae muchas ventajas:

1. **Control de versiones:** Permite volver a versiones anteriores de tu proyecto si algo sale mal.  
2. **Trabajo en equipo:** Varios desarrolladores pueden trabajar en el mismo proyecto sin pisarse los cambios.  
3. **Historial completo:** Registra quién hizo cada cambio y cuándo.  
4. **Ramas (branches):** Puedes experimentar nuevas ideas sin afectar el código principal.  
5. **Seguridad:** Los repositorios se pueden guardar localmente y también en la nube (por ejemplo, GitHub).  
6. **Integración:** Funciona con herramientas modernas como Visual Studio Code, GitHub, GitLab, Bitbucket, entre otras.

---

##  ¿Cuándo usar Git?

Git debe usarse **siempre que trabajes en proyectos que evolucionen con el tiempo**, especialmente si:

- Estás desarrollando **software o programas** (Python, C++, Java, etc.).
- Es un **trabajo en equipo**, para evitar conflictos de versiones.
- Deseas **mantener un historial** de los avances de tu proyecto.
- Vas a **publicar tu proyecto** o compartirlo en GitHub.

Incluso para proyectos personales, usar Git es buena práctica, ya que te ayuda a **organizar y documentar** tu progreso.

---

##  ¿Cómo usar Git paso a paso?

A continuación, te mostramos cómo comenzar a usar Git desde cero:

### 1.  Instalar Git

Descarga Git desde su página oficial:  
👉 [https://git-scm.com/downloads](https://git-scm.com/downloads)

Durante la instalación puedes dejar las opciones por defecto.

Para comprobar que se instaló correctamente, abre la terminal (o PowerShell) y escribe:

```bash
git --version

```
### 2. Configurar tu identidad

```bash
Configura tu nombre y correo, que quedarán guardados en cada cambio que hagas
git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@example.com"

```
### 3. Crea un nuevo repositorio
(Un **repositorio** es: una carpeta controlada por Git.)

``` bash
mkdir mi_proyecto
cd mi_proyecto
git init

```
### 4. agregar archivos
Para que Git controle los archivos, se deben agregar con:

```bash

git add .

```
### 5. Guardar los cambios **COMMIT**
Cada vez que se hace un cambio importante, se debe guardar con un mensaje descriptivo. Cada **COMMIT** representa una versión guardada del trabajo.

``` bash
git commit -m "Versión inicial del proyecto"

```
### 6. Crear y cambiar de rama ***BRANCH*
las **Branches** permiten trabajar nuevas ideas sin afectar el código principal.

``` bash
git checkout -b nueva_rama

``` 
Se puede crear una rama principal con:
``` bash
git checkout main

``` 
### 7. Subir el proyecto a Git  
En GitHub se crea un repositorio vacío.  
Luego, se conecta el proyecto local con ese repositorio remoto para que se guarde en la nube:

``` bash
git remote add origin https://github.com/usuario/nombre_repositorio.git
git branch -M main
git push -u origin main

```
### Clonar un repositorio existente  
Si se quiere descargar un proyecto de GitHub para trabajarlo localmente: 

``` bash
git clone https://github.com/usuario/proyecto.git

``` 
### 9. Subir y bajar cambios  
- Para **descargar actualizaciones** del repositorio remoto:

``` bash
git pull

``` 
- Para **subir los cambios** hechos en local:
``` bash
git push
```
---

## Conclusión
Git es una herramienta muy útil para gestionar proyectos de todo tipo, especialmente en programación.
Permite mantener un control total sobre el progreso, colaborar con otros y asegurar que nada se pierda.
Gracias a su funcionamiento basado en versiones, se pueden hacer pruebas sin miedo a dañar el proyecto original.  

En resumen, aprender Git no solo facilita el trabajo diario, sino que también mejora la organización, la seguridad y la calidad del resultado final.

--- 

## Fuentes consultadas
- Documentación oficial de Git: https://git-scm.com/doc

- GitHub Docs: https://docs.github.com/es

- Atlassian Git Tutorials: https://www.atlassian.com/git/tutorials
