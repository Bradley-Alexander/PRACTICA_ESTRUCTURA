class QueueArrayOperations:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_full(self):
        return len(self.queue) >= self.max_size

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue.append(item)

    @property
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def get_all(self):
        return self.queue

    def __str__(self):
        return "\n".join(str(item) for item in self.queue)
