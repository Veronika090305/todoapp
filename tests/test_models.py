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