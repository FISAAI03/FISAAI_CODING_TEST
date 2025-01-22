class Solution {
    public long solution(long n) {
        double answer = 0;
        int sq = (int) Math.sqrt(n);
        if(sq == Math.sqrt(n)){
            answer = Math.pow(sq+1,2);
        }
        else{
            answer = -1;
        }
        return (long) answer;
    }
}