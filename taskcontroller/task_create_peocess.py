from multiprocessing import Process, Queue
from .funcs import hello, world

class Task:
    def __init__(self, works):
        self._works = works

    def __call__(self):
        for work in self._works:
            work()

class CreateTaskProcess(Process):
    def __init__(self, task_queue: Queue):
        super().__init__()
        self.task_queue = task_queue

    def run(self):
        print("Producer Start")

        task = Task([hello, world])
        self.task_queue.put(task)