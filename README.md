# Gestor Inteligente de Clientes (GIC) - SolutionTech 💼

Este proyecto consiste en una plataforma integral de gestión de clientes desarrollada en **Python 3.13.7, diseñada para la startup *SolutionTech*. La solución aplica los principios de la Programación Orientada a Objetos (POO), persistencia de datos en bases de datos relacionales, manejo de archivos y una interfaz gráfica de usuario intuitiva.

## 🚀 Características Principales

- **Gestión de Clientes Multitipo**: Implementación de clases para Clientes Regulares, Premium y Corporativos mediante herencia y polimorfismo.
- **Validaciones Avanzadas**: Control robusto de formatos de email y teléfono utilizando expresiones regulares (Regex).
- **Persistencia de Datos**: Almacenamiento seguro en **SQLite** y capacidad de exportación de reportes en formato **JSON**.
- **Interfaz Gráfica (GUI)**: Panel de control desarrollado con **Tkinter** para una interacción fluida.
- **Registro de Actividad (Logging)**: Sistema de auditoría que guarda todas las operaciones y errores en archivos `.log`.
- **Arquitectura Modular**: Código organizado en paquetes (`core`, `database`, `gui`, `logs`) para facilitar la escalabilidad.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.13.7
- **Base de Datos**: SQLite3
- **Interfaz Gráfica**: Tkinter
- **Formato de Archivos**: JSON / CSV
- **Librerías Estándar**: `re`, `logging`, `json`, `sqlite3`

## 📂 Estructura del Proyecto

```text
GIC_Project/
├── core/                # Lógica de negocio (Clases y Validaciones)
├── database/            # Conexión a SQLite y manejo de archivos JSON
├── gui/                 # Interfaz de usuario con Tkinter
├── logs/                # Archivos de registro del sistema
├── tests/               # Pruebas unitarias
├── main.py              # Punto de entrada de la aplicación
└── README.md            # Documentación del proyecto

📋 Requisitos e Instalación
Clonar el repositorio:

git clone [https://github.com/CarobethPaez/gic_solutiontech.git]

cd gic_solutiontech

## Crear y activar un entorno virtual:
Bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

## Ejecutar la aplicación:

Bash
python main.py

⚙️ Funcionamiento
Al iniciar, la aplicación crea automáticamente la base de datos clientes.db si no existe.

A través del formulario, se pueden ingresar nuevos clientes. El sistema validará automáticamente que el email sea correcto y el ID sea único.

Cada vez que se agrega un cliente, la tabla se actualiza en tiempo real y se genera una entrada en logs/sistema.log.

🛡️ Principios de Desarrollo
Encapsulamiento: Uso de atributos privados y propiedades para proteger la integridad de los datos.

Manejo de Excepciones: Captura estructurada de errores de base de datos y validación.

Modularidad: Separación clara entre la interfaz de usuario y la lógica de acceso a datos.

🖋️ Autor

Carolina Páez