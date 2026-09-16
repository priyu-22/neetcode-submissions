class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Count = Counter(s1) 
        s2Count = Counter(s2[:len(s1)])
        if s1Count == s2Count:
            return True
        l=0
        for r in range(len(s1),len(s2)):
            s2Count[s2[r]] +=1
            s2Count[s2[l]] -=1
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]
            l+=1
            if s1Count == s2Count:
                return True
        return False