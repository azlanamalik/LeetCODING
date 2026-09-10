class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        set_of_dat = set()
        set_of_dat.update(nums)
        temp = 0
        for i,x in enumerate(nums):
            temp = (target - x)
            if temp in set_of_dat and i != nums.index(temp):
                print(temp)
                print(i)
                return [nums.index(temp),i]
        return




def test_case():
    Solution_inst = Solution()
    print(Solution_inst.twoSum([2,7,11,15],9))
    print(Solution_inst.twoSum([3,2,4],6))
    print(Solution_inst.twoSum([3,3],6))
test_case()