class Solution:
    def longestPalindrome(self, s: str) -> str:
        #
        # 1. get two indexes on head and tail
        # 2. while abs(i,j) > 1
        # 3. if str[i] != str[j]
        #

        i, j = 0, len(s) - 1

        while i < j:
            #
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True


# input: "babad"
# expected: "aba"
