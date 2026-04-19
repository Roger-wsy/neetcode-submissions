class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0

        for n in nums:
            count = 0
            i = n
            while i in seen:
                count+=1
                i+=1
            ans = max(ans, count)
        return ans