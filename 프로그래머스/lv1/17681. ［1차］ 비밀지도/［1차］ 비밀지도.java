class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
            
        for (int i = 0; i < n; i++) {
            int num = (arr1[i] | arr2[i]);
            String str = Integer.toBinaryString(num);
                        
            while (str.length() != n) {
                str = "0" + str;
            }
            
            answer[i] = str.replace('0', ' ').replace('1', '#');
        }
        return answer;
    }
}