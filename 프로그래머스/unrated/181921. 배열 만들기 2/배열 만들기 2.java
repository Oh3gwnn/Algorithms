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
        
        // mapToInt() 메서드 - Stream 요소를 IntStream 반환
        // toArray() 메서드 - IntStream -> int[] 배열로 변환
        return lst.stream().mapToInt(i -> i).toArray();
    }
}