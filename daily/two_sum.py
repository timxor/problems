class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        i, j = 0, 1

        while j < len(nums):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result
            j += 1

            if j == len(nums) - 1:
                i += 1

        return result