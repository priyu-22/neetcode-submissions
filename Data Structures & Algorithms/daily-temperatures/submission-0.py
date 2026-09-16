class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair: [temp, index]
        res = [0] * (len(temperatures))
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = index - stack_index
            stack.append((temp, index))
        return res
        