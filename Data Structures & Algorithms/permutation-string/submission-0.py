class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        testDict = {}
        for val in s1:
            if val not in testDict:
                testDict[val] = 1
            else:
                testDict[val] += 1


        resDict = {}
        for val in s2[l:r + 1]:
            if val not in resDict:
                resDict[val] = 1
            else:
                resDict[val] += 1

        while r <= len(s2) - 1:
            if resDict == testDict:
                return True
            else:
                if resDict[s2[l]] == 1:
                    resDict.pop(s2[l])
                else:
                    resDict[s2[l]] -= 1
                l += 1
                r += 1
                if r == len(s2):
                    break

                if s2[r] not in resDict:
                    resDict[s2[r]] = 1
                else:
                    resDict[s2[r]] += 1
        
        return False
        