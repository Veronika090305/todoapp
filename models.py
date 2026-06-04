class TaskManager:
    def __init__(self):
        self._tasks = []

    def __len__(self):
        return len(self._tasks)

    def add_task(self, title):
        self._tasks.append(title)