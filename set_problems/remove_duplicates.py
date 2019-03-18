"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        limit = len(nums)

        while j < limit:
            if nums[i] == nums[j]:
                nums.remove(nums[j])
                limit -= 1
            else:
                j += 1;
                i += 1
        return len(nums)


