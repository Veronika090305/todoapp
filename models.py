from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False


class TaskManager:
    def __init__(self):
        self._tasks = []

    def __len__(self):
        return len(self._tasks)

    def add_task(self, title):
        task = Task(title=title)
        self._tasks.append(task)
        return task