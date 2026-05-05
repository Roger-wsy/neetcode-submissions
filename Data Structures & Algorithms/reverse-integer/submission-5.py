class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0
        absX = abs(x)
        strX = str(absX)
        reverseStrX = strX[::-1]
        reverseIntX = int(reverseStrX)
        if isNeg:
            reverseIntX = -reverseIntX

        min_int = -(2 ** 31)
        max_int = (2 ** 31) - 1

        if reverseIntX < min_int or reverseIntX > max_int:
            return 0

        return reverseIntX