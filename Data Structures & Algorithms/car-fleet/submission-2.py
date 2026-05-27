class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Vars
        position[i] - i car's position in miles
        speed[i] - i car's speed in mph
        target - dest in miles
        
        Constraints
        A car can NOT pass another. Instead it can catch up and drive
        same speed. If that happens, these cars become a car fleet.
        A single car can also be a car fleet

        Return
        Unique car fleets

        Example:
        car 1: p = 1, s = 3
        car 2: p = 4, s = 2
        t = 10
        t = 1, car1 is at 4, car2 is at 6
        t = 2, car1 is at 7, car2 is at 8
        t = 3, car1 is at 10, car2 is at 10 --> 1 Car Fleet

        We want to calculate time it takes to reach dest for each car
        car0 = 4
        car1: 10/3 = 3.33
        car2: 10/2 = 5

        Because car2 is ahead of car1 at the start, and car 1 takes less time
        to destination, we know car1 and car2 become a fleet.
        """
        pairs = list(zip(position,speed))
        sorted_pairs = sorted(pairs,key=lambda x:x[0])
        print(sorted_pairs)

        stack = []
        for i in range(len(sorted_pairs)-1,-1,-1):
            time_to_dest = (target-sorted_pairs[i][0]) / sorted_pairs[i][1]
            stack.append(time_to_dest)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
