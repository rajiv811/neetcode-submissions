class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        arith = ["+","-","/","*"]
        res = 0
        for i in range(len(tokens)):
            if tokens[i] not in arith:
                stack.append(int(tokens[i]))
            else:
                f_num = stack.pop()
                s_num = stack.pop()
                if tokens[i] == "+":
                    res = f_num+s_num
                    stack.append(res)
                elif tokens[i] == "-":
                    res = s_num-f_num
                    stack.append(res)
                elif tokens[i] == "*":
                    res = f_num*s_num
                    stack.append(res)
                elif tokens[i] == "/":
                    res = int(float(s_num) / f_num)
                    stack.append(res)
        return res
                

                
            