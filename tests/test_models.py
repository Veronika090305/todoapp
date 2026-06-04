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