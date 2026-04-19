class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        for(String s: strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);
            res.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(res.values());
    }
}
