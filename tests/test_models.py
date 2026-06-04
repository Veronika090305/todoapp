from models import TaskManager

def test_new_list_is_empty():
    manager = TaskManager()
    assert len(manager) == 0