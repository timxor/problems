#https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums) -> int:
        return 0



# https://leetcode.com/problems/projection-area-of-3d-shapes/solution/



class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # string splicing
        for i in range(len(A)):
            #
            #
            if A[i+1:] + A[:i+1] == B:
                return True

        return False




             
        # for index in A:
        #     abf = B(1:)
        #     a = B(0:1)
        #     perhaps = abf + a
        #     if perhaps != A:
        #         return False
        # reutnr true
