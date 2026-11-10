class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        tog = zip(position, speed)

        togSort = sorted(tog, reverse=True)

        # (7, 1), (4, 2), (1, 2), (0, 1)

        endingTime = [] 
        for i in range(len(togSort)):
            if endingTime != [] and endingTime[-1] >= ((target - togSort[i][0]) / togSort[i][1]):
                continue
            else:
                endingTime.append((target - togSort[i][0]) / togSort[i][1])
        return len(endingTime)
        
