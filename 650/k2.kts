class Solution {
    fun minSteps(n: Int): Int {
        if (n == 1) return 0
        for (i in 2 until n) {
            if (n % i == 0) return i + minSteps(n / i)
        }
        return n
    }
}