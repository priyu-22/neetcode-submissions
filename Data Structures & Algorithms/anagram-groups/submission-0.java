class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // frequency count solution
        HashMap<String, List<String>> map = new HashMap<>();
        for(String str: strs){
            char[] charArray = new char[26];
            for(char c: str.toCharArray()){
                charArray[c-'a']++;
            }
            //add delimiter between count using stringBuilder
            StringBuilder keyBuilder = new StringBuilder();
            for(char ch: charArray){
                keyBuilder.append(ch).append('#');
            }
            String key = new String(keyBuilder);
            // put in map
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);

        }
        return new ArrayList<>(map.values());
    }
}
