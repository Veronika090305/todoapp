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
        if title is None or not title.strip():
            raise ValueError("Заголовок задачи не может быть пустым")
        task = Task(id=self._next_id, title=title.strip())
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def all_tasks(self):
        return list(self._tasks)

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task is not None:
            task.done = True
        return task

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task is not None:
            self._tasks.remove(task)
        return task

    def active_count(self):
        return sum(1 for task in self._tasks if not task.done)