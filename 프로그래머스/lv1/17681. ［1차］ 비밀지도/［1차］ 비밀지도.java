class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        for (int i = 0; i < n; i++) {
            String str = Integer.toBinaryString(arr1[i] | arr2[i]);
            while (str.length() != n) str = "0" + str;
            answer[i] = str.replace('0', ' ').replace('1', '#');
        }
        
        return answer;
    }
}