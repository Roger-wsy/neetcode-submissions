class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in hashStr:
                hashStr[sortedS] = []
            hashStr[sortedS].append(s)

        return list(hashStr.values())