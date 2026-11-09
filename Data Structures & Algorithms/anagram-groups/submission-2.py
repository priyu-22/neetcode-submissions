class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} 
        for st in strs:
            sortedSt = "".join(sorted(st))
            if sortedSt in anagrams:
                anagrams[sortedSt].append(st)
            else:
                anagrams[sortedSt] = [st]
        return list(anagrams.values())

