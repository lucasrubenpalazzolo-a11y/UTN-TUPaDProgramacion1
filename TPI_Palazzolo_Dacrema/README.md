# Sistema de Gestión y Estadísticas de Países 🌍
 
Proyecto Integrador desarrollado para la cátedra de **Programación 1** en la **Universidad Tecnológica Nacional (UTN)**. El sistema permite administrar de forma eficiente los datos de diferentes países, manejando registros de población, superficie y continente, utilizando persistencia de datos en archivos locales.

---

## 👥 Integrantes del Equipo
* **Maximiliano Dacrema**
* **Lucas Palazzolo**

---

## 📊 Estructura del Proyecto

El proyecto está diseñado bajo un enfoque modular, separando la lógica de las funciones de la interfaz del menú principal:

* **`main.py`**: Contiene el bucle principal de la aplicación, maneja la interfaz interactiva de usuario (menú) y gestiona los flujos de control.
* **`funciones.py`**: Alberga toda la lógica de negocio, manipulación de estructuras de datos y lectura/escritura de archivos.
* **`datos/paises.csv`**: Archivo de texto plano utilizado como base de datos local para almacenar los registros de forma permanente.

---

## 🚀 Características Principales

El sistema cuenta con las siguientes funcionalidades integradas en un menú interactivo:

1. **Carga Automática**: Al iniciar, el sistema lee el archivo CSV y carga los datos en memoria. Si el archivo no existe o contiene errores de formato, está protegido para no colapsar.
2. **Visualización Completa**: Muestra el listado de todos los países cargados con sus respectivos datos de habitantes, superficie y ubicación geográfica.
3. **Altas de Registros**: Permite añadir nuevos países validando que los campos esenciales no se envíen vacíos y que los datos numéricos sean correctos.
4. **Búsqueda Avanzada**: Localiza países mediante coincidencias parciales en el nombre, en el cazo de haber coincidencia permite si el usuario quiere cambiar los valores de superficie y población (sin distinguir mayúsculas de minúsculas).
5. **Filtrado Geográfico**: Agrupa y muestra en pantalla únicamente los países pertenecientes a un continente específico.
6. **Ordenamiento Eficiente**: Ordena el listado de países de menor a mayor según su población utilizando un algoritmo de ordenación propio.
7. **Estadísticas Generales**: Calcula e informa de manera automática qué país posee mayor y menor cantidad de habitantes, junto con el promedio general de población.
8. **Persistencia Garantizada**: Guarda los datos de manera manual o automática al seleccionar la opción de salida del programa para asegurar que no se pierda la información.

---

## 🛠️ Aspectos Técnicos Destacados

* **Estructuras de Datos**: Se implementó una **lista de diccionarios** para representar la base de datos en memoria, garantizando que toda la información de un mismo registro se mantenga unificada y ordenada.
* **Algoritmia Propia**: Para el ordenamiento de los datos se desarrolló manualmente el método de la **Burbuja (Bubble Sort)**, evitando el uso de funciones automáticas de ordenamiento de Python para cumplir con los requerimientos académicos.
* **Robustez y Control de Errores**: Se incorporaron bloques `try-except` para interceptar excepciones comunes como `FileNotFoundError` (archivo faltante) o `ValueError` (datos numéricos corruptos en el archivo o mal ingresados por el usuario), asegurando la continuidad del programa.
* **Seguridad de Datos**: En los procesos de ordenamiento se utiliza el método `.copy()` para trabajar sobre una réplica de la lista, evitando alterar el orden original de la base de datos a menos que el usuario lo decida.

---

## 💻 Requisitos e Instalación

Para ejecutar este proyecto de manera local, solo necesitás tener instalado **Python 3.x**.

1. Cloná o descargá este repositorio en tu computadora.
2. Asegurate de mantener la estructura de carpetas original (con la carpeta `datos` y el archivo `paises.csv` en su interior).
3. Ejecutá el archivo principal desde tu terminal o consola de comandos:

```bash
python main.py