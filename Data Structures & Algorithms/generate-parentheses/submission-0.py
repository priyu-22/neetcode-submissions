class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack:List[str] = []
        res:List[str] = []
        def backtracking(openCnt:int, closeCnt: int):
            if openCnt == closeCnt == n:
                res.append("".join(stack))
                return
            if openCnt < n:
                stack.append('(')
                backtracking(openCnt + 1, closeCnt)
                stack.pop()
            if openCnt > closeCnt:
                stack.append(')')
                backtracking(openCnt, closeCnt+1)
                stack.pop()
        backtracking(0,0)
        return res
