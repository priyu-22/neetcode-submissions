class Solution {
    public int[] twoSum(int[] nums, int target) throws Exception {
        
        //Exception handling
        if (nums == null || nums.length == 0) {
            throw new IllegalArgumentException("Invalid nums array as input");
        }

        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(nums[0], 0);
        for (int i = 1; i <= nums.length-1; i++) {
            int remainder = target - nums[i];
            if (map.containsKey(remainder)) {
                return new int[]{map.get(remainder), i};
            }
            map.put(nums[i], i);
        }

            throw new IllegalArgumentException("Invalid nums array as input");
    }
}
