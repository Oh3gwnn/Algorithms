class Solution {
    public int solution(int[] num_list) {
        int odd = 0, even = 0;
        
        for (int i : num_list) {
            if (i % 2 == 1) odd = odd*10 + i;
            else even = even*10 + i;
        }
        return odd+even;
    }
}