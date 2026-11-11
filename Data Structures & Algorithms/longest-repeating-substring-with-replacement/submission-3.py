class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxLength = 0
        maxCount = 0
        seen = {}

        for val in s:
            if val not in seen:
                seen[val] = 0

        while r <= len(s) - 1:
            seen[s[r]] += 1
            if seen[s[r]] > maxCount:
                maxCount = seen[s[r]]

            if (r - l + 1) - maxCount > k:
                if seen[s[l]] == maxCount:
                    maxCount -= 1
                    seen[s[l]] -= 1
                else:
                    seen[s[l]] -= 1
                l += 1
                r += 1
            else:
                if (r - l + 1) > maxLength:
                    maxLength = r - l + 1
                r += 1
        
        return maxLength





        