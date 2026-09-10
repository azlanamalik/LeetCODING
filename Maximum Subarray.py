"""
solved using hint

else naive approach was taken of adding prev array to next int

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        maximum = 0
        temp = 0
        while (l <= len(nums) and r <= len(nums) - 1 ):
            temp = temp + nums[r]
            if temp <0:
                l = r
                temp = 0
            else:
                print(temp)
                maximum = max(maximum , temp)
            print("maximum " + str(maximum))
            r = r + 1
        return maximum
