import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> lst = new ArrayList<>();
        
        for (int i = 1; i < 64; i++) {
            int num = Integer.parseInt(Integer.toBinaryString(i)) * 5;
            if (l <= num && num <= r)
                lst.add(num);
        }
        
        if (lst.size() == 0) lst.add(-1);
            
        return lst.stream().mapToInt(i -> i).toArray();
    }
}