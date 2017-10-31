import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    class QueueEntry {
        int level;
        TreeNode node;

        public QueueEntry(int level, TreeNode node) {
            this.level = level;
            this.node = node;
        }
    }

    public int widthOfBinaryTree(TreeNode root) {
        Queue<QueueEntry> queue = new LinkedList<>();
        queue.add(new QueueEntry(0, root));
        int firstNonNull = -1;
        int lastNonNull = 0;
        int lastLevel = -1;
        int idx = 0;
        int maxWidth = 1;
        while (!queue.isEmpty()) {
            QueueEntry next = queue.poll();
            if (next.node != null) {
                if (next.node.left != null) {
                    queue.add(
                        new QueueEntry(next.level+1, next.node.left)
                    );
                }
                if (next.node.right != null) {
                    queue.add(
                        new QueueEntry(next.level+1, next.node.right)
                    );
                }
            }
            if (lastLevel == next.level) {
                if (next.node != null) {
                    lastNonNull = idx;
                    if (firstNonNull < 0) {
                        firstNonNull = idx;
                    }
                }
                idx+=1;
            } else {
                maxWidth = Math.max(maxWidth, lastNonNull - firstNonNull + 1);
                firstNonNull = -1;
                lastNonNull = 0;
                idx = 0;
                lastLevel = next.level;
            }
        }
        return maxWidth;
    }
}