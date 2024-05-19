from controls.tda.queue.queueOperations import QueueOperation
 
class Queue:
    def __init__(self, tope):
        self.__queue = QueueOperation(tope)

    def push(self, data):
        self.__queue.queue(data)

    def pop(self):
        self.__queue.dequeue
    
    @property
    def print(self):
        self.__queue.print
    
    @property
    def verify(self):
        return self.__queue.verifyTop
    