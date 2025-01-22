class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {
            return new int[]{-1};
        }
        
        int[] answer = new int[arr.length-1];
        int small = arr[0];
        int index = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < small) {
                small = arr[i];
            }
        }
        for (int i = 0; i < arr.length; i++){
            if (arr[i] != small){
                answer[index] = arr[i];
                index++;
            }
        }
        return answer;
    }
}