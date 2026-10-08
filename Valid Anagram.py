class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)



#alternative way is to use hashmaps:
#see this methodology to get familiar with hashmaps


class solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)#gfor the value at s[i] we increment by 1 but get allows us to add a 0 case incase dont exist(new val)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT