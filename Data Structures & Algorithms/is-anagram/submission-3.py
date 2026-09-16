class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for ch in s:
            hm[ch] = hm.get(ch,0)+1
        for ch in t:
            hm[ch] = hm.get(ch,0)-1

        return all(count == 0 for count in hm.values())
