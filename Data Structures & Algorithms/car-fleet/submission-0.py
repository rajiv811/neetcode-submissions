class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position: len n, position[i] position of ith car
        # speed: len n, speed[i] speed of ith car

        # [4,1,0,7] [2,2,1,1] target = 10
        """
        1. 6,3,1,8
        2. 8,5,2,9
        3. 10,7,3,10
        """
        pairs = [[pos,speed] for pos,speed in zip(position,speed)]
        pairs.sort(reverse=True)
        stack = []

        for p,s in pairs:
            stack.append((target-p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)