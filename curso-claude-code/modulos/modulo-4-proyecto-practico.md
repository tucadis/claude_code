# Módulo 4: Proyecto Práctico - Aplicación Todo List

## 📖 Introducción

En este módulo desarrollarás una aplicación completa de lista de tareas (Todo List) usando Claude Code como tu asistente. Este proyecto te permitirá practicar todo lo aprendido y experimentar un flujo de trabajo real de desarrollo con IA.

### Características del proyecto

- ✅ Agregar tareas
- ✅ Listar tareas
- ✅ Marcar tareas como completadas
- ✅ Eliminar tareas
- ✅ Persistencia de datos (archivo JSON)
- ✅ Interfaz de línea de comandos
- ✅ Tests unitarios
- ✅ Manejo de errores

### Tecnologías

- **Lenguaje**: Python 3.x
- **Almacenamiento**: JSON
- **Testing**: pytest
- **Control de versiones**: Git

---

## 🚀 Paso 1: Configuración Inicial del Proyecto

### 1.1 Crear estructura del proyecto

```bash
# Ir al directorio de proyectos
cd ~/proyectos

# Crear directorio del proyecto
mkdir todo-list-app
cd todo-list-app

# Crear estructura de directorios
mkdir -p src tests data docs

# Crear archivos base
touch README.md
touch src/__init__.py
touch src/todo.py
touch src/storage.py
touch src/cli.py
touch tests/__init__.py
touch tests/test_todo.py
touch tests/test_storage.py
touch .gitignore
touch requirements.txt
```

**Verificar estructura:**
```bash
tree
```

**Estructura esperada:**
```
todo-list-app/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
├── docs/
├── src/
│   ├── __init__.py
│   ├── todo.py
│   ├── storage.py
│   └── cli.py
└── tests/
    ├── __init__.py
    ├── test_todo.py
    └── test_storage.py
```

### 1.2 Inicializar Git

```bash
# Inicializar repositorio
git init

# Configurar git (si no lo has hecho)
git config user.name "Tu Nombre"
git config user.email "tu@email.com"
```

### 1.3 Crear .gitignore

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
ENV/
env/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Testing
.pytest_cache/
.coverage
htmlcov/

# Data
data/*.json
!data/.gitkeep

# Environment
.env
.env.local

# Logs
*.log
EOF
```

### 1.4 Crear requirements.txt

```bash
cat > requirements.txt << 'EOF'
# Testing
pytest==7.4.3
pytest-cov==4.1.0

# Development
black==23.12.1
flake8==7.0.0
EOF
```

### 1.5 Crear README inicial

```bash
cat > README.md << 'EOF'
# Todo List Application

Aplicación de línea de comandos para gestionar tareas.

## Características

- Agregar tareas
- Listar tareas
- Marcar tareas como completadas
- Eliminar tareas
- Persistencia en archivo JSON

## Instalación

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
# Añadir una tarea
python -m src.cli add "Comprar leche"

# Listar todas las tareas
python -m src.cli list

# Completar una tarea
python -m src.cli complete 1

# Eliminar una tarea
python -m src.cli delete 1
```

## Tests

```bash
pytest tests/ -v
```

## Autor

Desarrollado como proyecto de aprendizaje con Claude Code
EOF
```

### 1.6 Crear entorno virtual de Python

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

**Salida esperada:**
```
Successfully installed pytest-7.4.3 pytest-cov-4.1.0 black-23.12.1 flake8-7.0.0
```

### 1.7 Commit inicial

```bash
# Añadir archivos
git add .

# Commit inicial
git commit -m "Initial commit: estructura base del proyecto Todo List"
```

---

## 💻 Paso 2: Desarrollo con Claude Code

### 2.1 Iniciar Claude Code

```bash
# Asegurarse de estar en el directorio correcto
cd ~/proyectos/todo-list-app

# Iniciar Claude Code
claude
```

### 2.2 Desarrollar el modelo de datos (todo.py)

**Petición a Claude:**

```
Crea el archivo src/todo.py con las siguientes características:

1. Una clase Task que represente una tarea con:
   - id: identificador único (int)
   - title: título de la tarea (str)
   - description: descripción opcional (str)
   - completed: estado de completado (bool)
   - created_at: fecha de creación (datetime)
   - completed_at: fecha de completado (datetime opcional)

2. Una clase TodoList que gestione múltiples tareas:
   - Método add_task: añadir nueva tarea
   - Método get_task: obtener tarea por id
   - Método get_all_tasks: obtener todas las tareas
   - Método complete_task: marcar tarea como completada
   - Método delete_task: eliminar tarea por id
   - Método get_pending_tasks: obtener tareas pendientes
   - Método get_completed_tasks: obtener tareas completadas

3. Requisitos:
   - Usar type hints en todas las funciones
   - Documentación completa en español
   - Usar dataclasses para Task
   - Manejo de excepciones personalizado
```

**Claude creará un archivo similar a este:**

```python
#!/usr/bin/env python3
"""
Módulo para gestionar tareas (Todo items).

Este módulo contiene las clases principales para crear y gestionar
una lista de tareas.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict


class TaskNotFoundError(Exception):
    """Excepción lanzada cuando no se encuentra una tarea."""
    pass


@dataclass
class Task:
    """
    Representa una tarea individual.

    Attributes:
        id: Identificador único de la tarea
        title: Título de la tarea
        description: Descripción detallada de la tarea
        completed: Estado de completado
        created_at: Fecha y hora de creación
        completed_at: Fecha y hora de completado (si aplica)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

    def to_dict(self) -> Dict:
        """
        Convierte la tarea a diccionario para serialización.

        Returns:
            Diccionario con los datos de la tarea
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """
        Crea una tarea desde un diccionario.

        Args:
            data: Diccionario con los datos de la tarea

        Returns:
            Instancia de Task
        """
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            created_at=datetime.fromisoformat(data["created_at"]),
            completed_at=datetime.fromisoformat(data["completed_at"]) if data.get("completed_at") else None
        )


class TodoList:
    """
    Gestiona una lista de tareas.

    Attributes:
        tasks: Lista de tareas
        next_id: Próximo ID a asignar
    """

    def __init__(self):
        """Inicializa una lista de tareas vacía."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Añade una nueva tarea a la lista.

        Args:
            title: Título de la tarea
            description: Descripción de la tarea (opcional)

        Returns:
            La tarea creada

        Raises:
            ValueError: Si el título está vacío
        """
        if not title.strip():
            raise ValueError("El título no puede estar vacío")

        task = Task(
            id=self.next_id,
            title=title.strip(),
            description=description.strip()
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Task:
        """
        Obtiene una tarea por su ID.

        Args:
            task_id: ID de la tarea

        Returns:
            La tarea encontrada

        Raises:
            TaskNotFoundError: Si no se encuentra la tarea
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError(f"No se encontró la tarea con ID {task_id}")

    def get_all_tasks(self) -> List[Task]:
        """
        Obtiene todas las tareas.

        Returns:
            Lista de todas las tareas
        """
        return self.tasks.copy()

    def get_pending_tasks(self) -> List[Task]:
        """
        Obtiene todas las tareas pendientes.

        Returns:
            Lista de tareas no completadas
        """
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self) -> List[Task]:
        """
        Obtiene todas las tareas completadas.

        Returns:
            Lista de tareas completadas
        """
        return [task for task in self.tasks if task.completed]

    def complete_task(self, task_id: int) -> Task:
        """
        Marca una tarea como completada.

        Args:
            task_id: ID de la tarea

        Returns:
            La tarea completada

        Raises:
            TaskNotFoundError: Si no se encuentra la tarea
        """
        task = self.get_task(task_id)
        if not task.completed:
            task.completed = True
            task.completed_at = datetime.now()
        return task

    def delete_task(self, task_id: int) -> Task:
        """
        Elimina una tarea de la lista.

        Args:
            task_id: ID de la tarea

        Returns:
            La tarea eliminada

        Raises:
            TaskNotFoundError: Si no se encuentra la tarea
        """
        task = self.get_task(task_id)
        self.tasks.remove(task)
        return task

    def to_dict(self) -> Dict:
        """
        Convierte la lista de tareas a diccionario.

        Returns:
            Diccionario con todas las tareas y metadatos
        """
        return {
            "tasks": [task.to_dict() for task in self.tasks],
            "next_id": self.next_id
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'TodoList':
        """
        Crea una TodoList desde un diccionario.

        Args:
            data: Diccionario con los datos

        Returns:
            Instancia de TodoList
        """
        todo_list = cls()
        todo_list.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
        todo_list.next_id = data.get("next_id", 1)
        return todo_list
```

**Guardar el código en src/todo.py**

### 2.3 Desarrollar la capa de persistencia (storage.py)

**Petición a Claude:**

```
Crea el archivo src/storage.py con las siguientes características:

1. Una clase JSONStorage que maneje el almacenamiento de tareas en JSON:
   - Método save: guardar TodoList en archivo JSON
   - Método load: cargar TodoList desde archivo JSON
   - Método existe: verificar si existe el archivo
   - Ruta del archivo por defecto: data/tasks.json

2. Requisitos:
   - Manejo de errores si el archivo no existe
   - Crear directorio data si no existe
   - Type hints completos
   - Documentación en español
```

**Claude creará:**

```python
#!/usr/bin/env python3
"""
Módulo para gestionar la persistencia de tareas en JSON.
"""

import json
import os
from pathlib import Path
from typing import Optional
from .todo import TodoList


class StorageError(Exception):
    """Excepción para errores de almacenamiento."""
    pass


class JSONStorage:
    """
    Gestiona el almacenamiento de tareas en formato JSON.

    Attributes:
        file_path: Ruta al archivo de almacenamiento
    """

    def __init__(self, file_path: str = "data/tasks.json"):
        """
        Inicializa el sistema de almacenamiento.

        Args:
            file_path: Ruta al archivo JSON
        """
        self.file_path = Path(file_path)
        self._ensure_data_directory()

    def _ensure_data_directory(self) -> None:
        """Crea el directorio data si no existe."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def exists(self) -> bool:
        """
        Verifica si existe el archivo de almacenamiento.

        Returns:
            True si existe, False en caso contrario
        """
        return self.file_path.exists()

    def save(self, todo_list: TodoList) -> None:
        """
        Guarda la lista de tareas en el archivo JSON.

        Args:
            todo_list: Lista de tareas a guardar

        Raises:
            StorageError: Si hay un error al guardar
        """
        try:
            data = todo_list.to_dict()
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise StorageError(f"Error al guardar tareas: {e}")

    def load(self) -> TodoList:
        """
        Carga la lista de tareas desde el archivo JSON.

        Returns:
            Lista de tareas cargada

        Raises:
            StorageError: Si hay un error al cargar
        """
        if not self.exists():
            return TodoList()

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return TodoList.from_dict(data)
        except json.JSONDecodeError as e:
            raise StorageError(f"Error al decodificar JSON: {e}")
        except Exception as e:
            raise StorageError(f"Error al cargar tareas: {e}")
```

### 2.4 Desarrollar la interfaz CLI (cli.py)

**Petición a Claude:**

```
Crea el archivo src/cli.py con una interfaz de línea de comandos usando argparse:

1. Comandos:
   - add: Añadir tarea (con título y descripción opcional)
   - list: Listar tareas (todas, pendientes, o completadas)
   - complete: Marcar tarea como completada
   - delete: Eliminar tarea

2. Características:
   - Mensajes coloridos con ANSI (verde para éxito, rojo para error)
   - Mostrar tareas en formato de tabla
   - Confirmación antes de eliminar
   - Type hints y documentación
```

**Claude creará:**

```python
#!/usr/bin/env python3
"""
Interfaz de línea de comandos para la aplicación Todo List.
"""

import argparse
import sys
from typing import List, Optional
from .todo import TodoList, Task, TaskNotFoundError
from .storage import JSONStorage, StorageError


# Códigos ANSI para colores
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_success(message: str) -> None:
    """Imprime mensaje de éxito en verde."""
    print(f"{Colors.GREEN}✓ {message}{Colors.END}")


def print_error(message: str) -> None:
    """Imprime mensaje de error en rojo."""
    print(f"{Colors.RED}✗ {message}{Colors.END}", file=sys.stderr)


def print_info(message: str) -> None:
    """Imprime mensaje informativo en azul."""
    print(f"{Colors.BLUE}ℹ {message}{Colors.END}")


def format_task(task: Task) -> str:
    """
    Formatea una tarea para mostrar.

    Args:
        task: Tarea a formatear

    Returns:
        Cadena formateada
    """
    status = "✓" if task.completed else "○"
    color = Colors.GREEN if task.completed else Colors.YELLOW

    result = f"{color}[{status}] {task.id}. {task.title}{Colors.END}"
    if task.description:
        result += f"\n    {task.description}"

    created = task.created_at.strftime("%Y-%m-%d %H:%M")
    result += f"\n    Creada: {created}"

    if task.completed and task.completed_at:
        completed = task.completed_at.strftime("%Y-%m-%d %H:%M")
        result += f" | Completada: {completed}"

    return result


def print_tasks(tasks: List[Task], title: str) -> None:
    """
    Imprime una lista de tareas.

    Args:
        tasks: Lista de tareas
        title: Título de la lista
    """
    if not tasks:
        print_info(f"{title}: No hay tareas")
        return

    print(f"\n{Colors.BOLD}{title}{Colors.END}")
    print("=" * 50)
    for task in tasks:
        print(format_task(task))
        print("-" * 50)
    print(f"\nTotal: {len(tasks)} tarea(s)\n")


def add_command(args: argparse.Namespace, storage: JSONStorage) -> None:
    """Comando para añadir tarea."""
    try:
        todo_list = storage.load()
        task = todo_list.add_task(args.title, args.description or "")
        storage.save(todo_list)
        print_success(f"Tarea añadida: #{task.id} - {task.title}")
    except ValueError as e:
        print_error(str(e))
        sys.exit(1)
    except StorageError as e:
        print_error(f"Error de almacenamiento: {e}")
        sys.exit(1)


def list_command(args: argparse.Namespace, storage: JSONStorage) -> None:
    """Comando para listar tareas."""
    try:
        todo_list = storage.load()

        if args.filter == "all":
            tasks = todo_list.get_all_tasks()
            print_tasks(tasks, "Todas las tareas")
        elif args.filter == "pending":
            tasks = todo_list.get_pending_tasks()
            print_tasks(tasks, "Tareas pendientes")
        elif args.filter == "completed":
            tasks = todo_list.get_completed_tasks()
            print_tasks(tasks, "Tareas completadas")
    except StorageError as e:
        print_error(f"Error al cargar tareas: {e}")
        sys.exit(1)


def complete_command(args: argparse.Namespace, storage: JSONStorage) -> None:
    """Comando para completar tarea."""
    try:
        todo_list = storage.load()
        task = todo_list.complete_task(args.id)
        storage.save(todo_list)
        print_success(f"Tarea completada: #{task.id} - {task.title}")
    except TaskNotFoundError as e:
        print_error(str(e))
        sys.exit(1)
    except StorageError as e:
        print_error(f"Error de almacenamiento: {e}")
        sys.exit(1)


def delete_command(args: argparse.Namespace, storage: JSONStorage) -> None:
    """Comando para eliminar tarea."""
    try:
        todo_list = storage.load()
        task = todo_list.get_task(args.id)

        # Confirmación
        if not args.yes:
            print_info(f"¿Eliminar tarea #{task.id} - {task.title}?")
            response = input("Escriba 'sí' para confirmar: ")
            if response.lower() not in ['sí', 'si', 'yes', 'y']:
                print_info("Operación cancelada")
                return

        todo_list.delete_task(args.id)
        storage.save(todo_list)
        print_success(f"Tarea eliminada: #{task.id} - {task.title}")
    except TaskNotFoundError as e:
        print_error(str(e))
        sys.exit(1)
    except StorageError as e:
        print_error(f"Error de almacenamiento: {e}")
        sys.exit(1)


def main():
    """Función principal de la CLI."""
    parser = argparse.ArgumentParser(
        description="Aplicación de línea de comandos para gestionar tareas",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando add
    add_parser = subparsers.add_parser("add", help="Añadir nueva tarea")
    add_parser.add_argument("title", help="Título de la tarea")
    add_parser.add_argument("-d", "--description", help="Descripción de la tarea")

    # Comando list
    list_parser = subparsers.add_parser("list", help="Listar tareas")
    list_parser.add_argument(
        "-f", "--filter",
        choices=["all", "pending", "completed"],
        default="all",
        help="Filtrar tareas"
    )

    # Comando complete
    complete_parser = subparsers.add_parser("complete", help="Completar tarea")
    complete_parser.add_argument("id", type=int, help="ID de la tarea")

    # Comando delete
    delete_parser = subparsers.add_parser("delete", help="Eliminar tarea")
    delete_parser.add_argument("id", type=int, help="ID de la tarea")
    delete_parser.add_argument("-y", "--yes", action="store_true", help="No pedir confirmación")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Inicializar almacenamiento
    storage = JSONStorage()

    # Ejecutar comando
    if args.command == "add":
        add_command(args, storage)
    elif args.command == "list":
        list_command(args, storage)
    elif args.command == "complete":
        complete_command(args, storage)
    elif args.command == "delete":
        delete_command(args, storage)


if __name__ == "__main__":
    main()
```

---

## 🧪 Paso 3: Crear Tests

### 3.1 Tests para todo.py

**Petición a Claude:**

```
Crea tests completos en tests/test_todo.py para las clases Task y TodoList:
- Tests para crear tareas
- Tests para operaciones de TodoList
- Tests para casos edge
- Tests para excepciones
```

**Claude creará tests/test_todo.py**

### 3.2 Tests para storage.py

**Petición a Claude:**

```
Crea tests en tests/test_storage.py para JSONStorage:
- Tests de guardado y carga
- Tests de manejo de errores
- Tests de archivos no existentes
```

---

## 🎯 Paso 4: Probar la Aplicación

### 4.1 Añadir tareas

```bash
# Asegúrate de estar en el entorno virtual
source venv/bin/activate

# Añadir tareas
python -m src.cli add "Completar el curso de Claude Code"
python -m src.cli add "Practicar con proyectos reales" -d "Crear al menos 3 proyectos pequeños"
python -m src.cli add "Leer documentación de Python"
```

### 4.2 Listar tareas

```bash
# Listar todas las tareas
python -m src.cli list

# Listar solo pendientes
python -m src.cli list -f pending

# Listar solo completadas
python -m src.cli list -f completed
```

### 4.3 Completar tareas

```bash
# Completar tarea con ID 1
python -m src.cli complete 1

# Verificar
python -m src.cli list
```

### 4.4 Eliminar tareas

```bash
# Eliminar con confirmación
python -m src.cli delete 2

# Eliminar sin confirmación
python -m src.cli delete 3 -y
```

### 4.5 Ejecutar tests

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Ejecutar con cobertura
pytest tests/ --cov=src --cov-report=html
```

---

## 🔄 Paso 5: Mejoras y Refactorización

### 5.1 Pedir mejoras a Claude

```
Sugiere 5 mejoras para el proyecto Todo List que podríamos implementar
```

### 5.2 Implementar prioridades

```
Añade soporte para prioridades de tareas (alta, media, baja) en la clase Task
```

### 5.3 Añadir búsqueda

```
Crea una función de búsqueda en TodoList que permita buscar tareas por palabra clave
```

---

## 📊 Paso 6: Documentación Final

### 6.1 Generar documentación

**Petición a Claude:**

```
Crea un archivo docs/guia-usuario.md con:
- Guía completa de usuario
- Todos los comandos disponibles
- Ejemplos de uso
- Solución de problemas
```

### 6.2 Actualizar README

```
Actualiza el README.md con:
- Características implementadas
- Ejemplos de uso reales
- Screenshots simulados (descripciones textuales)
- Instrucciones de instalación actualizadas
```

---

## 🎓 Paso 7: Control de Versiones

### 7.1 Commits organizados

```bash
# Ver cambios
git status

# Añadir cambios por módulo
git add src/todo.py
git commit -m "feat: implementar modelo de datos Task y TodoList"

git add src/storage.py
git commit -m "feat: implementar capa de persistencia JSONStorage"

git add src/cli.py
git commit -m "feat: implementar interfaz CLI con argparse"

git add tests/
git commit -m "test: añadir tests unitarios completos"

git add README.md docs/
git commit -m "docs: actualizar documentación del proyecto"
```

### 7.2 Ver historial

```bash
# Ver historial de commits
git log --oneline --graph --all

# Ver estadísticas
git log --stat
```

---

## ✅ Checklist del Proyecto

Verifica que hayas completado:

- [ ] Estructura del proyecto creada
- [ ] Entorno virtual configurado
- [ ] Modelo de datos implementado (todo.py)
- [ ] Capa de persistencia implementada (storage.py)
- [ ] Interfaz CLI implementada (cli.py)
- [ ] Tests unitarios creados y pasando
- [ ] Puedes añadir tareas
- [ ] Puedes listar tareas
- [ ] Puedes completar tareas
- [ ] Puedes eliminar tareas
- [ ] Las tareas persisten entre ejecuciones
- [ ] Documentación completa
- [ ] Commits organizados en Git

---

## 🚀 Ejercicios de Extensión

### Ejercicio 1: Fechas límite
Añade soporte para fechas límite en las tareas.

### Ejercicio 2: Etiquetas
Implementa un sistema de etiquetas para categorizar tareas.

### Ejercicio 3: Exportación
Añade capacidad de exportar tareas a CSV o Markdown.

### Ejercicio 4: Estadísticas
Crea un comando `stats` que muestre estadísticas de las tareas.

### Ejercicio 5: Interfaz interactiva
Crea un modo interactivo con menú de opciones.

---

## 🎓 Conceptos Clave Aprendidos

- ✅ Desarrollo completo de aplicación con Claude Code
- ✅ Arquitectura de aplicación CLI en Python
- ✅ Uso de dataclasses y type hints
- ✅ Persistencia de datos en JSON
- ✅ Testing con pytest
- ✅ Manejo de excepciones personalizadas
- ✅ Interfaz de usuario en terminal
- ✅ Control de versiones con Git
- ✅ Documentación de proyectos

---

## ➡️ Próximo Paso

¡Felicidades! Has completado un proyecto real con Claude Code. Ahora aprenderás las mejores prácticas para maximizar tu productividad.

**[Continuar al Módulo 5: Mejores Prácticas y Recursos →](./modulo-5-mejores-practicas.md)**

---

## 📚 Recursos Adicionales

- [Python Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [JSON in Python](https://docs.python.org/3/library/json.html)
