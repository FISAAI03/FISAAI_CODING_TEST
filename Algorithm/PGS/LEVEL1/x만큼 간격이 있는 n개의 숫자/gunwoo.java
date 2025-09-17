class Solution {
    public long[] solution(long x, int n) {
        long[] answer = new long[n];
        long first = 0;
        first = x;
        for(int i = 0; i < n; i++){
            answer[i] = x;
            x += first;
        }
        return answer;
    }
}