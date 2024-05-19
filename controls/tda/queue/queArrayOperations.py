class QueueArray:
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

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]

    def get_all(self):
        return self.queue

    def delete_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop()