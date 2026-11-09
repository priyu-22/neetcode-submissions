class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for st in strs:
            sortedSt = "".join(sorted(st))
            anagrams[sortedSt].append(st)
        return list(anagrams.values())

