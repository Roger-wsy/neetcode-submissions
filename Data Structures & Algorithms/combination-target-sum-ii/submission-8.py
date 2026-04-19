class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def dfs(start, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if total > target or start >=n:
                return
            
            for i in range(start, n):
                # 🔥 skip duplicates at same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()
        
        dfs(0,[], 0)
        return ans