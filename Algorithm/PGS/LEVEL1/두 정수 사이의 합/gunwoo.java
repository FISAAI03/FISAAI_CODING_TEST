class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int change = 0;
        if(a > b){
            change = a;
            a = b;
            b = change;
        }
        for(int i = a; i <= b; i++){
            answer += i;
        }
        return answer;
    }
}