class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x,y = 0,0
        ans = []
        while x < len(word1) or y < len(word2):
            if x < len(word1):
                ans.append(word1[x])
            if y < len(word2):
                ans.append(word2[y])
            x += 1
            y += 1
        return "".join(ans)
