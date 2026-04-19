class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> visited = new HashMap<>();
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++){
            Integer a = target - nums[i];
            if(visited.containsKey(a)){
                res[0] = visited.get(a);
                res[1] = i;
                return res;
            }
            visited.put(nums[i], i);
        }
        return new int[] {}; 
    }
}
