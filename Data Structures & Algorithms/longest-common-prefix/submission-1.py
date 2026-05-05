class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        slen = float('inf')
        for s in strs:
            if len(s) < slen:
                slen = len(s)

        res = ''
        i = 0
        while i < slen:
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return res

            res += current_char
            i+=1


        return res