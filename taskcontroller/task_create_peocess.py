from multiprocessing import Process, Queue
from .funcs import hello, world

class Task:
    def __init__(self, works, params):
        self._works = works
        self._params = params

    def __call__(self):
        for work, param in zip(self._works, self._params):
            work(param)

class CreateTaskProcess(Process):
    def __init__(self, task_queue: Queue):
        super().__init__()
        self.task_queue = task_queue

    def run(self):
        print("Producer Start")

        task = Task([hello, world],["asdf",])
        
        self.task_queue.put(task)