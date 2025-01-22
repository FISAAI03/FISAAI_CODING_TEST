class Solution {
    boolean solution(String s) {
        int countp = 0;
        int county = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'p' || c == 'P') {
                countp++;
            } else if (c == 'y' || c == 'Y') {
                county++;
            }
        }
        return countp == county;
    }
}
