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
