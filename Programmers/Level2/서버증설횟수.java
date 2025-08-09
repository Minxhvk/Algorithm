import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int curServerNum = 1;
        
        Deque<int[]> q = new ArrayDeque<>();
        
        for (int i=0; i<players.length; i++) {
            
            int[] arr = q.peek();
            if (arr != null && arr[0] == i) {
                curServerNum -= arr[1];
                q.poll();
            }
            
            int curPlayerNum = players[i];
            int capacity = curServerNum * m;
            int need = curPlayerNum - capacity;
            
            if (need >= 0) {
                int add = (need + m) / m;
                
                curServerNum += add;
                q.add(new int[]{i+k, add});
                answer += add;
            }
        }
        
        return answer;
    }
}