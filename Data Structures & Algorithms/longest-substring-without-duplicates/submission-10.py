class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        bestLength = 0
        count = 0
        seen = set()

        while l <= len(s) - 1 and r <= len(s) - 1:
            if s[r] in seen:
                if count > bestLength:
                    bestLength = count
                seen.discard(s[l])
                count = count - 1
                l += 1
            else:
                count += 1
                seen.add(s[r])
                r += 1
        if count > bestLength:
            return count
        return bestLength



        