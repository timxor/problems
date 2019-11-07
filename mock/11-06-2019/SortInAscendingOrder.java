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

class RelativeSortArray {
    public int[] run(int[] arr1, int[] arr2) {

        // relative ordering = ??
        // ascending order = small to big

        // arr1 = [2,3,1,3,2,4,6,7,9,2,19]
        // arr2 = [2,1,4,3,9,6]
        // arr3 = [2,2,2,1,4,3,3,9,6,7,19]

        int[] arr3 = new int[arr1.length];
        int[] arr4 = new int[arr2.length];
        int sortedCount = 0;
        int notFoundCount = 0;

        // should do hashmap
        // key to count
        // three for loops ---> O(n)

        Map<Integer, Integer> result = new HashMap<>();


        for(int i = 0; i < arr2.length; i++)
        {

            for(int j = 0; j < arr1.length; j++)
            {

                // if the element does appear
                if(arr1[j] == arr2[i])
                {
                    // copy value to be overwritten
                    int tmp = arr1[sortedCount];
                    arr1[sortedCount] = arr1[j];
                    arr1[j] = tmp;
                    sortedCount++;
                }
                else // if the element does not appear
                {

                }
            }

        }



        return arr3;
    }
}
