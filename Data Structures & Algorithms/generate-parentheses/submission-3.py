class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Backtracking
        Make a choice — choose a possible option to proceed with.
        Explore — move forward recursively with that choice.
        Check if solution — if the current state meets the problem requirements, save or return it.
        Backtrack — undo the choice and try another option.
        Brute Force Approach
Generate all possible strings of length 2n using '(' and ')'.

That’s 2^2n possibilities.

Then check each one if it's valid (balanced parentheses).

Huge problem:

Most generated strings are invalid, so you're wasting tons of time checking useless candidates.

The time complexity explodes exponentially with 
𝑛
n.

Backtracking Approach (Your Code)
Build strings step-by-step, but only make valid moves:

You add '(' only if you still have '(' left to add.

You add ')' only if it won’t unbalance the string (only if closedN < openN).

This prunes the search space drastically:

You never explore invalid partial strings.

The recursion tree is much smaller than brute force.
        """
        stack = []
        res = []

        def backtrack(openN,closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res
        """
        Brute Force
        """
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
        