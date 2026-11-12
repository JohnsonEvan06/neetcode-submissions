class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        result = []
        pastVal = float('inf')
        currVal = 0
        test = False

        while r <= len(nums) - 1:
            for val in nums[l:r + 1]:
                currVal = val
                if k == 1:
                    test = True
                if pastVal == float('inf'):
                    pastVal = val
                elif pastVal + 1 != currVal:
                    result.append(-1)
                    test = False
                    break
                else:
                    test = True
                pastVal = currVal
            if test:
                result.append(nums[r])
            pastVal = float('inf')
            test = False
            currVal = 0
            l += 1
            r += 1

        return result

