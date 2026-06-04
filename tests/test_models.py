import pytest

from models import TaskManager

def test_new_list_is_empty():
    manager = TaskManager()
    assert len(manager) == 0

def test_add_task_increases_count():
    manager = TaskManager()
    manager.add_task("Купить хлеб")
    assert len(manager) == 1

def test_add_task_sets_title():
    manager = TaskManager()
    task = manager.add_task("Купить хлеб")
    assert task.title == "Купить хлеб"

def test_new_task_is_not_done():
    manager = TaskManager()
    task = manager.add_task("Купить хлеб")
    assert task.done is False

def test_tasks_get_unique_ids():
    manager = TaskManager()
    first = manager.add_task("Задача 1")
    second = manager.add_task("Задача 2")
    assert first.id != second.id
    assert second.id == first.id + 1

def test_get_task_by_id():
    manager = TaskManager()
    task = manager.add_task("Задача")
    assert manager.get_task(task.id) is task
    assert manager.get_task(999) is None

def test_complete_task_marks_done():
    manager = TaskManager()
    task = manager.add_task("Задача")
    manager.complete_task(task.id)
    assert task.done is True

def test_delete_task_removes_it():
    manager = TaskManager()
    task = manager.add_task("Задача")
    manager.delete_task(task.id)
    assert len(manager) == 0

def test_add_empty_title_raises():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("   ")

def test_active_count():
    manager = TaskManager()
    a = manager.add_task("A")
    manager.add_task("B")
    manager.complete_task(a.id)
    assert manager.active_count() == 1

def test_clear_completed():
    manager = TaskManager()
    a = manager.add_task("A")
    manager.add_task("B")
    manager.complete_task(a.id)
    manager.clear_completed()
    assert len(manager) == 1
    assert manager.active_count() == 1

def test_rename_task():
    manager = TaskManager()
    task = manager.add_task("Старое название")
    manager.rename_task(task.id, "Новое название")
    assert task.title == "Новое название"
