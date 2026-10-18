class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        l = 0
        curr_sum = 0
        count = 0

        for r in range(len(arr)):
            curr_sum += arr[r]
            if (r-l+1) > k:
                curr_sum-= arr[l]
                l+=1
            if (r-l+1) ==k and curr_sum >= (threshold*k):
                count+=1
        return count

