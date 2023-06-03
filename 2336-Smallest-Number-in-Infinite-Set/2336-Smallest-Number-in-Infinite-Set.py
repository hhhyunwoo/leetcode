from queue import PriorityQueue

class SmallestInfiniteSet:

    def __init__(self):
        self.queue = PriorityQueue()
        self.visited = []
        for i in range(1,1001):
            self.queue.put(i)
            self.visited.append(i)

    def popSmallest(self) -> int:
        popNum = self.queue.get()
        if popNum in self.visited:
            self.visited.remove(popNum)
        return popNum
        

    def addBack(self, num: int) -> None:
        if num not in self.visited:
            self.queue.put(num)
            self.visited.append(num)
        return