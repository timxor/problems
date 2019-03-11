class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        if x == 0:
            return True

        # get number of digits
        num_digits = math.floor(math.log10(x)) + 1

        # get most sig digit mask
        msd_mask = 10**(num_digits - 1)

        for i in range(num_digits // 2):
            if x // msd_mask != x % 10:
                return False
            x %= msd_mask  # remove msd
            x //= 10   # remove least sig digit
            msd_mask //= 100

        return True
