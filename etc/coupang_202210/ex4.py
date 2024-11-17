import bisect


class HitCounter:

    def __init__(self):
        self.record = []

    def hit(self, timestamp: int) -> None:
        bisect.insort(self.record, timestamp)

    def getHits(self, timestamp: int) -> int:
        idx = 0
        start = 0
        end = len(self.record)
        for i in range(start, len(self.record)):
            if timestamp > 300 and timestamp - 300 <= self.record[i] and start == 0:
                start = i
            if self.record[i] > timestamp:
                end = i
                break
        print(end - start)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

hitCounter = HitCounter()
hitCounter.hit(1)
hitCounter.hit(2)
hitCounter.hit(3)
hitCounter.getHits(4)
hitCounter.hit(300)
hitCounter.getHits(300)
hitCounter.getHits(301)
hitCounter.hit(999)
hitCounter.hit(998)
hitCounter.hit(997)
hitCounter.hit(996)
hitCounter.getHits(998)

