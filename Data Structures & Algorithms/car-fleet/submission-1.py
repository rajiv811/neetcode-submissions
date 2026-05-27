class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position: position of car i in miles
        speed: speed of car i in mph
        target: destination in miles

        Constraints:
        - car can not pass another car, can only catch up
        - car fleet: non empty set of cars driving at same speed

        Return:
        - # of unique/different car fleets

        Example:
        p = [1,4] meaning car 0 is at mile 1 and car 1 is at mile 4
        s = [3,2] car 0 going 3 mph and car 1 going 2 mph
        t = 10 miles

        Algorithm:
        1. new list with (position,mph)
        2. Sort list, in reverse order
        3. Compare time to target (distance / mph)
        4. If ttt[i] < ttt[j] (j = i + 1), then they become a fleet.
        5. Pop greater value from the stack as there is no need for it.
        """

        pairs = zip(position,speed)
        list_pairs = list(pairs)
        list_pairs.sort(reverse=True)
        stack = []

        for p,s in list_pairs:
            stack.append((target-p) / s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)