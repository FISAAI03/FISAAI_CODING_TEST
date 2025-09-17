class Solution {
    public long solution(int price, int money, int count) {
        long answer = money;
        int first = price;
        for(int i = 1; i <= count; i++){
            price = first*i;
            answer -= price;
        }

        if(answer < 0){
            answer = Math.abs(answer);
        }
        else{
            answer = 0;
        }
        
        return answer;
    }
}