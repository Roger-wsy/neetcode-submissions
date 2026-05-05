class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nextArr = []

    def next(self, val: int) -> float:
        self.nextArr.append(val)

        if len(self.nextArr) > self.size:
            self.nextArr.pop(0)

        sumArr = sum(self.nextArr)
        ave = sumArr / len(self.nextArr)

        return ave