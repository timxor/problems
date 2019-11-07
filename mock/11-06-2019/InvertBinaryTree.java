/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// recursive solution
// time = o(height)
// space = o(n)
class InvertBinaryTree {
    public TreeNode invertTree(TreeNode root) {

        // 1. check if null
        if(root == null){
            return null;
        }

        // 2. get right and left nodes
        TreeNode right = invertTree(root.right);
        TreeNode left = invertTree(root.left);

        // 3. swap them
        root.left = right;
        root.right = left;

        // 4. return
        return root;
    }
}
