from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def __len__(self):
        return len(self._tasks)

    def add_task(self, title):
        task = Task(id=self._next_id, title=title)
        self._tasks.append(task)
        self._next_id += 1
        return task