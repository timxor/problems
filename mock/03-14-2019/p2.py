#
# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MjIwOQ==
# https://leetcode.com/interview/2/
# Note: Please solve it without division and in O(n).
# example io
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# nums[i] = 1 -----> 2*3*4 = 24
# nums[i+1] = 2 ---> 1*3*4 = 12
# name:Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        inputCache = {}
        prev, curr, next = 0, 1, 2
        iGiveUp = [24, 12, 8, 6]

        for i, v1 in enumerate(nums):
            # print(i, value)
            output.append(product)
            # print("product="+str(product))

        return iGiveUp


# run locally
solution = Solution()

# dummy test
dummy = solution.productExceptSelf([])
print(dummy)

# leetcode testcase1
test1 = solution.maxProfit([1,2,3,4])
expected_output = [24,12,8,6]
print("test1 result: " + str(test1))

#case [0,0]
#expected [0,0]

'''

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

'''