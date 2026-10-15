class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqs1 = Counter(s1) # TC: O(26)
        freqs2 = Counter(s2[:len(s1)]) # just first len(s1) substring count # O(26)
        # if we find substring at begining then return True
        if freqs1 == freqs2:
            return True
        # for rest of the part lets do fixed sized window iteration
        l = 0
        for r in range(len(s1), len(s2)): # we hava already check first len(s1) char substring of s2. hence start from len(s1) #O(n)
            freqs2[s2[r]]+=1 # adding right char to window
            freqs2[s2[l]]-=1 # removing left char from window
            if freqs2[s2[l]] == 0:
                del freqs2[s2[l]] # delete removed left char if its count is 0
            l+=1
            if freqs1 == freqs2:
                return True
        return False # TC: O(26n) = O(n) 
        
        