class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] tmp = arr;
        for (int[] que : queries) {
            for(int i = que[0]; i <= que[1]; i++) {
                if (i % que[2] == 0) {
                    arr[i] += 1;
                }
            }
        }
        return arr;
    }
}