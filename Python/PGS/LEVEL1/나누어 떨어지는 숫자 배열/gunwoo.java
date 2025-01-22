import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> temp = new ArrayList<>();

        for (int value : arr) {
            if (value % divisor == 0) {
                temp.add(value);
            }
        }
        if (temp.isEmpty()) {
            temp.add(-1);
        }
        int[] answer = temp.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(answer);

        return answer;
    }
}
