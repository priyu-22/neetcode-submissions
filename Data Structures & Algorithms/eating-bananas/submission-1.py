class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # start from 1 to the max number in piles. 
        res = r #max at the rate of k, koko can eat bananas
        # we need to find minimum rate of k 
        while l <= r:
            k = (l+r)//2
            
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res