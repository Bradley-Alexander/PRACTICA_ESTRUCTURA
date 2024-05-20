from controls.tda.queue.queueArrayOperations import QueueArrayOperations

class QueueArray:
    def __init__(self, max_size):
        self.queue_operations = QueueArrayOperations(max_size)

    def push(self, item):
        self.queue_operations.enqueue(item)

    def pop(self):
        return self.queue_operations.dequeue

    @property
    def print_queue(self):
        return self.queue_operations.get_all()

    @property
    def print(self):
        data = ""
        for item in self.queue_operations.get_all():
            data += str(item) + "\t"
        print("Lista de Datos:")
        print(data)

    def __str__(self):
        return str(self.queue_operations)
