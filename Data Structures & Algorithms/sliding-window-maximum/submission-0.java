public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;

        if (n == 0 || k == 0) {
            return new int[0];
        }

        int[] leftMax = new int[n];
        int[] rightMax = new int[n];

        // Step 1: Build leftMax
        // leftMax[i] = max from start of current block to index i
        leftMax[0] = nums[0];

        for (int i = 1; i < n; i++) {
            // If i is the start of a new block, reset
            if (i % k == 0) {
                leftMax[i] = nums[i];
            } else {
                leftMax[i] = Math.max(leftMax[i - 1], nums[i]);
            }
        }

        // Step 2: Build rightMax
        // rightMax[i] = max from index i to end of current block
        rightMax[n - 1] = nums[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            // If i is the end boundary when scanning right-to-left
            // Actually this means i is the start of a block
            if (i % k == 0) {
                rightMax[i] = nums[i];
            } else {
                rightMax[i] = Math.max(rightMax[i + 1], nums[i]);
            }
        }

        // Step 3: Calculate result
        int[] output = new int[n - k + 1];

        for (int i = 0; i <= n - k; i++) {
            int windowStart = i;
            int windowEnd = i + k - 1;

            output[i] = Math.max(
                rightMax[windowStart],
                leftMax[windowEnd]
            );
        }

        return output;
    }
}