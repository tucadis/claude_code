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
