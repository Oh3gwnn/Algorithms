class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for (int[] que : queries) {
            int temp = arr[que[0]];
            arr[que[0]] = arr[que[1]];
            arr[que[1]] = temp;
        }
        return arr;
    }
}