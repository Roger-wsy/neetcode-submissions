class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        int[] countS = new int[26];
        for (int i = 0; i < s.length(); i++) {
            countS[s.charAt(i) - 'a']++; // Increment for s
            countS[t.charAt(i) - 'a']--; // Decrement for t
        }

        for(int val:countS){
            if(val != 0){
                return false;
            }
        }
        return true;
    } 
}
