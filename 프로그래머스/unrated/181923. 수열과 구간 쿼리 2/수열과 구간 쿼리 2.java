class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int num = 0;
        
        for (int[] que : queries) {
            int tmp = 0;
                
            for(int i = que[0]; i <= que[1]; i++) {
                if (que[2] < arr[i]) {
                    if (tmp == 0 || arr[i] < tmp) tmp = arr[i];
                }
            }
            System.out.println(tmp);
            if (tmp == 0) tmp = -1;
                
            answer[num] = tmp;
            num += 1;
        }
        return answer;
    }
}