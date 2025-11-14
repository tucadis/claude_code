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
