// https://leetcode.com/problems/missing-number/
// time = O(n), space = O(1)

class Solution {
    public int missingNumber(int[] nums) {
        int missingNumber = nums.length;

        for(int i = 0; i < nums.length; i++){
          missingNumber ^= i ^ nums[i];
        }

        return missingNumber;
    }
}
