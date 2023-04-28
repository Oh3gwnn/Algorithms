// 파이썬 풀이 그대로 자바에서 쓸 수 있는 모든 자원을 갖다 썼다.
// 나는 파이썬으로 풀어야겠다...

import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        ArrayList<Integer> stack = new ArrayList<>();
        
        for (int i = 0; i < score.length; i++) {
            if (stack.size() < k) {
                stack.add(score[i]);
                Collections.sort(stack);
                answer[i] = stack.get(0);
            }
            else if (stack.size() == k) {
                int minscore = stack.get(0);
                
                if (score[i] > minscore) {
                    stack.remove(0);
                    stack.add(score[i]);
                    Collections.sort(stack);
                }
                answer[i] = stack.get(0);
            }
        }
        return answer;
    }
}

/** 파이썬 풀이
def solution(k, score):
    answer = []
    stack = []*len(score)
    
    for i in range(len(score)):
        if len(stack) != k : 
            stack.append(score[i])
            stack.sort()
            answer.append(stack[0])
            
        elif (len(stack) == k):
            if score[i] > min(stack):
                stack.pop(0)
                stack.append(score[i])
                stack.sort()
                answer.append(stack[0])
            else : answer.append(stack[0])
            
    return answer
**/