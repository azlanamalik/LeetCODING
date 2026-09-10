#not sure why it says beats 63% check it???
##seems like the fastest possible method CHECK THIS

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        keep_track = set()
        for x in nums:
            if x in keep_track:
                return True
            keep_track.add(x)
        return False