# https://leetcode.com/interview/1
#https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MjIwOQ==
#name:Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices) -> int:
        # extract profit
        max_profit = 0
        i, j = 0, len(prices) - 1

        # for value in enumerate(prices):

        while (i < j):
            # do stuff
            if prices[j] - prices[i] > max_profit:
                print("found new max profit. old profit=" + str(max_profit))
                print("new max_profit=" + str(prices[j] - prices[i]))
                max_profit = prices[j] - prices[i]
            i += 1;
            j -= 1
        return max_profit

# run locally
solution = Solution()

# dummy test
dummy = solution.maxProfit([1,2,3,4,5,6,7])
print(dummy)

# leetcode test case
test1 = solution.maxProfit([7,1,5,3,6,4])
print("test1 result: " + str(test1))

# leetcode testcase2
test2 = solution.maxProfit([7,6,4,3,1])
print("test2 result: " + str(test2))

test3 = solution.maxProfit([1,4,2])
# exp 3, actual 1

# [7,6,4,3,1]
# exp 0, actua; -3

