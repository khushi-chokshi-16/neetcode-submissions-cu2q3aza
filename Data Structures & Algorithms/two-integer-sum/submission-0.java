class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] output = new int[2]; // Initialize array

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) { // Fix loop condition
                if (nums[i] + nums[j] == target) {
                    output[0] = i;
                    output[1] = j;
                    return output; // Return immediately after finding a solution
                }
            }
        }

        return new int[]{}; // Return an empty array if no solution is found
    }
}
