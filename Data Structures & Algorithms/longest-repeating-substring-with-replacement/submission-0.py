class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLength = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]]+=1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1
            maxLength = max(maxLength, (r-l+1))
        return maxLength