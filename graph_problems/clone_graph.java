//https://leetcode.com/problems/clone-graph

class Solution {

  class Node {
      public int val;
      public List<Node> neighbors;

      public Node() {}

      public Node(int _val,List<Node> _neighbors) {
          val = _val;
          neighbors = _neighbors;
      }
  };

  public Node cloneGraph(Node node) {
      Map<Node, Node> clones = new HashMap<>();
      cloneAllNodes(node, clones);
      return clones.get(node);
  }

  public void cloneAllNodes(Node node, Map<Node, Node> clones) {
    if (clones.containsKey(node)) return;
    Node clone = new Node(node.val, new ArrayList<>());
    clones.put(node, clone);
    for(Node neighbor : node.neightbors){
      cloneAllNodes(neighbor, clones);
      Node clonedNeighbor = clones.get(neighbor);
      clone.neightbors.add(clonedNeighbor);
    }
  }
}
