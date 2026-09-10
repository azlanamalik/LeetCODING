"""

This is a O(n^2) approach, best is O(n)


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_arr = []
        for x in range(0,len(nums)):
            temp = 1
            for i in range(0,len(nums)):
                if (x != i):
                    print(temp)
                    temp = temp * nums[i]
            final_arr.append(temp)
        return final_arr


