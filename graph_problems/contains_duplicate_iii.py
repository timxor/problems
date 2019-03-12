'''
https://leetcode.com/problems/contains-duplicate-iii/
'''

# still needs work
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        for i, value1 in enumerate(nums):
            for j, value2 in enumerate(nums, start=1):
                print(i, value1, j, value2)
                if (j-i) < k and abs(value2 - value1) < t:
                    return True
        return False
