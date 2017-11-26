class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun constructMaximumBinaryTreeRec(nums: IntArray, start: Int, end: Int): TreeNode? {
        if (start == end) {
            return TreeNode(nums[start])
        } else {
            var maxIdx = start
            for (i: Int in start..end) {
                if (nums[maxIdx] < nums[i]) {
                    maxIdx = i
                }
            }
            val res = TreeNode(nums[maxIdx])
            res.left = if (maxIdx == start) {
                null
            } else {
                constructMaximumBinaryTreeRec(nums, start, maxIdx - 1)
            }
            res.right = if (maxIdx == end) {
                null
            } else {
                constructMaximumBinaryTreeRec(nums, maxIdx + 1, end)
            }
            return res
        }
    }

    fun constructMaximumBinaryTree(nums: IntArray): TreeNode? {
        if (nums.isEmpty()) {
            return null
        }
        return constructMaximumBinaryTreeRec(nums, 0, nums.size-1)
    }
}