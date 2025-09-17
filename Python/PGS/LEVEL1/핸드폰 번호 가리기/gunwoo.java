class Solution {
    public String solution(String phone_number) {
        String answer = "";
        for(int i=0; i<phone_number.length()-4; i++){
            answer += "*";
        }
        for(int i= phone_number.length()-4; i< phone_number.length(); i++){
            answer += phone_number.charAt(i); //문자열에 접근할 때는 charAt(i)
        }
        return answer;
    }
}