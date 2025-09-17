class Solution {
    public int[] solution(long n) {
        String strn = Long.toString(n);
        int index = 0;
        int[] answer = new int[strn.length()];
        for(int i = strn.length()-1; i >= 0; i--){
            answer[index] = strn.charAt(i) - '0'; //0의 아스키 값이 48 
            index++;
        }
        return answer;
    }
}