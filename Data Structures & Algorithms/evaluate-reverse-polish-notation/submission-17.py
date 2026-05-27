class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Input: tokens = ["1","2","+","3","*","4","-"]
        Data structure -> Stack
        1. Append elements until you come across +-*/
        2. When you come across +-*/, pop 2 elements and perform arithmetic
        3. Append result.
        4. Repeat
        """
        stack = []
        for element in tokens:
            if element == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first+second)
            elif element == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first)
            elif element == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first*second)
            elif element == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(element))
        return stack.pop()