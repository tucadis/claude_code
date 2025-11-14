#!/usr/bin/env python3
"""
Tests para el módulo todo.
"""

import pytest
from datetime import datetime
from src.todo import Task, TodoList, TaskNotFoundError


class TestTask:
    """Tests para la clase Task."""

    def test_create_task_with_defaults(self):
        """Test crear tarea con valores por defecto."""
        task = Task(id=1, title="Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.completed is False
        assert isinstance(task.created_at, datetime)
        assert task.completed_at is None

    def test_create_task_with_description(self):
        """Test crear tarea con descripción."""
        task = Task(id=1, title="Test Task", description="Test Description")

        assert task.description == "Test Description"

    def test_task_to_dict(self):
        """Test conversión de tarea a diccionario."""
        task = Task(id=1, title="Test Task", description="Description")
        task_dict = task.to_dict()

        assert task_dict["id"] == 1
        assert task_dict["title"] == "Test Task"
        assert task_dict["description"] == "Description"
        assert task_dict["completed"] is False
        assert "created_at" in task_dict
        assert task_dict["completed_at"] is None

    def test_task_from_dict(self):
        """Test crear tarea desde diccionario."""
        data = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": False,
            "created_at": "2024-01-15T10:30:00",
            "completed_at": None
        }

        task = Task.from_dict(data)

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False


class TestTodoList:
    """Tests para la clase TodoList."""

    def test_create_empty_todo_list(self):
        """Test crear lista vacía."""
        todo_list = TodoList()

        assert len(todo_list.tasks) == 0
        assert todo_list.next_id == 1

    def test_add_task(self):
        """Test añadir tarea."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Task", "Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert len(todo_list.tasks) == 1
        assert todo_list.next_id == 2

    def test_add_task_increments_id(self):
        """Test que el ID se incrementa correctamente."""
        todo_list = TodoList()
        task1 = todo_list.add_task("Task 1")
        task2 = todo_list.add_task("Task 2")

        assert task1.id == 1
        assert task2.id == 2
        assert todo_list.next_id == 3

    def test_add_task_with_empty_title_raises_error(self):
        """Test que título vacío lanza error."""
        todo_list = TodoList()

        with pytest.raises(ValueError, match="El título no puede estar vacío"):
            todo_list.add_task("")

        with pytest.raises(ValueError):
            todo_list.add_task("   ")

    def test_get_task(self):
        """Test obtener tarea por ID."""
        todo_list = TodoList()
        added_task = todo_list.add_task("Test Task")

        retrieved_task = todo_list.get_task(1)

        assert retrieved_task.id == added_task.id
        assert retrieved_task.title == added_task.title

    def test_get_task_not_found_raises_error(self):
        """Test que buscar tarea inexistente lanza error."""
        todo_list = TodoList()

        with pytest.raises(TaskNotFoundError, match="No se encontró la tarea con ID 999"):
            todo_list.get_task(999)

    def test_get_all_tasks(self):
        """Test obtener todas las tareas."""
        todo_list = TodoList()
        todo_list.add_task("Task 1")
        todo_list.add_task("Task 2")
        todo_list.add_task("Task 3")

        all_tasks = todo_list.get_all_tasks()

        assert len(all_tasks) == 3
        assert all_tasks[0].title == "Task 1"
        assert all_tasks[2].title == "Task 3"

    def test_get_pending_tasks(self):
        """Test obtener tareas pendientes."""
        todo_list = TodoList()
        task1 = todo_list.add_task("Task 1")
        task2 = todo_list.add_task("Task 2")
        task3 = todo_list.add_task("Task 3")

        # Completar una tarea
        task2.completed = True

        pending = todo_list.get_pending_tasks()

        assert len(pending) == 2
        assert task1 in pending
        assert task3 in pending
        assert task2 not in pending

    def test_get_completed_tasks(self):
        """Test obtener tareas completadas."""
        todo_list = TodoList()
        task1 = todo_list.add_task("Task 1")
        task2 = todo_list.add_task("Task 2")
        task3 = todo_list.add_task("Task 3")

        # Completar dos tareas
        task1.completed = True
        task3.completed = True

        completed = todo_list.get_completed_tasks()

        assert len(completed) == 2
        assert task1 in completed
        assert task3 in completed
        assert task2 not in completed

    def test_complete_task(self):
        """Test completar tarea."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Task")

        completed_task = todo_list.complete_task(1)

        assert completed_task.completed is True
        assert completed_task.completed_at is not None
        assert isinstance(completed_task.completed_at, datetime)

    def test_complete_already_completed_task(self):
        """Test completar tarea ya completada."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Task")

        # Completar dos veces
        first_completion = todo_list.complete_task(1)
        first_completed_at = first_completion.completed_at

        second_completion = todo_list.complete_task(1)

        # La fecha de completado no debería cambiar
        assert second_completion.completed_at == first_completed_at

    def test_delete_task(self):
        """Test eliminar tarea."""
        todo_list = TodoList()
        todo_list.add_task("Task 1")
        todo_list.add_task("Task 2")
        todo_list.add_task("Task 3")

        deleted_task = todo_list.delete_task(2)

        assert deleted_task.title == "Task 2"
        assert len(todo_list.tasks) == 2
        assert deleted_task not in todo_list.tasks

    def test_delete_task_not_found_raises_error(self):
        """Test que eliminar tarea inexistente lanza error."""
        todo_list = TodoList()

        with pytest.raises(TaskNotFoundError):
            todo_list.delete_task(999)

    def test_todo_list_to_dict(self):
        """Test conversión de TodoList a diccionario."""
        todo_list = TodoList()
        todo_list.add_task("Task 1")
        todo_list.add_task("Task 2")

        data = todo_list.to_dict()

        assert "tasks" in data
        assert "next_id" in data
        assert len(data["tasks"]) == 2
        assert data["next_id"] == 3

    def test_todo_list_from_dict(self):
        """Test crear TodoList desde diccionario."""
        data = {
            "tasks": [
                {
                    "id": 1,
                    "title": "Task 1",
                    "description": "",
                    "completed": False,
                    "created_at": "2024-01-15T10:30:00",
                    "completed_at": None
                },
                {
                    "id": 2,
                    "title": "Task 2",
                    "description": "Description",
                    "completed": True,
                    "created_at": "2024-01-15T10:30:00",
                    "completed_at": "2024-01-15T11:00:00"
                }
            ],
            "next_id": 3
        }

        todo_list = TodoList.from_dict(data)

        assert len(todo_list.tasks) == 2
        assert todo_list.next_id == 3
        assert todo_list.tasks[0].title == "Task 1"
        assert todo_list.tasks[1].title == "Task 2"
        assert todo_list.tasks[1].completed is True
