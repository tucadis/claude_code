# Todo List Application - Ejemplo Completo

Aplicación de línea de comandos para gestionar tareas desarrollada con Claude Code.

## Descripción

Este es el código completo del proyecto práctico del Módulo 4 del curso de Claude Code.
Incluye toda la funcionalidad implementada y lista para usar.

## Características

- ✅ Agregar tareas con título y descripción
- ✅ Listar todas las tareas
- ✅ Filtrar tareas (pendientes/completadas)
- ✅ Marcar tareas como completadas
- ✅ Eliminar tareas
- ✅ Persistencia de datos en JSON
- ✅ Interfaz CLI con colores
- ✅ Tests unitarios completos

## Instalación

```bash
# Clonar o copiar el proyecto
cd proyecto-practico/todo-list

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

### Añadir una tarea

```bash
python -m src.cli add "Comprar leche"
python -m src.cli add "Estudiar Python" -d "Completar capítulos 5-7"
```

### Listar tareas

```bash
# Todas las tareas
python -m src.cli list

# Solo pendientes
python -m src.cli list -f pending

# Solo completadas
python -m src.cli list -f completed
```

### Completar una tarea

```bash
python -m src.cli complete 1
```

### Eliminar una tarea

```bash
# Con confirmación
python -m src.cli delete 2

# Sin confirmación
python -m src.cli delete 2 -y
```

## Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=html

# Ver reporte de cobertura
open htmlcov/index.html  # En Linux: xdg-open htmlcov/index.html
```

## Estructura del Proyecto

```
todo-list/
├── README.md                  # Este archivo
├── requirements.txt           # Dependencias
├── .gitignore                # Archivos a ignorar en Git
├── data/                     # Datos persistentes
│   └── tasks.json           # Archivo de tareas (generado automáticamente)
├── docs/                     # Documentación
│   └── guia-usuario.md      # Guía completa de usuario
├── src/                      # Código fuente
│   ├── __init__.py
│   ├── todo.py              # Modelos de datos
│   ├── storage.py           # Capa de persistencia
│   └── cli.py               # Interfaz de línea de comandos
└── tests/                    # Tests
    ├── __init__.py
    ├── test_todo.py         # Tests de modelos
    └── test_storage.py      # Tests de almacenamiento
```

## Tecnologías Utilizadas

- **Python 3.8+**
- **pytest**: Testing
- **argparse**: CLI
- **JSON**: Almacenamiento
- **dataclasses**: Modelos de datos

## Desarrollo

Este proyecto fue desarrollado como parte del curso básico de Claude Code,
demostrando cómo usar IA para asistir en el desarrollo de software.

### Características de código

- Type hints completos
- Documentación en español
- Manejo de excepciones
- Tests unitarios
- Código limpio y mantenible

## Licencia

Proyecto educativo - Libre uso para aprendizaje

## Autor

Desarrollado como proyecto de aprendizaje con Claude Code
