// https://leetcode.com/problems/search-in-a-binary-search-tree/
// time = O(tree height) = O(logN) avg and O(N) worst. space = O(1)

public class Solution {

  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { this.val = x; }
  }

  public TreeNode searchBST(TreeNode root, int val) {
    while(root != null && val != root.val) {
      root = val < root.val ? root.left : root.right;
    }
    return root;
  }
}
