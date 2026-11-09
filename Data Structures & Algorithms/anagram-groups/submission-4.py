class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #optimized solution
        anagrams = defaultdict(list)

        for st in strs:
            count = [0] * 26 # create array of 26 size
            for ch in st:
                count[ord(ch)-ord('a')] +=1
            anagrams[tuple(count)].append(st)
        return list(anagrams.values())


