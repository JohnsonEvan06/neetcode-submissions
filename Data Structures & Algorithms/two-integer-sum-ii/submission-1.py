class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        for l in range(len(numbers)):
            if numbers[l] in seen:
                continue
            
            for r in range(l + 1, len(numbers)):
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                else:
                    continue
            seen.add(numbers[l])
        
        