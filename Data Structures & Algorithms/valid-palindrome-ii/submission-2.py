class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Try skipping either the left or the right character
                case1 = s[l+1:r+1]
                case2 = s[l:r]
                return case1 == case1[::-1] or case2 == case2[::-1]
            
            l += 1
            r -= 1
        
        return True