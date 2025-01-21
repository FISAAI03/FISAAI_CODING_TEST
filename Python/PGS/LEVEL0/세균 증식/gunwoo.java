class Solution {
    public int solution(int n, int t) {
        int answer = 1;
        for(int i = 1; i <= t; i++){
            answer = 2 * answer;
        }
        answer = n * answer;
        return answer;
    }
}