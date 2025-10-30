# Teoria Unit Testing 

## Introducción

En el desarrollo de software, garantizar que el código funcione correctamente es fundamental.  
Uno de los métodos más eficaces para lograrlo es mediante el **Unit Testing** o **pruebas unitarias**, una técnica que permite verificar el comportamiento de pequeñas partes del programa 
*(llamadas “unidades”)* de forma automatizada.

---

## ¿Qué es Unit Testing?

El **Unit Testing** es una práctica de desarrollo de software que consiste en **probar de manera automática y aislada las partes más pequeñas del código**, como: funciones, métodos o clases, para asegurar que cada una realice su tarea correctamente.

Cada prueba unitaria se ejecuta de forma independiente y devuelve un resultado: **éxito o fallo**.  
Si una unidad falla, el desarrollador puede detectar y corregir el error de manera temprana, evitando problemas más graves en etapas posteriores.

---

## ¿Por qué usar Unit Testing?

### 1. Mejora la calidad del código
Permite detectar errores antes de que el software llegue al usuario final, reduciendo costos y tiempos de mantenimiento.

### 2. Facilita el mantenimiento y refactorización
Con pruebas unitarias, los desarrolladores pueden modificar el código sin temor a romper funcionalidades existentes, ya que las pruebas alertan de inmediato sobre cualquier cambio que cause fallos.

### 3. Incrementa la confianza del equipo
Un conjunto de pruebas exitosas brinda seguridad al equipo de desarrollo sobre la estabilidad del sistema antes de realizar despliegues.

### 4. Automatiza la validación del código
Las pruebas unitarias pueden ejecutarse automáticamente con herramientas de integración continua (CI/CD), asegurando que cada versión del software cumpla los estándares de calidad.

---

## ¿Cuándo usar Unit Testing?

| Situación | ¿Usar Unit Testing? | Motivo |
|------------|---------------------|---------|
| En el desarrollo de **nuevas funciones** |  Sí | Garantiza que las nuevas unidades funcionen correctamente |
| Al **refactorizar código existente** |  Sí | Asegura que los cambios no rompan funcionalidades previas |
| En **proyectos grandes o colaborativos** |  Sí | Permite mantener la coherencia y confiabilidad del sistema |
| En **scripts pequeños o pruebas rápidas** |  Opcional | Puede ser innecesario por simplicidad |
| Durante el **desarrollo ágil o iterativo** |  Sí | Facilita el control de calidad en cada iteración |

**se recomienda usar pruebas unitarias en cualquier proyecto que requiera mantenimiento o crecimiento a largo plazo**.

---

## ¿Cómo usar Unit Testing en Python?

Python incluye un módulo estándar llamado **`unittest`**, inspirado en JUnit (de Java), que permite escribir y ejecutar pruebas de forma estructurada.

### 🧱 Ejemplo básico con `unittest`

Supongamos que tenemos una función que suma dos números:

```python
# archivo: calculadora.py
def sumar(a, b):
    return a + b

```
Creamos un archivo de prueba  llamadotest_calculadora.py
```python
import unittest
from calculadora import sumar

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertNotEqual(sumar(10, 5), 20)

if __name__ == '__main__':
    unittest.main()

```
Ejecutar las pruebas:
```bash
python -m unittest test_calculadora.py

```
Resultado esperado:

```md
...
----------------------------------------------------------------------
Ran 1 test in 0.001s
OK

---

```
### Relación entre: Unit Testing, Python, Poetry y Git

---

#### Python

Python proporciona herramientas nativas para realizar pruebas unitarias, como el módulo unittest.
Además, existen frameworks más avanzados como pytest, nose o doctest, que permiten escribir pruebas de manera más concisa y legible.
El lenguaje, por su simplicidad, facilita el aprendizaje y la aplicación del Unit Testing incluso en proyectos complejos.

#### Poetry

Poetry ayuda a gestionar las dependencias y entornos virtuales donde se ejecutan las pruebas.
Con él, se pueden instalar librerías de testing (como pytest) y mantener versiones estables del entorno de desarrollo.  
Ejemplo:
```bash
poetry add --dev pytest

```
Ejecutar las pruebas dentro del entorno virtual:
```bash
poetry run pytest

```
#### Git
Git se integra directamente con las prácticas de Unit Testing, formando parte del flujo de trabajo de control de versiones.
Su relación es esencial por las siguientes razones:

- Historial de pruebas: Cada commit puede incluir nuevas pruebas o modificaciones a las existentes, documentando el progreso del desarrollo.

- Integración continua: Plataformas como GitHub Actions, GitLab CI o Jenkins pueden ejecutar automáticamente las pruebas unitarias en cada push, asegurando que el código subido funcione correctamente.

- Colaboración y revisión: Los colaboradores pueden verificar que las pruebas pasen antes de aprobar una fusión (merge), garantizando estabilidad en la rama principal del proyecto.  
Ejemplo de flujo con Git:

```bash
git add .
git commit -m "Agrego pruebas unitarias para la función sumar"
git push origin main

```
Luego una integración continua puede ejecutarse automáticamente:
```bash
poetry run pytest

---

```
### Buenas prácticas en UNIT TESTING

- **Nombrar las pruebas claramente:** los nombres deben describir qué comportamiento se está probando.

- **Mantener las pruebas independientes:** cada prueba debe ejecutarse sin depender de otras.

- **Usar entornos controlados:** evita modificar archivos o bases de datos reales durante las pruebas.

- **Automatizar:** integra la ejecución de las pruebas en el flujo de CI/CD.

- **Cobertura de código:** utiliza herramientas como coverage.py para medir qué porcentaje del código está siendo probado.

---

### Ejemplo de flujo completo con Poetry y Git

---

```bash
# Crear un nuevo proyecto con Poetry
poetry new proyecto_pruebas
cd proyecto_pruebas

# Agregar pytest como dependencia de desarrollo
poetry add --dev pytest

# Crear archivo de pruebas
echo "def test_ejemplo():\n    assert 2 + 2 == 4" > tests/test_ejemplo.py

# Ejecutar las pruebas
poetry run pytest

# Subir a GitHub
git init
git add .
git commit -m "Inicialización del proyecto con pruebas unitarias"
git remote add origin https://github.com/usuario/proyecto_pruebas.git
git push -u origin main

```
## Conclusión

El Unit Testing es una herramienta esencial para asegurar la calidad del software.
Permite detectar errores tempranos, mantener la estabilidad del código y fomentar la confianza en el desarrollo colaborativo.

Al combinar Python (lenguaje accesible y potente), Poetry (gestor de dependencias) y Git (control de versiones), se obtiene un entorno de trabajo profesional y reproducible donde las pruebas unitarias son parte integral del ciclo de vida del proyecto.

## Referencias

- [Documentación oficial de Python: unittest](https://docs.python.org/3/library/unittest.html)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Documentación oficial de Poetry](https://python-poetry.org/docs/)
- [Sitio oficial de Git](https://git-scm.com/)
- [PEP 8 – Estilo de código en Python](https://peps.python.org/pep-0008/)
- [Guía sobre Testing en Python – Real Python](https://realpython.com/python-testing/)
