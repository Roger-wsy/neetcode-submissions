class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder();
        int n1 = 0;
        int n2 = 0;

        while(n1 < word1.length() && n2 < word2.length()){
            res.append(word1.charAt(n1));
            res.append(word2.charAt(n2));
            n1++;
            n2++;
        }

        if(n1 < word1.length()){
            res.append(word1.substring(n1));
        }else if(n2 < word2.length()){
            res.append(word2.substring(n2));
        }

        return res.toString();
    }
}