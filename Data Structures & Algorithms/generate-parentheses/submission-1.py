class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_p, close_p = 0,0
        res = []
        def backtrack(open_p,close_p, sol):
            if open_p == close_p == n:
                res.append(sol)
            if open_p > close_p:
                backtrack(open_p, close_p + 1, sol +")")
            if n > open_p:
                backtrack(open_p+1, close_p, sol +"(")
        
        backtrack(open_p,close_p,"")
        return res