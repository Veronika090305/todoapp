class TaskManager:
    def __init__(self):
        self._tasks = []

    def __len__(self):
        return len(self._tasks)