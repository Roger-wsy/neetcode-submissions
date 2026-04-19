class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.numList)
        self.numList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx = self.numMap[val]
        lastElement = self.numList[-1]
        self.numList[idx] = lastElement
        self.numMap[lastElement] = idx
        self.numList.pop()
        del self.numMap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.numList)