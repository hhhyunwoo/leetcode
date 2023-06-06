from queue import PriorityQueue

class MedianFinder:

    def __init__(self):
        self.q1 = PriorityQueue()
        self.q2 = PriorityQueue()

    def addNum(self, num: int) -> None:
        # Add num to q1 for default. q1 is Max heap
        self.q1.put(-1 * num)

        while True:
            qDiff = self.q1.qsize() - self.q2.qsize()
            if qDiff < -1:
                minFromQ2 = self.q2.get()
                self.q1.put(minFromQ2 * -1)
            elif qDiff > 1:
                maxFromQ1 = self.q1.get() * -1
                self.q2.put(maxFromQ1)
            elif self.q1.qsize() > 0 and self.q2.qsize() > 0 :
                if self.q1.queue[0] * -1 <= self.q2.queue[0]:
                    break
                else:
                    maxFromQ1 = self.q1.get() * -1
                    self.q2.put(maxFromQ1)
            else:
                break

    def findMedian(self) -> float:
        if self.q1.qsize() == 0:
            return self.q2.queue[0]
        elif self.q2.qsize() == 0 :
            return self.q1.queue[0] * -1
        elif self.q1.qsize() > self.q2.qsize():
            return self.q1.queue[0] * -1
        elif self.q1.qsize() < self.q2.qsize():
            return self.q2.queue[0]
        else:
            return (self.q1.queue[0] * -1 + self.q2.queue[0]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(-1)
# print(obj.findMedian())
# obj.addNum(-2)
# print(obj.findMedian())
# obj.addNum(-3)
# print(obj.findMedian())
# obj.addNum(-4)
# print(obj.findMedian())
# obj.addNum(-5)
# print(obj.findMedian())

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())