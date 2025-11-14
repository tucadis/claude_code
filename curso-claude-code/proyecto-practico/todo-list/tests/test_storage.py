#!/usr/bin/env python3
"""
Tests para el módulo storage.
"""

import pytest
import json
import tempfile
from pathlib import Path
from src.storage import JSONStorage, StorageError
from src.todo import TodoList


class TestJSONStorage:
    """Tests para la clase JSONStorage."""

    @pytest.fixture
    def temp_file(self):
        """Fixture para crear archivo temporal."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_path = f.name
        yield temp_path
        # Cleanup
        Path(temp_path).unlink(missing_ok=True)

    @pytest.fixture
    def temp_dir(self):
        """Fixture para crear directorio temporal."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield temp_dir

    def test_create_storage_creates_directory(self, temp_dir):
        """Test que crear storage crea el directorio."""
        storage_path = Path(temp_dir) / "data" / "tasks.json"
        storage = JSONStorage(str(storage_path))

        assert storage_path.parent.exists()

    def test_exists_returns_false_for_new_file(self, temp_dir):
        """Test que exists retorna False para archivo nuevo."""
        storage_path = Path(temp_dir) / "tasks.json"
        storage = JSONStorage(str(storage_path))

        assert storage.exists() is False

    def test_exists_returns_true_for_existing_file(self, temp_file):
        """Test que exists retorna True para archivo existente."""
        storage = JSONStorage(temp_file)

        assert storage.exists() is True

    def test_save_todo_list(self, temp_dir):
        """Test guardar lista de tareas."""
        storage_path = Path(temp_dir) / "tasks.json"
        storage = JSONStorage(str(storage_path))

        todo_list = TodoList()
        todo_list.add_task("Task 1", "Description 1")
        todo_list.add_task("Task 2", "Description 2")

        storage.save(todo_list)

        assert storage_path.exists()

        # Verificar contenido del archivo
        with open(storage_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        assert "tasks" in data
        assert "next_id" in data
        assert len(data["tasks"]) == 2
        assert data["next_id"] == 3

    def test_load_empty_file_returns_empty_todo_list(self, temp_dir):
        """Test que cargar archivo vacío retorna TodoList vacía."""
        storage_path = Path(temp_dir) / "tasks.json"
        storage = JSONStorage(str(storage_path))

        todo_list = storage.load()

        assert len(todo_list.tasks) == 0
        assert todo_list.next_id == 1

    def test_load_todo_list(self, temp_dir):
        """Test cargar lista de tareas."""
        storage_path = Path(temp_dir) / "tasks.json"
        storage = JSONStorage(str(storage_path))

        # Crear y guardar
        original_list = TodoList()
        original_list.add_task("Task 1", "Description 1")
        original_list.add_task("Task 2", "Description 2")
        original_list.complete_task(1)
        storage.save(original_list)

        # Cargar
        loaded_list = storage.load()

        assert len(loaded_list.tasks) == 2
        assert loaded_list.next_id == 3
        assert loaded_list.tasks[0].title == "Task 1"
        assert loaded_list.tasks[0].completed is True
        assert loaded_list.tasks[1].title == "Task 2"
        assert loaded_list.tasks[1].completed is False

    def test_save_and_load_preserves_data(self, temp_dir):
        """Test que guardar y cargar preserva todos los datos."""
        storage_path = Path(temp_dir) / "tasks.json"
        storage = JSONStorage(str(storage_path))

        # Crear lista con datos completos
        original_list = TodoList()
        task1 = original_list.add_task("Task 1", "Description 1")
        task2 = original_list.add_task("Task 2", "Description 2")
        original_list.complete_task(1)

        # Guardar y cargar
        storage.save(original_list)
        loaded_list = storage.load()

        # Verificar que los datos son idénticos
        assert loaded_list.next_id == original_list.next_id
        assert len(loaded_list.tasks) == len(original_list.tasks)

        for orig, loaded in zip(original_list.tasks, loaded_list.tasks):
            assert loaded.id == orig.id
            assert loaded.title == orig.title
            assert loaded.description == orig.description
            assert loaded.completed == orig.completed

    def test_load_corrupted_json_raises_error(self, temp_file):
        """Test que cargar JSON corrupto lanza error."""
        # Escribir JSON inválido
        with open(temp_file, 'w') as f:
            f.write("{ invalid json }")

        storage = JSONStorage(temp_file)

        with pytest.raises(StorageError, match="Error al decodificar JSON"):
            storage.load()

    def test_save_with_unicode_characters(self, temp_dir):
        """Test guardar con caracteres unicode."""
        storage_path = Path(temp_dir) / "tasks.json"
        storage = JSONStorage(str(storage_path))

        todo_list = TodoList()
        todo_list.add_task("Tarea en español", "Descripción con ñ y acentos: áéíóú")
        todo_list.add_task("任务", "中文描述")

        storage.save(todo_list)
        loaded_list = storage.load()

        assert loaded_list.tasks[0].title == "Tarea en español"
        assert "ñ" in loaded_list.tasks[0].description
        assert loaded_list.tasks[1].title == "任务"

    def test_multiple_save_load_cycles(self, temp_dir):
        """Test múltiples ciclos de guardar y cargar."""
        storage_path = Path(temp_dir) / "tasks.json"
        storage = JSONStorage(str(storage_path))

        # Primer ciclo
        list1 = TodoList()
        list1.add_task("Task 1")
        storage.save(list1)

        # Segundo ciclo
        list2 = storage.load()
        list2.add_task("Task 2")
        storage.save(list2)

        # Tercer ciclo
        list3 = storage.load()
        list3.add_task("Task 3")
        storage.save(list3)

        # Verificar resultado final
        final_list = storage.load()
        assert len(final_list.tasks) == 3
        assert final_list.next_id == 4
