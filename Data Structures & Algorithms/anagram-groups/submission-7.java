class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        for(String s: strs){
            String sorted = s.chars()           // IntStream of characters
                    .sorted()                       // Sorts the stream
                    .collect(StringBuilder::new, 
                            StringBuilder::appendCodePoint, 
                            StringBuilder::append) // Rebuilds the string
                    .toString();
            String key = String.valueOf(sorted);
            res.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(res.values());
    }
}
