class Solution {
    public boolean solution(int x) {
        int first = x;
        int plus = 0;
        while(x>0){
            plus += x%10;
            x /= 10;
        }
        return first % plus == 0;      
    }
}