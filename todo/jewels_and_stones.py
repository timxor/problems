class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        count = 0
        for index in enumerate(J):
            if num(index) in S:
                count +=1
        return count
