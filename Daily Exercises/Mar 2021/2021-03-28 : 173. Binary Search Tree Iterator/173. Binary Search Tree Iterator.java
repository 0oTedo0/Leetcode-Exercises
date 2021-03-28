/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class BSTIterator {
    Deque<TreeNode> s=new LinkedList<TreeNode>();
    public BSTIterator(TreeNode root) {
        s.push(root);
        while(s.peek().left!=null){
            s.push(s.peek().left);
        }
    }
    
    public int next() {
        TreeNode ans=s.peek();
        s.pop();
        if(ans.right!=null){
            s.push(ans.right);
            while(s.peek().left!=null){
            s.push(s.peek().left);
            }
        }
        return ans.val;
    }
    
    public boolean hasNext() {
        return !s.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
