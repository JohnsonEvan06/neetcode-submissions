class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        start = int((r - l) / 2)

        while l != r and r > l:
            if nums[start] == target:
                return start
            elif nums[start] > target:
                r = start - 1
                start = int((r + l) / 2)
            else:
                l = start + 1
                start = int((r + l) / 2)

        
        if nums[l] == target:
            return l
        return -1