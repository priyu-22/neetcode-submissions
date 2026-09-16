class Solution {
    public boolean hasDuplicate(int[] nums) {
       if(nums == null || nums.length <= 1){
        return false;
       }
       HashSet<Integer> set = new HashSet<>();
       for(int i: nums){
        if(set.contains(i)){
            return true;
        }
        set.add(i);
       }
       return false;
    }
}

