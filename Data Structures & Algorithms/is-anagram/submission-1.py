class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}
        x,y = 0, 0
        n,m = len(s), len(t)
        if n != m:
            return False
        
        
        while x < n and y < m:
            mapS[s[x]] = mapS.get(s[x], 0) + 1
            mapT[t[x]] = mapT.get(t[x], 0) + 1
            x += 1
            y += 1

        return mapS == mapT