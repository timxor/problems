// date: 11/06/2019
// type: amazon online assesment
// time: 60 minutes
// p1: sorting - easy
// p2: probability - medium
// url: https://leetcode.com/interview/1/
// https://leetcode.com/problems/relative-sort-array/discuss/335056/Java-in-place-solution-using-counting-sort
/*
  Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

  Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

  Example 1:

  Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
  Output: [2,2,2,1,4,3,3,9,6,7,19]

  Constraints:

  arr1.length, arr2.length <= 1000
  0 <= arr1[i], arr2[i] <= 1000
  Each arr2[i] is distinct.
  Each arr2[i] is in arr1.
*/
// relative ordering = ??
// ascending order = small to big

// arr1 = [2,3,1,3,2,4,6,7,9,2,19]
// arr2 = [2,1,4,3,9,6]
// arr3 = [2,2,2,1,4,3,3,9,6,7,19]


class RelativeSortArray {

    // time = O(n log n), space = O(n)
    public int[] run(int[] arr1, int[] arr2) {

        TreeMap<Integer, Integer> result = new TreeMap<>();

        for(int n : arr1){map.put(n, map.getOrDefault(n, 0) + 1);}

        int i = 0;

        for(int n : arr2){
          while(map.get(n) > 0) {
            arr1[i++] = n;
            map.put(n, map.get(n)-1);
          }
        }

        for(int n : map.keySet()){
          while(map.get(n) > 0){
            arr1[i++] = n;
            map.put(n, map.get(n)-1);
          }
        }

        return arr1;
    }

    // solution 2
    // time = O(n log n), space = O(n)
}
