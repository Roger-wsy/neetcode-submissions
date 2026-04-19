class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in visited:
                return [visited[compliment], i]
            visited[n] = i
        
        