class Solution {
    public int solution(int n) {
        int answer = 0;
        double sqrtn = Math.sqrt(n);
            
        if(sqrtn == (int) sqrtn){
            answer = 1;
        }
        else{
            answer = 2;
        }
        return answer;
    }
}