class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        seen = []
        result = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):

            while seen != [] and temperatures[seen[-1]] < temperatures[i]:
                x = seen.pop()
                result[x] = i - x

            seen.append(i)
        return result