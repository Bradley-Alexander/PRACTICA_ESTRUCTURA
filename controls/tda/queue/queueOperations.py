from controls.tda.linked.linkedList import Linked_List
class QueueOperation(Linked_List):
    def __init__(self, top):
        super().__init__()
        self.__top = top

    @property
    def _top(self):
        return self.__top

    @_top.setter
    def _top(self, value):
        self.__top = value

    @property
    def verifyTop(self):
        return self._lenght < self._top
    
    
    def queue(self, data):
        if self.verifyTop:
            self.add(data, self._lenght)
        else:
            raise print("Queue is Full")
        
    @property
    def dequeue(self):
        if self.isEmpty:
            raise print("Queue is Empty")
        else:
            self.delete(0)
