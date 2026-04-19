class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for index,num in enumerate(nums):
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for key, value in hashMap.items():
            if value >= 2:
                return True
        
        return False