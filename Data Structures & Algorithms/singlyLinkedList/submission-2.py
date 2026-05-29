from collections import deque
class LinkedList:
    
    def __init__(self):
        self.d = deque()
    
    def get(self, index: int) -> int:
        try:
            return self.d[index]
        except IndexError:
            return -1

    def insertHead(self, val: int) -> None:
        self.d.appendleft(val)

    def insertTail(self, val: int) -> None:
        self.d.append(val)

    def remove(self, index: int) -> bool:
        try:
            del self.d[index]
            return True
        except IndexError:
            return False

    def getValues(self) -> List[int]:
        return list(self.d)
