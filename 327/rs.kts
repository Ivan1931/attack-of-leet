class Solution {
    var upper = 0
    var lower = 0

    fun mergeSumCount(nums: IntArray, start: Int, end: Int): Int {

        // nums.slice(start..end).forEach{ print(" $it") }
        // println(end - start)

        if (end - start <= 1) return 0
        val mid = (start + end) / 2
        var count = mergeSumCount(nums, start, mid) + mergeSumCount(nums, mid, end)

        val copy = mutableListOf<Int>()

        var j = mid
        var k = mid
        var t = mid

        for (i in start..mid-1) {
            while (t < end && nums[t] < nums[i]) {
                copy.add(nums[t])
                t += 1
            }
            while (k < end && nums[k] - nums[i] < lower) k++
            while (j < end && nums[j] - nums[i] <= upper) j++
            println("j - k ${j - k}")
            count += j - k
            copy.add(nums[i])
        }

        copy.forEachIndexed { i, n -> nums[start+i] = n}
        println(nums.joinToString(", "))
        return count
    }

    fun countRangeSum(nums: IntArray, lower: Int, upper: Int): Int {
        this.upper = upper
        this.lower = lower
        var sum = 0
        val sums = nums.map {
            sum += it
            sum
        } . toIntArray()
        return mergeSumCount(sums, 0, sums.size)
    }

}

val nums = intArrayOf(-2, 5, -1)
val lower = -2
val upper = 2
val solution = Solution()
println("Final solution: ${solution.countRangeSum(nums, lower, upper)}")
// assert(solution.countRangeSum(nums, lower, upper) == 3)
