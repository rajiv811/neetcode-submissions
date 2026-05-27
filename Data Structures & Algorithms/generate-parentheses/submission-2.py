class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(s):
            stack = []
            for i in (range(len(s))):
                if s[i] == ")" and (stack == [] or stack.pop() != "("):
                    return False
                if s[i] == "(":
                    stack.append(s[i])
            return stack == []

        def recursion(s):
            if n*2 == len(s):
                if isValid(s):
                    res.append(s)
                return
            recursion(s+"(")
            recursion(s+")")
        
        recursion("")
        return res
        